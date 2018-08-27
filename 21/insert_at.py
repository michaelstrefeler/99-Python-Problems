# Inserts an element at a given position into a list
def insert_at(thing, position, the_list):
    the_list = the_list[:position] + [thing] + the_list[position:]
    return the_list


# Tests
print(insert_at('intruder', 1, ['a', 'b', 'c', 'd']))
print(insert_at('intruder', 3, ['a', 'b', 'c', 'd']))
print(insert_at('intruder', 4, ['a', 'b', 'c', 'd']))
