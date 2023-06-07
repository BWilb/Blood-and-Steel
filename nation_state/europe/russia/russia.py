import random
import time
from datetime import datetime, timedelta
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
"""population functions"""
def population_change(russia):
    if russia.past_year < russia.date.year:
        russia.pop_change = (russia.current_pop - russia.past_pop / (
                (russia.current_pop + russia.current_pop) / 2)) * 100

        russia.past_pop = russia.current_pop

        if russia.pop_change <= 5.50:
            """possible implementation of viagra with somewhat moderate growth, due to low population"""
            print(f"Your population growth for {russia.past_year} was {russia.population_change}%.\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                russia.viagra_subsidy = True

                if russia.condom_subsidy:
                    """Checking to see if condom subsidies exist"""
                    russia.condom_subsidy = False

        elif russia.pop_change >= 15.50:
            print(f"Your population growth for {russia.past_year} was {russia.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == 'y' or choice.lower() == "yes":
                russia.condom_subsidy = True

                if russia.viagra_subsidy:
                    russia.viagra_subsidy = False

        else:
            if russia.date < datetime(1914, 7, 28):
                births = random.randrange(100, 1000)
                deaths = random.randrange(100, 950)

                russia.current_pop += births
                russia.births += births

                russia.current_pop -= deaths
                russia.deaths += deaths

            elif russia.date > datetime(1914, 7, 28) and russia.date < datetime(1923, 6, 16):
                births = random.randrange(100, 800)
                deaths = random.randrange(100, 750)

                russia.current_pop += births
                russia.births += births

                russia.current_pop -= deaths
                russia.deaths += deaths

            elif russia.date > datetime(1923, 6, 16) and russia.date < datetime(1941, 6, 22):
                births = random.randrange(100, 500)
                deaths = random.randrange(100, 450)

                russia.current_pop += births
                russia.births += births

                russia.current_pop -= deaths
                russia.deaths += deaths

            elif russia.date > datetime(1941, 6, 22) and russia.date < datetime(1945, 5, 8):
                births = random.randrange(100, 1300)
                deaths = random.randrange(100, 1250)

                russia.current_pop += births
                russia.births += births

                russia.current_pop -= deaths
                russia.deaths += deaths

            elif russia.date > datetime(1945, 5, 8):
                births = random.randrange(100, 600)
                deaths = random.randrange(100, 550)

                russia.current_pop += births
                russia.births += births

                russia.current_pop -= deaths
                russia.deaths += deaths

def manual_game(year):
    russia = Russia(year)
    while russia.current_pop > 3000000:
        print("hi")
        population_change(russia)
        time.sleep(3)
class Russia:
    def __init__(self, year):
        """Time variables"""
        self.date = datetime(int(year), 1, 1)
        self.past_year = self.date.year
        """Political Variables"""
        self.leader = dictators[year]
        """Population Variables"""
        self.current_pop = population[year]
        self.past_pop = self.current_pop
        self.deaths = None
        self.births = None
        self.pop_change = None
        self.condom_subsidy = None
        self.viagra_subsidy = None
        """Economic Variables"""
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
