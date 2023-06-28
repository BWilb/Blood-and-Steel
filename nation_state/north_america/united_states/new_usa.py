import random
import time
from datetime import datetime, timedelta
from us_states import (alabama, alaska, arizona, arkansas, california, colorado,
                       conneticut, delaware, florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas,
                       kentucky, louisiana, maine, maryland, michigan, minnesota, mississppi, missouri, montana, n_d,
                       n_m, nebraska, nevada, new_hampshire, new_jersey, new_york, north_carolina, ok, oregon, pennsylvania,
                       rhode_island, ohio, s_d, south_carolina, tennessee, texas, utah, vermont, virginia, washington,
                       west_virginia, wisconsin, wyoming)
from nation_state.europe.britain import britain_ai
from nation_state.europe.germany import german_ai
from nation_state.europe.russia import russia_ai
from nation_state.europe.italy import italy_ai
import globe
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
def social_stats(us):
    print(f"Your current happiness level is {round(us.happiness, 2)}%.\n")
    time.sleep(3)
    if us.happiness < 35.45 and not us.improve_happiness:
        choice = input(f"{us.happiness}% doesnt represent a healthy civilian relationship with the government.\n"
                       f"A low happiness could lead to potential rebellions occurring.\n"
                       f"Would you like to improve your citizens' happiness over a course of 30 days?(y or n): ")
        if choice.lower() == "y":
            us.improve_happiness = us.date + timedelta(days=30)
    print(f"Your current population {us.current_pop}.\n")
    time.sleep(3)
    print(f"There have been {us.births} births in {us.date.year}.\n")
    time.sleep(3)
    print(f"There have been {us.deaths} deaths in {us.date.year}.\n")
    time.sleep(3)

def political_stats(us):
    print(f"Your current political stability is {round(us.stability, 2)}%.\n")
    time.sleep(3)
    print(f"Your current political capital and power is {us.political_power}.\n")
    time.sleep(3)
    if us.stability < 45.45 and not us.improve_stability:
        choice = input(f"{us.stability}% doesnt represent a functional government.\n"
                       f"Would you like to improve your government's stability for a course of 30 days?(y or n): ")
        if choice.lower() == "y":
            us.improve_stability = us.date + timedelta(days=30)
    print(f"There are {len(us.states)} states in the Union\n")
    time.sleep(3)
    low = 100.00
    high = 0.00
    high_nation = ""
    low_nation = ""
    for i in range(0, len(us.states) - 1):
        if i < len(us.states) - 1:
            if us.states[i].union_favorability < low and us.states[i].union_favorability < us.states[i + 1].union_favorability:
                low_nation = us.states[i].name
                low = us.states[i].union_favorability

            elif us.states[i].union_favorability > high and us.states[i].union_favorability > us.states[i + 1].union_favorability:
                high_nation = us.states[i].name
                high = us.states[i].union_favorability
        print(us.states[i].name, us.states[i].union_favorability)
        time.sleep(1)

    print(f"{low_nation} holds the lowest favorability of staying in the American Union at {round(low, 2)}%.\n")
    time.sleep(3)
    print(f"{high_nation} holds the highest favorability of staying in the American Union at {round(high, 2)}%.\n")
    time.sleep(3)

def economic_stats(us):
    print(f"Your current GDP is ${round(us.current_gdp, 2)}.\n")
    time.sleep(3)
    print(f"Your current yearly gdp growth is {round(((us.current_gdp - us.past_gdp) / ((us.past_gdp + us.current_gdp) / 2)) * 100, 5)}%\n")
    time.sleep(3)
    print(f"Your current national debt is ${round(us.national_debt, 2)}.\n")
    time.sleep(3)

    if us.national_debt > 1000000000 and not us.debt_repayment:
        choice = input(f"You are going to want to pay back some of your debt before it outpaces your assets.\n"
              f"Would you like to pay back some of your debt for 120 days?(y or n): ")
        if choice.lower() == "y":
            us.debt_repayment = us.date + timedelta(days=120)

def international_stats(us, globe, nations):
    done = True
    while done:
        choice = input("Would you like to view European, Asian, or Latin American relations?(enter no, to quit): ")
        if choice.lower() == "european":
            print(f"Your relations with Great Britain are at {round(us.english_relations, 2)}%.\n")
            time.sleep(3)
            print(f"Your relations with Russia are at {round(us.russian_relations, 2)}%.\n")
            time.sleep(3)
            print(f"Your relations with Italy are at {round(us.italian_relations, 2)}%.\n")
            time.sleep(3)
            print(f"Your relations with Germany are at {round(us.german_relations, 2)}%.\n")
            time.sleep(3)

            improvement = input("would you like to improve your international status?(y or n): ")
            if improvement.lower() == "y":
                done = True
                while done:
                    nation = input("Which nation would you like to save face with?(if done, enter none): ")
                    # if user wants to do multiple maneuvers towards another nation
                    if nation.lower() == "germany":
                        for i in range(0, len(nations) - 1):
                            if nations[i].name == "Germany":
                                german_ai.us_manual_relations(us, nations[i], globe)

                    elif nation.lower() == "italy":
                        for i in range(0, len(nations) - 1):
                            if nations[i].name == "Italy":
                                italy_ai.manual_us_relations(us, nations[i], globe)

                    elif nation.lower() == "none":
                        done = False

        elif choice.lower() == "quit":
            done = False

def daily_decisions(us, globe, nations):
    done = True
    while done:
        choice = input("Would you like to view your political, social, economic, or international stats?(enter quit to quit): ")
        if choice.lower() == "political":
            political_stats(us)
        elif choice.lower() == "economic":
            economic_stats(us)
        elif choice.lower() == "social":
            social_stats(us)
        elif choice.lower() == "international":
            international_stats(us, globe, nations)
        elif choice.lower() == "quit":
            done = False
            us.check_stats = us.date + timedelta(days=3)

# internal functions (changing of internal stats of nation)
"""Improvements based upon decisions made during daily decisions"""
def improvements(us):
    if us.date < us.debt_repayment:
        payment = round(us.national_debt * round(random.uniform(0.001, 0.009), 5), 2)
        us.national_debt -= payment
        us.current_gdp -= payment

    if us.date < us.improve_stability:
        increase = round(random.uniform(0.01, 1.25), 2)
        if (increase + us.stability) < 100:
            us.stability += increase

    if us.date < us.improve_happiness:
        increase = round(random.uniform(0.01, 1.25), 2)
        if (increase + us.happiness) < 100:
            us.happiness += increase

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
"""Deals with national stability and happiness"""
def stability_and_happiness_changes(us):
    chance = random.randrange(0, 2)
    if chance == 0:
        stability_increase = round(random.uniform(0.25, 1.25), 2)
        if (stability_increase + us.stability) < 99:
            us.stability += stability_increase

        happiness_increase = round(random.uniform(0.25, 1.25), 2)
        if (happiness_increase + us.happiness) < 99:
            us.happiness += happiness_increase

    elif chance == 1:
        stability_decrease = round(random.uniform(0.25, 1.25), 2)
        if (stability_decrease - us.stability) > 5:
            us.stability -= stability_decrease

        happiness_decrease = round(random.uniform(0.25, 1.25), 2)
        if (happiness_decrease - us.happiness) > 5:
            us.happiness -= happiness_decrease

"""Deals with popularity of staying in Union for each state"""
def union_favorability_states(us):
    """daily changes in each state's opinion towards staying in Federal Union"""
    for i in range(0, len(us.states) - 1):
        chance = random.randrange(0, 2)
        if chance == 0:
            us.states[i].union_favorability -= round(random.uniform(0.01, 0.25), 2)
        elif chance == 1:
            us.states[i].union_favorability += round(random.uniform(0.01, 0.25), 2)

"""1Deals with changing of political capital of USA"""
def political_power_change(us):
    us.political_power += us.political_exponent

def international_changes(us):
    if us.date < us.improve_german_relations:
        if us.political_power <= 0:
            us.german_relations += random.randrange(1, 5)
            us.political_power -= 1.5

        else:
            print("Your proceedings with improving relations with Germany have been cancelled, due to lack of political capital.\n")
            time.sleep(3)
            us.improve_german_relations = us.date
    else:
        chance = random.randrange(0, 2)
        if chance == 0:
            us.german_relations += round(random.uniform(0.25, 1.25), 2)
            us.english_relations += round(random.uniform(0.25, 1.25), 2)
            us.italian_relations += round(random.uniform(0.25, 1.25), 2)
            us.russian_relations += round(random.uniform(0.25, 1.25), 2)
        elif chance == 1:
            us.german_relations -= round(random.uniform(0.25, 1.25), 2)
            us.english_relations -= round(random.uniform(0.25, 1.25), 2)
            us.russian_relations -= round(random.uniform(0.25, 1.25), 2)
            us.italian_relations -= round(random.uniform(0.25, 1.25), 2)

def changes(us):
    stability_and_happiness_changes(us)
    political_power_change(us)
    union_favorability_states(us)
    international_changes(us)


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
    # establishment of national population and economy
    establish_population(us)
    establish_economy(us)

def manual_game(us, globe2):
    foreign_nations = []
    establish_states(us)

    italy = italy_ai.Italy(str(us.date.year))
    foreign_nations.append(italy)
    germany = german_ai.GermanAI(str(us.date.year))
    foreign_nations.append(germany)
    britain = britain_ai.BritainAI(str(us.date.year))
    foreign_nations.append(britain)

    while us.current_pop > 1000000:
        print(f"Current date: {us.date.date()}\n")
        time.sleep(3)

        for i in range(0, len(us.states) - 1):
            """looping through list of state files to access population and economic growth functions
            each iteration interacts with each state Object
            """
            states[i].economic_growth(us.states[i])
            states[i].population_growth(us.states[i])

        improvements(us)
        population_migrations(us)
        if us.date > us.check_stats:
            daily_decisions(us, globe2, foreign_nations)
        changes(us)
        us.date += timedelta(days=1)
        italy_ai.ai_game(italy, globe2)
        german_ai.ai_game(germany, globe2)
        britain_ai.ai_game(britain, globe2)

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
        self.stability = 95.00
        self.political_power = 200
        self.political_exponent = 3.56
        # international variables
        self.italian_relations = 50.00
        self.english_relations = 50.00
        self.russian_relations = 50.00
        self.german_relations = 50.00
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
        self.improve_stability = self.date
        """Ditto to improve stability"""
        self.improve_happiness = self.date
        """variable for repaying debt over given time"""
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        """international time variables"""
        self.alliance = ""
        # German
        self.improve_german_trade = self.date
        self.improve_german_relations = self.date
globe1 = globe.Globe()
us = UnitedStates("1918")
manual_game(us, globe1)