# Returns last two elements in list
def last_two(elements):
    return list(elements[-2:]) if elements and len(elements) >= 2 else None


# Tests
print(last_two([]))
print(last_two(['Hi']))
print(last_two(['Hello', 'World']))
print(last_two([1, 2, 3, 4]))
