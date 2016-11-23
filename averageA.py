#!/usr/bin/python
i = 1
nums = []

while i <= 3:
    nums.append(int(input("Please enter 3 numbers: ")))
    i += 1

total = 0
j = 0
while j < 3:
    total += nums[j]
    j += 1

print("\nThe average of these three numbers is", total/3)
