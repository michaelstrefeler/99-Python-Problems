# Makes nested list into one list
def flatten(nested_list):
    if nested_list == []:
        return nested_list
    if isinstance(nested_list[0], list):
        return flatten(nested_list[0]) + flatten(nested_list[1:])
    return nested_list[:1] + flatten(nested_list[1:])


# Tests
print(flatten([]))
print(flatten(['A', ['B', 'C'], 'D', 'E']))
print(flatten(['A', 'B', 'C']))
print(flatten(['A', ['B', 'C', ['what', 'the', '****']], 'D', 'E']))
