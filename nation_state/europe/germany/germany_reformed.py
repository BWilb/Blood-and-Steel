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
def population_change(germany, pop):
    """Numbers within function are exaggerated
    incorporates population growth
    """
    print('hi')

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

def econommic_change(germany):
    print("hi")

class Germany:
    def __init__(self, year):
        # population variables
        self.population = population[year]
        self.population_change = 0
        self.procurement_subsidize = False
        self.condom_subsidize = False
        # political variables
        self.leader = leaders[year]
        # economic variables
        self.economic_state = business_cycle[random.randrange(0, len(business_cycle) - 1)]
        self.gdp = gdp[year]
        # military variables
        # international variables
        # time variables
        self.date = date = datetime(int(year), 1, 1)
        self.current_year = self.date.year