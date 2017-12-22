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
Usage: pack.py [OPTIONS] COMMAND [ARGS]...

  Packing List!

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  main*
  init
  list

$ python pack.py list
Baby
Beach
Bicycling
Business casual
Business formal
Camping
Essentials
Everyday Carry
Fancy dinner
Gym
Hiking
International
Motorcycling
Photography
Road Trip
Running
Snow sports
Swimming
Toiletries
Working

$ python pack.py --nights=4
## Essentials
- [ ] Belt
- [ ] Boarding Pass
- [ ] Book
- [ ] Camera
- [ ] Casual Pants: 2
- [ ] Casual Shirts: 4
- [ ] Casual Watch
- [ ] Cell Phone
- [ ] Cell Phone Charger
- [ ] Chapstick
- [ ] Ear Plugs
- [ ] Eye Mask
- [ ] Hand Sanitizer
- [ ] House Key
- [ ] Jacket
- [ ] Medications
- [ ] Pain Reliever Pills
- [ ] Pajamas
- [ ] Printed Trip Itinerary
- [ ] Reading Glasses
- [ ] Shorts
- [ ] Socks - Long: 2
- [ ] Socks - Short: 2
- [ ] Sunglasses
- [ ] Sweater
- [ ] Umbrella
- [ ] Underwear: 4
- [ ] Vitamins
- [ ] Wallet

## Toiletries
- [ ] Blemish Stick
- [ ] Contact Solution
- [ ] Contacts
- [ ] Deodorant
- [ ] Floss
- [ ] Hairbrush
- [ ] Nail Clippers
- [ ] Qtips
- [ ] Shaver
- [ ] Shaving Gel
- [ ] Toothbrush
- [ ] Toothpaste
- [ ] Tweezers
```

## Todo

- [ ] Make adding custom packing lists easier.
- [ ] Handle gender assumptions better since I'm working with pre-existing data and potentially invalid assumptions.
- [ ] Add location support
- [ ] Add weather support
- [ ] Add a proper setup.py and list on pypi

## Contact / Social Media

Here are a few ways to keep up with me online. If you have a question about this project, please consider opening a GitHub Issue. 

[![](https://jefftriplett.com/assets/images/social/github.png)](https://github.com/jefftriplett)
[![](https://jefftriplett.com/assets/images/social/globe.png)](https://jefftriplett.com/)
[![](https://jefftriplett.com/assets/images/social/twitter.png)](https://twitter.com/webology)
[![](https://jefftriplett.com/assets/images/social/docker.png)](https://hub.docker.com/u/jefftriplett/)
