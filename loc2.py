#!/usr/bin/python


class Location:
    # Methods
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
loc.setPosition(-33.8, 151.2)

print(loc.getLat())
print(loc.getLong())
loc.printMe()
