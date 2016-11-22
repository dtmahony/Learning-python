#!/usr/bin/python
pi = 3.141593

radius = int(input("Please enter the radius of a circle: "))
diameter = radius * 2
circumference = diameter * pi
area = pi * radius ** 2
sphereVol = 4/3 * pi * radius ** 3

print("\nA circle with a radius of ", radius, "cm")
print("has a diameter of", diameter, "cm")
print("a circumference of ", circumference, "cm")
print("an area of ", area, "cm square")
print("and a spherical Volume of ", sphereVol, "cm cubed.")

