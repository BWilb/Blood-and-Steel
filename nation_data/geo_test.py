import geopandas as gpd
import numpy as np

# Load the GeoJSON file
gdf = gpd.read_file("json_fiels/world_1914.geojson")
print(gdf.head())
dictionary = []
for index, row in gdf.iterrows():
    name = row['NAME']  # Access an attribute
    geometry = row['geometry']  # Access the geometry

    # print(f"Feature {index}: {name}, {geometry}")
    print(name, "", geometry)


    dictionary.append(name)

"""for i in range(0, len(dictionary)):
    print(dictionary[i])
    if not np.isnan(dictionary[i]):
        dictionary.pop(i)

"""
import numpy as np

original_list = [1.0, 2.0, np.nan, 4.0, 5.0]
print(original_list)

result_list = [x for x in original_list if not np.isnan(x)]

print(result_list)