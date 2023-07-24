import random
import time
from datetime import datetime, timedelta
leaders = {
    "1910" : "Robert Comtesse",
    "1914" : "Arthur Hoffmann",
    "1918" : "Felix Calonder",
    "1932" : "Giuseppe Motta",
    "1936" : "Albert Meyer",
    "1939" : "Philipp Etter"
}

population = {
    "1910": 3585751,
    "1914": 3695000,
    "1918": 3818000,
    "1932": 4111500,
    "1936": 4156167,
    "1939": 4184833
}
gdp = {
    "1910": 1765677700,
    "1914": 1975776780,
    "1918": 2021174168,
    "1932": 1595825500,
    "1936": 2443434342,
    "1939": 2061627844
}

class SwitzerlandAI:
    def __init__(self, year):
        self.region = "europe"
        self.name = "Switzerland"
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
        # foreign
        self.alliance = ""
        self.us_relations = 85.24
        # other
    # population functions
    def population_change(self):
        """instead of having the headache of calling both national objects separately, why not combine them"""
        if self.current_year < self.date.year:
            pop_change = ((self.births - self.deaths) / ((self.births + self.deaths) / 2)) * 100

            if pop_change < 2.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)

                if choice == 1:
                    print("The Swiss government has decided to implement policies to increase growth in births.\n")
                    time.sleep(1.25)

                    self.birth_enhancer = True

                    if self.birth_control:
                        self.birth_control = False

            elif pop_change > 12.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)

                if choice == 1:
                    print("The Swiss government has decided to implement policies to control births.\n")
                    time.sleep(1.25)

                    self.birth_control = True

                    if self.birth_enhancer:
                        self.birth_enhancer = False
        else:
            if self.birth_enhancer:
                births = random.randrange(20, 40)
                deaths = random.randrange(11, 30)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            if self.birth_control:
                births = random.randrange(10, 30)
                deaths = random.randrange(25, 35)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            else:
                births = random.randrange(7, 15)
                deaths = random.randrange(4, 10)
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
                    print("Your economy is now in an expansionary period.\n")
                    time.sleep(3)

                elif self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
                    self.e_s = "recovery"
                    print("Your economy is now in recovery period.\n")
                    time.sleep(3)

            elif self.current_gdp < self.past_gdp:
                if self.e_s.lower() == "recession":
                    self.e_s = "depression"
                    print("Your economy is now in a recessionary period.\n")
                    time.sleep(3)

                elif self.e_s.lower() == "recovery" or self.e_s.lower() == "expansion":
                    self.e_s = "recession"
                    print("Your economy is now in a depression period.\n")
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
    # main
    def main(self):
        while self.population > 2500000:
            self.check_economic_state()
            self.population_change()
            break