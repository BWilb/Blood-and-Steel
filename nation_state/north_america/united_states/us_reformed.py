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

tax_rate = {
    "1910" : 0,
    "1914" : 1.00,
    "1918" : 6.00,
    "1932" : 4.00,
    "1936" : 4.00,
    "1939" : 4.00
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
def low_growth(us):
    if us.economic_state == "expansion":
        us.consumer_spending += round(random.uniform(30000, 75000), 2)
        us.investment += round(random.uniform(20000, 54000), 2)
        us.government_spending += round(random.uniform(300000, 500000), 2)
        us.exports = round(random.uniform(20000, 560000), 2)
        us.imports = round(random.uniform(32000, 560000), 2)
    else:
        print("hi")
def moderate_growth(us):
    if us.economic_state == "expansion":
        print("hi")
    else:
        print("hi")

def high_growth(us):
    if us.economic_state == "expansion":
        print("hi")
    else:
        print("hi")
def stimulus(us):
    """Fucntion deals with increased government spending"""
    """Function covering government spending and taxes
    in times of economic crisis
    """
    us.economic_stimulus = True
    """us.government_spending += random.randrange(24000, 100000)"""
    if us.recess_years < 3 and us.economic_growth >= 0.5:

        choice = input("Do you want to increase tax rate(Remember this applies to the entire population).\n"
                       "Yes or No?: ")
        """Prompting user to choose if they want to increase taxes"""

        if choice.lower() == 'yes' or choice.lower() == 'y':
            """if statement covering if answer is yes"""
            valid_choice = False
            while valid_choice:
                tax_hike = float(input("what will your new tax rate(between 0.5 & 10.0 be?: "))
                if tax_hike <= 10.00 and tax_hike >= 0.5:
                    """if statement if tax rate meets criteria"""
                    print(f"{tax_hike}% is new tax rate.")

                    valid_choice = True
                elif tax_hike <= 0:
                    """if statement if tax rate is below 0"""
                    print("new tax rate will be impossible to carry out. choose another tax rate")

                elif tax_hike >= 10:
                    """if statement if tax rate is too high"""
                    print("New tax rate will piss a lot of people off. Choose another tax rate.")
                else:
                    print("not a valid tax rate")

    elif us.recess_years >= 3:
        """if statement if economy has been growing slowly for past 3 years"""
        us.tax_rate = round(random.uniform(us.tax_rate, 10.0), 2)
        print("Congress has voted to raise the tax rate, without your involvement!")
        print(f"New tax rate {us.tax_rate}%")

def gdp_change(us):
    """Function covers direction of gdp change
    over daily count
    """
    if us.tax_rate <= 3 and us.tax_rate >= 0.5:
        print("Hi")
        high_growth(us)

    elif us.tax_rate <= 7.5 and us.tax_rate >= 3.1:
        print("hi")
        moderate_growth(us)

    else:
        low_growth(us)

def economic_decisions(us):
    if us.current_year < us.date.year:

        us.economic_growth = (us.gdp - us.current_gdp / ((us.gdp + us.current_gdp) / 2)) * 100
        """Simplified calculation for economic growth"""
        us.current_gdp = us.gdp
        us.consumer_spending += 0
        us.investment += 0
        us.government_spending += 0
        """Resetting of specific GDP variables"""

        if us.economic_growth <= 1.5:
            choice = input(f"Your GDP grew {us.economic_growth}% last year.\n"
                           f"Do you want to stimulate your economy?: ")
            if choice.lower() == "yes" or choice.lower() == 'y':
                stimulus(us)

            elif choice.lower() == "no" or choice.lower() == 'n':
                """Incorporation of user choice no"""
                if us.recess_years > 3 and us.economic_growth <= 0.5:
                    """Implementation of Economic Stimulus if economy hasn't been growing 
                    for past 3 years
                    """
                    print("Your economy has been declining for three years.\n"
                          "An economic stimulus has been implemented!")
                    time.sleep(3)
                    stimulus(us)
    else:
        gdp_change(us)

"""Main function of US_Version of game"""
def manual_game(us):
    # Establishment of date variable
    while us.population > 2000000:
        us.date = us.date + timedelta(days=1)
        # function will incorporate daily changes in us population
        population_change(us)
        economic_decisions(us)
        """if us.current_year%4 == 0:
            us_elections(us)"""

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
        """holds current year of gdp(used for comparing with future GDP
        to determine GDP growth)
        """
        self.government_debt = 0
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        self.tax_rate = tax_rate[year]
        # military variables
        # international variables
        # time variables
        self.date = date = datetime(int(year), 1, 1)
        self.current_year = self.date.year

def main(time):
    united_states = UnitedStates(time)
    manual_game(united_states)