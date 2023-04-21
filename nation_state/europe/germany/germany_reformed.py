import random
import time
from datetime import *

"""Population Dictionaries"""
population = {
    "1910": 63200000,
    "1914": 63200000,
    "1918": 62400000,
    "1932": 67200000,
    "1936": 69100000,
    "1939": 70500000
}

"""Political Dictionaries"""
leaders = {
    "1910" : "Wilhelm II",
    "1914" : "Wilhelm II",
    "1918" : "Friedrich Ebert",
    "1932" : "Paul Von Hindenburg",
    "1936" : "Adolf Hitler",
    "1939" : "Adolf Hitler"
}

"""Economic dictionaries & Variables"""
business_cycle = ["expansion", "recession"]
gdp = {
    "1910" : 237000000,
    "1914" : 237395000,
    "1918" : 235968000,
    "1932" : 237947500,
    "1936" : 240000000,
    "1939" : 300456000
}

"""Subsidiary functions of game"""

"""Population functions"""
def population_change(germany):
    """Numbers within function are exaggerated
    incorporates population growth
    """
    if germany.current_year < germany.date.year:
        germany.population_change = (germany.population - germany.current_pop
                                     / ((germany.population + germany.current_pop) / 2)) * 100
        """Calculation of german population growth"""
        germany.current_year = germany.date.year
        germany.current_population = germany.population
        """resetting of yearly population and year"""
        if germany.procurement_subsidize:
            """Choice if population increase true"""
            germany.population += random.randrange(4000, 16000)
            germany.population -= random.randrange(1000, 5000)

            if germany.population_change >= 10:
                """choice if population growth out of control"""
                choice = input(f"your population growth rate of {germany.population_growth}%\n"
                               f"is unsustainable! Do you want to increase subsidies for condoms?: ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    germany.condom_subsidize = True
                    germany.procurement_subsidize = False

        elif germany.condom_subsidize:
            """choice if population control true"""
            germany.population += random.randrange(4500, 6000)
            germany.population -= random.randrange(2000, 8000)

            if germany.population_growth <= 1.5:
                """choice if under population control gets out of hand"""
                choice = input(f"your population growth rate of {germany.population_growth}%\n"
                               f"is unsustainable! Do you want to increase subsidizes for procurment options?: ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    germany.procurement_subsidize = True
                    germany.condom_subsidize = False

        else:
            germany.population += random.randrange(4000, 14500)
            germany.population -= random.randrange(5000, 10000)

            if germany.population_change >= 10:
                choice = input(f"your population growth rate of {germany.population_growth}%\n"
                               f"is unsustainable! Do you want to increase subsidies for condoms?: ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    germany.condom_subsidize = True
            elif germany.population_growth <= 1.5:
                choice = input(f"your population growth rate of {germany.population_growth}%\n"
                               f"is unsustainable! Do you want to increase subsidizes for procurment options?: ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    germany.procurement_subsidize = True
"""Economic Functions"""

def econommic_change(germany):

    if germany.current_year < germany.date.year:
        print("hi")
        germany.economic_growth =(germany.gdp - germany.current_gdp / ((germany.gdp + germany.current_gdp) / 2)) * 100
        """Calculation of economic growth over year"""
        if germany.economic_stimulus:
            germany.gdp += random.randrange(60000, 150000)

            if germany.economic_growth >= 6 or germany.economic_state == "recession":
                choice = input(f"Your GDP grew {germany.economic_growth} last year.\n"
                               f"This is unsustainable. If your economy continues to grow like this "
                               f"A recession might happen\nDo you want to take away economy stimulus?: ")

                if choice.lower() == "y" or choice.lower() == "yes":
                    germany.economic_stimulus = False

        if germany.economic_growth <= 0.5:
            print("hi")

"""Random Function"""

"""Main Function"""
def manual_game(germany):
    while germany.population > 200000:
        germany.date = germany.date + timedelta(days=1)
        population_change(germany)
        econommic_change(germany)

class Germany:
    def __init__(self, year):
        # population variables
        self.population = population[year]
        self.current_population = self.population
        self.population_change = 0
        self.procurement_subsidize = False
        self.condom_subsidize = False
        # political variables
        self.leader = leaders[year]
        # economic variables
        self.economic_state = business_cycle[random.randrange(0, len(business_cycle) - 1)]
        self.gdp = gdp[year]
        self.current_gdp = self.gdp
        self.economic_growth = 0
        self.economic_stimulus = False
        # military variables
        # international variables
        # time variables
        self.date = date = datetime(int(year), 1, 1)
        self.current_year = self.date.year