#!/usr/bin/python

name = input("What is your name? ")
age = int(input("What is your age? "))

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
