#!/usr/bin/python

name = input("What is your name? ")

i = 0

while i == 0:
    age = int(input("What is your age? "))
    if 0 < age < 120:
        i += 1
    else:
        print("Your age should be between 0 and 120. Please try again.")

if name == "Dan":
    print("Welcome, oh wise and noble one! Your age is only ", age, "!")
else:
    print("Hello, ", name, "!")
    if age > 45:
        print("My, you must be so wise!")
    else:
        if age == 21:
            print("The Perfect age!")
        print("You're just a spring chicken!")
