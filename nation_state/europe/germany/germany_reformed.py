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
              f"Independents make up {round((german.center_party / german.population) * 100, 2)}% of the population")

    elif german.date >= datetime(1933, 1, 30) and german.date <= datetime(1945, 5, 2):
        print(f"National Socialists make up {round((german.national_socialists / german.population), 3) * 100}% of the population.\n"
              f"German Rebels make up {round((german.rebels / german.population), 3) * 100}% of the population.")

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

"""Economic Functions"""
def economic_stimulus(germany):
    germany.economic_stimulus = True

    if germany.economic_state.lower() == "recession":
        choice = input("\nDo you want to increase the tax rate in order to support increased spending"
                       "(Remember this applies to the entire population)?:")
        """Prompting user to choose if they want to increase taxes"""

        if choice.lower() == "yes" or choice.lower() == "y":
            valid_choice = False

            while valid_choice:
                tax_hike = float(input("By how much do you want to increase taxes(max cap is 10)?: "))

                if tax_hike <= 10 and tax_hike >= 0.5:
                    """if statement covering if tax hike meets criteria"""

                    germany.tax_rate += round(tax_hike, 2)
                    print(f"{germany.tax_rate}% is your new tax rate")
                    germany.happiness -= round(random.uniform(0.25, 3.45), 2)
                    germany.stability -= round(random.uniform(0.25, 1.45), 2)
                    valid_choice = True

                elif tax_hike <= 0 or tax_hike > 25:
                    print(f"New tax hike of {tax_hike} is improper./n"
                          f"try again")
                    time.sleep(3)

                else:
                    print("Not a valid tax rate")
                    time.sleep(3)

    elif germany.economic_state.lower() == "depression":

        tax_hike = round(random.uniform(0.5, 10), 2)
        if (germany.tax_rate + tax_hike) <= 86.00:
            print(f"Congress has enacted a tax hike of {tax_hike} points")
def economic_state(germany):
    if germany.date >= germany.economic_change_date:
        """comparing current date with possible shift in business cycle, based upon 3 month cycle"""
        if germany.past_gdp > germany.current_gdp:
            """comparing past gdp to current gdp"""
            if germany.economic_state == "expansion" or germany.economic_state == "recovery":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recession":
                        print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                        time.sleep(3)
                        germany.economic_state = business_cycle[i]
                        germany.economic_change_date = germany.date + timedelta(days=240)
                        economic_stimulus(germany)
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif germany.economic_state == "recession":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "depression":
                        print("Your economy has entered into a depression "
                              "after exceeding 6 months of decayed growth.\n")
                        time.sleep(3)
                        germany.economic_state = business_cycle[i]
                        germany.economic_change_date = germany.date + timedelta(days=210)
                        economic_stimulus(germany)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """

        elif germany.past_gdp < germany.current_gdp:
            if germany.economic_state == "depression" or germany.economic_state == "recession":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recovery":
                        print("Your economy has finally entered its recovery period.\n")
                        time.sleep(3)
                        germany.economic_state = business_cycle[i]
                        germany.economic_change_date = germany.date + timedelta(days=360)
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif germany.economic_state == "recovery":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("Your economy has finally entered its expansionary period. Woo!!!\n")
                        time.sleep(3)
                        germany.economic_state = business_cycle[i]
                        germany.economic_change_date = germany.date + timedelta(days=120)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """
def recovery(germany):
    """Path taken if economy is currently in recovery"""
    if germany.economic_stimulus:
        """Recovery simulation if an economic stimulus is in effect"""
        germany.consumer_spending = round(random.uniform(3000, 7500), 2)
        germany.investment = round(random.uniform(2000, 7400), 2)

        germany.government_spending = round(random.uniform(1300, 5000), 2)
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.45), 2) +
                             germany.consumer_spending * round(random.uniform(0.05, 0.30), 2))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

    else:
        """Recovery simulation if an economic stimulus isn't in effect"""
        germany.consumer_spending = round(random.uniform(300, 1500), 2)
        germany.investment = round(random.uniform(200, 2400), 2)

        germany.government_spending = round(random.uniform(300, 2000), 2)
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.45), 2) +
                                  germany.consumer_spending * round(random.uniform(0.05, 0.30), 2))

    germany.exports = round(random.uniform(4500, 45000), 2)
    germany.imports = round(random.uniform(3200, 32000), 2)
    germany.current_gdp += (germany.consumer_spending + germany.investment + germany.government_spending +
                            (germany.exports - germany.imports))
def expansion(germany):
    """Path taken if economy is currently in expansion"""
    if germany.economic_stimulus:
        """Recovery simulation if an economic stimulus is in effect"""
        germany.consumer_spending = round(random.uniform(9000, 60000), 2)
        germany.investment = round(random.uniform(20000, 74000), 2)

        germany.government_spending = round(random.uniform(13000, 80000), 2)
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.45), 2) +
                                  germany.consumer_spending * round(random.uniform(0.05, 0.30), 2))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

    else:
        """Recovery simulation if an economic stimulus isn't in effect"""
        germany.consumer_spending = round(random.uniform(300, 1500), 2)
        germany.investment = round(random.uniform(200, 2400), 2)

        germany.government_spending = round(random.uniform(300, 2000), 2)
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.45), 2) +
                                  germany.consumer_spending * round(random.uniform(0.05, 0.30), 2))

    germany.exports = round(random.uniform(9000, 70000), 2)
    germany.imports = round(random.uniform(8000, 56000), 2)
    germany.current_gdp += (germany.consumer_spending + germany.investment + germany.government_spending +
                            (germany.exports - germany.imports))

def recession(germany):
    """Path taken if economy is currently in recession"""
    if germany.economic_stimulus:
        """Depression simulation if an economic stimulus is in effect"""
        germany.consumer_spending = -round(random.uniform(3000, 9000), 2)
        germany.investment = -round(random.uniform(4500, 10000), 2)

        germany.government_spending = round(random.uniform(90000, 700000), 2)
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.45), 2) +
                                  germany.consumer_spending * round(random.uniform(0.05, 0.30), 2))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

    else:
        """Depression simulation if an economic stimulus isn't in effect"""
        germany.consumer_spending = -round(random.uniform(10000, 30000), 2)
        germany.investment = -round(random.uniform(10000, 48000), 2)

        germany.government_spending = round(random.uniform(200000, 750000), 2)
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.45), 2) +
                                  germany.consumer_spending * round(random.uniform(0.05, 0.30), 2))

    germany.exports = round(random.uniform(9000, 65000), 2)
    germany.imports = round(random.uniform(8000, 90000), 2)
    germany.current_gdp += (germany.consumer_spending + germany.investment + germany.government_spending +
                            (germany.exports - germany.imports))

def depression(germany):
    """Path taken if economy is currently in depression"""
    if germany.economic_stimulus:
        """Depression simulation if an economic stimulus is in effect"""
        germany.consumer_spending = -round(random.uniform(6000, 20000), 2)
        germany.investment = -round(random.uniform(7500, 24000), 2)

        germany.government_spending = round(random.uniform(130000, 800000), 2)
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.45), 2) +
                                  germany.consumer_spending * round(random.uniform(0.05, 0.30), 2))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

    else:
        """Depression simulation if an economic stimulus isn't in effect"""
        germany.consumer_spending = -round(random.uniform(30000, 50000), 2)
        germany.investment = -round(random.uniform(20000, 67000), 2)

        germany.government_spending = round(random.uniform(300000, 850000), 2)
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.45), 2) +
                                  germany.consumer_spending * round(random.uniform(0.05, 0.30), 2))

    germany.exports = round(random.uniform(9000, 54000), 2)
    germany.imports = round(random.uniform(8000, 100000), 2)
    germany.current_gdp += (germany.consumer_spending + germany.investment + germany.government_spending +
                            (germany.exports - germany.imports))
def gdp_changes(germany):
    if germany.economic_state == "recovery":
        recovery(germany)

    elif germany.economic_state == "expansion":
        expansion(germany)

    elif germany.economic_state == "recession":
        recession(germany)

    elif germany.economic_state == "depression":
        depression(germany)

def economic_decisions(germany):
    """Primary economic function"""
    if germany.current_year < germany.date.year:

        germany.economic_growth = (germany.current_gdp - germany.past_gdp / ((germany.past_gdp + germany.current_gdp) / 2)) * 100

        if germany.economic_growth <= 2.0:
            choice = input(f"Your GDP grew {germany.economic_growth}% last year.\n"
                           f"Would you like to apply a stimulus?: ")

            if choice.lower() == "yes" or choice.lower() == "y":
                # economic_stimulus(germany)
                pass

    else:
        gdp_changes(germany)

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

"""Random Functions"""
def random_politics(germany):
    chance = random.randrange(10, 20000)
def random_economics(germany):
    pass
def random_social(germany):
    chance = random.randrange(10, 20000)

    if chance % 4 == 0:
        """Chance that somebody gets mugged
        - chance for death
        - decrease in happiness
        """
        death_chance = random.randrange(0, 2)
        print("A mugging has just occurred.\n")
        if death_chance == 1:
            print("The mugging has resulted in the victims death")
            germany.deaths += 1
            germany.population -= 1
            decrease = round(random.uniform(0.1, 0.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease
        else:
            decrease = round(random.uniform(0.1, 0.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease

    elif chance % 6 == 7:
        """Chance that someone burglarizes a house
        - internal chance for death
        - decrease in happiness
        """
        death_chance = random.randrange(0, 2)
        print("A burglary has just occurred.\n")
        if death_chance == 1:
            deaths = random.randrange(1, 7)
            print(f"The burglary has resulted in the {deaths} death(s)")
            germany.deaths += deaths
            germany.population -= deaths
            decrease = round(random.uniform(0.1, 0.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease
        else:
            decrease = round(random.uniform(0.1, 0.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease

    elif chance % 8 == 3:
        """Chance that somebod loses their savings @ a casino
        - decrease in happiness
        - slight decrease in GDP(Consumer spending)
        """
        loss = round(random.uniform(10000, 600000), 2)
        print(f"Someone just lost ${loss} at their local casino")

        decrease = round(random.uniform(0.25, 2.56), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        germany.current_gdp -= round(loss * round(random.uniform(0.25, 0.55), 2), 2)

    elif chance % 12 == 9:
        """Chance that a homicide occurs
        - decrease in stability and happiness
        - decrease in population
        """
        deaths = random.randrange(3, 56)
        print(f"A homicide has just occurred.\n"
              f"{deaths} deaths occurred during this homicide.\n")
        time.sleep(3)
        germany.population -= deaths
        germany.deaths += deaths

        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability

    elif chance % 14 == 10:
        """Chance that a certain public space gets shot up
        - Decrease in population
        - Decrease in stability and happiness
        """
        locations = ["School", "Library", "Restaurant", "Bakery", "Courthouse", "Bank"]
        deaths = random.randrange(6, 100)
        print(f"Oh no there was a shooting at a local {locations[random.randrange(0, len(locations) - 1)]}.\n"
              f"This shooting resulted in the deaths of {deaths} people.\n")
        germany.stability += round(random.uniform(0.25, 1.75), 2)
        germany.happiness += round(random.uniform(0.25, 4.75), 2)
        germany.population -= deaths
        germany.deaths += deaths

        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability

        time.sleep(3)

    elif chance % 16 == 5:
        """Chance that someone gets married
        - increase in happiness and stability
        """
        print("someone just got married\n")
        time.sleep(3)
        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability

    elif chance % 18 == 7:
        """Chance that a college dorm throws a party
        - increase in happiness
        - internal chance of death
            -> if death 
                - decrease in happiness
        """
        print("A college dorm is throwing a wild party\n")
        time.sleep(3)
        chance = random.randrange(0, 2)
        if chance == 1:
            people = random.randrange(1, 30)
            print(f"Well bad news...{people} people died from partying a little to hard.\n")
            time.sleep(3)
            germany.population -= people
            germany.deaths += people
            time.sleep(3)
            germany.happiness -= random.randrange(1, 4)
        else:
            germany.happiness += random.randrange(2, 7)

    elif chance % 21 == 10:
        """Chance that a high schooler throws a party
        - increase in happiness
        - internal chance of death
            -> if death 
                - decrease in happiness
        """
        print("A popular high schooler is throwing a wild party\n")
        time.sleep(3)
        chance = random.randrange(0, 2)
        if chance == 1:
            people = random.randrange(1, 30)
            print(f"Well bad news...{people} people died from partying a little to hard.\n")
            germany.population -= people
            germany.deaths += people
            time.sleep(3)
            germany.happiness -= random.randrange(1, 4)
        else:
            germany.happiness += random.randrange(2, 7)

    elif chance % 26 == 8:
        """Chance that car rolls into group of people
        - decrease in population
        - decrease in happiness and stability
        """
        deaths = random.randrange(3, 25)
        print(f"Someone just rolled their car into a group of people. {deaths} people died.\n")
        germany.population -= deaths
        time.sleep(3)

        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability

    elif chance % 36 == 7:
        """Chance that somebody converts and begins to believe in God
        -> Christian, Islamic, Jewish, or other
        - increase in happiness and stability
        """
        religions = ["Jewish", "Christian", "Islamic"]
        print(
            f"An Atheist just converted to believing in the {religions[random.randrange(0, len(religions) - 1)]} God\n")
        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability
        time.sleep(3)
"""Primary Random Function"""
def random_functions(germany):
    random_social(germany)
    random_politics(germany)
    random_economics(germany)

"""Main function of manual German version of game"""
def manual_game(germany):
    # establishment of check upon game status
    while germany.population > 200000:
        germany.date = germany.date + timedelta(days=1)
        # incrementing of time
        print(germany.date)
        # primary functions
        economic_decisions(germany)
        population_change(germany)
        political_change(germany)
        random_functions(germany)
        if germany.stability >= 50:
            choice = input("Important!!! view your stats: ")
            if choice == "y" or choice == "yes":
                check_stats(germany)
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