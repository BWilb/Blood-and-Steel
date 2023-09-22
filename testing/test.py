import enum
import json
import pyautogui
import json as js
from colors.color import Color

"""ith open('../nation_data/nation.json', 'r') as file:
    data = json.load(file)"""
"""WIDTH, HEIGHT = pyautogui.size().width, pyautogui.size().height * 0.9
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
"""
# print(coordinates)

"""import pygame

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
"""
"""for i in range(0, len(data['countries'])):
    print(data['countries'][i]['nation_name'], i)"""
"""import geopandas as gpd

# Load the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file('../nation_data/custom.geo (3).json')

# Iterate over each feature in the GeoDataFrame
for index, row in gdf.iterrows():
    geometry = row['geometry']

    # Check if the geometry is a Polygon
    if geometry.geom_type == 'Polygon':
        polygon = geometry

        # Extract the coordinates of the polygon's exterior ring, if it exists
        if polygon.exterior:
            exterior_coordinates = list(polygon.exterior.coords)

            # Print the exterior coordinates
            print(f"Polygon {index + 1} Exterior Coordinates:")
            for coord in exterior_coordinates:
                print(coord)
        else:
            print(f"Polygon {index + 1} has no exterior coordinates.")
    else:
        print(f"Feature {index + 1} is not a Polygon.")
"""
import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon

# Load the GeoJSON file into a GeoDataFrame (replace 'your_multipolygon.geojson' with your file)
gdf = gpd.read_file('../nation_data/custom.geo (3).json')

# Use the explode function to convert MultiPolygons into separate rows of Polygons
gdf_exploded = gdf.explode()

# Iterate through the rows of the exploded GeoDataFrame
for index, row in gdf_exploded.iterrows():
    print(index, row['name'], row['geometry'])

    # Extract the coordinates of the polygon's exterior ring


