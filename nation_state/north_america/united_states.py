leaders = {
    "1910" : "William Howard Taft",
    "1914" : "Woodrow Wilson",
    "1918" : "Woodrow Wilson",
    "1932" : "Herbert Hoover",
    "1936" : "Franklin D. Roosevelt",
    "1939" : "Franklin D. Roosevelt"
}

population = {
    "1910": 92410000,
    "1914": 99110000,
    "1918": 103210000,
    "1932": 124840000,
    "1936": 128050000,
    "1939": 130880000
}
class UnitedStates:
    def __init__(self, year):
        self.leader = leaders[year]
        self.population = population[year]
        # leader isn't initialized until time_frame is established.

    def printmetrics(self):
        print(self.population)