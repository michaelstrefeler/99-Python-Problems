# Decode lists made in problem 11
def decode(rle_list):
    output = []
    for item in rle_list:
        if type(item) == tuple:
            number = item[0]
            value = item[1]
            for _ in range(0, number):
                output.append(value)
        else:
            output.append(item)
    return output


# Tests
print(decode([(4, 'a'), 'b', (2, 'c'), 'a', 'd', (3, 'e')]))
print(decode([(5, 1), 2, (3, 3), (2, 4)]))
