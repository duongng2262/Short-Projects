# Author: Chip Nguyen
# Date: 11/06/2022
# Purpose: Lab 3 - Visualizing Cities

from quicksort import sort
from cs1lib import *

NO_CITIES = 50
WINDOW_HEIGHT = 180
WINDOW_WIDTH = 360

# Opens the file with cities sorted by order of decreasing population
in_file = open("cities_population.txt", "r")
cities_list = []

for line in in_file:
    line.strip()
    city_list = line.split(",")
    cities_list.append([city_list[0], int(city_list[1]), float(city_list[2]), float(city_list[3])])

in_file.close

counter = 0 # Counts how many cities have been visualized

# Load background image
background_img = load_image("world.png")

def draw_map():
    global counter
    clear()
    draw_image(background_img, 0, 0)
    set_fill_color(0, 1, 0)

    for i in range(0, counter):
        y = 2 * cities_list[i][2] # Gets the y-coordinate from the latitude
        x = 2 * cities_list[i][3] # Gets the x-coordinate from the longitude
        draw_circle(WINDOW_WIDTH + x, WINDOW_HEIGHT - y, 3)

    # Update the counter until all the cities have been added
    if counter < NO_CITIES:
        counter = counter + 1

start_graphics(draw_map, width = 720, height = 360)