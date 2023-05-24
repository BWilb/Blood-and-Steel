import random
import time
from datetime import datetime, timedelta

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
kaiser_succession = ["Wilhelm III", "Louis Ferdinand", "George Fredrick"]
nazi_succession = ["Hermann Goering", "Joseph Goebbels", "Martin Bormann", "Rudolf Hess", "Heinrich Himmler",
                   "Reinhard Heydrich", "Albert Speer", "Wilhelm Keitel", "Otto Strasser"]

"""Economic dictionaries & Variables"""
business_cycle = ["recovery", "expansion", "recession", "depression"]
gdp = {
    "1910": 237000000,
    "1914": 237395000,
    "1918": 235968000,
    "1932": 237947500,
    "1936": 240000000,
    "1939": 300456000
}

tax_rate = {
    "1910": 8.00,
    "1914": 8.00,
    "1918": 8.00,
    "1932": 60.00,
    "1936": 60.00,
    "1939": 65.00
}

"""Subsidiary functions of game"""

"""Statistics function"""
def check_stats(german):
    """Stats organized by...
    1. Politics
    2. Economics
    3. Social aspects
    4. Others
    """
    print(f"Your current Kaiser is {german.kaiser}\n"
          f"Your current Chancellor is {german.chancellor}.\n")
    if german.date < datetime(1933, 1, 30):
        print(f"Progressives make up {round((german.progressives / german.population) * 100, 2)}% of the population\n"
              f"Conservatives make up {round((german.free_conservatives / german.population) * 100, 2)}% of the population\n"
              f"Independents make up {round((german.center_party / german.population) * 100, 2)}% of the population\n")

    elif german.date >= datetime(1933, 1, 30) and german.date <= datetime(1945, 5, 2):
        print(f"National Socialists make up {round((german.national_socialists / german.population), 3) * 100}% of the population.\n"
              f"German Rebels make up {round((german.rebels / german.population), 3) * 100}% of the population.\n")

    print(f"Your current political stability is {round(german.stability, 2)}%\n"
          f"Your current GDP is ${round(german.current_gdp, 2)}\n"
          f"Your economy is currently in a(n) {german.economic_state} period\n"
          f"Your current yearly gdp growth is {round(((german.current_gdp - german.past_gdp) / ((german.past_gdp + german.current_gdp) / 2)) * 100, 5 )}%\n"
          f"Your current national debt is ${round(german.national_debt, 2)}\n"
          f"Your current tax rate is {round(german.tax_rate, 2)}%\n"
          f"There have been {german.deaths} deaths that have occurred in {german.current_year}\n"
          f"There have been {german.births} births that have occurred in {german.current_year}\n"
          f"The current happiness rating of Germany is {round(german.happiness, 2)}%\n")

"""Primary events function"""
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
def economic_events(germany):
    """definitive national economic events in germany"""
    pass
def political_events(germany):
    """definitive national political events in germany"""

    # events in January
    if germany.date == datetime(1919, 1, 5):
        print("\nGerman Workers Party has just been formed!!")
        time.sleep(3)

    elif germany.date == datetime(1933, 1, 30):
        """
        Adolf Hitler takes control of Germany
        Major decrease in happiness and stability
        Reshaping of political landscape
        """
        print("Adolf Hitler has taken full control of the government.\n"
              "The Third Reich has begun.")
        time.sleep(3)
        germany.national_socialists = round(germany.population * 0.85, 0)
        germany.rebels = germany.population - germany.national_socialists
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
def international_events(germany):
    """definitive national foreign relation events with germany and her allies"""
    pass
def events(germany):
    social_events(germany)
    economic_events(germany)
    political_events(germany)
    international_events(germany)
    pass

"""Political functions"""
def political_change(germany):
    if germany.date < datetime(1932, 1, 30):
        """Shifting of political landscape in German Empire and Weimar Republic"""
        chance = random.randrange(0, 3)
        """chance based upon whether each of three main parties lose supporters"""
        if chance == 0:
            progressive_loss = germany.progressives * round(random.uniform(0.01, 0.1), 2)
            if germany.progressives - progressive_loss > 0:
                """Check to see if progressives go negative"""
                germany.progressives -= progressive_loss
                germany.center_party += progressive_loss * 0.5
                germany.free_conservatives += progressive_loss * 0.5

        elif chance == 1:
            conservative_loss = germany.free_conservatives * round(random.uniform(0.01, 0.1), 2)
            if germany.free_conservatives - conservative_loss > 0:
                """Check to see if conservatives go negative"""
                germany.free_conservatives -= conservative_loss
                germany.center_party += conservative_loss * 0.5
                germany.progressives += conservative_loss * 0.5

        elif chance == 2:
            center_loss = germany.center_party * round(random.uniform(0.01, 0.1), 2)
            if germany.center_party - center_loss > 0:
                """Check to see if non-aligned go negative"""
                germany.center_party -= center_loss
                germany.free_conservatives += center_loss * 0.5
                germany.progressives += center_loss * 0.5

    elif germany.date > datetime(1932, 1, 30) and germany.date < datetime(1945, 5, 2):
        """Shifting of political landscape in Nazi Germany(Third Reich)"""
        chance = random.randrange(0, 2)
        """Chance whether Nazis gain more supporters or lose some"""
        if chance == 0:
            nazi_loss = germany.national_socialists * round(random.uniform(0.01, 0.1), 2)
            germany.national_socialists -= nazi_loss
            germany.rebels += nazi_loss
        elif chance == 1:
            rebel_loss = germany.rebels * round(random.uniform(0.01, 0.1), 2)
            germany.rebels -= rebel_loss
            germany.national_socialists += rebel_loss
    else:
        pass

"""Population functions"""
def population_change(germany):
    if germany.current_year < germany.date.year:
        germany.population_change = (germany.population - germany.current_pop / ((germany.population + germany.current_pop) / 2)) * 100

        germany.current_pop = germany.population
        """Resetting of current population(past)"""
        if germany.population_change <= 1.5:
            """Incorporation of what happens when population growth becomes too small"""
            print(f"Your population growth for {germany.current_year} was {germany.population_change}%\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == 'y':
                germany.viagra_subsidy = True

                if germany.condom_subsidy == True:
                    """Checking to see if condom subsidies exist"""
                    germany.condom_subsidy = False

        elif germany.population_change >= 8:
            """Incorporation of what happens when population growth becomes too large"""
            print(f"Your population growth for {germany.current_year} was {germany.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                germany.condom_subsidy = True

                if germany.viagra_subsidy == True:
                    """Checking to see if viagra subsidies exist"""
                    germany.viagra_subsidy = False

    else:
        if germany.viagra_subsidy:
            births = random.randrange(100, 300)
            germany.births += births
            germany.population += births

            if germany.date < datetime(1932, 1, 30):
                """Check to see if Hitler has taken power yet"""
                for i in range(0, births):
                    chance = random.randrange(0, 3)
                    if chance == 0:
                        """Chance that the births go to progressive party"""
                        germany.progressives += 1

                    elif chance == 1:
                        """Chance that the births go to free conservative party"""
                        germany.free_conservatives += 1

                    elif chance == 2:
                        """Chance that the births go to center party"""
                        germany.center_party += 1

            elif germany.date > datetime(1932, 1, 30) and germany.date < datetime(1945, 5, 2):
                """Check to see if Hitler is still in power"""
                for i in range(0, births):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        """Chance that the births go to the Nazi party"""
                        germany.national_socialists += 1

                    elif chance == 1:
                        """Chance that the births go to the rebels"""
                        germany.rebels += 1

            deaths = random.randrange(30, 60)
            germany.deaths += deaths
            germany.population -= deaths

        elif germany.condom_subsidy:
            births = random.randrange(48, 72)
            germany.births += births
            germany.population += births

            if germany.date < datetime(1932, 1, 30):
                """Check to see if Hitler has taken power yet"""
                for i in range(0, births):
                    chance = random.randrange(0, 3)
                    if chance == 0:
                        """Chance that the births go to progressive party"""
                        germany.progressives += 1

                    elif chance == 1:
                        """Chance that the births go to free conservative party"""
                        germany.free_conservatives += 1

                    elif chance == 2:
                        """Chance that the births go to center party"""
                        germany.center_party += 1

            elif germany.date > datetime(1932, 1, 30) and germany.date < datetime(1945, 5, 2):
                """Check to see if Hitler is still in power"""
                for i in range(0, births):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        """Chance that the births go to the Nazi party"""
                        germany.national_socialists += 1

                    elif chance == 1:
                        """Chance that the births go to the rebels"""
                        germany.rebels += 1

            deaths = random.randrange(50, 80)
            germany.deaths += deaths
            germany.population -= deaths

        else:
            births = random.randrange(50, 150)
            germany.births += births
            germany.population += births

            if germany.date < datetime(1932, 1, 30):
                """Check to see if Hitler has taken power yet"""
                for i in range(0, births):
                    chance = random.randrange(0, 3)
                    if chance == 0:
                        """Chance that the births go to progressive party"""
                        germany.progressives += 1

                    elif chance == 1:
                        """Chance that the births go to free conservative party"""
                        germany.free_conservatives += 1

                    elif chance == 2:
                        """Chance that the births go to center party"""
                        germany.center_party += 1

            elif germany.date > datetime(1932, 1, 30) and germany.date < datetime(1945, 5, 2):
                """Check to see if Hitler is still in power"""
                for i in range(0, births):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        """Chance that the births go to the Nazi party"""
                        germany.national_socialists += 1

                    elif chance == 1:
                        """Chance that the births go to the rebels"""
                        germany.rebels += 1

            deaths = random.randrange(50, 80)
            germany.deaths += deaths
            germany.population -= deaths

"""Main function of manual German version of game"""
def manual_game(germany):
    # establishment of check upon game status
    while germany.population > 200000:
        germany.date = germany.date + timedelta(days=1)
        # incrementing of time
        print(germany.date)
        # primary functions
        population_change(germany)
        political_change(germany)
        if germany.stability >= 50:
            choice = input("Important!!! view your stats: ")
            if choice == "y" or choice == "yes":
                check_stats(germany)
        print("hi")
        time.sleep(3)
class Germany:
    def __init__(self, year):
        # population variables
        self.population = population[year]
        self.population_change = 0
        self.current_pop = self.population
        self.births = 0
        self.deaths = 0
        self.happiness = 96.56
        """Population controller if birth rate gets out of control"""
        self.condom_subsidy = False
        """Population controller if birth rate flops"""
        self.viagra_subsidy = False
        # political variables
        """Leaders of Germany"""
        self.kaiser = kaisers[year]
        self.chancellor = chancellors[year]
        """Political parties of Germany
        based upon year
        """
        if int(year) < 1933:
            self.center_party = self.population * round(random.uniform(0.10, 0.33), 2)
            self.progressives = ((self.population - self.center_party) *
                                      round(random.uniform(0.10, 0.45), 2))
            self.free_conservatives = (self.population - self.center_party - self.progressives)
        else:
            self.national_socialists = self.population * 0.99
            self.rebels = self.population - self.national_socialists
            self.center_party = 0
            self.progressives = 0
            self.free_conservatives = 0
        """Other political variables"""
        self.stability = 95.00
        # economic variables
        if int(year) < 1918 and int(year) > 1914:
            for i in range(0, len(business_cycle) - 1):
                if business_cycle[i] == "recession":
                    self.economic_state = business_cycle[i]

        elif int(year) <= 1932 and int(year) > 1929:
            for i in range(0, len(business_cycle) - 1):
                if business_cycle[i] == "depression":
                    self.economic_state = business_cycle[i]

        else:
            for i in range(0, len(business_cycle) - 1):
                if business_cycle[i] == "recovery":
                    self.economic_state = business_cycle[i]

        """State of the economy variables"""
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        """holds current year of gdp(used for comparing with future GDP
        to determine GDP growth)
        """
        self.national_debt = 0
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        """Taxes components"""
        self.tax_rate = tax_rate[year]
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