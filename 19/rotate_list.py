# Rotates a list N palces to the left
def rotate(my_list, places):
    return my_list[places:] + my_list[:places]


# Tests
print(rotate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 3))
print(rotate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], -2))
