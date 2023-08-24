import random
import time
from datetime import datetime, timedelta

leaders = {
    "1910": "Ahmad Shah Qajar",
    "1914": "Ahmad Shah Qajar",
    "1918": "Ahmad Shah Qajar",
    "1932": "Reza shah",
    "1936": "Reza shah",
    "1939": "Reza shah"
}


population = {
    "1910": 10970000,
    "1914": 10320000,
    "1918": 9530000,
    "1932": 13270000,
    "1936": 14230000,
    "1939": 14970000
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

flags = {"1910": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1914": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1918": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1932": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1936": "../flags/iran/1920px-State_flag_of_Iran_(1933–1964).jpg",
         "1939": "../flags/iran/1920px-State_flag_of_Iran_(1933–1964).jpg"
         }

leader_images = {
    "1910": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1914": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1918": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1932": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg",
    "1936": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg",
    "1939": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg"
}

class AfghanistanAI:
    def __init__(self, year):
        self.name = "Afghanistan"
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
        self.leader_image = leader_images[year]
        """Stability"""
        self.stability = 95.56
        self.flag = flags[year]
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.e_s = "recovery"
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        """general"""
        self.alliance = ""
        # other
        self.sprite = False
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
                    print("The Austrian government has decided to impose birth enhancer.\n")
                    time.sleep(3)
                    if self.birth_control:
                        self.birth_control = False

            elif pop_change > 12.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)

                if choice == 0:
                    print("The Austrian government has decided to impose birth control.\n")
                    time.sleep(3)
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

    def stability_happiness_change(self, globe):
        print('hhi')
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
            """if global tension is above 75"""
            if self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
                if self.improve_stability > self.date:
                    """if improving of stability has been activated"""
                    stability_increase = round(random.uniform(0.05, 0.75), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase

                else:
                    stability_decrease = round(random.uniform(1.56, 3.75), 2)
                    if (self.stability + stability_decrease) < 100:
                        self.stability += stability_decrease

                if self.improve_happiness > self.date:
                    stability_increase = round(random.uniform(0.05, 0.99), 2)
                    if (self.stability + stability_increase) < 100:
                        self.stability += stability_increase
                else:
                    stability_decrease = round(random.uniform(1.56, 2.56), 2)
                    if (self.stability + stability_decrease) < 100:
                        self.stability += stability_decrease

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

    def main(self, globe):
        while self.population > 600000:
            self.check_economic_state()
            self.population_change()
            self.stability_happiness_change(globe)
            """if self.is_sprite == False:
                random_functions.random_functions(self, globe)"""
            self.date += timedelta(days=1)
            break