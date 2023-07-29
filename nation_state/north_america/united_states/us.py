# in-game libraries

import globe
from datetime import datetime, timedelta
from us_states import alabama, alaska, arizona, arkansas, california, colorado, \
    conneticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas, kentucky, louisiana, maine, \
    maryland, michigan, mississppi, missouri, montana, n_d, n_m, nebraska, nevada, new_hampshire, new_jersey, new_york, \
    north_carolina, ohio, ok, oregon, pennsylvania, rhode_island, s_d, south_carolina, tennessee, texas, utah, virginia, \
    vermont, west_virginia, washington, wisconsin, wyoming
# importation of Asian files
from nation_state.asia.se_asia.china import china_ai
from nation_state.asia.se_asia.japan import japan_ai
# importation of European files
from nation_state.europe.britain import britain_ai
from nation_state.europe.spain import spain_ai
from nation_state.europe.france import france_ai
from nation_state.europe.austria import austria_ai
from nation_state.europe.netherlands import netherlands_ai
from nation_state.europe.belgium import belgium_ai
from nation_state.europe.luxembourg import luxembourg_ai
from nation_state.europe.denmark import denmark_ai
from nation_state.europe.italy import italy_ai
from nation_state.europe.switzerland import swiss_ai
from nation_state.europe.sweden import sweden_ai
from nation_state.europe.norway import norway_ai
from nation_state.europe.greece import greece_ai
from nation_state.europe.romania import romania_ai
from nation_state.europe.serbia import serbia_ai
# from nation_state.europe.germany import german_ai
# importation of NorthAmerican files
from nation_state.north_america.canada import canada_ai
from nation_state.north_america.mexico import mexico_ai
from nation_state.north_america.cuba import cuba_ai
from nation_state.international_relations.north_america import mexico_relations, canada_relations
from nation_state.international_relations.europe import austria_relations, belgium_relations, brit_relations, \
    cuba_relations, france_relations, luxembourg_relations, netherlands_relations, spain_relations
from database_management import upload_database
from randomness import random_functions
# helper libraries
import os
import time
import random
import sys
from collections import OrderedDict

# function uploading to databas

"""Population Dictionaries"""
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

def establish_foreign_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function"""
    for i in range(0, len(args)):
        globe.nations.append(args[i])

def slow_print(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.19)

class UnitedStates:
    def __init__(self, year):
        self.name = "UnitedStates"
        # date variables
        self.date = datetime(int(year), 1, 1)
        self.upload_to_database = self.date.month
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = 0
        self.past_population = 0
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = presidents[year]
        self.vp = vice_presidents[year]
        if "self.monarch" in locals():
            print("ty")
        """Stability"""
        self.stability = 95.56
        self.political_power = 256
        self.political_exponent = 2.56
        self.states = []
        # economic
        self.national_debt = 0
        self.current_gdp = 0
        self.past_gdp = 0
        self.e_s = "recovery"
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
        self.alliance = ""
        # north america
        """canada"""
        self.canada_relations = 55.65
        self.guarantee_canada = False
        self.embargo_canada = False
        self.canada_nationals_dealt = False
        """mexico"""
        self.mexico_relations = 55.65
        self.guarantee_mexico = False
        self.embargo_mexico = False
        self.mexico_nationals_dealt = False
        """cuba"""
        self.cuba_relations = 86.56
        self.guarantee_cuba = False
        self.embargo_cuba = False
        self.cuba_nationals_dealt = False
        # na ordered dictionary
        self.na = OrderedDict()
        self.na["Dominion of Canada"] = self.canada_relations
        self.na["Republic of Cuba"] = self.cuba_relations
        self.na["Mexico"] = self.mexico_relations
        # asia
        """China"""
        self.china_relations = 65.45
        self.guarantee_china = False
        self.embargo_china = False
        self.china_nationals_dealt = False
        """Japan"""
        self.japan_relations = 76.45
        self.guarantee_japan = False
        self.embargo_japan = False
        self.japan_nationals_dealt = False
        # asia ordered dictionary
        self.asia = OrderedDict()
        self.asia["Republic of China"] = self.china_relations
        self.asia["Japanese Empire"] = self.japan_relations
        # europe
        """british"""
        self.brit_relations = 73.45
        self.guarantee_britain = False
        self.britain_embargo = False
        self.british_nationals_dealt = False
        """spanish"""
        self.spain_relations = 70.34
        self.guarantee_spain = False
        self.spain_embargo = False
        self.spain_nationals_dealt = False
        """french"""
        self.france_relations = 80.76
        self.guarantee_france = False
        self.france_embargo = False
        self.france_nationals_dealt = False
        """german"""
        """self.germany_relations = 76.45
        self.guarantee_germany = False
        self.germany_embargo = False
        self.germany_nationals_dealt = False"""
        """belgian"""
        self.belgium_relations = 81.65
        self.guarantee_belgium = False
        self.belgium_embargo = False
        self.belgium_nationals_dealt = False
        """austrian"""
        self.austria_relations = 58.45
        self.guarantee_austria = False
        self.austria_embargo = False
        self.austria_nationals_dealt = False
        """dutch"""
        self.netherlands_relations = 74.34
        self.guarantee_netherlands = False
        self.netherlands_embargo = False
        self.netherlands_nationals_dealt = False
        """luxembourg"""
        self.luxembourg_relations = 92.34
        self.guarantee_luxembourg = False
        self.luxembourg_embargo = False
        self.luxembourg_nationals_dealt = False
        """denmark"""
        self.danish_relations = 72.34
        self.guarantee_danish = False
        self.danish_embargo = False
        self.danish_nationals_dealt = False
        """italy"""
        self.italy_relations = 95.74
        self.guarantee_italy = False
        self.italy_embargo = False
        self.italy_nationals_dealt = False
        """norwegian"""
        self.norway_relations = 96.44
        self.guarantee_norway = False
        self.norway_embargo = False
        self.norway_nationals_dealt = False
        """swedish"""
        self.swedish_relations = 94.34
        self.guarantee_swedish = False
        self.swedish_embargo = False
        self.swedish_nationals_dealt = False
        """swiss"""
        self.swiss_relations = 98.74
        self.guarantee_swiss = False
        self.swiss_embargo = False
        self.swiss_nationals_dealt = False
        """estonian"""
        self.estonia_relations = 98.74
        self.guarantee_estonia = False
        self.estonia_embargo = False
        self.estonia_nationals_dealt = False
        """latvian"""
        self.latvia_relations = 98.74
        self.guarantee_latvia = False
        self.latvia_embargo = False
        self.latvia_nationals_dealt = False
        """lithuanian"""
        self.lithuania_relations = 98.74
        self.guarantee_lithuania = False
        self.lithuania_embargo = False
        self.lithuania_nationals_dealt = False
        """greek"""
        self.greece_relations = 82.34
        self.guarantee_greece = False
        self.greece_embargo = False
        self.greece_nationals_dealt = False
        """romanian"""
        self.romania_relations = 82.34
        self.guarantee_romania = False
        self.romania_embargo = False
        self.romania_nationals_dealt = False
        """serbian"""
        self.serbia_relations = 82.34
        self.guarantee_serbia = False
        self.serbia_embargo = False
        self.serbia_nationals_dealt = False
        # ordered dictionary of european nations
        self.european_nations = OrderedDict()
        self.european_nations['Great Britain'] = self.brit_relations
        self.european_nations['Kingdom of Spain'] = self.spain_relations
        self.european_nations['French Republic'] = self.france_relations
        self.european_nations['Kingdom of Belgium'] = self.belgium_relations
        self.european_nations['Austria-Hungary'] = self.austria_relations
        #self.european_nations['German Empire'] = self.germany_relations
        self.european_nations['Kingdom of Netherlands'] = self.netherlands_relations
        self.european_nations['Kingdom of Luxembourg'] = self.luxembourg_relations
        self.european_nations['Kingdom of Denmark'] = self.danish_relations
        self.european_nations['Kingdom of Italy'] = self.italy_relations
        self.european_nations['Kingdom of Norway'] = self.norway_relations
        self.european_nations['Republic of Sweden'] = self.swedish_relations
        self.european_nations['Republic of Switzerland'] = self.swiss_relations
        """self.european_nations['Republic of Estonia'] = self.estonia_relations
        self.european_nations['Republic of Latvia'] = self.latvia_relations
        self.european_nations['Republic of Lithuania'] = self.lithuania_relations"""
        # will be added in later, when I figure out how to set time constraints upon these 3 nations
        self.european_nations['Kingdom of Greece'] = self.greece_relations
        self.european_nations['Kingdom of Romania'] = self.romania_relations
        self.european_nations['Kingdom of Serbia'] = self.serbia_relations
        # asia
        """serbian"""
        self.ethiopia_relations = 72.34
        self.guarantee_ethiopia = False
        self.ethiopia_embargo = False
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
            for i in range(0, len(self.states)):
                self.states[i].population_change()

    # establishing internal states
    def establish_states(self):
        folder = "us_states"
        for file in os.listdir(folder):
            """Looping through us states folder, will be refined later on"""
            if file != '__pycache__' or file != "us.py" or file != "us_ai.py":
                if file.removesuffix(".py") == "alabama":
                    self.states.append(alabama.Alabama(self.date.year, self))
                if file.removesuffix(".py") == "alaska":
                    self.states.append(alaska.Alaska(self.date.year, self))
                if file.removesuffix(".py") == "arizona":
                    self.states.append(arizona.Arizona(self.date.year, self))
                if file.removesuffix(".py") == "arkansas":
                    self.states.append(arkansas.Arkansas(self.date.year, self))
                if file.removesuffix(".py") == "california":
                    self.states.append(california.California(self.date.year, self))
                if file.removesuffix(".py") == "colorado":
                    self.states.append(colorado.Colorado(self.date.year, self))
                if file.removesuffix(".py") == "connecticut":
                    self.states.append(conneticut.Conneticut(self.date.year, self))
                if file.removesuffix(".py") == "delaware":
                    self.states.append(delaware.Delaware(self.date.year, self))
                if file.removesuffix(".py") == "florida":
                    self.states.append(florida.Florida(self.date.year, self))
                if file.removesuffix(".py") == "georgia":
                    self.states.append(georgia.Georgia(self.date.year, self))
                if file.removesuffix(".py") == "hawaii":
                    self.states.append(hawaii.Hawaii(self.date.year, self))
                if file.removesuffix(".py") == "idaho":
                    self.states.append(idaho.Idaho(self.date.year, self))
                if file.removesuffix(".py") == "illinois":
                    self.states.append(illinois.Illinois(self.date.year, self))
                if file.removesuffix(".py") == "indiana":
                    self.states.append(indiana.Indiana(self.date.year, self))
                if file.removesuffix(".py") == "iowa":
                    self.states.append(iowa.Iowa(self.date.year, self))
                if file.removesuffix(".py") == "kansas":
                    self.states.append(kansas.Kansas(self.date.year, self))
                if file.removesuffix(".py") == "kentucky":
                    self.states.append(kentucky.Kentucky(self.date.year, self))
                if file.removesuffix(".py") == "louisiana":
                    self.states.append(louisiana.Louisiana(self.date.year, self))
                if file.removesuffix(".py") == "maine":
                    self.states.append(maine.Maine(self.date.year, self))
                if file.removesuffix(".py") == "maryland":
                    self.states.append(maryland.Maryland(self.date.year, self))
                if file.removesuffix(".py") == "michigan":
                    self.states.append(michigan.Michigan(self.date.year, self))
                if file.removesuffix(".py") == "mississippi":
                    self.states.append(mississppi.Mississippi(self.date.year, self))
                if file.removesuffix(".py") == "missouri":
                    self.states.append(missouri.Missouri(self.date.year, self))
                if file.removesuffix(".py") == "montana":
                    self.states.append(montana.Montana(self.date.year, self))
                if file.removesuffix(".py") == "n_d":
                    self.states.append(n_d.NorthDakota(self.date.year, self))
                if file.removesuffix(".py") == "n_m":
                    self.states.append(n_m.NewMexico(self.date.year, self))
                if file.removesuffix(".py") == "nebraska":
                    self.states.append(nebraska.Nebraska(self.date.year, self))
                if file.removesuffix(".py") == "nebraska":
                    self.states.append(nevada.Nevada(self.date.year, self))
                if file.removesuffix(".py") == "new_hampshire":
                    self.states.append(new_hampshire.NewHampshire(self.date.year, self))
                if file.removesuffix(".py") == "new_jersey":
                    self.states.append(new_jersey.NewJersey(self.date.year, self))
                if file.removesuffix(".py") == "new_york":
                    self.states.append(new_york.NewYork(self.date.year, self))
                if file.removesuffix(".py") == "north_carolina":
                    self.states.append(north_carolina.NorthCarolina(self.date.year, self))
                if file.removesuffix(".py") == "ohio":
                    self.states.append(ohio.Ohio(self.date.year, self))
                if file.removesuffix(".py") == "ok":
                    self.states.append(ok.Oklahoma(self.date.year, self))
                if file.removesuffix(".py") == "oregon":
                    self.states.append(oregon.Oregon(self.date.year, self))
                if file.removesuffix(".py") == "pennsylvania":
                    self.states.append(pennsylvania.Pennsylvania(self.date.year, self))
                if file.removesuffix(".py") == "rhode_island":
                    self.states.append(rhode_island.RhodeIsland(self.date.year, self))
                if file.removesuffix(".py") == "s_d":
                    self.states.append(s_d.SouthDakota(self.date.year, self))
                if file.removesuffix(".py") == "south_carolina":
                    self.states.append(south_carolina.SouthCarolina(self.date.year, self))
                if file.removesuffix(".py") == "tennessee":
                    self.states.append(tennessee.Tennessee(self.date.year, self))
                if file.removesuffix(".py") == "texas":
                    self.states.append(texas.Texas(self.date.year, self))
                if file.removesuffix(".py") == "utah":
                    self.states.append(utah.Utah(self.date.year, self))
                if file.removesuffix(".py") == "vermont":
                    self.states.append(vermont.Vermont(self.date.year, self))
                if file.removesuffix(".py") == "virginia":
                    self.states.append(virginia.Virginia(self.date.year, self))
                if file.removesuffix(".py") == "washington":
                    self.states.append(washington.Washington(self.date.year, self))
                if file.removesuffix(".py") == "west_virginia":
                    self.states.append(west_virginia.WestVirginia(self.date.year, self))
                if file.removesuffix(".py") == "wisconsin":
                    self.states.append(wisconsin.Wisconsin(self.date.year, self))
                if file.removesuffix(".py") == "wyoming":
                    self.states.append(wyoming.Wyoming(self.date.year, self))

        self.establish_economy_population()

    def establish_economy_population(self):
        for i in range(0, len(self.states) - 1):
            self.current_gdp += self.states[i].current_gdp
            self.population += self.states[i].population
        self.past_gdp = self.current_gdp
        self.past_population = self.population

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
            for i in range(0, len(self.states)):
                self.states[i].check_economic_state()

    # political growth functions
    """def political_growth(self, globe):
        self.political_power += self.political_exponent

        if globe.tension < 50:"""

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
        print(f"Your current vice president is {self.vp}.\n")
        time.sleep(3)
        print(f"The US is currently {self.stability}% politically stable.\n")
        time.sleep(3)
        print(
            f"You have {self.political_power} political power to manipulate both your central and state governments.\n"
            f"This power also ties into what you can do internationally.\n")
        time.sleep(3)
        print(f"Your political power currently grows at a {self.political_exponent} incremental rate.\n")
        time.sleep(3)
        print(f"There are currently {len(self.states)} states in the Union.\n")
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
                    for key, value in self.european_nations.items():
                        print(f"Relations with {key}: {value}.\n")
                        time.sleep(1.25)
                        """looping through european relations"""
                    choice = input(
                        "Would you like to manipulate your relations with one of those nations?(enter quit to escape):")

                    if choice.lower() == "yes" or choice.lower() == 'y':
                        nation_choice = input("Which European nation would you like to choose?: ")
                        if nation_choice.lower() == "britain" or nation_choice.lower() == "great britain":
                            for i in range(0, len(globe1.nations)):
                                """searching for Great Britain"""
                                if globe1.nations[i].name == "Great Britain":
                                    brit_relations.british_relations(self, globe1.nations[i], globe1)

                        if nation_choice.lower() == "spain":
                            for i in range(0, len(globe1.nations)):
                                """searching for Spain"""
                                if globe1.nations[i].name == "Kingdom of Spain":
                                    spain_relations.spanish_relations(self, globe1.nations[i], globe1)

                        if nation_choice.lower() == "france":
                            for i in range(0, len(globe1.nations)):
                                """searching for france"""
                                if globe1.nations[i].name == "French Republic":
                                    france_relations.french_relations(self, globe1.nations[i], globe1)

                        if nation_choice.lower() == "belgium":
                            for i in range(0, len(globe1.nations)):
                                """searching for Belgium"""
                                if globe1.nations[i].name == "Kingdom of Belgium":
                                    belgium_relations.belgian_relations(self, globe1.nations[i], globe1)

                        if nation_choice.lower() == "netherlands":
                            for i in range(0, len(globe1.nations)):
                                """searching for Netherlands"""
                                if globe1.nations[i].name == "Kingdom of Netherlands":
                                    netherlands_relations.dutch_relations(self, globe1.nations[i], globe1)

                        if nation_choice.lower() == "luxembourg":
                            for i in range(0, len(globe1.nations)):
                                """searching for Netherlands"""
                                if globe1.nations[i].name == "Kingdom of Luxembourg":
                                    luxembourg_relations.luxembourger_relations(self, globe1.nations[i], globe1)

                        if nation_choice.lower() == "austria":
                            for i in range(0, len(globe1.nations)):
                                """searching for Netherlands"""
                                if globe1.nations[i].name == "Austria-Hungary" or globe1.nations[i].name == "Republic of Austria":
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

                    choice = input(
                        "Would you like to manipulate your relations with one of those nations?(enter quit to escape):")
                    if choice.lower() == "yes" or choice.lower() == 'y':

                        nation_choice = input("Which North American nation would you like to choose?: ")
                        if nation_choice.lower() == "canada":
                            for i in range(0, len(globe1.nations)):
                                """Looping until canada is found
                                reason why globe variable is used for nation is to funnel down required amount of variables 
                                for proper use.
                                """
                                if globe1.nations[i].name == "Canada":
                                    canada_relations.canadian_relations(self, globe1.nations[i], globe1)

                        elif nation_choice.lower() == "mexico":

                            for i in range(0, len(globe1.nations)):
                                """Looping until Mexico is found
                                reason why globe variable is used for nation is to funnel down required amount of variables 
                                for proper use.
                                """
                                if globe1.nations[i].name == "Mexico":
                                    mexico_relations.mexican_relations(self, globe1.nations[i], globe1)

                        elif nation_choice.lower() == "cuba":

                            for i in range(0, len(globe1.nations)):
                                """Looping until Mexico is found
                                reason why globe variable is used for nation is to funnel down required amount of variables 
                                for proper use.
                                """
                                if globe1.nations[i].name == "Cuba":
                                    cuba_relations.cuban_relations(self, globe1.nations[i], globe1)

            elif region_choice.lower() == "quit":
                done = False
            else:
                print("Please answer carefully!!")

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

def main():
    globe1 = globe.Globe()
    us = UnitedStates('1914')
    us.establish_states()
    print(us.date.date())
    # establishing asian AIs
    chinese_ai = china_ai.ChinaAI("1914")
    japanese_ai = japan_ai.Japan("1914")
    # establishing european AIs
    british_ai = britain_ai.Britain("1914")
    spanish_ai = spain_ai.SpainAI("1914")
    french_ai = france_ai.FranceAI("1914")
    austrian_ai = austria_ai.Austria("1914")
    # germany_ai = german_ai.Germany("1914")
    """german ai will establish states, similar to US"""
    belgian_ai = belgium_ai.BelgiumAI("1914")
    dutch_ai = netherlands_ai.Netherlands("1914")
    italian_ai = italy_ai.ItalyAI("1914")
    lux_ai = luxembourg_ai.LuxembourgAI("1914")
    danish_ai = denmark_ai.Denmark("1914")
    swiss_ia = swiss_ai.SwitzerlandAI("1914")
    swedish_ai = sweden_ai.SwedenAI("1914")
    norwegian_ai = norway_ai.NorwayAI("1914")
    """
    These 3 nations will be uncommented, once I figure out how to exclude them until 1918
    estonian_ai = estonia_ai.EstoniaAI('1914')
    latvian_ai = latvia_ai.LatviaAI("1914")
    lithuanian_ai = lithuania_ai.Lithuania("1914")"""
    greek_ai = greece_ai.Greece("1914")
    romanian_ai = romania_ai.RomaniaAI('1914')
    serbian_ai = serbia_ai.SerbiaAI('1914')
    # establishing north american AIs
    canadian_ai = canada_ai.Canada("1914")
    mexican_ai = mexico_ai.MexicoAI("1914")
    cuban_ai = cuba_ai.CubaAI("1914")
    establish_foreign_nations(globe1, us, canadian_ai, mexican_ai, cuban_ai, chinese_ai, japanese_ai,
                              british_ai, austrian_ai, belgian_ai, dutch_ai, french_ai, spanish_ai, italian_ai, lux_ai,
                              danish_ai, swedish_ai, swiss_ia, norwegian_ai, greek_ai, romanian_ai, serbian_ai)

    upload_database.initial_upload_to_database(globe1.nations)

    while us.population > 3000000:
        """United States will stay afloat as a nation, as long as 3000000 people are left"""
        us.check_economic_state()
        us.population_change()
        us.stats(globe1)
        us.stability_happiness_change(globe1)
        random_functions.random_functions(us, globe1)

        """Looping through changes in US system"""

        for i in range(0, len(globe1.nations)):
            if not globe1.nations[i].name == "UnitedStates":
                globe1.nations[i].main(globe1)
                """
                looping through main function of each foreign nation object
                main function is connected to object itself, so as to use less memory space
                """

        upload_database.update_database_info(globe1.nations)
        time.sleep(1.75)
        us.date += timedelta(days=1)


if __name__ == '__main__':
    main()
