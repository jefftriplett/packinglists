# Packing List

Your mileage may vary. 

The data comes from a dump I found on Github from what looked like maybe an early copy of [PackPoint](http://www.packpnt.com/). I can't find it anymore after many searches, so I wrote my own in Python.

## Install

```shell
$ pipenv install
```

## Usage

```shell
$ python pack.py --help
Usage: pack.py [OPTIONS]

Options:
  --nights INTEGER   [required]
  --gender TEXT
  --location TEXT
  --activities TEXT
  --laundry
  --help             Show this message and exit.

Usage Examples:

$ python pack.py --nights=4
```

## Todo

- [ ] Make adding custom packing lists easier.
- [ ] Handle gender assumptions better since I'm working with pre-existing data and potentially invalid assumptions.
- [ ] Add location support
- [ ] Add weather support
- [ ] Add a proper setup.py and list on pypi
