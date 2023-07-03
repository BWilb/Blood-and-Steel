import random
from datetime import datetime, timedelta

population = {
    "1910": 31424522,
    "1914": 32424522,
    "1918": 33424522,
    "1932": 36424522,
    "1936": 39424522,
    "1939": 41915040,
}
gdp = {
    "1910": 118500000,
    "1914": 118697500,
    "1918": 117984000,
    "1932": 118973750,
    "1936": 120000000,
    "1939": 150228000,
}

def recovery(prussia):
    if prussia.master.economic_stimulus:
        prussia.consumer_spending = round(random.uniform(10, 400), 2)
        prussia.government_spending = round(random.uniform(500, 2000), 2)
        prussia.debt += round(
            (prussia.consumer_spending + prussia.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        prussia.investment = round(random.uniform(1000, 4500), 2)
        prussia.exports = round(random.uniform(600, 1000), 2)
        prussia.imports = round(random.uniform(600, 900), 2)

        prussia.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

        prussia.master.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

    else:
        prussia.consumer_spending = round(random.uniform(10, 400), 2)
        prussia.government_spending = round(random.uniform(3000, 6000), 2)
        prussia.debt += round((prussia.consumer_spending + prussia.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        prussia.investment = round(random.uniform(1000, 4000), 2)
        prussia.exports = round(random.uniform(600, 900), 2)
        prussia.imports = round(random.uniform(600, 900), 2)

        prussia.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

        prussia.master.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                       (prussia.exports - prussia.imports))
def recession(prussia):
    if prussia.master.economic_stimulus:
        prussia.consumer_spending = -round(random.uniform(10, 200), 2)
        prussia.government_spending = round(random.uniform(2000, 3500), 2)
        prussia.debt += round(
            (-prussia.consumer_spending + prussia.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        prussia.investment = -round(random.uniform(200, 1200), 2)
        prussia.exports = round(random.uniform(600, 900), 2)
        prussia.imports = round(random.uniform(700, 900), 2)

        prussia.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

        prussia.master.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))
    else:
        prussia.consumer_spending = -round(random.uniform(10, 400), 2)
        prussia.government_spending = round(random.uniform(4000, 8000), 2)
        prussia.debt += round(
            (-prussia.consumer_spending + prussia.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        prussia.investment = -round(random.uniform(1000, 4000), 2)
        prussia.exports = round(random.uniform(600, 900), 2)
        prussia.imports = round(random.uniform(700, 900), 2)

        prussia.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

        prussia.master.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                       (prussia.exports - prussia.imports))

def depression(prussia):
    if prussia.master.economic_stimulus:

        prussia.consumer_spending = -round(random.uniform(200, 1200), 2)
        prussia.government_spending = round(random.uniform(8000, 10000), 2)
        prussia.debt += round(
            (-prussia.consumer_spending + prussia.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        prussia.investment = -round(random.uniform(1500, 3500), 2)
        prussia.exports = round(random.uniform(600, 1500), 2)
        prussia.imports = round(random.uniform(700, 1800), 2)

        prussia.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

        prussia.master.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

    else:
        prussia.consumer_spending = -round(random.uniform(200, 1600), 2)
        prussia.government_spending = round(random.uniform(10000, 12000), 2)
        prussia.debt += round(
            (-prussia.consumer_spending + prussia.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        prussia.investment = -round(random.uniform(2000, 4000), 2)
        prussia.exports = round(random.uniform(600, 900), 2)
        prussia.imports = round(random.uniform(700, 1800), 2)

        prussia.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

        prussia.master.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                       (prussia.exports - prussia.imports))
def expansion(prussia):
    if prussia.master.economic_stimulus:
        prussia.consumer_spending = round(random.uniform(200, 3200), 2)
        prussia.government_spending = round(random.uniform(2000, 5000), 2)
        prussia.debt += round(
            (prussia.consumer_spending + prussia.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        prussia.investment = round(random.uniform(2000, 6000), 2)
        prussia.exports = round(random.uniform(600, 1200), 2)
        prussia.imports = round(random.uniform(600, 900), 2)

        prussia.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

        prussia.master.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                       (prussia.exports - prussia.imports))
    else:
        prussia.consumer_spending = round(random.uniform(200, 1600), 2)
        prussia.government_spending = round(random.uniform(5000, 8000), 2)
        prussia.debt += round(
            (prussia.consumer_spending + prussia.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
        prussia.investment = round(random.uniform(2000, 4000), 2)
        prussia.exports = round(random.uniform(600, 1200), 2)
        prussia.imports = round(random.uniform(600, 900), 2)

        prussia.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                (prussia.exports - prussia.imports))

        prussia.master.current_gdp += (prussia.consumer_spending + prussia.investment + prussia.government_spending +
                                       (prussia.exports - prussia.imports))

def economic_growth(prussia):
    """function determines which type of economic growth function code takes"""
    if prussia.current_date > prussia.economic_change_date:
        if prussia.current_gdp > prussia.past_gdp:

            if prussia.economic_state == "recovery":
                prussia.economic_state = "expansion"

            elif prussia.economic_state == "recession":
                prussia.economic_state = "recovery"

            elif prussia.economic_state == "depression":
                prussia.economic_state = "recession"

        elif prussia.current_gdp < prussia.past_gdp:

            if prussia.economic_state == "recovery":
                prussia.economic_state = "recession"

                choice = input("The administrative region of Prussia is requesting that you pass an economic stimulus.\n"
                               "The Prussian economy is starting to fail. Will you do this?: ")

                if choice.lower() == "yes" or choice.lower() == 'y':
                    prussia.master.economic_stimulus = True

                else:
                    chance = random.randrange(0, 11)
                    if chance % 6 == 0:
                        """27.27% chance that Prussian officials officiate a stimulus anyway"""
                        print("Prussian officials decided to go around your back an establish a stimulus anyway.\n")
                        prussia.master.economic_stimulus = True

            elif prussia.economic_state == "recession":
                prussia.economic_state = "depression"

                choice = input(
                    "The administrative region of Prussia is requesting that you pass an economic stimulus.\n"
                    "The Prussian economy has fallen into a depression. Will you do this?: ")

                if choice.lower() == "yes" or choice.lower() == 'y':
                    prussia.master.economic_stimulus = True

                else:
                    chance = random.randrange(0, 11)
                    if chance % 2 == 0:
                        """54.54% chance that Prussian officials officiate a stimulus anyway"""
                        print("Prussian officials decided to go around your back an establish a stimulus anyway.\n")
                        prussia.master.economic_stimulus = True

            elif prussia.economic_state == "expansion":
                prussia.economic_state = "recovery"

    else:
        if prussia.economic_state == "recovery":
            recovery(prussia)

        if prussia.economic_state == "depression":
            depression(prussia)

        if prussia.economic_state == "recession":
            recession(prussia)

        if prussia.economic_state == "expansion":
            expansion(prussia)

"""Population growth"""
def population_growth(prussia):
    if prussia.master.subsidize_pop_growth:
        births = random.randrange(3, 10)
        deaths = random.randrange(5, 8)
        prussia.current_pop += births
        prussia.master.current_pop += (births - deaths)
        prussia.master.births += births
        prussia.master.deaths += deaths
        if prussia.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    prussia.master.center_party += 1

                elif chance == 1:
                    prussia.master.progressives += 1

                elif chance == 2:
                    prussia.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                prussia.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                prussia.master.rebels += 1

    elif prussia.master.subsidize_pop_slow:
        births = random.randrange(2, 7)
        deaths = random.randrange(5, 8)
        prussia.current_pop += births
        prussia.master.current_pop += (births - deaths)
        prussia.master.births += births
        prussia.master.deaths += deaths

        if prussia.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    prussia.master.center_party += 1

                elif chance == 1:
                    prussia.master.progressives += 1

                elif chance == 2:
                    prussia.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                prussia.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                prussia.master.rebels += 1

    else:
        births = random.randrange(3, 9)
        deaths = random.randrange(3, 9)
        prussia.current_pop += births
        prussia.master.current_pop += (births - deaths)
        prussia.master.births += births
        prussia.master.deaths += deaths

        if prussia.master.date.year < 1933:

            for i in range(0, (births - deaths)):
                """assigning political parties to each birth"""
                chance = random.randrange(0, 3)
                if chance == 0:
                    prussia.master.center_party += 1

                elif chance == 1:
                    prussia.master.progressives += 1

                elif chance == 2:
                    prussia.master.free_conservatives += 1

        else:
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that the births go to the Nazi party"""
                prussia.master.national_socialists += 1

            elif chance == 1:
                """Chance that the births go to the rebels"""
                prussia.master.rebels += 1

class Prussia:
    def __init__(self, year, master_nation):
        self.current_date = datetime(year, 1, 1)
        # administrative variables
        self.name = "Prussia"
        # social variables
        self.current_pop = population[str(year)]
        self.happiness = 100
        # economic variables
        self.current_gdp = gdp[str(year)]
        self.past_gdp = self.current_gdp
        self.government_spending = 0
        self.investment = 0
        self.consumer_spending = 0
        self.exports = 0
        self.imports = 0
        self.debt = 0
        self.economic_stimulus = False
        self.economic_state = "recovery"
        self.economic_change_date = self.current_date + timedelta(days=30)
        # political variables
        self.stability = 96.65
        self.master = master_nation
