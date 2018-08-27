from itertools import combinations


# Generates combinations of x objects from a list
def make_combos(length, the_list):
    return list(combinations(the_list, length))


# Tests
print(
    make_combos(
        2, ['North', 'South', 'East', 'West']))
