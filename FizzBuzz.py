"""In a language of your choice write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print
"Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"."""

def fizzbuzz(start, end):
    for i in range(start, end + 1):
        # Returns FizzBuzz if number is divisible by 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # Returns Fizz if number is divisible by 3
        elif i % 3 == 0:
            print("Fizz")
        # Returns Buzz if number is divisible by 5
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(1, 100) # fizzbuzz(start, end)
