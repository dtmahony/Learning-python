#!/usr/bin/python

notPrime = True
num = 1000004

while notPrime:
    divisors = 0
    j = 2
    while 1 < j <= (num / 2):
        if (num % j) == 0:
            divisors += 1
            break
        else:
            j += 1
            continue

    if divisors == 0:
        notPrime = False
    else:
        num += 1

print("The first prime greater than 1,000,003 is:", num)
