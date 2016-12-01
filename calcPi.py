#!/usr/bin/python

iterations = int(input("Please enter the number of iterations: "))
pi = 4

for i in range(1, iterations + 1):
    newb = pow(-1, i)
    pi += newb * (4 / ((i * 2) + 1))
    # print("-1 ** ", i, " = ", newb)

print("The value of Pi is:", pi)
