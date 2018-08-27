from random import choice


# Draws N different random numbers from 1 to max number
def lotto_select(amount, max):
    return [
        choice([x for x in range(1, max)]) for _ in range(0, amount)
    ]


# Tests
print(lotto_select(6, 49))
