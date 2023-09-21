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

import geopandas as gpd

# Load the GeoJSON data
gdf = gpd.read_file('../nation_data/custom.geo (3).json').explode()


# Define the nation name you want to search for
target_nation = 'Netherlands'  # Replace with the nation you're interested in

# Filter the GeoDataFrame to get the specific nation
nation_data = gdf[gdf['name'] == target_nation]

# Extract the coordinates as a list
coordinates = []
# coordinates represents the entire list of polygons within nation

for geometry in nation_data.geometry:
    if geometry.geom_type == 'Polygon':
        coordinates.append(list(geometry.exterior.coords))
    elif geometry.geom_type == 'MultiPolygon':
        for polygon in geometry:
            coordinates.append(list(polygon.exterior.coords))

# Print the extracted coordinates
for outer_coords in range(0, len(coordinates)):
    #print(coordinates[outer_coords])
    # outer coords represent the entire list of coordinates within each polygon
    for inner_coords in range(0, len(coordinates[outer_coords])):
        print(coordinates[outer_coords][inner_coords][0], coordinates[outer_coords][inner_coords][1])
        #for index, row in range(0, len(coordinates[outer_coords][inner_coords])):
            #print()

"""
extracting coordinates from geojson based upon nation name, using json, geopandas, and python
ChatGPT
"""