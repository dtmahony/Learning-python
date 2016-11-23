#!/usr/bin/python


sentence = input("Please enter a sentence: ")
words = sentence.split(' ')
list.sort(words)
space = ' '
print(space.join(words))
