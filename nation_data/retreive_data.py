import geopandas as gpd
import json
with open("nation.json", 'r') as json_file:
    data = json.load(json_file)
    print(data)
gdf = gpd.read_file("custom.geo (3).json")
dictionary = []
for index, row in gdf.iterrows():
    nation_name = row['name']
    geometry = row['geometry']
    json_number = index
    if geometry.geom_type == 'Polygon':
        coordinates = list(geometry.exterior.coords)
        print(f"Coordinates for Polygon  {coordinates}")

        dictionary.append({
            'nation_id': index,
            'nation_name': nation_name,
            'coordinates': coordinates
        })

with open('nation.json', 'r') as nation:
    nation_object = json.loads(nation.read())

"""nation_object['countries'] = dictionary

with open('nation.json', 'w') as writing_file:
    json.dump(nation_object, writing_file, indent=4)"""
print(nation_object['countries'][0])