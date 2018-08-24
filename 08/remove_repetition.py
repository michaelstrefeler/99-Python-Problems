# Removes consecutive duplicates from a list
def compress(my_list):
    z = 0
    while z < 2:
        x = 0
        for i in my_list:
            if x == 0:
                if len(my_list) >= 2 and my_list[0] == my_list[1]:
                    del my_list[x]
            else:
                if i == my_list[x - 1]:
                    del my_list[x]
            x += 1
        z += 1
    return my_list


# Tests
print(compress(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e']))
