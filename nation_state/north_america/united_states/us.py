import random
from collections import ChainMap
import globe
import time
from datetime import datetime, timedelta
from us_states import (alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas,
                       kentucky, louisiana, maine, maryland, michigan, minnesota, mississppi, missouri, montana, n_d,
                       n_m, nebraska, nevada, new_hampshire, new_jersey, new_york, north_carolina, ok, oregon,
                       pennsylvania,
                       rhode_island, ohio, s_d, south_carolina, tennessee, texas, utah, vermont, virginia, washington,
                       west_virginia, wisconsin, wyoming)
from nation_state.europe.britain import britain_ai
# from nation_state.europe.germany import german_ai
from nation_state.europe.italy import italy_ai
import os

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


class UnitedStates:
    def __init__(self, year):
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
        self.europe_nations = {}
        # europe
        """british"""
        self.brit_relations = 73.45
        self.guarantee_britain = False
        """german"""
        self.german_relations = 65.45
        self.guarantee_german = False
        """russian"""
        self.russian_relations = 66.42
        self.guarantee_russian = False
        """french"""
        self.french_relations = 73.56
        self.guarantee_french = False
        """belgian"""
        self.belgian_relations = 70.56
        self.guarantee_belgian = False
        """austrian"""
        self.austrian_relations = 70.56
        self.guarantee_austrian = False
        """hungarian"""
        self.hungarian_relations = 68.56
        self.guarantee_hungarian = False
        """austrian"""
        self.danish_relations = 72.23
        self.guarantee_danish = False
        self.europe_nations = {'austria': self.austrian_relations, 'britain': self.brit_relations,
                               'belgium': self.belgian_relations,
                               'denmark': self.danish_relations, 'germany': self.german_relations,
                               "france": self.french_relations,
                               'hungary': self.hungarian_relations, 'russia': self.russian_relations}
        # asia
        """japanese"""
        self.japanese_relations = 67.94
        self.guarantee_japanese = False
        """chinese"""
        self.chinese_relations = 65.94
        self.guarantee_chinese = False
        """india"""
        self.indian_relations = 66.94
        self.guarantee_indian = False
        """iran"""
        self.iranian_relations = 72.94
        self.guarantee_iranian = False
        """turkey"""
        self.turkish_relations = 72.94
        self.guarantee_turkish = False
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
            if file != '__pycache__':
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

    # stability functions
    # stats functions
    def stats(self, british, globe1):
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
            self.international_stats(british, globe1)

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
        print(f"Your current GDP growth rate is {round(((self.current_gdp - self.past_gdp) / ((self.current_gdp + self.past_gdp) / 2)) * 100, 6)}%.\n")
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

    def international_stats(self, british_ai, globe1):
        """Checking of foreign relations"""
        done = True
        while done:
            region_choice = input(
                "Would you like to view your...European, Asian, South American, or African relations(enter quit to escape)?: ")
            if region_choice.lower() == "european":
                nations = ["austria", "belgium", "britain", "denmark", "france", "germany", "hungary", "russia"]
                for i in range(0, len(nations)):
                    print(f"{nations[i]} relations : {self.europe_nations[nations[i]]}.\n")
                    time.sleep(1.5)
                    """looping through european relations"""
                choice = input(
                    "would you like to improve your relations with one of those nations?(enter quit to escape):")
                if choice.lower() == "yes" or choice.lower() == 'y':
                    nation_choice = input("which European nation would you like to choose?: ")
                    if nation_choice.lower() == "austria":
                        pass
                    elif nation_choice.lower() == "belgium":
                        pass
                    elif nation_choice.lower() == "britain":
                        self.british_relations(british_ai, globe1)
                    elif nation_choice.lower() == "denmark":
                        pass
                    elif nation_choice.lower() == "france":
                        pass
                    elif nation_choice.lower() == "germany":
                        pass
                    elif nation_choice.lower() == "hungary":
                        pass
                    elif nation_choice.lower() == "russia":
                        pass

            elif region_choice.lower() == "asian":
                pass
            elif region_choice.lower() == "south american":
                pass
            elif region_choice.lower() == "african":
                pass
            elif region_choice.lower() == "quit":
                done = False
            else:
                print("Please answer carefully!!")

    def british_relations(self, british_ai, globe):
        positive = ["\n1. improve relations for 60 days(15 political power, decrease pp exponent by 0.2 points)",
                    "2. guarantee british independence(10 initial political power, decrease pp exponent by 0.5 points",
                    "3. increase exports to britain for 60 days(25 political power, improves US economy)",
                    "4. establish a US embassy within London(13 political power cost, decrease 0.1 pp exponent while its installed",
                    "5. establish an economic treaty with Britain(15 political power, improves both economies)",
                    "6. establish a military alliance with Britain(10 political power)",
                    "7. Establish student transfer student program(improve economy for 120 days)"]

        negative = ["1. Expel British nationals(loss in US population, worsen relations by 25%)",
                    "2. Jail British nationals(worsen relations by 1.25% every day nationals are in jail)",
                    "3. Kill British nationals(worsen relations by 50%, potential "
                    "for Britain to embargo or declare war on US)",
                    "4. Embargo British economy(worsen relations by 35%, hurts both economies)",
                    "5. Leave alliance(if not in alliance will not affect relationship)",
                    "6. Hurt British relations for 30 days(15 political power initially, decrease by 0.75% every day)",
                    "7. Declare war on Britain(if Britain is in an alliance, other nations could get involved)"]
        done = True
        while done:
            type_choice = input("\nWould you like to improve or hinder relations with Britain?(enter quit to escape)\n"
                                f"Remember you have {self.political_power} political power left: ")
            if type_choice.lower() == "improve":
                for i in range(0, len(positive)):
                    print(f"{positive[i]}.\n")
                    time.sleep(1.25)

                relation_choice = int(input("would you like to choose 1 - 7?(enter quit to escape): "))
                chance = random.randrange(0, 75)

                if globe.tension < 50 and self.brit_relations > 50:
                    """high chance that British parliament will accept proposals"""

                    if relation_choice == 1:
                        if self.political_power >= 15:
                            self.political_power -= 15
                            if chance % 2 == 0:
                                """50.67% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to improve relations with the United States.\n")
                                self.political_exponent -= 0.2
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.3% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 2:
                                """24% chance that US diplomats get killed """
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 2 and not self.guarantee_britain:
                        if self.political_power >= 10:
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has accepted our guarantee for their independence.\n")
                                self.political_exponent -= 0.5
                                self.guarantee_britain = True
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)


                            elif chance % 4 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 3:
                        if self.political_power >= 25:
                            self.political_power -= 25
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to buy more American goods.\n")
                                time.sleep(1.5)


                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)


                            elif chance % 4 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)
                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 4:
                        if self.political_power >= 13:
                            self.political_power -= 13
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to install an US embassy within London.\n")
                                self.political_exponent -= 0.1
                                time.sleep(1.5)


                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)


                            elif chance % 4 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 5:
                        if self.political_power >= 15:
                            self.political_power -= 15
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(
                                    f"{british_ai.pm} has agreed to establish an economic treaty with the United States\n")
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 6:
                        if self.political_power >= 10:
                            self.political_power -= 10
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                if british_ai.alliance:
                                    print(f"{british_ai.pm} has allowed us to enter the {british_ai.alliance}\n")
                                    time.sleep(1.5)
                                else:
                                    print(f"{british_ai.pm} has agreed to forming a military alliance")
                                    time.sleep(1.5)
                                    alliance = input("what would you like to name your alliance?: ")
                                    self.alliance = alliance
                                    british_ai.alliance = alliance

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 7:
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{british_ai.pm} has agreed to establish a student transfer program\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            british_ai.us_relations -= round(random.uniform(1, 2), 2)
                            self.brit_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 2:
                            """24% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            british_ai.us_relations -= round(random.uniform(1, 6), 2)
                            self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                if globe.tension < 50 and self.brit_relations < 50:
                    """moderate chance that British Parliament will accept proposals"""

                    if relation_choice == 1:
                        if self.political_power >= 15:
                            self.political_power -= 15
                            chance = random.randrange(1, 60)
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to improve relations with the United States.\n")
                                self.political_exponent -= 0.2
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 3:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 2 and not self.guarantee_britain:
                        if self.political_power >= 10:
                            self.political_power -= 10
                            chance = random.randrange(1, 60)
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has accepted our guarantee for their independence.\n")
                                self.political_exponent -= 0.5
                                self.guarantee_britain = True
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 3:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 3:
                        if self.political_power >= 25:
                            self.political_power -= 25
                            chance = random.randrange(1, 60)
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to buy more American goods.\n")
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 3:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 4:
                        if self.political_power >= 13:
                            self.political_power -= 13
                            chance = random.randrange(1, 60)
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to install an US embassy within London.\n")
                                self.political_exponent -= 0.1
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 3:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 5:
                        if self.political_power >= 15:
                            self.political_power -= 15
                            chance = random.randrange(1, 60)
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(
                                    f"{british_ai.pm} has agreed to establish an economic treaty with the United States\n")
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 3:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 6:
                        if self.political_power >= 10:
                            self.political_power -= 10
                            chance = random.randrange(1, 60)
                            if chance % 2 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                if british_ai.alliance:
                                    print(f"{british_ai.pm} has allowed us to enter the {british_ai.alliance}\n")
                                    time.sleep(1.5)
                                else:
                                    print(f"{british_ai.pm} has agreed to forming a military alliance")
                                    time.sleep(1.5)
                                    alliance = input("what would you like to name your alliance?: ")
                                    self.alliance = alliance
                                    british_ai.alliance = alliance

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 4 == 3:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 7:
                        chance = random.randrange(1, 60)
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{british_ai.pm} has agreed to establish a student transfer program\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            british_ai.us_relations -= round(random.uniform(1, 2), 2)
                            self.brit_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 3:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            british_ai.us_relations -= round(random.uniform(1, 6), 2)
                            self.brit_relations -= round(random.uniform(1, 6), 2)

                elif globe.tension > 50 and self.brit_relations > 50:
                    """low to moderate chance that British parliament will accept proposals"""
                    chance = random.randrange(0, 45)

                    if relation_choice == 1:
                        if self.political_power >= 15:
                            self.political_power -= 15
                            if chance % 3 == 0:
                                """33.3% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to improve relations with the United States.\n")
                                self.political_exponent -= 0.2
                                time.sleep(1.5)

                            elif chance % 2 == 0:
                                """51.1% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 5 == 2:
                                """20% chance that US diplomats get killed """
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)
                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 2 and not self.guarantee_britain:
                        if self.political_power >= 10:
                            if chance % 3 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has accepted our guarantee for their independence.\n")
                                self.political_exponent -= 0.5
                                self.guarantee_britain = True
                                time.sleep(1.5)

                            elif chance % 2 == 0:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)


                            elif chance % 5 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 3:
                        if self.political_power >= 25:
                            self.political_power -= 25
                            if chance % 3 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to buy more American goods.\n")
                                time.sleep(1.5)


                            elif chance % 2 == 0:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)


                            elif chance % 5 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)
                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 4:
                        if self.political_power >= 13:
                            """If player has enough political capital to follow through with choice"""
                            self.political_power -= 13
                            if chance % 3 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to install an US embassy within London.\n")
                                self.political_exponent -= 0.1
                                time.sleep(1.5)


                            elif chance % 2 == 0:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)


                            elif chance % 5 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)
                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 5:
                        if self.political_power >= 15:
                            self.political_power -= 15
                            if chance % 3 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(
                                    f"{british_ai.pm} has agreed to establish an economic treaty with the United States\n")
                                time.sleep(1.5)

                            elif chance % 2 == 0:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 5 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)
                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 6:
                        if self.political_power >= 10:
                            self.political_power -= 10
                            if chance % 3 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                if british_ai.alliance:
                                    print(f"{british_ai.pm} has allowed us to enter the {british_ai.alliance}\n")
                                    time.sleep(1.5)
                                else:
                                    print(f"{british_ai.pm} has agreed to forming a military alliance")
                                    time.sleep(1.5)
                                    alliance = input("what would you like to name your alliance?: ")
                                    self.alliance = alliance
                                    british_ai.alliance = alliance

                            elif chance % 2 == 0:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 5 == 2:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 7:
                        if chance % 3 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{british_ai.pm} has agreed to establish a student transfer program\n")
                            time.sleep(1.5)

                        elif chance % 2 == 0:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            british_ai.us_relations -= round(random.uniform(1, 2), 2)
                            self.brit_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 5 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            british_ai.us_relations -= round(random.uniform(1, 6), 2)
                            self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                elif globe.tension > 50 and self.brit_relations > 50:
                    """very low chance that British parliament will accept proposals"""

                    chance = random.randrange(0, 75)

                    if relation_choice == 1:
                        if self.political_power >= 15:
                            self.political_power -= 15
                            if chance % 5 == 0:
                                """20% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to improve relations with the United States.\n")
                                self.political_exponent -= 0.2
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.3% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 2 == 0:
                                """50.67% chance that US diplomats get killed """
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 2 and not self.guarantee_britain:
                        if self.political_power >= 10:
                            if chance % 5 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has accepted our guarantee for their independence.\n")
                                self.political_exponent -= 0.5
                                self.guarantee_britain = True
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 2 == 0:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)
                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 3:
                        if self.political_power >= 25:
                            self.political_power -= 25
                            if chance % 5 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to buy more American goods.\n")
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 2 == 0:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 4:
                        if self.political_power >= 13:
                            self.political_power -= 13
                            if chance % 5 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(f"{british_ai.pm} has agreed to install an US embassy within London.\n")
                                self.political_exponent -= 0.1
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 2 == 0:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 5:
                        if self.political_power >= 15:
                            self.political_power -= 15
                            if chance % 5 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                print(
                                    f"{british_ai.pm} has agreed to establish an economic treaty with the United States\n")
                                time.sleep(1.5)

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 2 == 0:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 6:
                        if self.political_power >= 10:
                            self.political_power -= 10
                            if chance % 5 == 0:
                                """49.1% chance that British parliament accepts proposal"""
                                if british_ai.alliance:
                                    print(f"{british_ai.pm} has allowed us to enter the {british_ai.alliance}\n")
                                    time.sleep(1.5)
                                else:
                                    print(f"{british_ai.pm} has agreed to forming a military alliance")
                                    time.sleep(1.5)
                                    alliance = input("what would you like to name your alliance?: ")
                                    self.alliance = alliance
                                    british_ai.alliance = alliance

                            elif chance % 3 == 1:
                                """33.8% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been kicked out of Parliament.\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 2), 2)
                                british_ai.us_relations -= round(random.uniform(1, 2), 2)
                                self.brit_relations -= round(random.uniform(1, 2), 2)

                            elif chance % 2 == 0:
                                """25.4% chance that US diplomats get kicked out of Britain"""
                                print("Your diplomats have been called out for espionage and have been killed\n")
                                time.sleep(1.5)
                                globe.tension += round(random.uniform(0.5, 5), 2)
                                british_ai.us_relations -= round(random.uniform(1, 6), 2)
                                self.brit_relations -= round(random.uniform(1, 6), 2)

                            else:
                                print("Your offer died in the sea of geopolitics.\n")
                                time.sleep(3)

                        else:
                            print(f"You do not have enough political capital to carry through with this task!!.\n")
                            time.sleep(1.25)

                    elif relation_choice == 7:
                        if chance % 5 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{british_ai.pm} has agreed to establish a student transfer program\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            british_ai.us_relations -= round(random.uniform(1, 2), 2)
                            self.brit_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 2 == 0:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            british_ai.us_relations -= round(random.uniform(1, 6), 2)
                            self.brit_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                        if type_choice.lower() == "quit":
                            done = False
            elif type_choice.lower() == "quit":
                done = False


def main():
    globe1 = globe.Globe()
    us = UnitedStates('1914')
    us.establish_states()
    british_ai = britain_ai.Britain("1914")
    while us.population > 3000000:
        us.check_economic_state()
        us.population_change()
        print(us.births, us.deaths, us.population)
        us.stats(british_ai, globe1)
        time.sleep(3)


if __name__ == '__main__':
    main()
