import os
import random

from core.globals import POSITIVE, NEUTRAL, NEGATIVE, ALLPOSITIVE, ALLNEUTRAL, ALLNEGATIVE
print(os.getcwd())
with open(os.path.join('..', 'core', 'data', 'traits', 'positive.txt')) as f: positive_traits = f.readlines()
with open(os.path.join('..', 'core', 'data', 'traits', 'neutral.txt')) as f: neutral_traits = f.readlines()
with open(os.path.join('..', 'core', 'data', 'traits', 'negative.txt')) as f: negative_traits = f.readlines()


def __trait_retrieval(count_postive=0, count_neutral=0, count_negative=0):
    traits = []
    for x in range(0, count_postive):
        traits.append(positive_traits[random.randint(0, len(positive_traits) - 1)].rstrip())
    for x in range(0, count_neutral):
        traits.append(neutral_traits[random.randint(0, len(neutral_traits) - 1)].rstrip())
    for x in range(0, count_negative):
        traits.append(negative_traits[random.randint(0, len(negative_traits) - 1)].rstrip())
    return traits


def get_traits(archtype):
    """

    :param archtype:
    :return:
    :rtype: list()
    """
    traits = []
    if archtype == POSITIVE:
        traits = __trait_retrieval(3, 1, 1)
    elif archtype == NEUTRAL:
        traits = __trait_retrieval(1, 3, 1)
    elif archtype == NEGATIVE:
        traits = __trait_retrieval(1, 1, 3)
    elif archtype == ALLPOSITIVE:
        traits = __trait_retrieval(5, 0, 0)
    elif archtype == ALLNEUTRAL:
        traits = __trait_retrieval(0, 5, 0)
    elif archtype == ALLNEGATIVE:
        traits = __trait_retrieval(0, 0, 5)
    return traits


def get_traits_by_count_and_archtype(count, archtype):
    traits = []
    if archtype == POSITIVE or archtype == ALLPOSITIVE:
        traits = __trait_retrieval(count_postive=count)
    elif archtype == NEUTRAL or archtype == ALLNEUTRAL:
        traits = __trait_retrieval(count_neutral=count)
    elif archtype == NEGATIVE or archtype == ALLNEGATIVE:
        traits = __trait_retrieval(count_negative=count)
    return traits
