#!/usr/bin/python

nums = []
enter = True

while enter:
    num = input("Please enter some numbers: ")
    if num == "":
        enter = False
    else:
        nums.append(int(num))


total = 0
i = 0
while i < len(nums):
    total += nums[i]
    i += 1

print("\nThe average of these three numbers is", total/len(nums))
