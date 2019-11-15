import random

from core import traits, globals, names

archtype = globals.POSITIVE
race = globals.ELF
sex = globals.FEMALE

name = names.generate_name(race, sex)
traits = traits.get_traits(archtype)

print("{archtype} {sex} {race}: {first} {last}".format(
    archtype=archtype,
    sex=sex,
    race=race,
    first=name['first'],
    last=name['last']
))
for trait in traits:
    print("\t{}".format(trait).rstrip())


