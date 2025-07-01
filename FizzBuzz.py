# Prints number 1 to 100 


def fizzbuzz(start, end):
    for i in range(start, end + 1):
        # returns FizzBuzz 
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(1, 100)