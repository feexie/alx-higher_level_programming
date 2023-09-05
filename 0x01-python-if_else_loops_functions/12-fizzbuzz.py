#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if (n % 3 == 0 or n % 5 == 0):
            if (n % 3 == 0):
                print("{}".format("Fizz"), end="")
                if (n % 5 == 0):
                    print("{}".format("Buzz"), end="")
                else:
                    print("{}".format(n), end="")
                    print(" ", end="")
