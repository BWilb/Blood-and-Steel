import geopandas as gpd
import json
class JsonWriter:
    def __init__(self):
        """if year < 1918:
            self.geo_file = gpd.read_file("../nation_data/world_1914.geojson").explode()
        elif year >= 1918 and year <= 1937:
            self.geo_file = gpd.read_file("../nation_data/world_1920.geojson").explode()

        else:
            self.geo_file = gpd.read_file("../nation_data/world_1938.geojson").explode()"""
        self.geo_file = gpd.read_file('../nation_data/custom.geo (3).json').explode()
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
        with open('/nation_data/json_fiels/nation.json', 'w') as clear_file:
            clear_file.write(self.json_cleaner)

        self.writing_new_info()

    def writing_new_info(self):
        names = self.geo_file['name'].unique()
        i = 0
        for name in names:
            nation_subset = self.geo_file[self.geo_file['name'] == name]
            # subset of data set that extracts columns based upon the name of the nation(row)
            national_coordinates = []

            for idx, row in nation_subset.iterrows():
                geometry = row['geometry']
                coords = list(geometry.exterior.coords)
                #print(coords)
                national_coordinates.append(coords)

            self.nation_dictionary.append({
                'nation_id': i,
                'nation_name': name,
                'coordinates': national_coordinates
            })

            i += 1
        for i in range(0, len(self.nation_dictionary)):
            print(self.nation_dictionary[i])
        with open('/nation_data/json_fiels/nation.json', 'r') as nation:
            nation_json = json.loads(nation.read())

        nation_json['countries'] = self.nation_dictionary
        with open('/nation_data/json_fiels/nation.json', 'w') as writing_file:
            json.dump(nation_json, writing_file, indent=4)

json_object = JsonWriter()
json_object.clear_old_file()