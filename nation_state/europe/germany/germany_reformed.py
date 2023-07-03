import random
import time
from datetime import datetime, timedelta
from nation_state.north_america.united_states import us_ai
from nation_state.europe.italy import italy_ai
from nation_state.europe.britain import britain_ai

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
    "1910": 23700000,
    "1914": 23739500,
    "1918": 23596800,
    "1932": 23794750,
    "1936": 24000000,
    "1939": 30045600
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
            germany.conscripts = round(germany.population * round(random.uniform(0.0001, 0.005), 5), 0)
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

                elif tax_hike <= 0 or tax_hike > 10:
                    print(f"New tax hike of {tax_hike} is improper./n"
                          f"try again")
                    time.sleep(3)

                else:
                    print("Not a valid tax rate")
                    time.sleep(3)

    elif germany.economic_state.lower() == "depression":

        tax_hike = round(random.uniform(0.5, 10), 2)
        if (germany.tax_rate + tax_hike) <= 86.00:
            if germany.date.year <= 1945:
                print(f"The Reichstag has enacted a tax hike of {tax_hike} points")
            else:
                print(f"The Bundestag has enacted a tax hike of {tax_hike} points")

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
                        germany.economic_change_date = germany.date + timedelta(days=270)
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
                economic_stimulus(germany)
                pass

    else:
        gdp_changes(germany)
        economic_state(germany)

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
        if germany.population_change <= 1.75:
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

def social_stats(germany):
    print(f"Your current happiness level is {germany.happiness}%.\n")
    time.sleep(3)
    if germany.happiness < 35.45 and not germany.improve_happiness:
        choice = input(f"{germany.happiness}% doesnt represent a healthy civilian relationship with the government.\n"
                       f"A low happiness could lead to potential rebellions occurring.\n"
                       f"Would you like to improve your citizens' happiness over a course of 30 days?(y or n): ")
        if choice.lower() == "y":
            germany.improve_happiness = germany.date + timedelta(days=30)
    print(f"Your current population {germany.current_pop}.\n")
    time.sleep(3)
    print(f"There have been {germany.births} births in {germany.date.year}.\n")
    time.sleep(3)
    print(f"There have been {germany.deaths} deaths in {germany.date.year}.\n")
    time.sleep(3)

def political_stats(germany):
    print(f"Your current political stability is {germany.stability}%.\n")
    time.sleep(3)
    if germany.stability < 45.45 and not germany.improve_stability:
        choice = input(f"{germany.stability}% doesnt represent a functional government.\n"
                       f"Would you like to improve your government's stability for a course of 30 days?(y or n): ")
        if choice.lower() == "y":
            germany.improve_stability = germany.date + timedelta(days=30)

def economic_stats(germany):
    print(f"Your current GDP is ${round(germany.current_gdp, 2)}.\n")
    time.sleep(3)
    print(f"Your current yearly gdp growth is {round(((germany.current_gdp - germany.past_gdp) / ((germany.past_gdp + germany.current_gdp) / 2)) * 100, 5)}%\n")
    time.sleep(3)
    print(f"Your current national debt is ${round(germany.national_debt, 2)}.\n")
    time.sleep(3)

    if germany.national_debt > 1000000 and not germany.debt_repayment:
        choice = input(f"You are going to want to pay back some of your debt before it outpaces your assets.\n"
              f"Would you like to pay back some of your debt for 120 days?(y or n): ")
        if choice.lower() == "y":
            germany.debt_repayment = germany.date + timedelta(days=120)
def military_stats(germany):
    print(f"Your current army size is {germany.army_size} soldiers.\n")
    time.sleep(3)
    print(f"Your current conscription law is {germany.conscription_status}.\n")
    time.sleep(3)
    print(f"You currently have {germany.conscripts} recruitable soldiers.\n")
    time.sleep(3)

def daily_decisions(germany):
    done = True
    while done:
        choice = input("Would you like to view your political, social, military, or economic stats?(enter quit to quit): ")
        if choice.lower() == "political":
            political_stats(germany)
        elif choice.lower() == "economic":
            economic_stats(germany)
        elif choice.lower() == "social":
            social_stats(germany)
        elif choice.lower() == "military":
            military_stats(germany)
        elif choice.lower() == "quit":
            done = False
            germany.check_stats = germany.date + timedelta(days=3)

"""Main function of manual German version of game"""
def manual_game(germany):
    # establishment of check upon game status
    us = us_ai.UnitedStatesAI(germany.date.year)
    italy = italy_ai.Italy(germany.date.year)
    britain = britain_ai.BritainAI(germany.date.year)
    while germany.population > 200000:
        print(f"Date: {germany.date}")
        # primary functions
        events(germany)
        economic_decisions(germany)
        population_change(germany)
        political_change(germany)
        military_functions(germany)

        if germany.date > germany.check_stats:
            daily_decisions(germany)

        italy_ai.ai_game(italy)
        britain_ai.ai_game(britain)
        us_ai.manual_game(us)
        # incrementing of time
        germany.date = germany.date + timedelta(days=1)
        time.sleep(3)
class Germany:
    def __init__(self, year):
        self.date = datetime(int(year), 1, 1)
        """Variable for improving stability of nation over given time"""
        self.improve_stability = None
        """Ditto to improve stability"""
        self.improve_happiness = None
        """variable for repaying debt over given time"""
        self.debt_repayment = None
        self.check_stats = self.date + timedelta(days=3)
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

        # military variables
        self.conscription_status = "limited"
        """Will also include extensive, required, and volunteer(Weimar Republic)"""
        self.war_deaths = 0
        self.conscripts = round(self.population * round(random.uniform(0.0001, 0.0009), 5), 2)
        self.army_size = army_size[year]
        # international variables
        self.alliance = ""
        """Wont be utilized until other nations are developed"""
        # time variables
        self.conscript_census = self.date + timedelta(days=75)
        self.tax_change_date = self.date + timedelta(days=75)
        self.economic_change_date = self.date + timedelta(days=60)
        self.current_year = self.date.year
        self.riot_over = None