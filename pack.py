import click
import math
import yaml

from pathlib import Path


DEFAULTS = [
    'Essentials',
    'Toiletries',
]


# class ActivityThing(object):

#     def __init__(self, **kwargs):
#         self.name = kwargs.get('name')
#         self.gender = kwargs.get('gender')
#         self.activity = kwargs.get('activity')
#         self.min_temperature = kwargs.get('min_temperature')
#         self.quantity = kwargs.get('quantity')
#         self.daily_count = kwargs.get('daily_count')
#         self.image = kwargs.get('image', None)
#         self.selected = kwargs.get('selected', False)
#         self.group_title = kwargs.get('group_title')
#         self.deleted = kwargs.get('deleted', False)

#     def __str__(self):
#         return '{group_title}: {name}'.format(
#             group_title=self.group_title,
#             name=self.name,
#         )


def load_packing_data():
    output = {}
    filenames = Path('packinglists').glob('*.yml')
    for filename in filenames:
        with open(filename, 'r') as input_stream:
            data = yaml.load(input_stream)
            if data is not None:
                output.update(data)
    return output


@click.command()
@click.option('--nights', required=True, type=click.INT)
@click.option('--gender', default='Unisex')
@click.option('--location', default=None)
@click.option('--activities', default=None)
@click.option('--laundry', is_flag=True, default=False)
def main(nights, gender, location, activities, laundry):
    packing_data = load_packing_data()

    categories = DEFAULTS
    if activities:
        categories += activities.split(',')

    categories = set(categories)

    if laundry:
        nights = min(2, nights)

    for category in categories:
        click.echo('## {0}'.format(category))
        for item in packing_data:
            packing = packing_data[item]

            # thing = ActivityThing(**packing)

            group_title = packing.get('group_title')
            if group_title in category and packing.get('gender') in ['Unisex', gender]:
                try:
                    count = math.ceil(float(packing.get('daily_count', 0.0)) * nights)
                    click.echo(
                        '- [ ] {name}: {count}'.format(
                            name=packing.get('name'),
                            count=count
                        )
                    )

                except ValueError:
                    count = ''
                    click.echo(
                        '- [ ] {name}'.format(
                            name=packing.get('name'),
                        )
                    )

                except Exception as e:
                    click.echo(e)

        click.echo()


if __name__ == '__main__':
    main()
