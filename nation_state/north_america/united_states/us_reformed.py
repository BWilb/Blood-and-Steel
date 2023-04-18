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

def population_change(us, pop):
    """Function is exaggerated in numbers
    incorporates population growth
    """
    if us.viagra_subsidize and us.population_change < 1.5:
        """If US birth rate too low"""
        us.population += random.randrange(25000, 50000)
        # Incorporation of deaths
        us.population -= random.randrange(4000, 15000)
        # Incorporation of births
    elif us.condom_subsidize and us.population_change >= 10:
        """if US birth rate too high"""
        us.population += random.randrange(3000, 6000)
        # Incorporation of deaths
        us.population -= random.randrange(4000, 15000)
        # Incorporation of births
    else:
        """Normal birth rate"""
        us.population += random.randrange(5000, 20000)
        # Incorporation of deaths
        us.population -= random.randrange(4000, 15000)
    if us.current_year < us.date.year:
        us.population_change = (us.population - pop / ((us.population + pop)/2)) * 100
        print(f"The US population changed by {us.population_change}%")
        time.sleep(3)
        pop = us.population
        us.current_year = us.date.year

def economic_change(us):
    if us.economic_state == "expansion":
        us.gdp += random.randrange(25945, 62352)
    elif us.economic_state == "recession":
        us.gdp -= random.randrange(23546, 73464)

"""Main function of US_Version of game"""
def manual_game(us, time):
    cur_pop = us.population
    # Establishment of date variable
    while us.population > 20000:
        us.date = us.date + timedelta(days=1)
        # function will incorporate daily changes in us population
        population_change(us, cur_pop)

class UnitedStates:
    def __init__(self, year):
        # population variables
        self.population = population[year]
        self.population_change = 0
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
    manual_game(united_states, time)