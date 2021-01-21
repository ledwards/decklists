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

* The file contents should be formatted like:
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

### Known Headers

* Use the **known headers** of:
  * `STARTING`
  * `CHARACTERS`
  * `EFFECTS`
  * `INTERRUPTS`
  * `LOCATIONS`
  * `STARSHIPS`
  * `WEAPON`
