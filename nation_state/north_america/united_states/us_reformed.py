import random
import time
from datetime import *

"""Population Dictionaries"""
population = {
    # population will be set up to increase or decrease randomly throughout every year
    "1910": 92410000,
    "1914": 99110000,
    "1918": 103210000,
    "1932": 124840000,
    "1936": 128050000,
    "1939": 130880000
}
"""Political Dictionaries"""
presidents = {
    "1910": "William Howard Taft",
    "1914": "Woodrow Wilson",
    "1918": "Woodrow Wilson",
    "1932": "Herbert Hoover",
    "1936": "Franklin D. Roosevelt",
    "1939": "Franklin D. Roosevelt"
}

vice_presidents = {
    # dictionary of vice presidents incase president gets assassinated
    "1910": "James S. Sherman",
    "1914": "Thomas R. Marshall",
    "1918": "Thomas R. Marshall",
    "1932": "Charles Curtis",
    "1936": "John Garner",
    "1939": "Henry Wallace"
}
"""Economic dictionaries & Variables"""
business_cycle = ["expansion", "recession"]
gdp = {
    "1910" : 520000000000,
    "1914" : 500000000000,
    "1918" : 550000000000,
    "1932" : 550000000000,
    "1936" : 575000000000,
    "1939" : 1100000000000
}

"""Subsidiary functions of game"""

def population_change(us):
    """Function is exaggerated in numbers
    incorporates population growth
    """
    if us.current_year < us.date.year:
        us.population_change = (us.population - us.current_pop / ((us.population + us.current_pop)/2)) * 100
        """Calculation of population change over year"""
        us.current_pop = us.population
        # reset of current population
        us.current_year = us.date.year
        # reset of current year

        if us.viagra_subsidize:
            us.population += random.randrange(25000, 50000)
            # Incorporation of deaths
            us.population -= random.randrange(4000, 15000)
            # Incorporation of births
            if us.population_change >= 10:
                """choice if population growth is out of control"""
                choice = input(f"your yearly population growth rate of {us.population_change}% is unsustainable"
                               f"Do you want to increase subsidies for population control?: ")
                if choice.lower() == "yes" or choice.lower() == "y":
                    us.viagra_subsidize = False
                    us.condom_subsidize = True

        elif us.condom_subsidize:
            """Choice if us population growth is too low"""
            if us.population_change <= 1.5:
                """Choice if population growth is too low"""
                choice = input(f"your yearly population growth rate of {us.population_change}% is unsustainable"
                               f"Do you want to increase subsidies for population growth?: ")
                us.viagra_subsidize = True
                us.condom_subsidize = False
    else:
        us.population += random.randrange(6700, 45000)
        us.population -= random.randrange(4500, 27000)

def economic_change(us):
    if us.economic_state == "expansion":
        us.gdp += random.randrange(25945, 62352)
    elif us.economic_state == "recession":
        us.gdp -= random.randrange(23546, 73464)

"""Main function of US_Version of game"""
def manual_game(us):
    # Establishment of date variable
    while us.population > 20000:
        us.date = us.date + timedelta(days=1)
        # function will incorporate daily changes in us population
        population_change(us)

class UnitedStates:
    def __init__(self, year):
        # population variables
        self.population = population[year]
        self.population_change = 0
        self.current_pop = self.population
        self.condom_subsidize = False
        """Population controller if birth rate gets out of control"""
        self.viagra_subsidize = False
        """Population controller if birth rate flops"""
        # political variables
        self.president = presidents[year]
        self.vice_president = vice_presidents[year]
        """Leaders of US"""
        self.republicans = self.population * 0.5
        self.democrats = self.population - self.republicans
        """Political parties of US"""
        # economic variables
        self.economic_state = business_cycle[random.randrange(len(business_cycle) - 1)]
        self.gdp = gdp[year]
        # military variables
        # international variables
        # time variables
        self.date = date = datetime(int(year), 1, 1)
        self.current_year = self.date.year

def main(time):
    united_states = UnitedStates(time)
    manual_game(united_states)