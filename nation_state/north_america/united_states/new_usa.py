import random
import time
from datetime import datetime, timedelta
from us_states import (alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois,
                       indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachuesetts,
                       missouri, michigan, minnesota, mississppi, n_d, n_m, nebraska, nevada,
                       new_hampshire, new_jersey, new_york, north_carolina, ok, oregon, pennsylvania,
                       rhode_island, s_d, south_carolina, tennessee, texas, utah, vermont, virginia,
                       washington, west_virginia, wisconsin, wyoming)
"""Storing files into an array in order to access state functions for population and economic growth"""
states = [alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois,
                       indiana, iowa, kansas, kentucky, louisiana, maine, maryland, massachuesetts,
                       missouri, michigan, minnesota, mississppi, n_d, n_m, nebraska, nevada,
                       new_hampshire, new_jersey, new_york, north_carolina, ok, oregon, pennsylvania,
                       rhode_island, s_d, south_carolina, tennessee, texas, utah, vermont, virginia,
                       washington, west_virginia, wisconsin, wyoming]
import arcade
import os
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
    for i in range(0, len(us.states)):
        us.current_gdp += us.states[i].gdp
def establish_population(us):
    """Incorporating state population into overall population
    doing in a separate function in order to prevent oversaturation
    """
    for i in range(0, len(us.states)):
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
            if file.removesuffix(".py") == "iowa":
                us.states.append(iowa.Iowa(us.date.year, us))
    # establishment of national population
    establish_population(us)
    establish_economy(us)
"""economic functions"""

"""population functions"""
def manual_game(us):
    establish_states(us)
    print(us.current_pop)
    print(us.current_gdp)
    while us.current_pop > 1000000:
        pass

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

us = UnitedStates("1910")
manual_game(us)