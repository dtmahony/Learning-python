#!/usr/bin/python

print("Inches\tCentimetres")
i = 1
while i <= 20:
    print("%2i" % i, "%10.2f" % (2.54 * i))
    i += 1
