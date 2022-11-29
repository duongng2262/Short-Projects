# Author: Chip Nguyen
# Date: 11/01/2022
# Purpose: Lab 3 - City Class

class City:
    def __init__(self, code, name, region, population, latitude, longitude):
        self.code = code
        self.name = name
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)


