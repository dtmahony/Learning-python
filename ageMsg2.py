#!/usr/bin/python
print("Hello, World")

name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello, ", name, ". Your age is", age, "!")

if age > 45:
    print("My, you must be so wise!")
else:
    if age == 21:
        print("The Perfect age!")
    print("You're just a spring chicken!")
