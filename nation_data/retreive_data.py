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
            self.geo_file = gpd.read_file("C:/Users/wilbu/Desktop/Capstone-Project/nation_data/json_fiels/world_1914.geojson").explode()
        if year == 1932 or year == 1936:
            self.geo_file = gpd.read_file("C:/Users/wilbu/Desktop/Capstone-Project/nation_data/json_fiels/world_1930.geojson").explode()
        if year == 1939:
            self.geo_file = gpd.read_file("C:/Users/wilbu\Desktop/Capstone-Project/nation_data/json_fiels/world_1938.geojson").explode()
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
        with open(r"C:\Users\wilbu\Desktop\Capstone-Project\nation_data\nation.json", 'w') as clear_file:
            clear_file.write(self.json_cleaner)

        self.writing_new_info()

    def writing_new_info(self):
        # re-writes information to json file
        try:
            coordinates = []

            for index, row in self.geo_file.iterrows():
                coordinates.append(list(row['geometry'].exterior.coords))
                self.nation_dictionary.append({
                    'index': index[0],
                    'nation_name': row['NAME'],
                    'coordinates': list(row['geometry'].exterior.coords)
                })

        except Exception as e:
            print(e.__str__())
        finally:
            #print('hi')
            self.push_to_json_file()
    def push_to_json_file(self):
        try:
            with open('C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json',
                      'r') as nation:
                nation_object = json.loads(nation.read())

            nation_object['countries'] = self.nation_dictionary
            # sets/appends nation_dictionary to 'countries' list
            with open('C:/Users/wilbu/Desktop/Capstone-Project/nation_data/nation.json',
                      'w') as writing_file:
                json.dump(nation_object, writing_file, indent=4)

        except Exception as e:
            print(e.args)
"""json_object = JsonWriter(1918)
json_object.clear_old_file()"""
