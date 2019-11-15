import random

POSITIVE = 'Positive' # 3 positive, 1 neutral, 1 negative
ALLPOSITIVE = 'All Positive' # 35positive
NEUTRAL = 'Neutral' # 1 positive, 3 neutral, 1 negative
ALLNEUTRAL = 'AllNeutral' # 5 neutral
NEGATIVE = 'Negative' # 1 positive, 1 neutral, 3 negative
ALLNEGATIVE = 'AllNegative' # 5 negative


def __trait_retrieval(count_postive, count_neutral, count_negative):
    traits = []
    for x in range(0, count_postive):
        traits.append(positive_traits[random.randint(0, len(positive_traits) - 1)])
    for x in range(0, count_neutral):
        traits.append(neutral_traits[random.randint(0, len(neutral_traits) - 1)])
    for x in range(0, count_negative):
        traits.append(negative_traits[random.randint(0, len(negative_traits) - 1)])
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

with open('../data/traits/positive.txt') as f: positive_traits = f.readlines()
with open('../data/traits/neutral.txt') as f: neutral_traits = f.readlines()
with open('../data/traits/negative.txt') as f: negative_traits = f.readlines()

archtype = ALLNEUTRAL
traits = get_traits(archtype)

print("{} NPC:".format(archtype))
for trait in traits:
    print("\t{}".format(trait).rstrip())


