import globe
import arcade
import os
import random
import time
from datetime import datetime, timedelta
from administrative_regions import prussia, bavaria, baden_wurttemburg, saxony, alsace_lorraine

"""Population Dictionaries"""
population = {
    "1910": 63200000,
    "1914": 63200000,
    "1918": 62400000,
    "1932": 67200000,
    "1936": 69100000,
    "1939": 70500000
}

"""Political Dictionaries"""
chancellors = {
    "1910": "Theobald von Bethmann Hollweg",
    "1914": "Theobald von Bethmann Hollweg",
    "1918": "Friedrich Ebert",
    "1932": "Kurt von Schleicher",
    "1936": "Adolf Hitler",
    "1939": "Adolf Hitler"
}

kaisers = {
    "1910": "Wilhelm II",
    "1914": "Wilhelm II",
    "1918": "None",
    "1932": "None",
    "1936": "None",
    "1939": "None"
}
"""events"""
# social events
def social_events(germany):
    """definitive national social events in germany"""

    if germany.date == datetime(germany.date.year, 2, 16):
        """Checking of date to see if the German version of Karneval has begun"""
        print("Karneval hat begonnen!!")
        time.sleep(3)

    if germany.date >= datetime(germany.date.year, 2, 16) and germany.date <= datetime(germany.date.year, 2, 22):

        increase = round(random.uniform(0.10, 0.75), 2)
        if (germany.happiness + increase) < 99:
            germany.happiness += increase

        if (germany.stability + increase) < 99:
            germany.stability += increase

        germany.current_gdp += round(random.uniform(300, 6000), 2)

        births = random.randrange(2, 20)
        """Very slight increase in births due to increased happiness"""

        if germany.date > datetime(1932, 1, 30):
            """Checking to see if Weimar Republic or German Empire is around"""
            for i in range(0, births):
                chance = random.randrange(0, 3)
                if chance == 0:
                    germany.center_party += 1

                elif chance == 1:
                    germany.progressives += 1

                elif chance == 2:
                    germany.free_conservatives += 1

        elif germany.date < datetime(1945, 5, 2) and germany.date >= datetime(1932, 1, 30):
            for i in range(0, births):
                chance = random.randrange(0, 2)
                if chance == 0:
                    germany.national_socialists += 1

                elif chance == 1:
                    germany.rebels += 1

    if germany.date == datetime(germany.date.year, 4, 7):
        """Checking to see if Easter weekend has begun"""
        print("Das Osterwochenende hat begonnen")
        time.sleep(3)

    if germany.date <= datetime(germany.date.year, 4, 7) and germany.date >= datetime(germany.date.year, 4, 10):
        increase = round(random.uniform(0.10, 0.75), 2)
        if (germany.happiness + increase) < 99:
            germany.happiness += increase

        if (germany.stability + increase) < 99:
            germany.stability += increase

        births = random.randrange(2, 20)
        """Very slight increase in births due to increased happiness and stability"""

        if germany.date > (1932, 1, 30):
            """Checking to see if Weimar Republic or German Empire is around"""
            for i in range(0, births):
                chance = random.randrange(0, 3)
                if chance == 0:
                    germany.center_party += 1

                elif chance == 1:
                    germany.progressives += 1

                elif chance == 2:
                    germany.free_conservatives += 1

        elif germany.date < datetime(1945, 5, 2) and germany.date >= datetime(1932, 1, 30):
            for i in range(0, births):
                chance = random.randrange(0, 2)
                if chance == 0:
                    germany.national_socialists += 1

                elif chance == 1:
                    germany.rebels += 1

    if germany.date == datetime(germany.date.year, 9, 16):
        """Checking of date to see if Oktoberfest has begun"""
        print("Oktoberfest hat begonnen!!")
        time.sleep(3)

    if germany.date >= datetime(germany.date.year, 9, 16) and germany.date <= datetime(germany.date.year, 10, 3):
        """Checking to see if Oktoberfest is still occurring"""
        increase = round(random.uniform(0.10, 0.75), 2)
        if (germany.happiness + increase) < 99:
            germany.happiness += increase

        if (germany.stability + increase) < 99:
            germany.stability += increase

        germany.current_gdp += round(random.uniform(300, 6000), 2)

        births = random.randrange(2, 20)
        """Very slight increase in births due to increased happiness"""

        if germany.date > (1932, 1, 30):
            """Checking to see if Weimar Republic or German Empire is around"""
            for i in range(0, births):
                chance = random.randrange(0, 3)
                if chance == 0:
                    germany.center_party += 1

                elif chance == 1:
                    germany.progressives += 1

                elif chance == 2:
                    germany.free_conservatives += 1

        elif germany.date < datetime(1945, 5, 2) and germany.date >= datetime(1932, 1, 30):
            for i in range(0, births):
                chance = random.randrange(0, 2)
                if chance == 0:
                    germany.national_socialists += 1

                elif chance == 1:
                    germany.rebels += 1
# political events

def political_events(germany):
    """definitive national political events in germany"""

    # events in January
    if germany.date == datetime(1919, 1, 5):
        print("\nGerman Workers Party has just been formed!!")
        time.sleep(3)

    elif germany.date == datetime(1932, 1, 30):
        """
        Adolf Hitler takes control of Germany
        Major decrease in happiness and stability
        Reshaping of political landscape
        """
        print("Adolf Hitler has taken full control of the government.\n"
              "The Third Reich has begun.")
        germany.chancellor = "Adolf Hitler"
        time.sleep(3)
        germany.national_socialists = round(germany.population * 0.85, 0)
        germany.rebels = germany.population - germany.national_socialists
        germany.progressives = 0
        germany.center_party = 0
        germany.free_conservatives = 0
        happy_decrease = round(random.uniform(0.75, 6.56), 2)
        stability_decrease = round(random.uniform(0.25, 4.25), 2)
        if germany.happiness - happy_decrease > 10:
            germany.happiness -= happy_decrease

        if germany.stability - stability_decrease > 10:
            germany.stability -= stability_decrease

    # Events in February
    elif germany.date == datetime(1920, 2, 24):
        print("\n The German Workers Party has changed its name to National Socialist German Workers Party!!!")
        time.sleep(3)

    # Events in September
    elif germany.date == datetime(1919, 9, 12):
        print("\nAdolf Hitler has just joined the German Workers Party!!")
        time.sleep(3)
    # Events in November
    elif germany.date == datetime(1923, 11, 8):
        print("Adolf Hitler just attempted a coup in a Beer Hall putsch in Munich!!")
        time.sleep(3)
        decrease = round(random.uniform(0.25, 2.25), 2)
        if (germany.stability - decrease) > 10:
            germany.stabilty -= decrease

# economic events
def economic_events(germany):
    """definitive national economic events in germany"""
    if germany.date == datetime(1915, 1, 1):
        """Represents the blockade on Germany causing...
        malnutrition and hunger
        """
        germany.happiness -= round(random.uniform(0.01, 0.09), 2)
        germany.stability -= round(random.uniform(0.01, 0.09), 2)
        # economic_stimulus(germany)
        germany.current_gdp -= round(random.uniform(1000, 3000), 2)

    if germany.date.year >= 1921 and germany.date.year <= 1923:
        """Time of germany hyperinflation"""
        chance = random.randrange(0, 10)
        if chance % 9 == 4:
            print("The German economy has fallen into a Recession, due to rapid hyperinflation")
            if germany.economic_state != "recession":
                germany.economic_state = "recession"
                stimulus_chance = random.randrange(0, 16)
                if stimulus_chance % 15 == 14:
                    if germany.economic_stimulus == False:
                        # economic_stimulus(germany)
                        pass
        germany.happiness -= round(random.uniform(0.01, 0.09), 2)
        germany.stability -= round(random.uniform(0.01, 0.09), 2)

    if germany.date == datetime(1929, 10, 24):
        print("The German Economy has fallen into a depression")
        print("It is being reported that nations across the globe are experiencing similar occurrences.\n")
        time.sleep(3)
        germany.current_gdp /= 10
        if germany.economic_state != "depression":
            germany.economic_state = "depression"
            # economic_stimulus(germany)

    if germany.date > datetime(1929, 10, 24) and germany.date < datetime(1933, 1, 30):
        """Period in time where germany experiences Great Depression"""
        decrease_happiness = round(random.uniform(0.01, 0.05), 2)
        decrease_stability = round(random.uniform(0.01, 0.05), 2)
        if (germany.happiness - decrease_happiness) > 5:
            germany.happiness -= decrease_happiness
        elif (germany.stability - decrease_stability) > 5:
            germany.happiness -= decrease_stability

def events(germany):
    social_events(germany)
    economic_events(germany)
    political_events(germany)

"""average"""
# military functions
# populace functions
def population_growth(germany):
    for i in range(0, len(germany.regions)):
        germany.regions[i].population_growth(germany.regions[i])
# economic functions
def economic_state(germany):
    if germany.date >= germany.economic_change_date:
        """Comparing current date with possible shift in economy, based upon cycles under each stage of economy"""
        if germany.past_gdp > germany.current_gdp:
            """comparing past gdp to current gdp"""
            if germany.economic_state == "expansion" or germany.economic_state == "recovery":
                germany.economic_state = "recession"
                print("Your economy has fallen into a recession.\n")
                germany.economic_change_date = germany.date + timedelta(days=240)
                """recession will last for 240 days"""

            elif germany.economic_state == "recession":
                germany.economic_state = "depression"
                print("Your economy has fallen into a depression.\n")
                germany.economic_change_date = germany.date + timedelta(days=210)
                """recession will last for 210 days"""

        if germany.past_gdp < germany.current_gdp:
            """comparing past gdp to current gdp"""
            if germany.economic_state == "recession" or germany.economic_state == "depression":
                germany.economic_state = "recovery"
                print("Your economy has stepped into recovery.\n")
                germany.economic_change_date = germany.date + timedelta(days=240)
                """recovery will last for 240 days"""

            elif germany.economic_state == "recovery":
                germany.economic_state = "expansion"
                print("Your economy has exploded into an expansion.\n")
                germany.economic_change_date = germany.date + timedelta(days=210)
                """expansion will last for 210 days"""
    else:
        for i in range(0, len(germany.regions)):
            germany.regions[i].economic_growth(germany.regions[i])
def economic_stimulus(germany):
    """Function that is called if German government is in a pickle and has to stimulate economic growth"""
    if germany.economic_state.lower() == "recession":
        choice = input("\nDo You want to implement an economic stimulus to mediate some of the effects of your current recession?: ")

        if choice.lower() == "yes" or choice.lower() == "y":
            germany.economic_stimulus = True

    elif germany.economic_state.lower() == "depression":
        germany.economic_stimulus = True

# stability and happiness functions

# establishing populace and economy of germany based off of inner administrative districts
def establish_initial_stats(germany):
    for state in germany.regions:
        germany.current_pop += state.current_pop
        germany.current_gdp += state.current_gdp
        germany.stability += state.stability
        germany.happiness += state.happiness

# establishing districts of germany
def establish_districts(germany):
    folder = "administrative_districts"
    for file in folder:
        if germany.date < datetime(1918, 11, 11):

            if file.removesuffix(".py") == "alsace_lorraine":
                germany.regions.append(alsace_lorraine.Alsace_Lorraine(germany.date.year, germany))

            elif file.removesuffix(".py") == "bavaria":
                germany.regions.append(bavaria.Bavaria(germany.date.year, germany))

            elif file.removesuffix(".py") == "prussia":
                germany.regions.append(prussia.Prussia(germany.date.year, germany))

            elif file.removesuffix(".py") == "saxony":
                germany.regions.append(saxony.Saxony(germany.date.year, germany))

            elif file.removesuffix(".py") == "baden-wurttemburg":
                germany.regions.append(baden_wurttemburg.Wurttemburg(germany.date.year, germany))

        else:
            if file.removesuffix(".py") == "bavaria":
                germany.regions.append(bavaria.Bavaria(germany.date.year, germany))

            elif file.removesuffix(".py") == "prussia":
                germany.regions.append(prussia.Prussia(germany.date.year, germany))

            elif file.removesuffix(".py") == "saxony":
                germany.regions.append(saxony.Saxony(germany.date.year, germany))

            elif file.removesuffix(".py") == "baden-wurttemburg":
                germany.regions.append(baden_wurttemburg.Wurttemburg(germany.date.year, germany))

def manual_game(germany, globe1):
    establish_districts(germany)

class Germany:
    def __init__(self, year):
        # date variables
        self.date = datetime(int(year), 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date
        # administrative and political variables
        """administrative"""
        self.regions = []
        # economic variables
        self.current_gdp = 0
        self.past_gdp = 0
        self.national_debt = 0
        self.economic_stimulus = False
        # social variables
        self.happiness = 0
        self.current_pop = 0
        self.past_pop = 0
        self.births = 0
        self.deaths = 0
        self.pop_growth = 0
        self.subsidize_pop_growth = False
        self.subsidize_pop_slow = False

        """political variables"""
        self.stability = 0
        self.kaiser = kaisers[year]
        self.leader = chancellors[year]
        self.political_power = 150
        self.political_exponent = 2.45

        if int(year) < 1933:
            self.center_party = self.current_pop * round(random.uniform(0.10, 0.33), 2)
            self.progressives = ((self.current_pop - self.center_party) *
                                 round(random.uniform(0.10, 0.45), 2))
            self.free_conservatives = (self.current_pop - self.center_party - self.progressives)
        else:
            self.national_socialists = self.current_pop * 0.99
            self.rebels = self.current_pop - self.national_socialists
            self.center_party = 0
            self.progressives = 0
            self.free_conservatives = 0