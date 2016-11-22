#!/usr/bin/python
pi = 3.141593

radius = int(input("Please enter the radius of a circle: "))
diameter = radius * 2
circumference = diameter * pi
area = pi * radius ** 2
sphereVol = 4/3 * pi * radius ** 3

print("\nA circle with a radius of %.3f cm" % radius)
print("has a diameter of %.3f cm" % diameter)
print("a circumference of %.3f cm" % circumference)
print("an area of %.3f cm square" % area)
print("and a spherical Volume of %.3f cm cubed." % sphereVol)
