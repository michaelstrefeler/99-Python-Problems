# Extracts a slice from a list
def slice(my_list, beginning, end):
    return my_list[beginning:end + 1]


# Tests
print(slice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 2, 6))
