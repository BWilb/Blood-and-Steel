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

file_dictionary = {
    1910: "C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/world_1914.geojson",
    1914: "C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/world_1914.geojson",
    1918: "C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/world_1930.geojson",
    1932: "world_1930.geojson",
    1936: "C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/world_1930.geojson",
    1939: "C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/world_1938.geojson"
}

class JsonWriter:
    def __init__(self, year):

        self.geo_file = gpd.read_file("../nation_data/world_1930.geojson").explode()
        # file stores geographic and geopolitical information on nations
        self.json_cleaner = '''
                                {
                                    "countries": []
                                }
                            '''
        # variable cleans out old file and replaces it with what it is assigned with
        self.nation_dictionary = []
        # list stores nation info as dictionary
        print(self.geo_file)

    def clear_old_file(self):
        # clears current file
        with open('C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/json_fiels/nation.json', 'w') as clear_file:
            clear_file.write(self.json_cleaner)

        self.writing_new_info()

    def writing_new_info(self):
        # re-writes information to json file
        """for index, row in self.geo_file.iterrows():
            geometry = row['geometry']
            multipolygon = row['geometry']
            if geometry.geom_type == 'Polygon':
                print(row['name'])

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

                old code; written primarily for polygons
                """
        try:
            coordinates = []

            for index, row in self.geo_file.iterrows():
                coordinates.append(list(row['geometry'].exterior.coords))
                self.nation_dictionary.append({
                    'index': index[0],
                    'nation_name': row['NAME'],
                    'coordinates': list(row['geometry'].exterior.coords)
                })
            print(self.nation_dictionary)

            """
            this piece has self.nation dictionary append the index, name, and coordinates of the specific nation
            this had to be re-written multiple times in order to get it to work
            
            taken from chatGPT edited to what I want it to do
            collecting name, coordinates, and index, from geojson file and dumping into json file
            import geopandas as gpd
            import json
            
            # Load the GeoJSON file
            geojson_file = "your_geojson_file.geojson"
            gdf = gpd.read_file(geojson_file)
            
            # Initialize a list to store the data
            data_list = []
            
            # Iterate through the GeoDataFrame
            for index, row in gdf.iterrows():
                # Extract name, coordinates, and index
                feature_data = {
                    "name": row['name_column'],  # Replace with the actual name column name
                    "coordinates": list(row['geometry'].exterior.coords.xy),  # Replace with the appropriate column name if needed
                    "index": index
                }
                data_list.append(feature_data)
            
            # Define the path for the output JSON file
            json_file = "output.json"
            
            # Write the data to the JSON file
            with open(json_file, "w") as outfile:
                json.dump(data_list, outfile)
            
            print(f"Data saved to {json_file}")
            """

        except Exception as e:
            print(e)
        finally:
            try:
                with open('C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/json_fiels/nation.json', 'r') as nation:
                    nation_object = json.loads(nation.read())


                nation_object['countries'] = self.nation_dictionary
                # sets/appends nation_dictionary to 'countries' list
                with open('C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/json_fiels/nation.json', 'w') as writing_file:
                    json.dump(nation_object, writing_file, indent=4)

            except Exception as e:
                print(e)

"""json_object = JsonWriter(1932)
json_object.clear_old_file()"""
