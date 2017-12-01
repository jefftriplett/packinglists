import click
import math
import os
import yaml

from click_default_group import DefaultGroup
from pathlib import Path
from slugify import slugify


class PackingManager(object):
    packing_data = {}

    def __init__(self, nights=None, gender='unisex', laundry=False, location=None):
        self.gender = gender
        self.laundry = laundry
        self.location = location

        if laundry:
            self.nights = min(2, nights)
        else:
            self.nights = nights

        self.load_packing_lists()

    @property
    def _default_packing_item_kwargs(self):
        return {
            'nights': self.nights,
            'laundry': self.laundry,
        }

    def add_packing_item(self, packing_item):
        self.packing_data[packing_item.id] = packing_item

    def get_activity_types(self):
        results = []

        for packing_item in sorted(self.packing_data):
            packing = self.packing_data[packing_item]
            results.append(packing.group_title)

        results = set(results)
        results = sorted(results)

        return results

    def get_global_packing_lists(self):
        return Path(Path(__file__).parent, 'data').glob('*.yml')

    def get_packing_item_by_id(self, id):
        pass

    def get_packing_data(self):
        return self.packing_data.copy()

    def get_packing_items_by_activity(self, activity_name):
        results = []

        for packing_item in sorted(self.packing_data):
            packing = self.packing_data[packing_item]
            if (
                    (packing.active) and \
                    (packing.group_title.lower() == activity_name.lower()) and \
                    (packing.gender.lower() in ['unisex', self.gender.lower()])
            ):
                results.append(packing)

        return results

    def get_user_packing_lists(self):
        user_folder = Path(os.path.expanduser('~'), '.config', 'packing-list')

        if user_folder.exists():
            return user_folder.glob('*.yml')

    def load_global_packing_lists(self):
        filenames = self.get_global_packing_lists()

        self.load_packing_lists_into_thing(filenames)

    def load_packing_lists(self):
        self.load_global_packing_lists()
        self.load_user_packing_lists()

    def load_packing_lists_into_thing(self, filenames):

        for filename in filenames:
            items = yaml.load(filename.read_text())

            if items is not None:
                for item in items:
                    packing_item_kwargs = self._default_packing_item_kwargs.copy()
                    packing_item_kwargs.update(items[item])
                    packing_item = PackingItem(**packing_item_kwargs)
                    self.add_packing_item(packing_item)

    def load_user_packing_lists(self):
        filenames = self.get_user_packing_lists()

        if filenames:
            self.load_packing_lists_into_thing(filenames)


class PackingItem(object):

    def __init__(self, nights=None, laundry=None, **kwargs):
        self.nights = nights
        self.laundry = laundry

        self.name = kwargs.get('name')
        self.activity = kwargs.get('activity')
        self.active = kwargs.get('active', True)
        self.daily_count = kwargs.get('daily_count', 0.0)
        self.gender = kwargs.get('gender', 'unisex')
        self.group_title = kwargs.get('group_title')
        self.min_temperature = kwargs.get('min_temperature')
        self.quantity = kwargs.get('quantity')

    def __str__(self):
        return '{group_title}: {name}'.format(
            group_title=self.group_title,
            name=self.name,
        )

    def __repr__(self):
        return '<{0}>'.format(self.__str__())

    @property
    def id(self):
        return slugify(f'{self.group_title}.{self.name}')

    @property
    def count(self):
        try:
            # print(self.daily_count, self.nights)
            return math.ceil(
                float(self.daily_count) * self.nights
            )
        except (TypeError, ValueError):
            return ''
