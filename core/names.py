import random

def generate_name(race, sex):
    """
    Generate a name based on a race and sex
    :param race: race to generate.  Enumerated in globals
    :param sex: sex to generate.  Male or Female (sorry :( )
    :type race: str
    :type sex: str
    :return: First and Last name in list
    """

    directory = "../data/races/{}/".format(race)
    with open(directory + 'first_{}.txt'.format(sex)) as f: first_names = f.readlines()
    with open(directory + 'last.txt'.format(sex)) as f: last_names = f.readlines()

    return {
        'first': first_names[random.randint(0, len(first_names)-1)].rstrip(),
        'last': last_names[random.randint(0, len(last_names)-1)].rstrip()
    }
