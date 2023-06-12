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
class Iowa:
    def __init__(self, year):
        """Population variables"""
        self.population = population[str(year)]
        """economic variables"""
        self.gdp = gdp[str(year)]