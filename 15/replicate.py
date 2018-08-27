from itertools import chain


# replicates the elements of a list x times
def replicate(elements, x):
    return list(chain(*[[e] * x for e in elements]))


# Tests
print(replicate(['a', 'b', 'c'], 3))
