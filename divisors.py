#!/usr/bin/python

i = 0

while i == 0:
    num = int(input("Please enter a positive integer between 2 and 65535: "))
    if 1 < num <= 65535:
        i += 1
    else:
        print(num, "is outside the specified range")

j = 2

while 1 < j <= (num / 2):
    if (num % j) == 0:
        print(j, end=' ')

    j += 1

print("\n")
