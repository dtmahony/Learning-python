#!/usr/bin/python
pi = 3.141593

radius = int(input("Please enter the radius of a circle: "))
diameter = radius * 2
circumference = diameter * pi
area = pi * radius ** 2
sphereVol = 4/3 * pi * radius ** 3

print("\nA circle with a radius of %5.2fcm" % radius)
print("has a diameter of \t\t\t%5.2fcm" % diameter)
print("a circumference of \t\t\t%5.2fcm" % circumference)
print("an area of \t\t\t\t\t%5.2fcm square" % area)
print("and a spherical Volume of \t%5.2fcm cubed." % sphereVol)
