dictators = {
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

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}
class Russia:
    def __init__(self, year):
        """Political Variables"""
        self.leader = dictators[year]
        """Population Variables"""
        self.population = population[year]
        """Economic Variables"""
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        # leader isn't initialized until time_frame is established.


def main(time):
    russia = Russia(time)
    print(russia.population)