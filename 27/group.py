from itertools import permutations


# Groups the elements of a set into disjoint subsets
def group(the_list, groups):
    output = []
    p = permutations(the_list, groups[0])
    output.append(p)
    return output


# Tests
print(group(['a', 'b', 'c', 'd'], [2, 1]))
