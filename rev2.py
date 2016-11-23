#!/usr/bin/python

sentence = input("Please enter a sentence: ")
words = sentence.split(' ')

i = len(words) - 1

while i >= 0:
    print(words[i], end=' ')
    i -= 1
