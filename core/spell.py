import json
import os
import json
import random
from json import JSONEncoder

SLOTS_PER_LEVEL = {
    1:  [3, 2],
    2:  [3, 3],
    3:  [3, 4, 2],
    4:  [4, 4, 3],
    5:  [4, 4, 3, 2],
    6:  [4, 4, 3, 3],
    7:  [4, 4, 3, 3, 1],
    8:  [4, 4, 3, 3, 2],
    9:  [4, 4, 3, 3, 3, 1],
    10: [5, 4, 3, 3, 3, 2],
    11: [5, 4, 3, 3, 3, 2, 1],
    12: [5, 4, 3, 3, 3, 2, 1],
    13: [5, 4, 3, 3, 3, 2, 1, 1],
    14: [5, 4, 3, 3, 3, 2, 1, 1],
    15: [5, 4, 3, 3, 3, 2, 1, 1, 1],
    16: [5, 4, 3, 3, 3, 2, 1, 1, 1],
    17: [5, 4, 3, 3, 3, 2, 1, 1, 1, 1],
    18: [5, 4, 3, 3, 3, 2, 1, 1, 1, 1],
    19: [5, 4, 3, 3, 3, 2, 2, 1, 1, 1],
    20: [5, 4, 3, 3, 3, 2, 2, 2, 1, 1],
}


class Spell(dict):

    def __init__(self, name, casting_time, components, description, duration, level, range, school ):
        dict.__init__(
            self,
            name = name,
            casting_time = casting_time,
            components = components,
            description = description,
            duration = duration,
            level = level,
            range = range,
            school = school
        )


def parse_spells():

    # spells = dict.fromkeys(range(0, 10), list())
    spells = dict()
    for x in range(0, 10):
        spells[x] = list()

    if os.getcwd() == '/app':
        base_path = '.'
    else:
        base_path = '..'

    with open(os.path.join(base_path, 'core', 'data', 'spells', 'spells.json'),  encoding="utf8") as json_data:
        spells_raw = json.loads(json_data.read())

    for name in spells_raw.keys():
        data = spells_raw[name]
        level = int(data['level'])
        spell = Spell(
            name=name,
            casting_time=data['casting_time'],
            components=data['components'],
            description=data['description'],
            duration=data['duration'],
            level=data['level'],
            range=data['range'],
            school=data['school']
        )
        spells[level].append(spell)

    return spells


def get_spells_by_level(level, full_spell_list):
    spell_slots = SLOTS_PER_LEVEL[level]
    spell_list = dict.fromkeys(range(0, len(spell_slots)))

    level = 0
    for spell_count in spell_slots:
        list_of_spells_for_level = full_spell_list[level]
        selected_spells_for_level = {}
        for x in range(0, spell_count):
            selected_spell = list_of_spells_for_level[random.randint(0, len(list_of_spells_for_level) - 1)]
            selected_spells_for_level[selected_spell['name']] = selected_spell
        spell_list[level] = selected_spells_for_level
        level += 1

    return spell_list
