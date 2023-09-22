"""import geopandas as gpd

# Load your GeoJSON data into a GeoDataFrame
gdf = gpd.read_file('../nation_data/custom.geo (3).json')  # Replace with the path to your GeoJSON file

# Use explode to convert MultiPolygons into individual polygons
individual_polygons = gdf.explode()
for i in range(0, len(gdf)):
    if "MultiPolygon" in gdf['geometry']:
        print(gdf['geometry'][i])
    else:
        print('none')

# Print the resulting GeoDataFrame with individual polygons
print(individual_polygons)"""
import time

import pyautogui

"""import geopandas as gpd
import shapely.geometry as sg

# Load your GeoJSON data into a GeoDataFrame
gdf = gpd.read_file('../nation_data/custom.geo (3).json')  # Replace with the path to your GeoJSON file"""
"""print(gdf.head())
print(gdf['geometry'][4])"""
"""print(len(gdf))
individual = gdf.explode()
print(len(individual))
for id in range(0, len(individual['name']) - 1):"""
# print(individual['name'][id], individual['geometry'][id])
""" if individual['name'][id] == "Kazakhstan":
    for coords in range(0, len(individual['geometry'][id])):
        print()"""
# print(individual['name'][id].any())
# print(individual['name'][id], individual['geometry'][id])
"""print(len(individual['geometry'][id]))
time.sleep(0.5)"""
# for j in range(0, id):
# print(individual['id'])
# print(individual)
i = 0
# name = individual['id'][0]
# print(name)
"""for geom in individual['name']:
    if geom == "American Samoa":
        print(individual['geometry'][i])
    i += 1"""
# Extract individual polygons from MultiPolygons
individual_polygons = []
"""for geom in gdf['geometry']:
    print(geom.geom_type)"""

# if geom.geom_type == 'MultiPolygon':
"""for i in range(0, len(individual['name'])):
    print(individual[i])"""

"""individual_polygons.extend(geom)
else:
individual_polygons.append(geom)"""

# Create a list of Shapely Polygon objects
# shapely_polygons = [sg.Polygon(p.exterior.coords) for p in individual_polygons]

# Now, you have a list of Shapely Polygon objects
"""for polygon in shapely_polygons:
    print(polygon)"""

def convert_coords(lon, lat):
    # lon is x
    # lat is y
    WIDTH = pyautogui.size().width
    HEIGHT = pyautogui.size().height
    lon_min, lon_max = -180, 180
    lat_min, lat_max = -90, 90
    x = ((lon - lon_min) / (lon_max - lon_min)) * WIDTH
    y = HEIGHT - ((lat - lat_min) / (lat_max - lat_min)) * HEIGHT
    return int(x), int(y)

import geopandas as gpd

# Load the GeoJSON data
gdf = gpd.read_file('../nation_data/custom.geo (3).json')


# Define the nation name you want to search for
target_nation = 'Russia'  # Replace with the nation you're interested in

# Filter the GeoDataFrame to get the specific nation
nation_data = gdf[gdf['name'] == target_nation]

# Extract the coordinates as a list
coordinates = []
# coordinates represents the entire list of polygons within nation

print(nation_data.geometry)
for geometry in nation_data.geometry.explode():
    if geometry.geom_type == 'Polygon':
        coordinates.append(list(geometry.exterior.coords))
    elif geometry.geom_type == 'MultiPolygon':
        for polygon in geometry:
            coordinates.append(list(polygon.exterior.coords))

# Print the extracted coordinates
coords = []
for outer_coords in range(0, len(coordinates)):
    #print(coordinates[outer_coords])
    points = []
    # outer coords represent the entire list of coordinates within each polygon
    for inner_coords in range(0, len(coordinates[outer_coords])):
        #pass
        points.append(convert_coords(coordinates[outer_coords][inner_coords][0], coordinates[outer_coords][inner_coords][1]))

        #print(i, coordinates[outer_coords][inner_coords][0], coordinates[outer_coords][inner_coords][1])
        #for index, row in range(0, len(coordinates[outer_coords][inner_coords])):
            #print()
    coords.append(points)

print(coords[0])


import pygame
#import pyautogui
WIDTH = pyautogui.size().width
HEIGHT = pyautogui.size().height * 0.9

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
    for i in range(0, len(coords)):
        pygame.draw.polygon(screen, (0, 222, 224), coords[i])
# Handle other geometry types as needed

    pygame.display.flip()
pygame.quit()

"""
extracting coordinates from geojson based upon nation name, using json, geopandas, and python
ChatGPT
"""