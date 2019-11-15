import random

from core import traits, globals, names

class NPC():
    def __init__(self, archtype=None, sex=None, race=None, name=None, traits=None):
        self.archtype = archtype
        self.sex = sex
        self.race = race
        self.name = name
        self.traits = traits

    def __repr__(self):
        header = "{archtype} {sex} {race}: {first} {last}".format(
            archtype=self.archtype,
            sex=sex,
            race=race,
            first=self.name['first'],
            last=self.name['last']
        )
        traits = ''.join(self.traits)
        return header + '\n' + traits


archtype = globals.POSITIVE
race = globals.HUMAN
sex = globals.MALE

npcs = [NPC(archtype, sex, race, names.generate_name(race, sex), traits.get_traits_by_count_and_archtype(2, archtype)) for i in range(0,10)]
for npc in npcs:
    print(npc)
# print("{archtype} {sex} {race}: {first} {last}".format(
#     archtype=archtype,
#     sex=sex,
#     race=race,
#     first=name['first'],
#     last=name['last']
# ))
# for trait in traits:
#     print("\t{}".format(trait).rstrip())


