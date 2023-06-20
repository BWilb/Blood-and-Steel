import random
import time
from datetime import datetime, timedelta
from us_states import (alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas,
                       kentucky, louisiana, maine, maryland, michigan, minnesota, mississppi, missouri, montana, n_d,
                       n_m, nebraska, nevada, new_hampshire, new_jersey, new_york, north_carolina, ok, oregon, pennsylvania,
                       rhode_island, ohio, s_d, south_carolina, tennessee, texas, utah, vermont, virginia, washington,
                       west_virginia, wisconsin, wyoming)
import arcade
import os
"""Storing files into an array in order to access state functions for population and economic growth"""
states = [alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas,
          kentucky, louisiana, maine, maryland, michigan, minnesota, mississppi, missouri, montana, n_d,
          n_m, nebraska, nevada, new_hampshire, new_jersey, new_york, north_carolina, ok, oregon, pennsylvania,
          rhode_island, ohio, s_d, south_carolina, tennessee, texas, utah, vermont, virginia, washington,
          west_virginia, wisconsin, wyoming]
folder = "us_states"
"""Political Dictionaries"""
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
"""establishment of states within US(national and regional files will influence each other)"""
def establish_economy(us):
    for i in range(0, len(us.states) - 1):
        us.current_gdp += us.states[i].current_gdp
    us.past_gdp = us.current_gdp
def establish_population(us):
    """Incorporating state population into overall population
    doing in a separate function in order to prevent oversaturation
    """
    for i in range(0, len(us.states) - 1):
        us.current_pop += us.states[i].population

def establish_states(us):
    """us.states.append(iowa.Iowa(us.date.year, us))
    us.states.append(alabama.Alabama(us.date.year, us))"""
    folder = "us_states"
    for file in os.listdir(folder):
        """Looping through us states folder, will be refined later on"""
        if file != '__pycache__':
            if file.removesuffix(".py") == "alabama":
                us.states.append(alabama.Alabama(us.date.year, us))
            if file.removesuffix(".py") == "alaska":
                us.states.append(alaska.Alaska(us.date.year, us))
            if file.removesuffix(".py") == "arizona":
                us.states.append(arizona.Arizona(us.date.year, us))
            if file.removesuffix(".py") == "arkansas":
                us.states.append(arkansas.Arkansas(us.date.year, us))
            if file.removesuffix(".py") == "california":
                us.states.append(california.California(us.date.year, us))
            if file.removesuffix(".py") == "colorado":
                us.states.append(colorado.Colorado(us.date.year, us))
            if file.removesuffix(".py") == "connecticut":
                us.states.append(conneticut.Conneticut(us.date.year, us))
            if file.removesuffix(".py") == "delaware":
                us.states.append(delaware.Delaware(us.date.year, us))
            if file.removesuffix(".py") == "florida":
                us.states.append(florida.Florida(us.date.year, us))
            if file.removesuffix(".py") == "georgia":
                us.states.append(georgia.Georgia(us.date.year, us))
            if file.removesuffix(".py") == "hawaii":
                us.states.append(hawaii.Hawaii(us.date.year, us))
            if file.removesuffix(".py") == "idaho":
                us.states.append(idaho.Idaho(us.date.year, us))
            if file.removesuffix(".py") == "illinois":
                us.states.append(illinois.Illinois(us.date.year, us))
            if file.removesuffix(".py") == "indiana":
                us.states.append(indiana.Indiana(us.date.year, us))
            if file.removesuffix(".py") == "iowa":
                us.states.append(iowa.Iowa(us.date.year, us))
            if file.removesuffix(".py") == "kansas":
                us.states.append(kansas.Kansas(us.date.year, us))
            if file.removesuffix(".py") == "kentucky":
                us.states.append(kentucky.Kentucky(us.date.year, us))
            if file.removesuffix(".py") == "louisiana":
                us.states.append(louisiana.Louisiana(us.date.year, us))
            if file.removesuffix(".py") == "maine":
                us.states.append(maine.Maine(us.date.year, us))
            if file.removesuffix(".py") == "maryland":
                us.states.append(maryland.Maryland(us.date.year, us))
            if file.removesuffix(".py") == "michigan":
                us.states.append(michigan.Michigan(us.date.year, us))
            if file.removesuffix(".py") == "mississippi":
                us.states.append(mississppi.Mississippi(us.date.year, us))
            if file.removesuffix(".py") == "missouri":
                us.states.append(missouri.Missouri(us.date.year, us))
            if file.removesuffix(".py") == "montana":
                us.states.append(montana.Montana(us.date.year, us))
            if file.removesuffix(".py") == "n_d":
                us.states.append(n_d.NorthDakota(us.date.year, us))
            if file.removesuffix(".py") == "n_m":
                us.states.append(n_m.NewMexico(us.date.year, us))
            if file.removesuffix(".py") == "nebraska":
                us.states.append(nebraska.Nebraska(us.date.year, us))
            if file.removesuffix(".py") == "nebraska":
                us.states.append(nevada.Nevada(us.date.year, us))
            if file.removesuffix(".py") == "new_hampshire":
                us.states.append(new_hampshire.NewHampshire(us.date.year, us))
            if file.removesuffix(".py") == "new_jersey":
                us.states.append(new_jersey.NewJersey(us.date.year, us))
            if file.removesuffix(".py") == "new_york":
                us.states.append(new_york.NewYork(us.date.year, us))
            if file.removesuffix(".py") == "north_carolina":
                us.states.append(north_carolina.NorthCarolina(us.date.year, us))
            if file.removesuffix(".py") == "ohio":
                us.states.append(ohio.Ohio(us.date.year, us))
            if file.removesuffix(".py") == "ok":
                us.states.append(ok.Oklahoma(us.date.year, us))
            if file.removesuffix(".py") == "oregon":
                us.states.append(oregon.Oregon(us.date.year, us))
            if file.removesuffix(".py") == "pennsylvania":
                us.states.append(pennsylvania.Pennsylvania(us.date.year, us))
            if file.removesuffix(".py") == "rhode_island":
                us.states.append(rhode_island.RhodeIsland(us.date.year, us))
            if file.removesuffix(".py") == "s_d":
                us.states.append(s_d.SouthDakota(us.date.year, us))
            if file.removesuffix(".py") == "south_carolina":
                us.states.append(south_carolina.SouthCarolina(us.date.year, us))
            if file.removesuffix(".py") == "tennessee":
                us.states.append(tennessee.Tennessee(us.date.year, us))
            if file.removesuffix(".py") == "texas":
                us.states.append(texas.Texas(us.date.year, us))
            if file.removesuffix(".py") == "utah":
                us.states.append(utah.Utah(us.date.year, us))
            if file.removesuffix(".py") == "vermont":
                us.states.append(vermont.Vermont(us.date.year, us))
            if file.removesuffix(".py") == "virginia":
                us.states.append(virginia.Virginia(us.date.year, us))
            if file.removesuffix(".py") == "washington":
                us.states.append(washington.Washington(us.date.year, us))
            if file.removesuffix(".py") == "west_virginia":
                us.states.append(west_virginia.WestVirginia(us.date.year, us))
            if file.removesuffix(".py") == "wisconsin":
                us.states.append(wisconsin.Wisconsin(us.date.year, us))
            if file.removesuffix(".py") == "wyoming":
                us.states.append(wyoming.Wyoming(us.date.year, us))
    # establishment of national population
    establish_population(us)
    establish_economy(us)
def check_stats(us):
    print(f"Your current President is {us.president}\n"
          f"Your current Vice President is {us.vice_president}\n"
          f"Your current political stability is {round(us.stability, 2)}%\n"
          f"Your current GDP is ${round(us.current_gdp, 2)}\n"
          f"Your current yearly gdp growth is {round(((us.current_gdp - us.past_gdp) / ((us.past_gdp + us.current_gdp) / 2)) * 100, 5 )}%\n"
          f"Your current national debt is ${round(us.national_debt, 2)}\n"
          f"There have been {us.deaths} deaths that have occurred in {us.current_year}\n"
          f"There have been {us.births} births that have occurred in {us.current_year}\n"
          f"The current happiness rating of the United States is {round(us.happiness, 2)}%\n"
          f"There are currently {len(us.states)} states in the Union")
def manual_game(us):
    establish_states(us)
    print(us.current_pop)
    print(us.current_gdp)
    while us.current_pop > 1000000:
        check = input("view stats?: ")
        """viewing stats"""
        if check.lower() == "yes" or check.lower() == 'y':
            check_stats(us)

        for i in range(0, len(us.states) - 1):
            """looping through list of state files to access population and economic growth functions
            each iteration interacts with each state Object
            """
            states[i].economic_growth(us.states[i])
            states[i].population_growth(us.states[i])
class UnitedStates:
    def __init__(self, year):
        # regional variables
        self.states = []
        # population variables
        self.current_pop = 0
        self.population_change = 0
        #self.past_pop = self.current_pop
        self.births = 0
        self.deaths = 0
        self.happiness = 96.56
        """Population controller if birth rate gets out of control"""
        self.condom_subsidy = False
        """Population controller if birth rate flops"""
        self.viagra_subsidy = False
        # political variables
        """Leaders of US"""
        self.president = presidents[year]
        self.vice_president = vice_presidents[year]
        """Political parties of US"""
        """self.republicans = self.population * 0.5
        self.democrats = self.population - self.republicans"""
        """Other political variables"""
        self.stability = 95.00
        # economic variables
        #self.economic_state = business_cycle[0]
        self.current_gdp = 0
        self.past_gdp = 0
        """holds current year of gdp(used for comparing with future GDP
        to determine GDP growth)
        """
        self.national_debt = 0
        """Components of GDP
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0"""
        """Economic Stimulus components"""
        self.economic_stimulus = False
        """Taxes components"""
        #self.tax_rate = tax_rate[year]
        # weather variables
        self.blackout = False
        self.blackout_date = None
        # military variables
        # international variables
        self.alliance = ""
        # time variables
        self.date = datetime(int(year), 1, 1)
        self.tax_change_date = self.date + timedelta(days=75)
        self.economic_change_date = self.date + timedelta(days=60)
        self.current_year = self.date.year

us = UnitedStates("1918")
manual_game(us)