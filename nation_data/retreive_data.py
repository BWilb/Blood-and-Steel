import geopandas as gpd
import json

"""json_cleaner = '''
                                {
                                    "countries": []
                                }
                            '''

with open('nation.json', 'w') as clear_file:
    clear_file.write(json_cleaner)

with open("nation.json", 'r') as json_file:
    data = json.load(json_file)
print(data)

gdf = gpd.read_file("custom.geo (3).json")

dictionary = []
# dictionary stores the wanted information as dictionaries
for index, row in gdf.iterrows():
    nation_name = row['name']
    geometry = row['geometry']
    if geometry.geom_type == 'Polygon':
        coordinates = list(geometry.exterior.coords)

        dictionary.append({
            'nation_id': index,
            'nation_name': nation_name,
            'coordinates': coordinates
        })

with open('nation.json', 'r') as nation:
    nation_object = json.loads(nation.read())

nation_object['countries'] = dictionary

with open('nation.json', 'w') as writing_file:
    json.dump(nation_object, writing_file, indent=4)

"""
from coordination.retreive_and_convert import convert_coords

"""class JsonWriter:
    def __init__(self):
        self.geo_file = gpd.read_file("custom.geo (3).json")
        # file stores geographic and geopolitical information on nations
        self.json_cleaner = '''
                                {
                                    "countries": []
                                }
                            '''
        # variable cleans out old file and replaces it with what it is assigned with
        self.nation_dictionary = []
        # list stores nation info as dictionary

    def clear_old_file(self):
        # clears current file
        with open('nation.json', 'w') as clear_file:
            clear_file.write(self.json_cleaner)

        self.writing_new_info()
    def handle_polygons(self, geometry):
        coordinates = list(geometry)
        # creating a list of coordinates
        coords = []
        for index, row in coordinates:
            coords.append(convert_coords(index, row))
            # coords list appends
        #return coords
        pass

    def handle_multi_polygons(self):
        pass

    def writing_new_info(self):
        # re-writes information to json file
        for index, row in self.geo_file.iterrows():

            nation_name = row['name']
            # print(nation_name)
            geometry = row['geometry']
            # print(geometry)
            coordinates = []
            if geometry.geom_type == 'Polygon':
                coordinates.append(self.handle_polygons(geometry))
                # extracts the coordinates of every nation through handle_polygons function; if polygon

            elif geometry.geom_type == "MultiPolygon":
                coordinates.append(self.handle_polygons(geometry.explode()))


            self.nation_dictionary.append({
                'nation_id': index,
                'nation_name': nation_name,
                'geometry': coordinates
            })

        with open('nation.json', 'r') as nation:
            nation_object = json.loads(nation.read())

        nation_object['countries'] = self.nation_dictionary
        # sets/appends nation_dictionary to 'countries' list
        with open('nation.json', 'w') as writing_file:
            json.dump(nation_object, writing_file, indent=4)


json_object = JsonWriter()
json_object.writing_new_info()"""
from shapely.geometry import MultiPolygon, Polygon

class JsonWriter:
    def __init__(self):
        self.geo_file = gpd.read_file("custom.geo (3).json")
        # file stores geographic and geopolitical information on nations
        self.json_cleaner = '''
                                {
                                    "countries": []
                                }
                            '''
        # variable cleans out old file and replaces it with what it is assigned with
        self.nation_dictionary = []
        # list stores nation info as dictionary

    def clear_old_file(self):
        # clears current file
        with open('nation.json', 'w') as clear_file:
            clear_file.write(self.json_cleaner)

        self.writing_new_info()

    def writing_new_info(self):
        # re-writes information to json file
        for index, row in self.geo_file.iterrows():
            geometry = row['geometry']
            multipolygon = row['geometry']
            if geometry.geom_type == 'Polygon':

                nation_name = row['name']
                polygon = geometry
                if polygon.exterior:
                    print(polygon.exterior.coords)
                    exterior_coords = list(polygon.exterior.coords)

                    self.nation_dictionary.append({
                        'nation_id': index,
                        'nation_name': nation_name,
                        'coordinates': exterior_coords
                    })

        with open('nation.json', 'r') as nation:
            nation_object = json.loads(nation.read())

        nation_object['countries'] = self.nation_dictionary
        # sets/appends nation_dictionary to 'countries' list
        with open('nation.json', 'w') as writing_file:
            json.dump(nation_object, writing_file, indent=4)


json_object = JsonWriter()
json_object.clear_old_file()