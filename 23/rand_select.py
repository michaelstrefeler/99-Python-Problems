from random import choice


# Extracts a given number of randomly selected elements from a list
def rand_select(the_list, amount):
    return [choice(the_list) for _ in range(0, amount)]


# Tests
print(rand_select(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 3))
