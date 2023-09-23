import pyautogui


def retreive_coords(coords_list):
    all_coordinates = []
    if len(coords_list) == 1:
        for points in coords_list:
            # print(points)
            for index, row in points:
                all_coordinates.append(convert_coords(index, row))
            # print(coordinates)
        return all_coordinates
    else:

        for points in coords_list:
            coordinates = []  # Create a list to store sets of coordinates for each point

            if isinstance(points, list):
                for index, row in points:
                    coordinates.append(convert_coords(index, row))
            else:
                coordinates.append(convert_coords(points[0], points[1]))

            all_coordinates.append(coordinates)  # Append the list of coordinates to the result
        print(all_coordinates)

        return all_coordinates

    """code taken from ChatGPT for solving how to draw multipolygons
    command = {improve this code:
    
    def retreive_coords(coords_list):
    coordinates = []
    if len(coords_list) == 1:
        for points in coords_list:
            #print(points)
            for index, row in points:
                coordinates.append(convert_coords(index, row))
            # print(coordinates)
            return coordinates
    elif len(coords_list) > 1:
        bigger_coords_list = []
        lists = []
        for points in range(0, len(coords_list)):
            lists.append(coords_list[points])
        #print(coordinates)
        for indice in range(0, len(lists)):
            print("hi")
            for point in range(0, len(lists[indice])):
                #print(lists[indice][point])
                #print(lists[indice][point])
                coordinates += (convert_coords(lists[indice][point][0], lists[indice][point][1]))
            bigger_coords_list.append([coordinates])
            print(bigger_coords_list)
        }
    """


def convert_coords(lon, lat):
    # taken from ChatGPT
    # lon is x
    # lat is y
    WIDTH = pyautogui.size().width
    HEIGHT = pyautogui.size().height
    lon_min, lon_max = -180, 180
    lat_min, lat_max = -90, 90
    x = ((lon - lon_min) / (lon_max - lon_min)) * WIDTH
    y = HEIGHT - ((lat - lat_min) / (lat_max - lat_min)) * HEIGHT
    return int(x), int(y)
