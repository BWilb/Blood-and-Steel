import random

population = {
    "1910": 2229146,
    "1914": 2301256,
    "1918": 2382629,
    "1932": 2488741,
    "1936": 2513360,
    "1939": 2532942
}

gdp = {
    "1910": 6000000,
    "1914": 6193245,
    "1918": 6509000,
    "1932": 6734500,
    "1936": 6796700,
    "1939": 6850000
}
def population_growth(iowa):
    births = random.randrange(10, 25)
    deaths = random.randrange(5, 15)
    iowa.population += (births - deaths)

"""economic_functions"""
def recovery(iowa):
    if iowa.nation.economic_stimulus:
        pass
    else:
        pass
def expansion(iowa):
    if iowa.nation.economic_stimulus:
        pass
    else:
        pass
def recession(iowa):
    if iowa.nation.economic_stimulus:
        pass
    else:
        pass
def deperession(iowa):
    if iowa.nation.economic_stimulus:
        pass
    else:
        pass
def economic_growth(iowa):
    """Economic growth of iowa as individual state"""
    if iowa.economic_state == "recovery":
        recovery(iowa)

class Iowa:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Iowa"
        # establishment of connection to United States
        self.nation = us
        """Population variables"""
        self.population = population[str(year)]
        """economic variables"""
        self.gdp = gdp[str(year)]
        self.consumer_spending = None
        self.government_spending = None
        self.investment = None
        self.exports = None
        self.imports = None
        self.economic_state = "recovery"