import pyautogui
def convert_coords(lon, lat):
    # lon is x
    # lat is y
    WIDTH = pyautogui.size().width
    HEIGHT = pyautogui.size().height
    lon_min, lon_max = -180, 180
    lat_min, lat_max = -90, 90
    x = ((lon - lon_min) / (lon_max - lon_min)) * WIDTH
    y = HEIGHT - ((lat - lat_min) / (lat_max - lat_min)) * HEIGHT
    return int(x), int(y)