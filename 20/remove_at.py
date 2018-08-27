# Removes element of list with given input.
# REALLY?? how is this even a problem? Python 2 OCaml 0


def remove_at(index, my_list):
    del my_list[index]
    return my_list


# Tests
print(remove_at(1, [1, 2, 3, 4]))
