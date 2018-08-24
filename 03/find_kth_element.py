# Returns k'th element of list
def at(k, elements):
    return elements[
        k] if elements and type(k) == int and k < len(elements) else None


# Tests
print(at(1, ['a', 'b', 'c']))
print(at('a', [1, 2]))
print(at(-1, ['One', 'Two', 'Three', 'Four']))
print(at(5, [0, 1, 0, 1]))
