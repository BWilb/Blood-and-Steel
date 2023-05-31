# political variables and dictionaries
from datetime import datetime

monarchs = {
    """Dictionary for english monarchs
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "Edward VII",
    "1914": "George V",
    "1918": "George V",
    "1932": "George V",
    "1936": "Edward VIII",
    "1939": "George VI"
}

pm = {
    "1910": "H.H. Asquith",
    "1914": "H.H. Asquith",
    "1918": "David Lloyd George",
    "1932": "Ramsay MacDonald",
    "1936": "Stanley Baldwin",
    "1939": "Neville Chamberlain"
}

# population variables and dictionaries
population = {
    """Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""

    "1910": 44915900,
    "1914": 42956900,
    "1918": 39582000,
    "1932": 46335000,
    "1936": 47081300,
    "1939": 46029200
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}

tax_rate = {
    "1910": 10.0,
    "1914": 50.0,
    "1918": 80.0,
    "1932": 60.0,
    "1936": 60.0,
    "1939": 80.0
}
class Britain:
    def __init__(self, time):
        """time variables"""
        self.date = datetime(int(time), 1, 1)
        """Political variables"""
        self.monarch = monarchs[time]
        self.pm = pm[time]

        """economic variables"""
        self.current_gdp = gdp[time]
        self.past_gdp = self.current_gdp
        """population variables"""
        self.current_pop = population[time]
        self.past_pop = self.current_pop
        # leader isn't initialized until time_frame is established.


"""def main(time):
    britain = Britain(time)
    print(britain.population)"""
