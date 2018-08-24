# Returns last element in list
def last(elements):
    return elements[-1] if elements else None


# Tests
print(last([]))
print(last([1]))
print(last(['Hello', 'World']))
print(last([(1, 2), (3, 4)]))
