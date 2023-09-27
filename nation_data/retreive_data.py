import geopandas as gpd
import json

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
        #print(year)
        if year == 1910 or year == 1914 or year == 1918:
            self.geo_file = gpd.read_file("C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/json_fiels/world_1914.geojson").explode()
        if year == 1932 or year == 1936:
            self.geo_file = gpd.read_file("C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/json_fiels/world_1930.geojson").explode()
        if year == 1939:
            self.geo_file = gpd.read_file("C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/json_fiels/world_1938.geojson").explode()
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
        with open('C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json', 'w') as clear_file:
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
            """for i in range(0, len(self.nation_dictionary)):
                print(self.nation_dictionary[i]['nation_name'])"""
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
            print(e.__str__())
        finally:
            #print('hi')
            self.push_to_json_file()
    def push_to_json_file(self):
        try:
            with open('C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json',
                      'r') as nation:
                nation_object = json.loads(nation.read())

            nation_object['countries'] = self.nation_dictionary
            # sets/appends nation_dictionary to 'countries' list
            with open('C:/Users/wilbu/OneDrive/Desktop/Capstone_Project/nation_data/nation.json',
                      'w') as writing_file:
                json.dump(nation_object, writing_file, indent=4)

        except Exception as e:
            print(e.args)
"""json_object = JsonWriter(1914)
json_object.clear_old_file()"""
