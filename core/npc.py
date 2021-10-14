import random

from core import traits, globals, names

class NPC():
    def __init__(self, archtype=None, gender=None, race=None, name=None, traits=None):
        self.archtype = archtype
        self.gender = gender
        self.race = race
        self.name = name
        self.traits = traits

    def __repr__(self):
        header = "{archtype} {gender} {race}: {first} {last}".format(
            archtype=self.archtype,
            gender=self.gender,
            race=self.race,
            first=self.name['first'],
            last=self.name['last']
        )
        traits = ''.join(self.traits)
        return header + '\n' + traits


# archtype = globals.POSITIVE
# race = globals.HUMAN
# gender = globals.MALE
#
# npcs = [NPC(archtype, gender, race, names.generate_name(race, gender), traits.get_traits_by_count_and_archtype(2, archtype)) for i in range(0,10)]
# for npc in npcs:
#     print(npc)
# print("{archtype} {gender} {race}: {first} {last}".format(
#     archtype=archtype,
#     gender=gender,
#     race=race,
#     first=name['first'],
#     last=name['last']
# ))
# for trait in traits:
#     print("\t{}".format(trait).rstrip())


