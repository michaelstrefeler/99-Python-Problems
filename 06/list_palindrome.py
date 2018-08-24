# Returns True if list is a palindrome else False
def is_palindrome(list):
    return True if list == list[::-1] else False


# Tests
print(is_palindrome(['n', 'o', 'p', 'e']))
print(is_palindrome(['r', 'a', 'c', 'e', 'c', 'a', 'r']))
print(is_palindrome([1, 2, 3, 2, 1]))
