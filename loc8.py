#!/usr/bin/python


class Location:
    # Methods
    def __init__(self):
        self.lat = 0.0
        self.long = 0.0

    def setPosition(self, lat, long):
        self.lat = lat
        self.long = long

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long

    def printMe(self):
        # print("The Location is \(%5.2f, 5.2f\)" % (self.lat, self.long))
        print("The Location is (", self.lat, ", ", self.long, ")")

loc = Location()

print(loc.getLat())
print(loc.getLong())
loc.printMe()


