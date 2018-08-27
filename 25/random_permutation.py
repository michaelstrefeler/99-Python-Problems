from itertools import permutations
from random import choice


# Generates a random permutation of the elements in a list
def random_permutation(the_list):
    return choice(list(permutations(the_list, len(the_list))))


# Tests
print(
    random_permutation(
        ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']))
