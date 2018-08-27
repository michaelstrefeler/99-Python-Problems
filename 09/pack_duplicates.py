from itertools import groupby


# Packs consecutive duplicates of list elements into sublists
def pack(items):
    output = []
    groups_of_dups = [sum(1 for _ in group) for _, group in groupby(items)]
    for group in groups_of_dups:
        value = items[group - 1]
        output.append([value] * group)
        items = items[group:]
    return output


# Tests
print(pack(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'd', 'e', 'e']))
print(pack([1, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4]))
