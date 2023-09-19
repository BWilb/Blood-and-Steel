import enum
import json
import pyautogui
import json as js
from colors.color import Color

with open('../nation_data/nation.json', 'r') as file:
    data = json.load(file)
WIDTH, HEIGHT = pyautogui.size().width, pyautogui.size().height * 0.9
for i in range(0, len(data['countries'])):
    print(data['countries'][i]['nation_name'], i)
# print(data['countries'][0]['coordinates'])
coordinates = []
lon_min, lon_max = -180, 180
lat_min, lat_max = -90, 90
def geo_to_pygame(lon, lat):
    x = ((lon - lon_min) / (lon_max - lon_min)) * WIDTH
    y = HEIGHT - ((lat - lat_min) / (lat_max - lat_min)) * HEIGHT
    return int(x), int(y)
for index, row in (data['countries'][94]['coordinates']):
    coordinates.append((geo_to_pygame(index, row)))

# print(coordinates)

import pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Country Map")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with white
    #color = Color()

    pygame.draw.polygon(screen, Color.DEER.value, coordinates)
# Handle other geometry types as needed

    pygame.display.flip()
pygame.quit()

# print((data['countries'][0]['coordinates'][1]))
