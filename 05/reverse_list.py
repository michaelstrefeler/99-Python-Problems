# Returns reversed list
def reverse(list):
    return list[::-1]


# Tests
print(reverse([]))
print(reverse([1, 2]))
print(reverse(['Hello', 'World']))
print(reverse([(1, 2), (3, 4)]))
