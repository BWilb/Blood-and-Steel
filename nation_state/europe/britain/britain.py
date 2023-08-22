import random
import socket
import sys
import time
from datetime import datetime, timedelta

import globe
from database_management import upload_database
from nation_state.asia.se_asia.china import china_ai
from nation_state.asia.se_asia.japan import japan_ai
from nation_state.europe.austria import austria_ai
from nation_state.europe.belgium import belgium_ai
from nation_state.europe.britain import britain_ai
from nation_state.europe.denmark import denmark_ai
from nation_state.europe.france import france_ai
from nation_state.europe.greece import greece_ai
from nation_state.europe.italy import italy_ai
from nation_state.europe.luxembourg import luxembourg_ai
from nation_state.europe.netherlands import netherlands_ai
from nation_state.europe.norway import norway_ai
from nation_state.europe.romania import romania_ai
from nation_state.europe.serbia import serbia_ai
from nation_state.europe.spain import spain_ai
from nation_state.europe.sweden import sweden_ai
from nation_state.europe.switzerland import swiss_ai
from nation_state.north_america.canada import canada_ai
from nation_state.north_america.cuba import cuba_ai
from random_functions import random_functions

monarchs = {
    """Dictionary for english monarchs
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "Edward VII",
    "1914": "George V",
    "1918": "George V",
    "1932": "George V",
    "1936": "Edward VIII",
    "1939": "George VI"
}

pm = {
    "1910": "H.H. Asquith",
    "1914": "H.H. Asquith",
    "1918": "David Lloyd George",
    "1932": "Ramsay MacDonald",
    "1936": "Stanley Baldwin",
    "1939": "Neville Chamberlain"
}

spare_pms = ["Duncan Pirie", "Henry Cowan", "Harold Baker", "James Calmont", "Ellis Ellis-Griffith",
             "Charles Craig", "William Jones", "Alfred Scott", "Sir Charles Hunter"]

spare_1900_1950_monarchs = ["Louis", "Prince Arthur", "Beatrice", "Prince Henry", "Alexander Ramsay",
                            "Alexander Cambridge",
                            "Albert Victor", "Victoria II", "George VI"]

# population variables and dictionaries
population = {
    """Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""

    "1910": 44915900,
    "1914": 42956900,
    "1918": 39582000,
    "1932": 46335000,
    "1936": 47081300,
    "1939": 46029200
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}

flags = {
    "1910": "../flags/britain/United-Kingdom-Flag.jpg",
    "1914": "../flags/britain/United-Kingdom-Flag.jpg",
    "1918": "../flags/britain/United-Kingdom-Flag.jpg",
    "1932": "../flags/britain/United-Kingdom-Flag.jpg",
    "1936": "../flags/britain/United-Kingdom-Flag.jpg",
    "1939": "../flags/britain/United-Kingdom-Flag.jpg"
}

leader_images = {"1910": "../leaders/britain/330px-Herbert_Henry_Asquith_till_1916.jpg",
                 "1914": "../leaders/britain/330px-Herbert_Henry_Asquith_till_1916.jpg",
                 "1918": "../leaders/britain/330px-David_Lloyd_George_1916-1922.jpg",
                 "1932": "../leaders/britain/J._Ramsay_MacDonald_LCCN2014715885_(cropped)_till_1935.jpg",
                 "1936": "../leaders/britain/Stanley_Baldwin_ggbain.35233_1935_1937.jpg",
                 "1939": "../leaders/britain/chamberlain_1937-1939.jpeg"
                 }

def establish_foreign_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function"""
    for i in range(0, len(args)):
        globe.nations.append(args[i])

def slow_print(words):
    # used in international relations function, when dealing out region names
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.19)

class Britain:
    def __init__(self, year):
        self.is_intact = True
        self.name = "Great Britain"
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
        self.past_population = self.population
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = pm[year]
        self.monarch = monarchs[year]
        self.leader_image = leader_images[year]
        self.flag = flags[year]
        self.political_power = 354
        self.political_exponent = 2.76
        """Stability"""
        self.stability = 95.56
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.economic_stimulus = False
        self.e_s = "recovery"
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        """Components of GDP"""
        self.consumer_spending = 500
        self.investment = 400
        self.government_spending = 1200
        self.exports = 10000
        self.imports = 9500
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        self.alliance = ""
        # other
        self.sprite = False

    # stats functions
    def stats(self, globe1):
        # asking user if they would like to see a specific area of their nation's stats
        choice = input("Would you like to view your domestic or foreign relations stats?: ")
        if choice.lower() == "domestic":
            domestic_areas = ["1. political", "2. social", "3. economic"]
            done = True
            while done:
                for i in domestic_areas:
                    print(i, end="\n")
                    time.sleep(1.25)
                area_choice = int(input("\nchoose your area(1-3)(enter 0 to quit): "))
                if area_choice == 1:
                    self.political_stats()
                elif area_choice == 2:
                    self.social_stats()
                elif area_choice == 3:
                    self.economic_stats()
                elif area_choice == 0:
                    done = False
                else:
                    print("please answer more carefully.\n")
                    time.sleep(1.25)
        """elif choice.lower() == "foreign":
            self.international_stats(globe1)"""

    def political_stats(self):
        print(f"Your current Prime Minister is {self.leader}.\n")
        time.sleep(3)
        print(f"Your current Monarch is {self.monarch}.\n")
        time.sleep(3)
        print(f"The United Kingdom is currently {self.stability}% politically stable.\n")
        time.sleep(3)
        print(
            f"You have {self.political_power} political power to manipulate both your central and state governments.\n"
            f"This power also ties into what you can do internationally.\n")
        time.sleep(3)
        print(f"Your political power currently grows at a {self.political_exponent} incremental rate.\n")
        time.sleep(3)

    def economic_stats(self):
        print(f"Your current GDP is ${self.current_gdp}.\n")
        time.sleep(1.25)
        print(
            f"Your current GDP growth rate is {round(((self.current_gdp - self.past_gdp) / ((self.current_gdp + self.past_gdp) / 2)) * 100, 6)}%.\n")
        time.sleep(1.25)
        print(f"Your current National Debt is ${self.national_debt}.\n")
        time.sleep(1.25)
        print(f"Your debt to GDP ratio is {(self.national_debt / self.current_gdp) * 100}%")
        time.sleep(1.25)
        print(f"Your corporate tax rate is {self.corporate_tax_rate}%")
        time.sleep(1.25)
        print(f"Your income tax rate is {self.income_tax_rate}%")
        time.sleep(1.25)

        inquiry = input("Would you like to edit any part of your economic policy?: ")
        editables = ["1. corporate tax rate", "2. income tax rate", "3. government spending"]
        if inquiry.lower() == "yes":
            for i in editables:
                slow_print(i)
            """slow printing of each choice"""
            answer = int(input("Of 1-3, which component would you like to edit?(enter 0 to escape question: "))
            if answer == 1:
                cur_rate = self.corporate_tax_rate
                """storing current corporate rate for later use"""
                self.corporate_tax_rate += float(input("enter any number by how much you would like to increment your corporate tax rate: "))

                if cur_rate > self.corporate_tax_rate:
                    """if user decides to lower corporate tax rate"""
                    chance = random.randrange(0, 4)
                    # chance that government may cut spending
                    self.investment += 150
                    increase = round(random.uniform(0.25, 1.25))
                    if (increase + self.stability) < 100:
                        self.stability += increase

                    if chance == 3:
                        self.government_spending -= 100

                if cur_rate < self.corporate_tax_rate:
                    """if user decides to raise corporate tax rate"""
                    chance = random.randrange(0, 4)
                    # chance that government may raise spending
                    self.investment -= 150
                    decrease = round(random.uniform(0.25, 1.25))
                    if (decrease - self.stability) > 5:
                        self.stability -= decrease

                    if chance % 2 == 0:
                        self.government_spending += 100

            if answer == 2:
                cur_rate = self.income_tax_rate
                """storing current corporate rate for later use"""
                self.income_tax_rate += float(input("enter any number by how much you would like to increment your income tax rate: "))

                if cur_rate > self.income_tax_rate:
                    """if user decides to lower income tax rate"""
                    chance = random.randrange(0, 4)
                    # chance that government may cut spending
                    self.consumer_spending += 150
                    increase = round(random.uniform(0.25, 1.25))
                    if (increase + self.stability) < 100:
                        self.stability += increase

                    if chance == 3:
                        self.government_spending -= 100

                if cur_rate < self.income_tax_rate:
                    """if user decides to raise income tax rate"""
                    chance = random.randrange(0, 4)
                    # chance that government may raise spending
                    self.consumer_spending -= 150
                    decrease = round(random.uniform(0.25, 1.25))
                    if (decrease - self.stability) > 5:
                        self.stability -= decrease

                    if chance % 2 == 0:
                        self.government_spending += 100

            if answer == 3:
                cur_rate = self.government_spending
                """storing current corporate rate for later use"""
                self.income_tax_rate += float(input("How much would you like to increase government spending by(as number)?: "))

                if cur_rate > self.government_spending:
                    """if user decides to lower government spending"""
                    chance = random.randrange(0, 4)
                    # chance that consumers may slow spending
                    self.investment += 150
                    increase = round(random.uniform(0.25, 1.25))
                    if (increase + self.stability) < 100:
                        self.stability += increase

                    if chance == 3:
                        self.consumer_spending -= 100

                if cur_rate < self.corporate_tax_rate:
                    """if user decides to raise income tax rate"""
                    chance = random.randrange(0, 4)
                    # chance that government may raise spending
                    self.investment -= 150
                    decrease = round(random.uniform(0.25, 1.25))
                    if (decrease - self.stability) > 5:
                        self.stability -= decrease

                    if chance % 2 == 0:
                        self.consumer_spending += 100

    def social_stats(self):
        print(f"There are {self.population} people living within the US.\n")
        time.sleep(1.5)
        print(f"The current birth rate is "
              f"{round(((self.population - self.past_population) / ((self.population + self.past_population) / 2)) * 100, 6)}% for {self.date.year}.\n")
        # ((self.births - self.deaths) / ((self.births + self.deaths) / 2)) * 100
        time.sleep(1.5)
        print(f"There have been {self.births} births and {self.deaths} deaths in {self.date.year}\n")
        time.sleep(1.5)
        print(f"US citizens are {self.happiness}% content with the current system.\n")
        time.sleep(1.5)

    # population functions
    def population_change(self):
        """instead of having the headache of calling both national objects separately, why not combine them"""
        if self.sprite:
            """condition if sprite version of game wasn't selected"""
            if self.current_year < self.date.year:
                pop_change = ((self.births - self.deaths) / ((self.births + self.deaths) / 2)) * 100

                if pop_change < 2.56:
                    """incorporation of what happens when Mexican birth rate becomes too low"""
                    choice = input(f"Your population growth rate for {self.current_year} was {pop_change}%.\n"
                                   f"Would you like to promote population growth?: ")
                    not_answered = False

                    while not_answered:
                        if choice.lower() == "y" or choice.lower() == "yes":
                            self.birth_enhancer = True
                            not_answered = True

                        elif choice.lower() == "n" or choice.lower() == "no":
                            not_answered = True

                        else:
                            print("Please enter your answer more efficiently. (y, yes, n, or no)\n")
                            time.sleep(3)
                elif pop_change > 12.56:
                    """incorporation of what happens when Mexican birth rate becomes too low"""
                    choice = input(f"Your population growth rate for {self.current_year} was {pop_change}%.\n"
                                   f"Would you like to slow your population growth?: ")
                    not_answered = False

                    while not_answered:
                        if choice.lower() == "y" or choice.lower() == "yes":
                            self.birth_control = True
                            not_answered = True

                        elif choice.lower() == "n" or choice.lower() == "no":
                            not_answered = True

                        else:
                            print("Please enter your answer more efficiently. (y, yes, n, or no)\n")
                            time.sleep(3)
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

    def stimulate_economy(self):
        """function will be called if economy falls into recession or depression (will affect components of GDP if implemented)"""
        not_answered = True
        while not_answered:
            """while loop controlling user input for primary question"""
            user_question = input(
                f"{socket.gethostname()} would you like to implement an economic stimulus to mitigate the effects\n"
                f"of your economic downturn?: ")

            if user_question.lower() == "yes":
                self.economic_stimulus = True
                not_answered = True
                while not_answered:
                    """While loop controlling user input for secondary question"""
                    solvent_question = input(f"{socket.gethostname()} would you like to increase corporate or income taxes,"
                                             f"increase government spending,\n or take a 1.5% portion of your GDP "
                                             f"and distribute it to your populace?: ")

                    if solvent_question.lower() == "increase corporate taxes":
                        self.corporate_tax_rate += 1.5
                        self.government_spending += (self.government_spending * 0.025)
                        self.investment -= 150
                        decrease = round(random.uniform(0.25, 1.25), 2)
                        if (self.stability - decrease) > 5:
                            self.stability -= decrease

                    elif solvent_question.lower() == "increase income taxes":
                        self.income_tax_rate += 1.5
                        self.government_spending += (self.government_spending * 0.025)
                        self.consumer_spending -= 150
                        decrease = round(random.uniform(0.25, 1.25), 2)
                        if (self.happiness - decrease) > 5:
                            self.happiness -= decrease

                    elif solvent_question.lower() == "increase government spending":
                        self.government_spending += (self.government_spending * 0.05)
                        self.investment -= (self.investment * 0.05)
                        self.income_tax_rate += (self.income_tax_rate * 0.05)
                        self.corporate_tax_rate += (self.corporate_tax_rate * 0.05)
                        decrease = round(random.uniform(0.25, 1.25), 2)
                        if (self.happiness - decrease) > 5:
                            self.happiness -= decrease

                        if (self.stability - decrease) > 5:
                            self.stability -= decrease

                    elif solvent_question.lower() == "1.5% portion of gdp":
                        spared = (self.current_gdp * 0.025)
                        self.current_gdp -= spared
                        self.consumer_spending += spared
                    else:
                        print(f"{socket.gethostname()}, I did not understand your answer, please try again.\n")

            elif user_question.lower() == "no":
                not_answered = False
            else:
                print(f"{socket.gethostname()}, I did not understand your answer, please try again.\n")
                time.sleep(1.25)
    # economic functions
    def check_economic_state(self):
        """function dealing with primary economic decisions of canadian parliament"""
        if self.date > self.economic_change_date:
            """instead of comparing an entire year, break the year up into sections
            - components of GDP will be reset
            """
            if self.current_gdp > self.past_gdp:
                if self.e_s.lower() == "recovery":
                    self.e_s = "expansion"
                    self.consumer_spending += 45
                    self.investment += 54
                    self.exports += 1000
                    self.imports += 900
                    print("Your economy is now in an expansionary period.\n")
                    time.sleep(3)

                elif self.e_s.lower() == "recession" or self.e_s.lower() == "depression":
                    self.e_s = "recovery"
                    self.consumer_spending = 355
                    self.investment = 390
                    self.exports = 1000
                    self.imports = 900
                    print("Your economy is now in recovery period.\n")
                    time.sleep(3)

            elif self.current_gdp < self.past_gdp:
                if self.e_s.lower() == "recession":
                    self.e_s = "depression"
                    self.consumer_spending = -355
                    self.investment = -390
                    self.exports = 900
                    self.imports = 1000
                    print("Your economy is now in a recessionary period.\n")
                    time.sleep(3)
                    self.stimulate_economy()

                elif self.e_s.lower() == "recovery" or self.e_s.lower() == "expansion":
                    self.e_s = "depression"
                    self.consumer_spending -= 250
                    self.investment -= 250
                    self.exports += 90
                    self.imports += 100
                    print("Your economy is now in a depression period.\n")
                    time.sleep(3)
                    self.stimulate_economy()
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
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

        else:
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

    def recovery(self):
        if self.economic_stimulus:
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))
        else:
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

    def expansion(self):
        if self.economic_stimulus:
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.imports = round(random.uniform(10, 400), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))
        else:
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

    def depression(self):
        if self.economic_stimulus:
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))
        else:
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)

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

def main(time1):
    uk = Britain(time1)
    globe1 = globe.Globe()
    # player nation
    chinese_ai = china_ai.ChinaAI(time1)
    japanese_ai = japan_ai.Japan(time1)
    # establishing european AIs
    spanish_ai = spain_ai.SpainAI(time1)
    french_ai = france_ai.FranceAI(time1)
    austrian_ai = austria_ai.Austria(time1)
    belgian_ai = belgium_ai.BelgiumAI(time1)
    dutch_ai = netherlands_ai.Netherlands(time1)
    italian_ai = italy_ai.ItalyAI(time1)
    lux_ai = luxembourg_ai.LuxembourgAI(time1)
    danish_ai = denmark_ai.Denmark(time1)
    swiss_ia = swiss_ai.SwitzerlandAI(time1)
    swedish_ai = sweden_ai.SwedenAI(time1)
    norwegian_ai = norway_ai.NorwayAI(time1)
    greek_ai = greece_ai.Greece(time1)
    romanian_ai = romania_ai.RomaniaAI(time1)
    serbian_ai = serbia_ai.SerbiaAI(time1)
    # establishing north american AIs
    # american_ai = us_ai.UnitedStates(time)
    cuban_ai = cuba_ai.CubaAI(time1)
    canadian_ai = canada_ai.Canada(time1)
    establish_foreign_nations(globe1, uk, canadian_ai, cuban_ai, chinese_ai, japanese_ai,
                              austrian_ai, belgian_ai, dutch_ai, french_ai, spanish_ai, italian_ai, lux_ai,
                              danish_ai, swedish_ai, swiss_ia, norwegian_ai, greek_ai, romanian_ai, serbian_ai)

    upload_database.initial_upload_to_database(globe1.nations)
    while uk.population > 6000000:
        print(f"Current Date: {uk.date}\n")
        time.sleep(1.5)
        uk.population_change()
        uk.check_economic_state()
        uk.stability_happiness_change(globe1)
        random_functions.random_functions(uk, globe1)

        for i in range(0, len(globe1.nations)):
            if not globe1.nations[i].name == "Great Britain":
                globe1.nations[i].main(globe1)
                """
                looping through main function of each foreign nation object
                main function is connected to object itself, so as to use less memory space
                """
        upload_database.update_database_info(globe1.nations)
        uk.stats(globe1)
        uk.date += timedelta(1)
        time.sleep(3)

#main("1914")