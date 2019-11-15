import random

POSITIVE = 'Positive' # 3 positive, 1 neutral, 1 negative
NEUTRAL = 'Neutral' # 1 positive, 3 neutral, 1 negative
NEGATIVE = 'Negative' # 1 positive, 1 neutral, 3 negative


with open('../data/traits/positive.txt') as f: positive_traits = f.readlines()
with open('../data/traits/neutral.txt') as f: neutral_traits = f.readlines()
with open('../data/traits/negative.txt') as f: negative_traits = f.readlines()

archtype = NEGATIVE

traits = []
if archtype == POSITIVE:
    traits.append(positive_traits[random.randint(0,len(positive_traits)-1)])
    traits.append(positive_traits[random.randint(0, len(positive_traits)-1)])
    traits.append(positive_traits[random.randint(0, len(positive_traits)-1)])
    traits.append(neutral_traits[random.randint(0, len(neutral_traits)-1)])
    traits.append(negative_traits[random.randint(0, len(negative_traits)-1)])
elif archtype == NEUTRAL:
    traits.append(positive_traits[random.randint(0,len(positive_traits)-1)])
    traits.append(neutral_traits[random.randint(0, len(neutral_traits)-1)])
    traits.append(neutral_traits[random.randint(0, len(neutral_traits)-1)])
    traits.append(neutral_traits[random.randint(0, len(neutral_traits)-1)])
    traits.append(negative_traits[random.randint(0, len(negative_traits)-1)])
elif archtype == NEGATIVE:
    traits.append(positive_traits[random.randint(0,len(positive_traits)-1)])
    traits.append(neutral_traits[random.randint(0, len(neutral_traits)-1)])
    traits.append(negative_traits[random.randint(0, len(negative_traits)-1)])
    traits.append(negative_traits[random.randint(0, len(negative_traits)-1)])
    traits.append(negative_traits[random.randint(0, len(negative_traits)-1)])

print("{} NPC:".format(archtype))
for trait in traits:
    print("\t{}".format(trait).rstrip())