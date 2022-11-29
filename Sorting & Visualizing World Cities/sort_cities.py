# Author: Chip Nguyen
# Date: 11/06/2022
# Purpose: Lab 3 - Sorting Cities

from quicksort import *
from city import City

# Function for comparing names of 2 cities
def compare_name(city1, city2):
    return city1.name.lower() <= city2.name.lower()

# Function for comparing the populations of 2 cities
def compare_population(city1, city2):
    return city1.population >= city2.population

# Function for comparing the latitudes of 2 cities
def compare_latitude(city1, city2):
    return city1.latitude <= city2.latitude

# Opens the master file
in_file = open("world_cities.txt", "r")

# Create a list containing all city objects
city_object_list = []

for line in in_file:
    line.strip() # Remove white space
    city_list = line.split(",") # Create a list containing the pieces of information for each city

    # Create a city object for city corresponding to each line in the text file
    # and add this object to the list of all city objects.
    city_object = City(city_list[0], city_list[1], city_list[2], str(city_list[3]), str(city_list[4]), str(city_list[5]))
    city_object_list.append(city_object)

in_file.close()

# Function that write separate lines for the city objects in the list and does not add a new line after the last line
def write_file(list, file):
    for i in range(len(list)):
        # As long as the object is not last in the list, create a new line below
        if i < len(list) - 1:
            file.write(str(list[i]) + "\n")
        # If the object is last in the list, do not create a new line
        else:
            file.write(str(list[i]))

# Sort the cities in alphabetical order and write to file cities_alpha.txt
in_file1 = open("cities_alpha.txt", "w")
sort(city_object_list, compare_name)
write_file(city_object_list, in_file1)
in_file1.close()

# Sort the cities in order of decreasing population and write to file cities_population.txt
in_file2 = open("cities_population.txt", "w")
sort(city_object_list, compare_population)
write_file(city_object_list, in_file2)
in_file2.close()

# Sort the cities in order of decreasing population and write to file cities_population.txt
in_file3 = open("cities_latitude.txt", "w")
sort(city_object_list, compare_latitude)
write_file(city_object_list, in_file3)
in_file3.close()