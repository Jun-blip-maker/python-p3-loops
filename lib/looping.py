#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter >= 1:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def square_integers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
