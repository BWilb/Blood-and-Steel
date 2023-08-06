import random
import time
from datetime import datetime, timedelta
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
        self.region = "North America"
        self.name = "United States"
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
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = presidents[year]
        """Stability"""
        self.stability = 95.56
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
        # other
        self.is_ai = True
    # population functions
    def population_change(self):
        """instead of having the headache of calling both national objects separately, why not combine them"""
        if self.current_year < self.date.year:
            pop_change = ((self.births - self.deaths) / ((self.births + self.deaths) / 2)) * 100

            if pop_change < 2.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)

                if choice == 1:
                    print("The American government has initiated a program for increasing births.\n")
                    time.sleep(1.25)
                    self.birth_enhancer = True
                    if self.birth_control:
                        self.birth_control = False

            elif pop_change > 12.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = random.randrange(0, 2)

                if choice == 1:
                    print("The American government has initiated a program for decreasing births.\n")
                    time.sleep(1.25)
                    self.birth_control = True
                    if self.birth_enhancer:
                        self.birth_enhancer = False
        else:
            if self.birth_enhancer:
                births = random.randrange(20, 50)
                deaths = random.randrange(25, 45)
                self.population = (births - deaths)
                self.births += births
                self.deaths += deaths

            if self.birth_control:
                births = random.randrange(10, 30)
                deaths = random.randrange(25, 35)
                self.population = (births - deaths)
                self.births += births
                self.deaths += deaths

            else:
                births = random.randrange(15, 35)
                deaths = random.randrange(20, 30)
                self.population = (births - deaths)
                self.births += births
                self.deaths += deaths

    # establishing internal states
    def establish_states(self):
        from nation_state.north_america.united_states.us_states import alabama, alaska, arizona, arkansas, california, \
            colorado, \
            conneticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas, kentucky, louisiana, \
            maine, \
            maryland, michigan, mississppi, missouri, montana, n_d, n_m, nebraska, nevada, new_hampshire, new_jersey, \
            new_york, \
            north_carolina, ohio, ok, oregon, pennsylvania, rhode_island, s_d, south_carolina, tennessee, texas, utah, \
            virginia, \
            vermont, west_virginia, washington, wisconsin, wyoming
        folder = "united_states"
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
        population = 0
        for i in range(0, len(self.states) - 1):
            self.current_gdp += self.states[i].current_gdp
            self.population += self.states[i].population
        #print(population)


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
        while self.population > 3000000:
            self.stability_happiness_change(globe)
            self.population_change()
            self.check_economic_state()
            break