# Creates a list containing all integers within a given range
def list_in_range(first, last):
    return [x for x in range(first, last + 1)] if first < last else sorted([
        x for x in range(last, first + 1)], reverse=True)


# Tests
print(list_in_range(4, 9))
print(list_in_range(9, 4))
