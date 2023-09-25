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
class JsonWriter:
    def __init__(self):
        self.geo_file = gpd.read_file("../nation_data/world_1914.geojson").explode()
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
            for index, row in self.geo_file.iterrows():
                #print(list(row['geometry'].exterior.coords))
                self.nation_dictionary.append({
                    'index': index[0],
                    'nation_name': row['NAME'],
                    'coordinates': list(row['geometry'].exterior.coords)
                })
            print(len(self.nation_dictionary))
            for i in range(0, len(self.nation_dictionary)):
                print(self.nation_dictionary[i])

        except Exception as e:
            print(e)

json_object = JsonWriter()
json_object.clear_old_file()