import random
import time
from collections import OrderedDict
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
from nation_state.north_america.mexico import mexico_ai
import randomness


def establish_foreign_nations(globe, *args):
    """labelling second parameter as *args, due to unknown number of nations that will be sent into this function"""
    for i in range(0, len(args)):
        globe.nations.append(args[i])


"""Population Dictionaries"""
population = {
    "1910": 7041174,
    "1914": 7674382,
    "1918": 8302357,
    "1932": 10477365,
    "1936": 10957346,
    "1939": 11413434
}

"""Political Dictionaries"""
pms = {
    "1910": "Wilfrid Laurier",
    "1914": "Robert Borden",
    "1918": "Robert Borden",
    "1932": "R. B. Bennett",
    "1936": "William Mackenzie King",
    "1939": "William Mackenzie King"
}

gdp = {
    "1910": 50000000,
    "1914": 65993945,
    "1918": 73348873,
    "1932": 72348873,
    "1936": 72348873,
    "1939": 74348873
}


class Canada:
    def __init__(self, year):
        self.is_intact = True
        self.name = "Canada"
        # date variables
        self.date = datetime(int(year), 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_stimulus = self.date
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[year]
        self.birth_enhancer = False
        self.birth_control = False
        self.births = 0
        self.deaths = 0
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = pms[year]
        """Stability"""
        self.stability = 95.56
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
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
        """general"""
        self.alliance = ""
        # north america
        """canada"""
        self.mexico_relations = 55.65
        self.mexico_nationals_dealt = False
        """cuba"""
        self.cuba_relations = 86.56
        self.cuba_nationals_dealt = False
        # na ordered dictionary
        self.na = OrderedDict()
        self.na["Mexico"] = self.mexico_relations
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
        """spanish"""
        self.spain_relations = 70.34
        self.spain_nationals_dealt = False
        """french"""
        self.france_relations = 80.76
        self.france_nationals_dealt = False
        """german"""
        """self.germany_relations = 76.45
        self.guarantee_germany = False
        self.germany_embargo = False
        self.germany_nationals_dealt = False"""
        """belgian"""
        self.belgium_relations = 81.65
        self.belgium_nationals_dealt = False
        """austrian"""
        self.austria_relations = 58.45
        self.austria_nationals_dealt = False
        """dutch"""
        self.netherlands_relations = 74.34
        self.netherlands_nationals_dealt = False
        """luxembourg"""
        self.luxembourg_relations = 92.34
        self.luxembourg_nationals_dealt = False
        """denmark"""
        self.danish_relations = 72.34
        self.danish_nationals_dealt = False
        """italy"""
        self.italy_relations = 95.74
        self.italy_nationals_dealt = False
        """norwegian"""
        self.norway_relations = 96.44
        self.norway_nationals_dealt = False
        """swedish"""
        self.swedish_relations = 94.34
        self.swedish_nationals_dealt = False
        """swiss"""
        self.swiss_relations = 98.74
        self.swiss_nationals_dealt = False
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
        """romanian"""
        self.romania_relations = 82.34
        self.romania_nationals_dealt = False
        """serbian"""
        self.serbia_relations = 82.34
        self.serbia_nationals_dealt = False
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
                births = random.randrange(8, 15)
                deaths = random.randrange(3, 11)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            if self.birth_control:
                births = random.randrange(3, 10)
                deaths = random.randrange(6, 15)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            else:
                births = random.randrange(5, 12)
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

            self.consumer_spending = -round(random.uniform(10, 200), 2)
            self.government_spending = round(random.uniform(100, 500), 2)
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = round(random.uniform(50, 150), 2)
            self.exports = round(random.uniform(10, 50), 2)
            self.imports = round(random.uniform(10, 20), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

        else:
            self.consumer_spending = -round(random.uniform(10, 200), 2)
            self.government_spending = round(random.uniform(100, 500), 2)
            self.national_debt += round(
                (-self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = -round(random.uniform(100, 300), 2)
            self.exports = round(random.uniform(10, 50), 2)
            self.imports = round(random.uniform(10, 75), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

    def recovery(self):
        if self.economic_stimulus:
            self.consumer_spending = round(random.uniform(10, 350), 2)
            self.government_spending = round(random.uniform(100, 300), 2)
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = round(random.uniform(100, 500), 2)
            self.exports = round(random.uniform(10, 60), 2)
            self.imports = round(random.uniform(10, 40), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))
        else:
            self.consumer_spending = round(random.uniform(10, 200), 2)
            self.government_spending = round(random.uniform(100, 500), 2)
            self.national_debt += round(
                (self.consumer_spending + self.government_spending) * round(random.uniform(0.15, 0.35), 4), 2)
            self.investment = round(random.uniform(100, 300), 2)
            self.exports = round(random.uniform(10, 50), 2)
            self.imports = round(random.uniform(10, 20), 2)

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
            self.exports = round(random.uniform(10, 50), 2)
            self.imports = round(random.uniform(10, 20), 2)

            self.current_gdp += (self.consumer_spending + self.investment + self.government_spending +
                                 (self.exports - self.imports))

    def depression(self):
        if self.economic_stimulus:
            self.consumer_spending = round(random.uniform(5, 10), 2)
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
            self.government_spending = round(random.uniform(100, 500), 2)
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

def main(time):
    globe1 = globe.Globe()
    canada = Canada(time)
    # establishing asian AIs
    chinese_ai = china_ai.ChinaAI(time)
    japanese_ai = japan_ai.Japan(time)
    # establishing european AIs
    british_ai = britain_ai.Britain(time)
    spanish_ai = spain_ai.SpainAI(time)
    french_ai = france_ai.FranceAI(time)
    austrian_ai = austria_ai.Austria(time)
    # germany_ai = german_ai.Germany("1914")
    """german ai will establish states, similar to US"""
    belgian_ai = belgium_ai.BelgiumAI(time)
    dutch_ai = netherlands_ai.Netherlands(time)
    italian_ai = italy_ai.ItalyAI(time)
    lux_ai = luxembourg_ai.LuxembourgAI(time)
    danish_ai = denmark_ai.Denmark(time)
    swiss_ia = swiss_ai.SwitzerlandAI(time)
    swedish_ai = sweden_ai.SwedenAI(time)
    norwegian_ai = norway_ai.NorwayAI(time)
    """
    These 3 nations will be uncommented, once I figure out how to exclude them until 1918
    estonian_ai = estonia_ai.EstoniaAI('1914')
    latvian_ai = latvia_ai.LatviaAI("1914")
    lithuanian_ai = lithuania_ai.Lithuania("1914")"""
    greek_ai = greece_ai.Greece("1914")
    romanian_ai = romania_ai.RomaniaAI('1914')
    serbian_ai = serbia_ai.SerbiaAI('1914')
    # establishing north american AIs
    mexican_ai = mexico_ai.MexicoAI("1914")
    cuban_ai = cuba_ai.CubaAI("1914")
    establish_foreign_nations(globe1, canada, mexican_ai, cuban_ai, chinese_ai, japanese_ai,
                              british_ai, austrian_ai, belgian_ai, dutch_ai, french_ai, spanish_ai, italian_ai, lux_ai,
                              danish_ai, swedish_ai, swiss_ia, norwegian_ai, greek_ai, romanian_ai, serbian_ai)

    upload_database.initial_upload_to_database(globe1.nations)

    while canada.population > 1000000:
        print(f"Current Date {canada.date}.\n")
        time.sleep(1.5)
        """United States will stay afloat as a nation, as long as 3000000 people are left"""
        canada.check_economic_state()
        canada.population_change()
        #canada.stats(globe1)
        canada.stability_happiness_change(globe1)
        randomness.random_functions(canada, globe1)

        """Looping through changes in US system"""

        for i in range(0, len(globe1.nations)):
            if not globe1.nations[i].name == "Canada":
                globe1.nations[i].main(globe1)
                """
                looping through main function of each foreign nation object
                main function is connected to object itself, so as to use less memory space
                """

        upload_database.update_database_info(globe1.nations)
        time.sleep(1.75)
        canada.date += timedelta(days=1)
