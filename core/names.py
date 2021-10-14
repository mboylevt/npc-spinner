import os
import random

from core import globals

def generate_name(race, gender):
    """
    Generate a name based on a race and sex
    :param race: race to generate.  Enumerated in globals
    :param gender: sex to generate.  Male or Female (sorry :( )
    :type race: str
    :type gender: str
    :return: First and Last name in list
    """

    # raise BaseException(os.getcwd())
    if os.getcwd() == '/app':
        base_path = '.'
    else:
        base_path = '..'

    if gender == globals.NONBINARY:
        with open(os.path.join(base_path, 'core', 'data', 'races', race,
                               'first_male.txt')) as f: first_names = f.readlines()
        with open(os.path.join(base_path, 'core', 'data', 'races', race,
                               'first_female.txt')) as f: first_names.extend(f.readlines())

    else:
        with open(os.path.join(base_path, 'core', 'data', 'races', race, 'first_{}.txt'.format(gender))) as f: first_names = f.readlines()

    with open(os.path.join(base_path, 'core', 'data', 'races', race, 'last.txt')) as f: last_names = f.readlines()

    return {
        'first': first_names[random.randint(0, len(first_names)-1)].rstrip(),
        'last': last_names[random.randint(0, len(last_names)-1)].rstrip()
    }
