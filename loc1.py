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

loc = Location()
loc.setPosition(-33.8, 151.2)

print(loc.getLat())
print(loc.getLong())
