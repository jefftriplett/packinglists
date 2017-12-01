import click
import math
import os
import yaml

from click_default_group import DefaultGroup

from .__version__ import __version__
from .core import PackingManager


DEFAULT_ACTIVITY_TYPES = [
    'Essentials',
    'Toiletries',
]


@click.group(cls=DefaultGroup, default='preview', default_if_no_args=True)
@click.version_option(prog_name='packinglist', version=__version__)
def cli():
    """
    Packing List!
    """


@cli.command('create')
def cmd_create():
    packing_manager = PackingManager()
    activity_types = packing_manager.get_activity_types()
    for activity_type in activity_types:
        click.echo(activity_type)


@cli.command('init')
def cmd_init():
    click.echo('init')
    # filenames = load_packing_list_files()
    # print([filename for filename in filenames])
    packing_manager = PackingManager()


@cli.command('list')
def cmd_list():
    packing_manager = PackingManager()
    activity_types = packing_manager.get_activity_types()
    click.echo('Activity Types:')
    for activity_type in activity_types:
        click.echo(f'- {activity_type}')


@cli.command('preview')
@click.option('--nights', required=True, type=click.INT)
@click.option('--activities', default=None)
@click.option('--gender', default='unisex', type=click.Choice(['unisex', 'female', 'male']))
@click.option('--laundry', is_flag=True, default=False)
@click.option('--location', default=None)
def cmd_preview(nights, gender, location, activities, laundry):
    activity_types = DEFAULT_ACTIVITY_TYPES.copy()

    if activities:
        activity_types += activities.split(',')

    activity_types = set(activity_types)

    packing_manager = PackingManager(nights=nights, laundry=laundry, gender=gender)

    for activity in sorted(activity_types):
        click.echo('## {0}'.format(activity))
        packing_data = packing_manager.get_packing_items_by_activity(activity)

        for item in packing_data:
            count_text = f': {item.count}' if item.count else ''
            click.echo(f'- [ ] {item.name}{count_text}')

        click.echo()


if __name__ == '__main__':
    cli()
