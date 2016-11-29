#!/usr/bin/python
pi = 3.141593
radius = 0
while True:
    rad = input("Please enter the radius of a circle: ")
    if rad.isdigit():
        radius = int(rad)
        break
    else:
        print("Please use only digits in the radius!")


diameter = radius * 2
circumference = diameter * pi
area = pi * radius ** 2
sphereVol = 4/3 * pi * radius ** 3

print("\n%-30s %-5.2fcm" % ("A circle with a radius of ", radius))
print("%-30s %5.2fcm" % ("has a diameter of ", diameter))
print("%-30s %5.2fcm" % ("a circumference of ", circumference))
print("%-30s %5.2fcm square" % ("an area of ", area))
print("%-30s %5.2fcm cubed." % ("and a spherical Volume of ", sphereVol))