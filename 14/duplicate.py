# duplicates the elements of a list
def duplicate(elements):
    return [element for element in elements for _ in (0, 1)]


# Tests
print(duplicate(['a', 'b', 'c', 'c', 'd']))
