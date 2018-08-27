# Splits a list into two parts. The length of the first part is given
def split(my_list, x):
    split_lists = []

    split_lists.append(my_list[:x])
    split_lists.append(my_list[x:])
    return split_lists


# Tests
print(split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 3))
print(split(['a', 'b', 'c', 'd'], 5))
