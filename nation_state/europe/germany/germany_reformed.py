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

"""Military dictionaries"""
army_size = {
    "1910": 673000,
    "1914": 862000,
    "1918": 2000000,
    "1932": 100000,
    "1936": 601000,
    "1939": 2970000
}

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

"""Military functions"""

def retire_soldiers(germany):
    """Function for retiring old, wounded, or stupid soldiers"""
    germany.army_size -= random.randrange(2, 100)
def increase_army_size(germany):
    if germany.date < datetime(1918, 11, 11) or germany.date.year > datetime(1933, 1, 30):
        """Periods in time where Germany doesn't have army size restrictions"""
        increase = round(germany.conscripts * round(random.uniform(0.0001, 0.0005), 5), 0)
        germany.army_size += increase
        germany.conscripts -= increase

    elif germany.date > datetime(1918, 11, 12) and germany.date < datetime(1933, 1, 30):
        increase = round(germany.conscripts * round(random.uniform(0.0001, 0.0005), 5), 0)
        if (germany.army_size + increase) < 100000:
            germany.army_size += increase
            germany.conscripts -= increase
def increase_conscripts(germany):
    """Function for increasing eligible candidates in draft"""
    if germany.conscription_status == "volunteer":
        if germany.date == germany.conscript_census:
            """Amount of population that is eligible under volunteering draft"""
            germany.conscripts = round(germany.population * round(random.uniform(0.0001, 0.0009), 5), 0)
            germany.conscript_census = germany.date + timedelta(days=15)

    elif germany.conscription_status == "limited":
        if germany.date == germany.conscript_census:
            """Amount of population that is eligible under limited draft"""
            germany.conscripts = round(germany.population * round(random.uniform(0.0001, 0.002), 5), 0)
            germany.conscript_census = germany.date + timedelta(days=20)

    elif germany.conscript_status == "extensive":
        if germany.date == germany.conscript_census:
            """Amount of population that is eligible under extensive draft"""
            germany.conscripts = round(germany.population * round(random.uniform(0.0001, 0.009), 5), 0)
            germany.conscript_census = germany.date + timedelta(days=25)

    elif germany.conscript_status == "required":
        if germany.date == germany.conscript_census:
            """Amount of population that is eligible under required drafting"""
            germany.conscripts = round(germany.population * round(random.uniform(0.0001, 0.02), 5), 0)
            germany.conscript_census = germany.date + timedelta(days=30)

def military_functions(germany):
    increase_conscripts(germany)
    increase_army_size(germany)
    retire_soldiers(germany)

"""Statistics function"""
def check_stats(german):
    """Stats organized by...
    1. Politics
    2. Economics
    3. Social aspects
    4. Others
    """
    print(f"Your current Kaiser is {german.kaiser}\n"
          f"Your current Chancellor is {german.chancellor}.\n"
          f"Your current population is {german.population}.\n"
          f"You have {german.conscripts} conscripts.\n"
          f"Your army has {german.army_size} soldiers")
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
                    decrease_happiness = round(random.uniform(0.25, 3.45), 2)
                    decrease_stability = round(random.uniform(0.25, 1.45), 2)
                    if (germany.happiness - decrease_happiness) < 5:
                        germany.happiness -= decrease_happiness

                    if (germany.stability - decrease_stability) < 5:
                        germany.stability -= decrease_stability
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
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.35), 2) +
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
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.35), 2) +
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
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.35), 2) +
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
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.35), 2) +
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
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.35), 2) +
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
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.35), 2) +
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
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.35), 2) +
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
        germany.national_debt += (germany.government_spending * round(random.uniform(0.05, 0.35), 2) +
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
    pass
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
    if chance % 5 == 10:
        """Chance that politician of any political party makes a speech
        - if politician is making speech from 1932 to 1945
            * Potential for politicians death and portion of rebels death
            * increase in stability and decrease in happiness
        """
        if germany.date < datetime(1932, 1, 30):
            chance = random.randrange(0, 3)

            if chance == 0:
                """Chance that the free conservative party holds a speech"""
                print("The free conservative party just held a speech in Berlin.\n")
                time.sleep(3)
                for i in range(0, random.randrange(100, 2000)):
                    chance = random.randrange(0, 2)
                    """Chance that influence either takes supporters away from progressive
                    or center party
                    """
                    if chance == 0:
                        germany.center_party -= 1
                        germany.free_conservatives += 1
                    elif chance == 1:
                        germany.progressives -= 1
                        germany.free_conservatives += 1

            elif chance == 1:
                """Chance that the progressive party holds a speech"""
                print("The progressive party just held a speech in Berlin.\n")
                time.sleep(3)

                for i in range(0, random.randrange(100, 2000)):
                    chance = random.randrange(0, 2)
                    """Chance that influence either takes supporters away from progressive
                    or center party
                    """
                    if chance == 0:
                        germany.center_party -= 1
                        germany.progressives += 1
                    elif chance == 1:
                        germany.free_conservatives -= 1
                        germany.progressives += 1

            elif chance == 2:
                """Chance that the center party holds a speech"""
                print("The center party just held a speech in Berlin.\n")
                time.sleep(3)

                for i in range(0, random.randrange(100, 2000)):
                    chance = random.randrange(0, 2)
                    """Chance that influence either takes supporters away from progressive
                    or center party
                    """
                    if chance == 0:
                        germany.progressives -= 1
                        germany.center_party += 1
                    elif chance == 1:
                        germany.free_conservatives -= 1
                        germany.center_party += 1

    elif chance % 19 == 15:
        """Chance that politician secretly influences GDP
        - increase in GDP and national debt
        """
        increase = round(random.uniform(12000, 300000), 2)
        germany.current_gdp += increase
        germany.national_debt += round(round(random.uniform(0.09, 0.30), 2), 2)

    elif chance % 25 == 21:
        """Chance that politician secretly influences population
        - increases in population
        """
        births = random.randrange(13, 2000)
        germany.births += births
        germany.population += births
        for i in range(0, births):
            chance = random.randrange(0, 3)
            if chance == 0:
                germany.free_conservatives += 1

            elif chance == 1:
                germany.progressives += 1

            elif chance == 2:
                germany.center_party += 1

    elif chance % 48 == 38:
        """Chance that an assassination attempt is made on the German Chancellor
        - internal chance if successful or not
            -> other people will die as well
        - economy goes into recession
            -> GDP slashed by 1.25
        - decrease in stability
        """

    elif chance % 60 == 59:
        """Chance that the Kaiser or Heir to the throne is assassinated
        - internal chance if successful or not
            -> other people will die as well
        - if Kaiser is in power...GDP will be slashed by 1.5
        - decrease in stability
        """
        chance = random.randrange(0, 9)
        if germany.date < datetime(1918, 11, 11):
            if chance % 8 == 0:
                print(f"Kaiser {germany.kaiser} has been assassinated!!!\n")
                germany.kaiser = kaisers[0]
                kaisers.pop(0)
                print(f"{germany.kaiser} has replace him")
                germany.current_gdp /= 1.5
                economic_stimulus(germany)
                germany.stability -= round(random.uniform(1.25, 10.25), 2)
def random_economics(germany):
    chance = random.randrange(10, 20000)
    if chance % 3 == 7:
        """Chance that someone starts a new business
        - slight increase in GDP
            -> investment
        - increase in happiness and stability
        - increase in national debt
            -> loans required for starting business
        """
        print("Someone has begun a new business.\n")
        time.sleep(3)

        gdp_increase = round(random.uniform(1200, 3000), 2)
        germany.current_gdp += gdp_increase
        germany.national_debt += round(gdp_increase * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(0.1, 1.00), 2)
        happiness_increase = round(random.uniform(0.1, 1.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase

    elif chance % 6 == 5:
        """Chance that someone gets sued
        - decrease in happiness
        - slight decrease in GDP
            -> Consumer spending
        """
        print("Someone just got sued.\n")
        time.sleep(3)

        germany.current_gdp -= round(random.uniform(1000, 30000), 2)
        # representing loss in CPP

        happiness_decrease = round(random.uniform(0.1, 1.00), 2)
        if (germany.happiness - happiness_decrease) > 5:
            germany.happiness -= happiness_decrease

    if chance % 8 == 3:
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

    elif chance % 9 == 5:
        """Chance that somebody begins to invest in economy
        - increase in happiness and stability
        - slight increase in GDP
            -> Investment
        """
        print("Someone has begun to invest. "
              "What a smart lad\n")

        germany.current_gdp += round(random.uniform(1200, 6000), 2)

        stability_increase = round(random.uniform(0.1, 1.00), 2)
        happiness_increase = round(random.uniform(0.1, 1.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase

    elif chance % 17 == 9:
        """Chance that somebody wins the lottery
        - increase in GDP by 3/4 of winnings
        - increase in national debt by randomized selection of 1/4 to 3/4
            -> consumer debt
        - increase in happiness and stability
        """
        winnings = round(random.uniform(100000, 2000000), 2)
        print(f"somebody won {winnings} in the Eurojackpot.\n")
        time.sleep(3)

        germany.current_gdp += winnings * 0.75
        germany.national_debt += round(winnings * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(0.1, 0.5), 2)
        happiness_increase = round(random.uniform(1.25, 3.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase

    elif chance % 20 == 11:
        """Chance of the Bundestag/Reichstag spending an extra amount of money
        - increase in GDP by randomized selection of 1/4 to 3/4 of money
            -> increase in national debt by same amount
        - increase in stability and happiness
        """
        spending = round(random.uniform(10000, 500000), 2)
        print(f"The Bundestag decided to spend an extra ${spending} today\n")
        time.sleep(3)

        germany.current_gdp += round(spending * round(random.uniform(0.25, 0.75), 2), 2)
        germany.national_debt += round(spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(1.00, 1.5), 2)
        happiness_increase = round(random.uniform(0.25, 1.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase

    elif chance % 27 == 17:
        """Chance of a certain amount of banks(1-15) collapse
        - Decrease in GDP
            -> loss based upon severity
        - increase in national debt
            -> government and consumer spending
        - decrease in stability and happiness
        """
        banks = random.randrange(1, 16)
        loss = 0
        if banks < 10:
            loss = round(random.uniform(10000, 200000), 2)
        if banks > 10:
            loss = round(random.uniform(200000, 1000000), 2)

        print(f"{banks} bank(s) collapsed today resulting in a loss of ${loss}.\n")
        time.sleep(3)
        germany.current_gdp -= loss
        germany.national_debt += round(loss * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(1.00, 5.5), 2)
        happiness_increase = round(random.uniform(2.25, 8.00), 2)

        if (germany.happiness - happiness_increase) > 5:
            germany.happiness -= happiness_increase

        if (germany.stability - stability_increase) > 5:
            germany.stability -= stability_increase

    elif chance % 32 == 11 and germany.date >= germany.tax_change_date:
        """Chance that the Bundestag/Reichstag raises taxes
        - decrease in stability and happiness
        **Internal checks will be put in place to prevent 
        rates over 100%**
        """
        tax_hike = round(random.uniform(0.25, 5.56), 2)
        if (germany.tax_rate + tax_hike) < 100:
            print(f"the Bundestag raised taxes by {tax_hike}% today.\n")
            time.sleep(3)
            stability_increase = round(random.uniform(0.20, 1.00), 2)
            happiness_increase = round(random.uniform(0.25, 2.00), 2)

            if (germany.happiness - happiness_increase) > 5:
                germany.happiness -= happiness_increase

            if (germany.stability - stability_increase) > 5:
                germany.stability -= stability_increase
            germany.tax_change_date = germany.date + timedelta(days=60)

        else:
            print(f"the Bundestag attempted to raise taxes by {tax_hike}%.\n"
                  f"However the hike would've made the tax rate exceed 100%.\n")

    elif chance % 39 == 13 and germany.date >= germany.tax_change_date:
        """Chance that the Bundestag/Reichstag lowers taxes
        - increase in stability and happiness
        - increase in GDP
            -> Consumer and government spending and investment
        - increase in National debt
            -> government and consumer spending
        **Internal checks will be put in place to prevent 
        rates below 10% **
        """
        tax_hike = round(random.uniform(0.25, 5.56), 2)
        if (germany.tax_rate - tax_hike) >= 10:
            print(f"the Bundestag lowered taxes by {tax_hike}% today.\n")
            time.sleep(3)
            stability_increase = round(random.uniform(0.20, 1.00), 2)
            happiness_increase = round(random.uniform(0.25, 2.00), 2)

            if (germany.happiness + happiness_increase) < 98:
                germany.happiness += happiness_increase

            if (germany.stability + stability_increase) < 98:
                germany.stability += stability_increase
            germany.tax_change_date = germany.date + timedelta(days=60)

        else:
            print(f"the Bundestag attempted to lower taxes by {tax_hike}%.\n"
                  f"However the hike would've made the tax rate dip below 10%.\n")

    elif chance % 49 == 20 and (germany.date >= germany.economic_change_date) and \
            germany.economic_state != "recession":
        """Chance that German economy shifts into a Recession
        - stimulus function gets called
        - GDP gets slashed by 1.5
        - stability and happiness decrease
        - Government spending increases alongside national debt by 1/4 to 3/4 of that spending
        - later on, potential for Brandenburg-Prussia to lose control of other states
            -> especially Bavaria
        """
        print("The German economy has randomly fallen into a Recession.\n")
        time.sleep(3)
        germany.economic_state = "recession"
        germany.current_gdp /= 1.5
        spending = round(random.uniform(120000, 1000000), 2)
        germany.current_gdp += spending
        germany.national_debt += round(spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(2.20, 5.00), 2)
        happiness_increase = round(random.uniform(3.25, 8.00), 2)

        if (germany.happiness - happiness_increase) > 5:
            germany.happiness -= happiness_increase

        if (germany.stability - stability_increase) > 5:
            germany.stability -= stability_increase

        germany.economic_change_date = germany.date + timedelta(days=120)
        economic_stimulus(germany)

    elif chance % 49 == 15 and (germany.date >= germany.economic_change_date) and \
            germany.economic_state != "recovery":
        """Chance that German economy shifts into a Recovery stage
                - GDP gets multiplied by 1.5
                - stability and happiness increase
                - Government spending increases alongside national debt by 1/4 to 3/4 of that spending
        """

        print("The German economy has randomly fallen into a Recession.\n")
        time.sleep(3)
        germany.economic_state = "recovery"
        germany.current_gdp *= 1.5
        consumer_spending = round(random.uniform(120000, 1000000), 2)
        germany.current_gdp += consumer_spending
        germany.national_debt += round(consumer_spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(2.20, 5.00), 2)
        happiness_increase = round(random.uniform(3.25, 8.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability - stability_increase) < 98:
            germany.stability -= stability_increase

        germany.economic_change_date = germany.date + timedelta(days=120)

    elif chance % 60 == 29 and (germany.date >= germany.economic_change_date) and \
            germany.economic_state != "depression":
        """Chance that German economy collapses in a depression
        - stimulus function gets called
        - GDP gets slashed by 3
        - stability and happiness decrease
        - Government spending increases alongside national debt by 1/4 to 3/4 of that spending
        - later on, potential for Brandenburg-Prussia to lose control of other states
            -> especially Bavaria
        """
        print("The German economy has randomly fallen into a Depression.\n")
        time.sleep(3)
        germany.economic_state = "depression"
        germany.current_gdp /= 3
        spending = round(random.uniform(1000000, 9000000), 2)
        germany.current_gdp += spending
        germany.national_debt += round(spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(10.20, 15.00), 2)
        happiness_increase = round(random.uniform(13.25, 20.00), 2)

        if (germany.happiness - happiness_increase) > 5:
            germany.happiness -= happiness_increase

        if (germany.stability - stability_increase) > 5:
            germany.stability -= stability_increase
        economic_stimulus(germany)

    elif chance % 60 == 15 and (germany.date >= germany.economic_change_date) and \
            germany.economic_state != "expansion":
        """Chance that German economy shifts into an expansion stage
                - GDP gets multiplied by 3
                - stability and happiness increase
                - Government spending increases alongside national debt by 1/4 to 3/4 of that spending
        """
        print("The German economy has randomly fallen into an expansion.\n")
        time.sleep(3)
        germany.economic_state = "expansion"
        germany.current_gdp *= 3
        consumer_spending = round(random.uniform(1000000, 9000000), 2)
        germany.current_gdp += consumer_spending
        germany.national_debt += round(consumer_spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(10.20, 15.00), 2)
        happiness_increase = round(random.uniform(13.25, 20.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase
def random_social(germany):
    chance = random.randrange(10, 20000)

    if chance % 10 == 3:
        """Chance that a parade occurs
        - increase in happiness and stability
        """
        print("A parade just occurred.\n")
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
        if (germany.happiness + decrease) < 98:
            germany.happiness += decrease

        if (germany.stability + decrease_stability) < 98:
            germany.stability += decrease_stability
        time.sleep(3)

def random_crime(germany):
    chance = random.randrange(10, 20000)
    if chance % 4 == 5:
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

    elif chance % 13 == 7:
        """Chance that somebody decides to rob a bank
        - internal chance of it being successful or not
            -> further internal chance if death occurs
                * Decrease happiness and stability
                * Decrease in population if people are killed
            * Decrease in happiness and stability
            * Decrease in GDP
                - will be a drop by 3/4 of what was lost
            * increase in national debt to replace losses
                - both government and consumer spending
        """
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance if bank robbery is successful"""
            chance_two = random.randrange(0, 2)
            if chance_two == 0:
                """Chance that the failed robbery is non-lethal"""
                print("A bank robbery was just attempted.\n"
                      "The robber was unsuccessful and nobody got hurt.\n")
                time.sleep(3)

            elif chance_two == 1:
                """Chance that failed robbery is lethal"""
                deaths = random.randrange(3, 20)
                print("A bank robbery was just attempted.\n"
                      f"The robber was unsuccessful, but killed {deaths} people in the process\n")
                time.sleep(3)
                germany.deaths += deaths
                germany.population -= deaths
                stability_increase = round(random.uniform(0.1, 1.00), 2)
                happiness_increase = round(random.uniform(1.25, 3.00), 2)

                if (germany.happiness - happiness_increase) > 5:
                    germany.happiness -= happiness_increase

                if (germany.stability - stability_increase) > 5:
                    germany.stability -= stability_increase

        elif chance == 1:
            """Chance that bank robbery is successful"""
            chance_two = random.randrange(0, 2)
            if chance_two == 0:
                """Chance that bank robbery was successful yet non lethal"""
                loss = round(random.uniform(10000, 900000), 2)
                print(f"A bank robbery just occurred. The specific bank lost ${loss}.\n"
                      f"Fortunately nobody was hurt")
                time.sleep(3)

                germany.current_gdp -= loss
                germany.national_debt += round(loss * round(random.uniform(0.05, 0.25), 2), 2)

                stability_increase = round(random.uniform(0.5, 1.25), 2)
                happiness_increase = round(random.uniform(1.00, 2.25), 2)

                if (germany.happiness - happiness_increase) < 5:
                    germany.happiness -= happiness_increase

                if (germany.stability - stability_increase) < 5:
                    germany.stability -= stability_increase

            elif chance == 1:
                """Chance that bank robbery is successful and lethal"""
                loss = round(random.uniform(10000, 900000), 2)
                deaths = random.randrange(3, 20)
                print(f"A bank robbery just occurred. The specific bank lost ${loss}.\n"
                      f"{deaths} deaths occurred during this bank robbery\n")
                time.sleep(3)

                germany.current_gdp -= loss
                germany.national_debt += round(loss * round(random.uniform(0.05, 0.25), 2), 2)

                stability_increase = round(random.uniform(1.00, 2.00), 2)
                happiness_increase = round(random.uniform(1.00, 3.25), 2)

                if (germany.happiness - happiness_increase) > 5:
                    germany.happiness -= happiness_increase

                if (germany.stability - stability_increase) > 5:
                    germany.stability -= stability_increase

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

    elif chance % 17 == 13:
        """Chance that a human trafficking ring gets exposed(suppose all victims died)
        - decrease in population
        - decrease in happiness and stability
        - increase in national debt and GDP
            -> govt spending to clean mess up
        """
        if germany.date.year > 1918:
            people = random.randrange(700, 15000)
            print(f"A human trafficking ring with {people} victims was just uncovered")
            time.sleep(3)
            germany.population -= people
            decrease = round(random.uniform(1.10, 5.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease
            if (germany.stability - decrease) > 5:
                germany.stability -= decrease
            increase = round(random.uniform(10000, 2000000), 2)
            germany.current_gdp += increase
            germany.national_debt += round(increase * round(random.uniform(0.05, 0.25), 2), 2)

    elif chance % 25 == 30:
        """Chance that a major political scandal is uncovered
        - potential rebellion occurs
        - major decrease in stability and GDP(slash by 1.5)
        """
        loss = round(random.uniform(100000, 3000000), 2)
        print(f"A major political scandal has just been uncovered.\n"
              f"It is being reported that ${loss} was siphoned from Germany's GDP")
        time.sleep(3)
        germany.current_gdp -= loss

    elif chance % 60 == 50 and germany.rebellion != True:
        """Chance that a riot begins(could lead to rebellion)
        - major decrease in stability and happiness
        - can arise in any of the states of Germany
        - major decrease in GDP(slashed by factor of 2.5 or 5, depends)
            -> causes economy to go into depression or recession
                * based on chance
        - increase in national debt
        - later on, initiates a buildup of troops
        """
        days = random.randrange(30, 120)
        rebels = germany.population * round(random.uniform(0.01, 0.15), 2)
        print(f"A riot has begun in the region of {germany.regions[random.randrange(0, len(germany.regions) - 1)]}\n"
              f"It is being said that it will take {days} to quell this riot before it gets out of hand.\n'"
              f"So far, only {rebels} rebels have joined the cause/riot.\n")
        time.sleep(3)
        economic_chance = random.randrange(0, 2)
        if economic_chance == 0:
            print("Due to infighting the Germany economy has fallen into a Recession.\n")
            time.sleep(3)
            germany.economic_state = "recession"
            germany.economic_change_date = germany.date + timedelta(days=days)
            # economic_stimulus(germany)

        elif chance == 1:
            print("Due to infighting the Germany economy has fallen into a Depression.\n")
            time.sleep(3)
            germany.economic_state = "depression"
            germany.economic_change_date = germany.date + timedelta(days=days)
            # economic_stimulus(germany)
        germany.riot_over = germany.date + timedelta(days=days)

def random_international(germany):
    chance = random.randrange(10, 20000)
    if chance % 6 == 9:
        """Chance that Germany's relations with another nation improves
        - later on...
            * improved relations with other nation
            * more potential for trade relations
        """
    elif chance % 10 == 11:
        """Chance that Germany's relations with another nation deteriorate
        - later on...
            * worsened relations with specific nation
            * less potential for trade
        """

    elif chance % 15 == 14:
        """Chance that Germany randomly embargoes another nation
        - nation will not be in alliance
        """

    elif chance % 34 == 19:
        """Chance that a terrorist attack occurs on German soil
        - nation that commences terrorism will not be in alliance
        """

    elif chance % 50 == 46:
        """Random chance that Germany decides to go to war with another nation
        - nation will not be in alliance
        """
    pass

"""Primary Random Function"""
def random_functions(germany):
    random_social(germany)
    random_politics(germany)
    random_economics(germany)
    random_crime(germany)

"""Function dealing with potential rebellions"""
def rebellion(germany):
    if (germany.date <= germany.riot_over) or germany.rebellers != 0:
        loss = round(random.uniform(0.01, 0.09), 2) * germany.rebellers
        print(f"Today, we were able to defeat(kill) {round(loss, 2)} rebels today")
        time.sleep(3)
        civilian_loss = random.randrange(30, 1000)
        germany.rebel_deaths += (loss + civilian_loss)
        germany.deaths += loss
        germany.rebellers -= loss
        germany.population -= loss

        germany.stability -= round(random.uniform(0.75, 3.75), 2)
        germany.happiness -= round(random.uniform(1.75, 5.75), 2)

        germany.current_gdp -= round(random.uniform(1000, 40000), 2)
        germany.national_debt += round(random.uniform(100000, 400000), 2)

    else:
        print("The rebellion in our Vaterland is finally over.\n"
              f"Around {germany.rebel_deaths} deaths(both civilian and rebels) occurred in our scuffle.\n")
        time.sleep(3)
        germany.stability += round(random.uniform(0.75, 3.75), 2)
        germany.happiness += round(random.uniform(1.75, 5.75), 2)

"""Main function of manual German version of game"""
def manual_game(germany):
    # establishment of check upon game status
    while germany.population > 200000:
        germany.date = germany.date + timedelta(days=1)
        # incrementing of time
        print(germany.date)
        # primary functions
        events(germany)
        economic_decisions(germany)
        population_change(germany)
        political_change(germany)
        random_functions(germany)
        military_functions(germany)
        if germany.stability >= 50:
            choice = input("Important!!! view your stats: ")
            if choice == "y" or choice == "yes":
                check_stats(germany)
        if germany.rebellion == True:
            rebellion(germany)
        time.sleep(3)
class Germany:
    def __init__(self, year):
        self.date = datetime(int(year), 1, 1)
        # population variables
        self.population = population[year]
        self.population_change = 0
        self.current_pop = self.population
        self.births = 0
        self.deaths = 0
        self.rebel_deaths = 0
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
        self.rebellers = 0
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
        self.rebellion = False
        # economic variables
        if int(year) < 1918 and int(year) > 1914:
            for i in range(0, len(business_cycle) - 1):
                if business_cycle[i] == "recession":
                    self.economic_state = business_cycle[i]

        if int(year) < 1932 and int(year) > 1929:
            for i in range(0, len(business_cycle) - 1):
                if business_cycle[i] == "depression":
                    self.economic_state = business_cycle[i]

        if int(year) <= 1914 or int(year) >= 1932:
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
        # land variables
        if int(year) < 1918:
            self.regions = ["East Prussia", "Posen", "Silesia", "West Prussia", "Pomerania", "Brandenburg",
                            "Schleswig-Holstein", "Saxony", "Bavaria", "Alsace-Lorraine", "Hanover",
                            "Rhine", "Baden", "Wurttemberg", "Westphalia"]
        if int(year) > 1918 and int(year) < 1938:
            self.regions = ["East Prussia", "Silesia", "Brandenburg", "Pomerania", "Schleswig-Holstein", "Saxony",
                            "Bavaria", "Baden", "Wurttemberg", "Westphalia", "Hessen-Nassau"]

        if int(year) > 1938 and int(year) < 1944:
            self.regions = ["East Prussia", "Silesia", "Brandenburg", "Pomerania", "Schleswig-Holstein", "Saxony",
                            "Bavaria", "Baden", "Wurttemberg", "Westphalia", "Hessen-Nassau", "Bohemia", "Moravia",
                            "Austria", "Sudetenland"]
        # military variables
        self.conscription_status = "limited"
        """Will also include extensive, required, and volunteer(Weimar Republic)"""
        self.war_deaths = 0
        self.conscripts = round(self.population * round(random.uniform(0.0001, 0.0009), 5), 2)

        self.army_size = army_size[year]
        # international variables
        self.alliance = ""
        self.global_market_share = 0
        """Wont be utilized until other nations are developed"""
        # time variables
        self.conscript_census = self.date + timedelta(days=75)
        self.tax_change_date = self.date + timedelta(days=75)
        self.economic_change_date = self.date + timedelta(days=60)
        self.current_year = self.date.year
        self.riot_over = None