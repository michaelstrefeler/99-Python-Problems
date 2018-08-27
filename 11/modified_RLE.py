from itertools import groupby


# Outputs Run-Length Encoding of a list.
# If there are no duplicates the item gets added to the list
# without beign in it's own list
def encode(items):
    output = []
    groups_of_dups = [sum(1 for _ in group) for _, group in groupby(items)]
    for group in groups_of_dups:
        value = items[group - 1]
        if group > 1:
            output.append((group, value))
        else:
            output.append(value)
        items = items[group:]
    return output


# Tests
print(encode(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'd', 'e', 'e', 'e']))
print(encode([1, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4]))
