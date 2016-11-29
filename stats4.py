#!/usr/bin/python

print("Please enter numbers - return to finish")

stats = {"total" : 0, "number" : 0, "negative": 0, "positive": 0, "zero" : 0}

while True:
    nextNum = input()
    if nextNum == "":
        break
    else:
        stats["total"] += float(nextNum)
        stats["number"] += 1

        if stats["number"] == 1:
            stats["min"] = float(nextNum)
            stats["max"] = float(nextNum)

        if float(nextNum) < stats["min"]:
            stats["min"] = float(nextNum)

        if float(nextNum) > stats["max"]:
            stats["max"] = float(nextNum)

        if float(nextNum) < 0:
            stats["negative"] += 1

        if float(nextNum) > 0:
            stats["positive"] += 1

        if float(nextNum) == 0:
            stats["zero"] += 1

print("Statistics")
print("-" * 30)
print("%-18s %-5.5f" % ("Total:", stats["total"]), )
print("%-18s %-5.5f" % ("Average:", (stats["total"]/stats["number"])))
print("%-18s %-5i" % ("Minimum:", stats["min"]))
print("%-18s %-5i" % ("Maximum:", stats["max"]))
print("%-18s %-5i" % ("Positive No.s:", stats["positive"]))
print("%-18s %-5i" % ("Negative No.s:", stats["negative"]))
print("%-18s %-5i" % ("Zeros:", stats["zero"]))
