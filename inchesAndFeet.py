#!/usr/bin/python

print("Inches", " " * 2, "Feet/Inches", " " * 2, "Centimetres")
i = 1
while i <= 20:
    print("%2i" % i, " " * 5, "%2i/%2i" % (i/12, i % 12), " " * 5, "%10.2f" % (2.54 * i))
    i += 1
