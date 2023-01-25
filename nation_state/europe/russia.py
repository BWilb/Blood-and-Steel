leaders = {
    "1910" : "Nicolaus II",
    "1914" : "Nicolaus II",
    "1918" : "Vladimir Lenin",
    "1932" : "Joseph Stalin",
    "1936" : "Joseph Stalin",
    "1939" : "Joseph Stalin"
}

population = {
    "1910": 126200000,
    "1914": 130000000,
    "1918": 136800000,
    "1932": 126000000,
    "1936": 104900000,
    "1939": 109397463
}
class UnitedStates:
    def __init__(self, year):
        self.leader = leaders[year]
        self.population = population[year]
        # leader isn't initialized until time_frame is established.

    def printmetrics(self):
        print(self.population)