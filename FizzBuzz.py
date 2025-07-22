DIVISIBLE_BY_3_OUTPUT = "Fizz"
DIVISIBLE_BY_5_OUTPUT = "Buss"
DIVISIBLE_BY_BOTH_OUTPUT = DIVISIBLE_BY_3_OUTPUT+DIVISIBLE_BY_5_OUTPUT

def fizzbuzz(start, end):
    """
    Prints numbers from start to end.
    Prints DIVISIBLE_BY_3_OUTPUT for multiples of 3,
    DIVISIBLE_BY_5_OUTPUT for multiples of 5,
    DIVISIBLE_BY_BOTH_OUTPUT for multiples of both.
    """
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(DIVISIBLE_BY_BOTH_OUTPUT)
        elif i % 3 == 0:
            print(DIVISIBLE_BY_3_OUTPUT)
        elif i % 5 == 0:
            print(DIVISIBLE_BY_5_OUTPUT)
        else:
            print(i)

fizzbuzz(1, 100) # fizzbuzz(start, end)
