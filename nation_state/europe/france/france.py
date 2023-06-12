"""Political dictionaries and variables"""
import random
import time

leaders = {
    "1910" : "Armand Fallières",
    "1914" : "Raymond Poincaré",
    "1918" : "Raymond Poincaré",
    "1932" : "Paul Doumer",
    "1936" : "Albert Lebrun",
    "1939" : "Albert Lebrun"
}
"""Population dictionaries and variables"""
population = {
    "1910": 41216590,
    "1914": 41472264,
    "1918": 39270374,
    "1932": 41911927,
    "1936": 42000000,
    "1939": 41989772
}
"""Economic dictionaries and variables"""
gdp = {
    "1910": 8842315789,
    "1914": 11616143158,
    "1918": 8854091053,
    "1932": 19443842105,
    "1936": 25525526316,
    "1939": 31316842105
}

"""Population functions"""
def population_growth(france):
    if france.past_year > france.date.year:
        france.pop_change = (france.current_pop - france.past_pop / (
                (france.current_pop + france.past_pop) / 2)) * 100

        france.past_pop = france.current_pop
        france.births = 0
        france.deaths = 0

        if france.pop_change <= 2.25:
            """possible implementation of viagra with somewhat moderate growth, due to low population"""
            print(f"Your population growth for {france.past_year} was {france.population_change}%.\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                france.viagra_subsidy = True

                if france.condom_subsidy:
                    """Checking to see if condom subsidies exist"""
                    france.condom_subsidy = False

        elif france.pop_change >= 8.25:
            print(f"Your population growth for {france.past_year} was {france.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == 'y' or choice.lower() == "yes":
                france.condom_subsidy = True

                if france.viagra_subsidy:
                    france.viagra_subsidy = False

    else:
        if france.viagra_subsidy:
            births = random.randrange(50, 300)
            deaths = random.randrange(25, 150)

            france.current_pop += births
            france.births += births

            france.current_pop -= deaths
            france.deaths += deaths

        elif france.condom_subsidy:
            births = random.randrange(50, 200)
            deaths = random.randrange(50, 150)

            france.current_pop += births
            france.births += births

            france.current_pop -= deaths
            france.deaths += deaths

        else:
            births = random.randrange(50, 250)
            deaths = random.randrange(50, 150)

            france.current_pop += births
            france.births += births

            france.current_pop -= deaths
            france.deaths += deaths
def manual_function(france):
    while france.population > 1500000:
        population_growth(france)
        time.sleep(3)

class France:
    def __init__(self, year):
        """Political variables"""
        self.leader = leaders[year]
        """Population variables"""
        self.current_pop = population[year]
        self.births = 0
        self.deaths = 0
        self.past_pop = self.current_pop
        self.happiness = 90.56
        self.condom_subsidy = False
        self.viagra_subsidy = False