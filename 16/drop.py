# Removes every N'th element from a list
def drop(my_list, n):
    items_to_remove = [
        e - 1 for e in range(0, len(my_list)) if e % n == 0 and e > 0
    ]

    items_to_remove = sorted(items_to_remove, reverse=True)

    # tbd = To Be Deleted
    for tbd in items_to_remove:
        del my_list[tbd]
    return my_list


# Tests
print(drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 3))
