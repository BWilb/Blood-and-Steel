import random
import time
from datetime import timedelta, datetime

from random_functions import random_functions

population = {
    "1910": 10300000,
    "1914": 10900000,
    "1918": 11500000,
    "1932": 14000000,
    "1936": 14900000,
    "1939": 15500000
}
leaders = {
    "1910": "Habte Giyorgis Dinagde",
    "1914": "Habte Giyorgis Dinagde",
    "1918": "Habte Giyorgis Dinagde",
    "1932": "Tafari Makonnen",
    "1936": "Tafari Makonnen",
    "1939": "Tafari Makonnen"
}

emperors = {
    "1910": "Menelik II",
    "1914": "Lij Lyasu",
    "1918": "Zewditu",
    "1932": "Halie Selassie I",
    "1936": "Halie Selassie I",
    "1939": "Halie Selassie I"
}
class Ethiopia:
    def __init__(self, year):
        self.region = "africa"
        self.name = "Ethiopian Empire"
        # date variables
        self.date = datetime(int(year), 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[year]
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = leaders[year]
        self.monarch = emperors[year]
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # other
        # international
        self.alliance = ""
        """north america"""
        self.us_relations = 56.56
        self.us_guarantee = False
    # population functions
    def population_change(self):
        """instead of having the headache of calling both national objects separately, why not combine them"""
        if self.current_year < self.date.year:
            pop_change = ((self.births - self.deaths) / ((self.births + self.deaths) / 2)) * 100

            if pop_change < 2.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)
                if choice == 0:
                    self.birth_enhancer = True
                    print("The British government has decided to impose birth enhancer.\n")
                    time.sleep(3)
                    if self.birth_control:
                        self.birth_control = False

            elif pop_change > 12.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)

                if choice == 0:
                    print("The British government has decided to impose birth control.\n")
                    time.sleep(3)
                    self.birth_control = True
                    if self.birth_enhancer:
                        self.birth_enhancer = False

        else:
            if self.birth_enhancer:
                births = random.randrange(10, 20)
                deaths = random.randrange(4, 11)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            if self.birth_control:
                births = random.randrange(5, 15)
                deaths = random.randrange(7, 18)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            else:
                births = random.randrange(7, 15)
                deaths = random.randrange(4, 12)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths
    # economic functions
    def check_economic_state(self):
        """function dealing with primary economic decisions of canadian parliament"""
        if self.date > self.economic_change_date:
            """instead of comparing an entire year, break the year up into sections"""
            if self.current_gdp > self.past_gdp:
                if self.e_s.lower() == "recovery":
                    self.e_s = "expansion"
                    print("The British economy is now in an expansionary period.\n")
                    time.sleep(3)

                elif self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
                    self.e_s = "recovery"
                    print("The British economy is now in recovery period.\n")
                    time.sleep(3)

            elif self.current_gdp < self.past_gdp:
                if self.e_s.lower() == "recession":
                    self.e_s = "depression"
                    print("Your economy is now in a depressionary period.\n")
                    time.sleep(3)

                elif self.e_s.lower() == "recovery" or self.e_s.lower() == "expansion":
                    self.e_s = "recession"
                    print("The British economy is now in a recessionary period.\n")
                    time.sleep(3)
        else:
            if self.e_s == "recession":
                self.recession()

            elif self.e_s == "recovery":
                self.recovery()

            elif self.e_s == "depression":
                self.depression()

            elif self.e_s == "expansion":
                self.expansion()
    def recession(self):
        if self.economic_stimulus:

            self.consumer_spending = -round(random.uniform(10, 150), 2)
            self.government_spending = round(random.uniform(100, 600), 2)
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = round(random.uniform(50, 350), 2)
            self.exports = round(random.uniform(10, 45), 2)
            self.imports = round(random.uniform(10, 75), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

        else:
            self.consumer_spending = -round(random.uniform(10, 200), 2)
            self.government_spending = round(random.uniform(100, 700), 2)
            self.national_debt += round((-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = -round(random.uniform(100, 500), 2)
            self.exports = round(random.uniform(10, 30), 2)
            self.imports = round(random.uniform(10, 105), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                    (self.exports - self.imports))
    def recovery(self):
        if self.economic_stimulus:
            self.consumer_spending = round(random.uniform(10, 450), 2)
            self.government_spending = round(random.uniform(100, 200), 2)
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = round(random.uniform(100, 700), 2)
            self.exports = round(random.uniform(10, 100), 2)
            self.imports = round(random.uniform(10, 75), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))
        else:
            self.consumer_spending = round(random.uniform(10, 350), 2)
            self.government_spending = round(random.uniform(100, 350), 2)
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = round(random.uniform(100, 500), 2)
            self.exports = round(random.uniform(10, 75), 2)
            self.imports = round(random.uniform(10, 58), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

    def expansion(self):
        if self.economic_stimulus:
            self.consumer_spending = round(random.uniform(10, 2000), 2)
            self.government_spending = round(random.uniform(100, 600), 2)
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = round(random.uniform(100, 300), 2)
            self.exports = round(random.uniform(10, 500), 2)
            self.imports = round(random.uniform(10, 400), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))
        else:
            self.consumer_spending = round(random.uniform(10, 200), 2)
            self.government_spending = round(random.uniform(100, 500), 2)
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = round(random.uniform(100, 300), 2)
            self.exports = round(random.uniform(10, 500), 2)
            self.imports = round(random.uniform(10, 350), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

    def depression(self):
        if self.economic_stimulus:
            self.consumer_spending = round(random.uniform(10, 15), 2)
            self.government_spending = round(random.uniform(100, 500), 2)
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = -round(random.uniform(100, 300), 2)
            self.exports = round(random.uniform(10, 50), 2)
            self.imports = round(random.uniform(10, 20), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))
        else:
            self.consumer_spending = -round(random.uniform(10, 200), 2)
            self.government_spending = round(random.uniform(100, 100), 2)
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = -round(random.uniform(100, 300), 2)
            self.exports = round(random.uniform(10, 50), 2)
            self.imports = round(random.uniform(10, 20), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))
    # stability functions
    def stability_happiness_change(self, globe):
        if globe.tension > 25 and globe.tension < 50:
            """if global tension is between 25 and 50"""
            if self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
                if self.improve_stability > self.date:
                    """if improving of stability has been activated"""
                    stability_increase = round(random.uniform(0.25, 1.56), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.25, 1.25), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    happiness_increase = round(random.uniform(1.56, 2.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

                else:
                    happiness_increase = round(random.uniform(1.25, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.50, 1.75), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.45, 1.65), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.75, 2.76), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(1.25, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

        elif globe.tension > 50 and globe.tension < 75:
            """if global tension is between 50 and 75"""
            if self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.10, 1.25), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.05, 1.05), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.15, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(1.15, 2.25), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(0.13, 0.96), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_increase = round(random.uniform(0.10, 0.76), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """if improving of happiness has been activated
                    improved happiness improves stability
                    """
                    happiness_increase = round(random.uniform(1.05, 1.96), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(0.96, 1.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase

        elif globe.tension > 75:
            """if global tension is above 75"""
            if self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
                if self.improve_stability > self.date:
                    """if improving of stability has been activated"""
                    stability_increase = round(random.uniform(0.05, 0.75), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                else:
                    stability_decrease = round(random.uniform(1.56, 3.75), 2)
                    if (self.stability - stability_decrease) > 5:
                        self.stability -= stability_decrease

                if self.improve_happiness > self.date:
                    stability_increase = round(random.uniform(0.05, 0.99), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_decrease = round(random.uniform(1.56, 2.56), 2)
                    if (self.stability - stability_decrease) > 5:
                        self.stability -= stability_decrease

            else:
                if self.improve_stability > self.date:
                    stability_increase = round(random.uniform(1.56, 2.56), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                else:
                    stability_increase = round(random.uniform(1.45, 2.34), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                if self.improve_happiness > self.date:
                    """If policies toward improving happiness have been imposed"""
                    happiness_increase = round(random.uniform(1.05, 2.96), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
                else:
                    happiness_increase = round(random.uniform(0.96, 2.56), 2)
                    if (self.happiness + happiness_increase) < 100:
                        self.happiness += happiness_increase
        else:
            if self.improve_stability > self.date:
                stability_increase = round(random.uniform(1.56, 2.56), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

            else:
                stability_increase = round(random.uniform(1.45, 2.34), 2)
                if (self.stability + stability_increase) < 100:
                    self.stability += stability_increase

            if self.improve_happiness > self.date:
                """If policies toward improving happiness have been imposed"""
                happiness_increase = round(random.uniform(1.05, 2.96), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase
            else:
                happiness_increase = round(random.uniform(0.96, 2.56), 2)
                if (self.happiness + happiness_increase) < 100:
                    self.happiness += happiness_increase
    # international functions
    # main function
    """
    main function is connected to AI object itself, so as to reduce the amount of storage space needed to keep 
    track of the object. I also dont have to individually each file of every nation
    """

    def main(self, globe):
        while self.population > 10000000:
            self.check_economic_state()
            self.population_change()
            self.stability_happiness_change(globe)
            random_functions.random_functions(self, globe)
            self.date += timedelta(days=1)
            break