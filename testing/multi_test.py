import json
from shapely.geometry import MultiPolygon

"""def extract_coordinates(json_data):
    coordinates = []

    # Load JSON data
    data = json.loads(json_data)

    # Convert to MultiPolygon using Shapely
    multi_polygon = MultiPolygon(data['coordinates'])

    if multi_polygon.geom_type == 'MultiPolygon':
        for polygon in multi_polygon:
            if polygon.geom_type == 'Polygon':
                for point in polygon.exterior.coords:
                    coordinates.append(point)

    return coordinates

extracted_coordinates = extract_coordinates(json_data)
print(extracted_coordinates)"""