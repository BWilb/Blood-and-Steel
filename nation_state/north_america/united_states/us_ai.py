import random
import time
from datetime import datetime, timedelta
from us_states import (alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas,
                       kentucky, louisiana, maine, maryland, michigan, minnesota, mississppi, missouri, montana, n_d,
                       n_m, nebraska, nevada, new_hampshire, new_jersey, new_york, north_carolina, ok, oregon, pennsylvania,
                       rhode_island, ohio, s_d, south_carolina, tennessee, texas, utah, vermont, virginia, washington,
                       west_virginia, wisconsin, wyoming)
business_cycle = ["recession", "depression", "recovery", "expansion"]
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
"""Random function"""
"""def random_function(us):
    for i in range(0, len(us.states) - 1):
        us.states[i].random_events(us.states[i])"""
"""Daily decisions"""
def social_stats(us):
    print(f"Your current happiness level is {us.happiness}%.\n")
    time.sleep(3)
    if us.happiness < 35.45 and not us.improve_happiness:
        choice = input(f"{us.happiness}% doesnt represent a healthy civilian relationship with the government.\n"
                       f"A low happiness could lead to potential rebellions occurring.\n"
                       f"Would you like to improve your citizens' happiness over a course of 30 days?(y or n): ")
        if choice.lower() == "y":
            us.improve_happiness = us.date + timedelta(days=30)
    print(f"Your current population {us.current_pop}.\n")
    print(f"There have been {us.births} births in {us.date.year}.\n")
    print(f"There have been {us.deaths} deaths in {us.date.year}.\n")

def political_stats(us):
    print(f"Your current political stability is {us.stability}%.\n")
    if us.stability < 45.45 and not us.improve_stability:
        choice = input(f"{us.stability}% doesnt represent a functional government.\n"
                       f"Would you like to improve your government's stability for a course of 30 days?(y or n): ")
        if choice.lower() == "y":
            us.improve_stability = us.date + timedelta(days=30)
    print(f"There are {len(us.states) - 1} states in the Union\n")
    time.sleep(3)

def economic_stats(us):
    print(f"Your current GDP is ${us.current_gdp}.\n"
          f"Your current yearly gdp growth is {round(((us.current_gdp - us.past_gdp) / ((us.past_gdp + us.current_gdp) / 2)) * 100, 5 )}%\n"
          f"Your current national debt is ${us.national_debt}.\n")

    if us.national_debt > 1000000000 and not us.debt_repayment:
        choice = input(f"You are going to want to pay back some of your debt before it outpaces your assets.\n"
              f"Would you like to pay back some of your debt for 120 days?(y or n): ")
        if choice.lower() == "y":
            us.debt_repayment = us.date + timedelta(days=120)
def daily_decisions(us):
    done = False
    while done:
        choice = input("Would you like to view your political, social, or economic stats?(enter quit to quit): ")
        if choice.lower() == "political":
            political_stats(us)
        elif choice.lower() == "economic":
            economic_stats(us)
        elif choice.lower() == "social":
            social_stats(us)
        elif choice.lower() == "quit":
            done = True

"""Economic Functions"""
def economic_state(us):
    if us.date >= us.economic_change_date:
        """comparing current date with possible shift in business cycle, based upon 3 month cycle"""
        if us.past_gdp > us.current_gdp:
            """comparing past gdp to current gdp"""
            if us.economic_state == "expansion" or us.economic_state == "recovery":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recession":
                        print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=240)
                        if not us.economic_stimulus:
                            us.economic_stimulus = True
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif us.economic_state == "recession":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "depression":
                        print("Your economy has entered into a depression "
                              "after exceeding 6 months of decayed growth.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=210)
                        if not us.economic_stimulus:
                            us.economic_stimulus = True
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """

        elif us.past_gdp < us.current_gdp:
            if us.economic_state == "depression" or us.economic_state == "recession":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recovery":
                        print("Your economy has finally entered its recovery period.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=360)
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif us.economic_state == "recovery":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("Your economy has finally entered its expansionary period. Woo!!!\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=120)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """

def economic_decisions(us):
    if us.current_year < us.date.year:
        us.economic_growth = (us.current_gdp - us.past_gdp / ((us.past_gdp + us.current_gdp) / 2)) * 100

        if us.economic_growth <= 1.5:
            chance = random.randrange(0, 2)
            if chance == 0:
                print("The US congress has decided to enact a stimulus to the US economy.\n")
                time.sleep(3)
                us.economic_stimulus = True

        elif us.economic_growth > 7.5 and us.economic_stimulus:
            chance = random.randrange(0, 2)
            if chance == 1:
                print("The US congress has decide to remove their economic stimulus, due to very high growth in last years economy.\n")
                time.sleep(3)
                us.economic_stimulus = False
    else:
        for i in range(0, len(us.states) - 1):
            """looping through list of state files to access population and economic growth functions
            each iteration interacts with each state Object
            """
            states[i].economic_growth(us.states[i])

"""Internal Population migration"""
def population_migrations(us):
    migrants = 0
    if us.date > us.migrant_change:
        for i in range(0, len(us.states) - 1):
            migrants += round(us.states[i].population * round(random.uniform(0.001, 0.009), 5), 0)
            """Amount of people from each state that will be leaving the specific state"""
        for i in range(0, len(us.states) - 1):
            us.states[i].population += round(migrants * round(random.uniform(0.001, 0.009), 5), 0)
            """Amount of people migrating to new specific state"""

        us.migrant_change = us.date + timedelta(days=3)

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
def manual_game(us):
    establish_states(us)
    print(us.current_pop)
    print(us.current_gdp)
    while us.current_pop > 1000000:

        for i in range(0, len(us.states) - 1):
            """looping through list of state files to access population and economic growth functions
            each iteration interacts with each state Object
            """
            states[i].economic_growth(us.states[i])
            states[i].population_growth(us.states[i])
        population_migrations(us)
        daily_decisions(us)
        us.date += timedelta(days=3)
class UnitedStates:
    def __init__(self, year):
        # regional variables
        self.states = []
        # population variables
        self.current_pop = 0
        self.births = 0
        self.deaths = 0
        self.happiness = 96.56
        # political variables
        """Leaders of US"""
        self.president = presidents[year]
        self.vice_president = vice_presidents[year]
        """Political parties of US"""
        self.stability = 95.00
        # economic variables
        #self.economic_state = business_cycle[0]
        self.current_gdp = 0
        self.past_gdp = 0
        """holds current year of gdp(used for comparing with future GDP
        to determine GDP growth)
        """
        self.national_debt = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # time variables
        self.date = datetime(int(year), 1, 1)
        self.economic_change_date = self.date + timedelta(days=60)
        self.current_year = self.date.year
        """Internal redistribution of citizens"""
        self.migrant_change = self.date + timedelta(days=3)
        """Variable for improving stability of nation over given time"""
        self.improve_stability = None
        """Ditto to improve stability"""
        self.improve_happiness = None
        """variable for repaying debt over given time"""
        self.debt_repayment = None

us = UnitedStates("1918")
manual_game(us)