Grand Repository of SWCCG Decks
===============================

These are decks composed for use by players in **SWCCG** events.

The decks are provided in _`plaintext`_ and then converted in to a consumable `yaml` or `json` format.


## Adding Decks

### Directories

* Add decks to the `txt` directory.
* Ensure that the subdirectory within `txt` is a category representing the event.<br />For example: `2021_worlds_day1`
* If specifying a more-specific date, use the format: `YYYYmmdd_eventname`.<br />For example: `20210121_worlds_dayx`.


### Filename

* The filename should be something like: `EriksenLS-Legend.txt`
  * That is the player **username**: `Eriksen` + the deck **side**: `LS`
  * And then the **name of the deck**: `Legend`

### Deck File Format _(File Contents)_

_The file contents should be formatted like:_

* **line 1** should contain the deck info, for example: `Rikard Eriksen - Worlds Day 1 - LS Legend`

* There are multiple sections of the deck which represent different card types.<br />Each section starts with a header in **ALL CAPS**, followed by a list of cards. For example:
```
STARTING
Anger, Fear, Aggression (V)
The Galaxy May Need A Legend

CHARACTERS
Ahsoka Tano
Anakin Skywalker, Padawan Learner

```

* To indicate that a deck has multiples of the same card do one of:
  1. List the card multiple times
  2. Prefix the listing with a `number` and an `x` followed by a `space` before the `cardname`.<br />For example: 
```
2x Obi-Wan With Lightsaber
2x Rey With Lightsaber
3x A Jedi's Resilience
2x All Wings Report In & Darklighter Spin
2x Rebel Leadership (V)
Ahch-To: Luke's Hut
Ahch-To: Luke's Hut
The Falcon
The Falcon
The Falcon
```


### Known Headers

* Use the **known headers** of:
  * `STARTING`
  * `CHARACTERS`
  * `EFFECTS`
  * `INTERRUPTS`
  * `LOCATIONS`
  * `STARSHIPS`
  * `WEAPON`
