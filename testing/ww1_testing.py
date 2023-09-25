"""import geopandas as gpd
import pygame

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("GeoJSON MultiPolygon Rendering by Name")

# Replace 'your_geojson_file.geojson' with your GeoJSON file path
geojson_file = '../nation_data/world_1914.geojson'

# Load GeoJSON data into a GeoDataFrame
gdf = gpd.read_file(geojson_file)

# Specify the name (property value) you want to filter by
target_name = 'Belgium'  # Replace with the name you're looking for

# Filter MultiPolygon geometries based on the specified name
filtered_gdf = gdf[gdf['NAME'] == target_name]

# Check if there are any matching MultiPolygons
if not filtered_gdf.empty:
    # Initialize an empty list to store coordinates
    coordinates = []

    # Iterate through the filtered GeoDataFrame
    for index, row in filtered_gdf.iterrows():
        # Extract the MultiPolygon geometry
        multi_polygon = row['geometry']
        if multi_polygon.geom_type == 'Polygon':
            # If it's a single Polygon, extract coordinates
            exterior_coords = list(multi_polygon.exterior.coords)
            coordinates.extend(exterior_coords)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Clear the screen

        # Draw the polygons using extracted coordinates
        pygame.draw.polygon(screen, (0, 0, 255), coordinates)

        pygame.display.update()

# Quit Pygame (outside of the if condition)
pygame.quit()
"""
import geopandas as gpd
import json

from shapely import MultiPolygon, Polygon

from testing.test import multi_polygon


class JsonWriter:
    def __init__(self, year):
        if year < 1918:
            self.geo_file = gpd.read_file("../nation_data/json_fiels/world_1914.geojson").explode()

        elif year >= 1918 and year <= 1936:
            self.geo_file = gpd.read_file("../nation_data/world_1930.geojson").explode()

        else:
            self.geo_file = gpd.read_file("../nation_data/world_1938.geojson").explode()
        # file stores geographic and geopolitical information on nations
        self.json_cleaner = '''
                                {
                                    "countries": []
                                }
                            '''
        # variable cleans out old file and replaces it with what it is assigned with
        self.nation_dictionary = []
        self.convert = None
        # list stores nation info as dictionary

    def clear_old_file(self):
        # clears current file
        with open('nation.json', 'w') as clear_file:
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
            idx = 0

            for index, row in self.geo_file.iterrows():
                coordinates.append(list(row['geometry'].exterior.coords))
                #print(row['NAME'],row['geometry'])

                idx += 1
                self.nation_dictionary.append({
                    'index': index[0],
                    'nation_name': row['NAME'],
                    'coordinates': list(row['geometry'].exterior.coords)
                })
            #print(self.nation_dictionary)
            """for i in range(0, len(self.nation_dictionary)):
                if self.nation_dictionary[i]['nation_name'] == "Russia":
                    print(len(self.nation_dictionary[i]['coordinates']))
                    print(self.nation_dictionary[i]['coordinates'])"""

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
        """finally:
            try:
                with open('nation.json', 'r') as nation:
                    nation_object = json.loads(nation.read())

                nation_object['countries'] = self.nation_dictionary
                # sets/appends nation_dictionary to 'countries' list
                with open('nation.json', 'w') as writing_file:
                    json.dump(nation_object, writing_file, indent=4)

            except Exception as e:
                print(e)"""
jsons = JsonWriter(1920)
jsons.clear_old_file()