import random
import sys
import time
from collections import OrderedDict
from datetime import datetime, timedelta
"""from other_images.flags import mexico"""
import pygame.image
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
from nation_state.international_relations.europe import brit_relations, spain_relations, \
    france_relations, belgium_relations, netherlands_relations, luxembourg_relations, austria_relations
from nation_state.international_relations.north_america import canada_relations, cuba_relations
from nation_state.north_america.canada import canada_ai
from nation_state.north_america.cuba import cuba_ai
from random_functions import random_functions

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


"""Population Dictionaries"""
population = {
    "1910": 14702456,
    "1914": 14742623,
    "1918": 14782786,
    "1932": 17635255,
    "1936": 18971701,
    "1939": 19961661
}

"""Political Dictionaries"""
leaders = {
    "1910": "Porfirio Diaz",
    "1914": "Victoriano Huerta",
    "1918": "Venustiano Carranza",
    "1932": "Abelardo Rodriguez",
    "1936": "Lázaro Cárdenas",
    "1939": "Lázaro Cárdenas"
}

gdp = {
    "1910": 500000000,
    "1914": 659939450,
    "1918": 733488730,
    "1932": 723488730,
    "1936": 723488730,
    "1939": 743488730
}


class Mexico:
    def __init__(self, year):
        self.is_intact = True
        self.name = "Mexico"
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
        self.leader = leaders[year]
        self.political_power = 200
        self.political_exponent = 1.25
        """Stability"""
        self.stability = 95.56
        # economic
        self.e_s = "recovery"
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.tax_rate = 10.00
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
        # north america
        """canada"""
        self.canada_relations = 55.65
        self.canada_nationals_dealt = False
        """cuba"""
        self.cuba_relations = 86.56
        self.cuba_nationals_dealt = False
        # na ordered dictionary
        self.na = OrderedDict()
        self.na["Dominion of Canada"] = self.canada_relations
        self.na["Republic of Cuba"] = self.cuba_relations
        # asia
        """China"""
        self.china_relations = 65.45
        self.china_nationals_dealt = False
        """Japan"""
        self.japan_relations = 76.45
        self.japan_nationals_dealt = False
        # asia ordered dictionary
        self.asia = OrderedDict()
        self.asia["Republic of China"] = self.china_relations
        self.asia["Japanese Empire"] = self.japan_relations
        # europe
        """british"""
        self.brit_relations = 73.45
        self.british_nationals_dealt = False
        self.britain_guarantee = False
        self.britain_embargo = False
        """spanish"""
        self.spain_relations = 70.34
        self.spain_nationals_dealt = False
        self.spain_guarantee = False
        self.spain_embargo = False
        """french"""
        self.france_relations = 80.76
        self.france_nationals_dealt = False
        self.france_guarantee = False
        self.france_embargo = False
        """german"""
        """self.germany_relations = 76.45
        self.guarantee_germany = False
        self.germany_embargo = False
        self.germany_nationals_dealt = False"""
        """belgian"""
        self.belgium_relations = 81.65
        self.belgium_nationals_dealt = False
        self.belgium_guarantee = False
        self.belgium_embargo = False
        """austrian"""
        self.austria_relations = 58.45
        self.austria_nationals_dealt = False
        self.austria_guarantee = False
        self.austria_embargo = False
        """dutch"""
        self.netherlands_relations = 74.34
        self.netherlands_nationals_dealt = False
        self.dutch_guarantee = False
        self.dutch_embargo = False
        """luxembourg"""
        self.luxembourg_relations = 92.34
        self.luxembourg_nationals_dealt = False
        self.luxembourg_guarantee = False
        self.luxembourg_embargo = False
        """denmark"""
        self.danish_relations = 72.34
        self.danish_nationals_dealt = False
        self.denmark_guarantee = False
        self.denmark_embargo = False
        """italy"""
        self.italy_relations = 95.74
        self.italy_nationals_dealt = False
        self.italy_guarantee = False
        self.italy_embargo = False
        """norwegian"""
        self.norway_relations = 96.44
        self.norway_nationals_dealt = False
        self.norway_guarantee = False
        self.norway_embargo = False
        """swedish"""
        self.swedish_relations = 94.34
        self.swedish_nationals_dealt = False
        self.swedish_guarantee = False
        self.swedish_embargo = False
        """swiss"""
        self.swiss_relations = 98.74
        self.swiss_nationals_dealt = False
        self.britain_guarantee = False
        self.britain_embargo = False
        """estonian"""
        self.estonia_relations = 98.74
        self.estonia_nationals_dealt = False
        """latvian"""
        self.latvia_relations = 98.74
        self.latvia_nationals_dealt = False
        """lithuanian"""
        self.lithuania_relations = 98.74
        self.lithuania_nationals_dealt = False
        """greek"""
        self.greece_relations = 82.34
        self.greece_nationals_dealt = False
        self.greece_guarantee = False
        self.greece_embargo = False
        """romanian"""
        self.romania_relations = 82.34
        self.romania_nationals_dealt = False
        self.romania_guarantee = False
        self.romania_embargo = False
        """serbian"""
        self.serbia_relations = 82.34
        self.serbia_nationals_dealt = False
        self.serbia_guarantee = False
        self.serbia_embargo = False
        # ordered dictionary of european nations
        self.european_nations = OrderedDict()
        self.european_nations['Great Britain'] = self.brit_relations
        self.european_nations['Kingdom of Spain'] = self.spain_relations
        self.european_nations['French Republic'] = self.france_relations
        self.european_nations['Kingdom of Belgium'] = self.belgium_relations
        self.european_nations['Austria-Hungary'] = self.austria_relations
        # self.european_nations['German Empire'] = self.germany_relations
        self.european_nations['Kingdom of Netherlands'] = self.netherlands_relations
        self.european_nations['Kingdom of Luxembourg'] = self.luxembourg_relations
        self.european_nations['Kingdom of Denmark'] = self.danish_relations
        self.european_nations['Kingdom of Italy'] = self.italy_relations
        self.european_nations['Kingdom of Norway'] = self.norway_relations
        self.european_nations['Republic of Sweden'] = self.swedish_relations
        self.european_nations['Republic of Switzerland'] = self.swiss_relations
        self.european_nations['Kingdom of Greece'] = self.greece_relations
        self.european_nations['Kingdom of Romania'] = self.romania_relations
        self.european_nations['Kingdom of Serbia'] = self.serbia_relations
        # asia
        """serbian"""
        self.ethiopia_relations = 72.34
        self.ethiopia_nationals_dealt = False
        self.african_nations = OrderedDict()
        self.african_nations['Ethiopian Empire'] = self.ethiopia_relations
        # time limitations on diplomats if you commit horrendous action(you will be temporarily expelled from region for 5 days)
        self.europe_limit = self.date
        self.africa_limit = self.date
        self.na_limit = self.date
        self.asia_limit = self.date
        # other
        self.is_ai = False

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

        elif choice.lower() == "foreign":
            self.international_stats(globe1)

    def political_stats(self):
        print(f"Your current president is {self.leader}.\n")
        time.sleep(3)
        print(f"Mexico is currently {self.stability}% politically stable.\n")
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

    def international_stats(self, globe1):
        """Checking of foreign relations"""
        print(f"\nCurrent global tension {globe1.tension}%\n")
        time.sleep(1.25)
        done = True
        while done:
            """region_choice = input(
                "Of the following regions, would you like to view your relations in..." +
                slow_print("\nNorth America, Europe, Asia, South America, or Africa") +
                "\nNorth America, Europe, Asia, South America, or Africa(enter quit to escape)?: ")"""
            print("Of the following regions...")
            time.sleep(1.25)
            slow_print("North America, Europe, Asia, South America, or Africa\n")
            time.sleep(0.75)
            region_choice = input("\nWhich one would you like to view your relations?(enter quit to escape)?: ")

            if region_choice.lower() == "europe":
                if self.europe_limit > self.date:
                    """only go down this path if you decided to harm any european country"""
                    print(f"Your diplomats have been temporarily banned from any European country for "
                          f"{self.europe_limit.date() - self.date.date()} days.\n")
                    time.sleep(3)

                else:
                    i = 1
                    for key, value in self.european_nations.items():
                        print(f"{i}. Relations with {key}: {value}.\n")
                        time.sleep(1.25)
                        """looping through european relations"""
                        i+=1
                    choice = input(
                        "Would you like to manipulate your relations with one of those nations?(enter quit to escape):")

                    if choice.lower() == "yes" or choice.lower() == 'y':
                        nation_choice = int(input("Which European nation would you like to choose, based off its number?(enter 0 to quit): "))
                        if nation_choice == 1:
                            for i in range(0, len(globe1.nations)):
                                """searching for Great Britain"""
                                if globe1.nations[i].name == "Great Britain":
                                    brit_relations.british_relations(self, globe1.nations[i], globe1)

                        if nation_choice == 2:
                            for i in range(0, len(globe1.nations)):
                                """searching for Spain"""
                                if globe1.nations[i].name == "Kingdom of Spain":
                                    spain_relations.spanish_relations(self, globe1.nations[i], globe1)

                        if nation_choice == 3:
                            for i in range(0, len(globe1.nations)):
                                """searching for france"""
                                if globe1.nations[i].name == "French Republic":
                                    france_relations.french_relations(self, globe1.nations[i], globe1)

                        if nation_choice == 4:
                            for i in range(0, len(globe1.nations)):
                                """searching for Belgium"""
                                if globe1.nations[i].name == "Kingdom of Belgium":
                                    belgium_relations.belgian_relations(self, globe1.nations[i], globe1)

                        if nation_choice == 5:
                            for i in range(0, len(globe1.nations)):
                                """searching for Netherlands"""
                                if globe1.nations[i].name == "Kingdom of Netherlands":
                                    netherlands_relations.dutch_relations(self, globe1.nations[i], globe1)

                        if nation_choice == 6:
                            for i in range(0, len(globe1.nations)):
                                """searching for Netherlands"""
                                if globe1.nations[i].name == "Kingdom of Luxembourg":
                                    luxembourg_relations.luxembourger_relations(self, globe1.nations[i], globe1)

                        if nation_choice == 7:
                            for i in range(0, len(globe1.nations)):
                                """searching for Netherlands"""
                                if globe1.nations[i].name == "Austria-Hungary" or globe1.nations[
                                    i].name == "Republic of Austria":
                                    austria_relations.austrian_relations(self, globe1.nations[i], globe1)

            elif region_choice.lower() == "asia":
                if self.asia_limit > self.date:
                    """only go down this path if you decided to harm any european country"""
                    print(f"Your diplomats have been temporarily banned from any Asian country for "
                          f"{self.asia_limit.date() - self.date.date()} days.\n")
                    time.sleep(3)

                else:
                    for key, value in self.asia.items():
                        print(f"Relations with {key}: {value}.\n")
                        time.sleep(1.25)
            elif region_choice.lower() == "south america":
                pass
            elif region_choice.lower() == "africa":
                if self.africa_limit > self.date:
                    """only go down this path if you decided to harm any european country"""
                    print(f"Your diplomats have been temporarily banned from any African country for "
                          f"{self.africa_limit.date() - self.date.date()} days.\n")
                    time.sleep(3)

                else:
                    for key, value in self.african_nations.items():
                        print(f"Relations with {key}: {value}.\n")
                        time.sleep(1.25)

            elif region_choice.lower() == "north america":
                """only go down this path if you decided to harm any neighboring country"""
                if self.na_limit > self.date:
                    print(f"Your diplomats have been temporarily banned from any neighboring country for "
                          f"{self.na_limit.date() - self.date.date()} days.\n")
                    time.sleep(3)

                else:
                    for key, value in self.na.items():
                        print(f"relations with {key}: {value}.\n")
                        time.sleep(1.25)

                    """choice = input(
                        "Would you like to manipulate your relations with one of those nations?(enter quit to escape):")
                    if choice.lower() == "yes" or choice.lower() == 'y':

                        nation_choice = input("Which North American nation would you like to choose?: ")
                        if nation_choice.lower() == "canada":
                            for i in range(0, len(globe1.nations)):
                                Looping until canada is found
                                reason why globe variable is used for nation is to funnel down required amount of variables 
                                for proper use.
                                if globe1.nations[i].name == "Canada":
                                    canada_relations.canadian_relations(self, globe1.nations[i], globe1)

                        elif nation_choice.lower() == "cuba":

                            for i in range(0, len(globe1.nations)):
                                Looping until cuba is found
                                reason why globe variable is used for nation is to funnel down required amount of variables 
                                for proper use.
                                
                                if globe1.nations[i].name == "Cuba":
                                    cuba_relations.cuban_relations(self, globe1.nations[i], globe1)"""

            elif region_choice.lower() == "quit":
                done = False
            else:
                print("Please answer carefully!!")

    # population functions
    def population_change(self):
        """instead of having the headache of calling both national objects separately, why not combine them"""
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
                births = random.randrange(20, 50)
                deaths = random.randrange(25, 45)
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
                births = random.randrange(15, 35)
                deaths = random.randrange(20, 30)
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
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
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


def main(time1):
    globe1 = globe.Globe()
    # player nation
    mexico = Mexico(time1)
    chinese_ai = china_ai.ChinaAI(time1)
    japanese_ai = japan_ai.Japan(time1)
    # establishing european AIs
    british_ai = britain_ai.Britain(time1)
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
    #american_ai = us_ai.UnitedStates(time)
    cuban_ai = cuba_ai.CubaAI(time1)
    canadian_ai = canada_ai.Canada(time1)
    establish_foreign_nations(globe1, mexico, canadian_ai, cuban_ai, chinese_ai, japanese_ai,
                              british_ai, austrian_ai, belgian_ai, dutch_ai, french_ai, spanish_ai, italian_ai, lux_ai,
                              danish_ai, swedish_ai, swiss_ia, norwegian_ai, greek_ai, romanian_ai, serbian_ai)

    upload_database.initial_upload_to_database(globe1.nations)
    while mexico.population > 6000000:
        print(f"Current Date: {mexico.date}\n")
        time.sleep(1.5)
        mexico.population_change()
        mexico.check_economic_state()
        mexico.stability_happiness_change(globe1)
        random_functions.random_functions(mexico, globe1)

        for i in range(0, len(globe1.nations)):
            if not globe1.nations[i].name == "Mexico":
                globe1.nations[i].main(globe1)
                """
                looping through main function of each foreign nation object
                main function is connected to object itself, so as to use less memory space
                """
        upload_database.update_database_info(globe1.nations)
        mexico.stats(globe1)
        mexico.date += timedelta(1)
        time.sleep(3)


if __name__ == '__main__':
    main("1914")
