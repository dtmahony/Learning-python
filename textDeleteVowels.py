#!/usr/bin/python

data = input("Please enter some text: ")
for vowel in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
    data = data.replace(vowel, "")

print(data)
