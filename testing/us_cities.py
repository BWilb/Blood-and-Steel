class UsCities:
    def __init__(self, population, north, north_east, east, south_east, south, south_west,
                 west, north_west, population_growth):
        self.population = population
        self.growth = population_growth
        self.north = north
        self.ne = north_east
        self.east = east
        self.se = south_east
        self.south = south
        self.sw = south_west
        self.west = west
        self.nw = north_west

cities = ["Anchorage", "Honolulu", "Seattle", ""]
""" in order from west coast(Hawaii and Alaksa included) to East Coast
    will only incorporate capitals so far
"""
