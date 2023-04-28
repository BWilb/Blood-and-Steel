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

"""population functions"""
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
            us.population += random.randrange(5000, 20000)
            # Incorporation of deaths
            us.population -= random.randrange(8000, 25000)
            # Incorporation of births
            if us.population_change <= 1.5:
                """Choice if population growth is too low"""
                choice = input(f"your yearly population growth rate of {us.population_change}% is unsustainable"
                               f"Do you want to increase subsidies for population growth?: ")
                us.viagra_subsidize = True
                us.condom_subsidize = False
    else:
        us.population += random.randrange(6700, 45000)
        us.population -= random.randrange(4500, 27000)

"""political functions"""

"""Economic Functions"""
def gdp_changes(us):
    choice = random.randrange(1, 3)
    if choice == 1:
        us.consumer_spending += random.randrange(1200, 34500)
        us.govnerment_spending += random.randrange(1400, 24500)
        us.investment += random.randrange(1600, 36570)
        us.exports += random.randrange(1155, 45000)
        us.imports += random.randrange(2245, 34500)
        us.gdp += (us.consumer_spending + us.government_spending + us.investment +
                   (us.exports - us.imports))
    elif choice == 2:
        us.consumer_spending -= random.randrange(1200, 34500)
        us.govnerment_spending -= random.randrange(1400, 24500)
        us.investment -= random.randrange(1600, 36570)
        us.exports -= random.randrange(1155, 45000)
        us.imports -= random.randrange(2245, 34500)
        us.gdp += (us.consumer_spending + us.government_spending + us.investment +
                   (us.exports - us.imports))

def economic_change(us):
    if us.current_year < us.date.year:
        us.economic_growth = (us.gdp - us.current_gdp / ((us.gdp + us.current_gdp) / 2)) * 100

        if us.economic_growth <= 1.5:
            choice = input(f"Your GDP grew {us.economic_growth}% last year.\n"
                           f"Do you want to stimulate your economy?: ")
            if choice.lower() == "yes" or choice.lower() == 'y':
                us.economic_stimulus = True

            elif choice.lower() == "no" or choice.lower() == 'n':
                if us.recess_years > 3 and us.economic_growth <= 0.5:
                    print("Your economy has been declining for three years.\n"
                          "An economic stimulus has been implemented!")
                    us.economic_stimulus = True
    else:
        gdp_changes(us)

"""Main function of US_Version of game"""
def manual_game(us):
    # Establishment of date variable
    while us.population > 2000000:
        us.date = us.date + timedelta(days=1)
        # function will incorporate daily changes in us population
        population_change(us)
        if us.current_year%4 == 0:
            us_elections(us)

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
        self.current_gdp = self.gdp
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        self.economic_stimulus = False
        # military variables
        # international variables
        # time variables
        self.date = date = datetime(int(year), 1, 1)
        self.current_year = self.date.year

def main(time):
    united_states = UnitedStates(time)
    manual_game(united_states)