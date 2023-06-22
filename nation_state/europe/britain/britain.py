# political variables and dictionaries
import random
import time
from datetime import datetime, timedelta

monarchs = {
    """Dictionary for english monarchs
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "Edward VII",
    "1914": "George V",
    "1918": "George V",
    "1932": "George V",
    "1936": "Edward VIII",
    "1939": "George VI"
}

pm = {
    "1910": "H.H. Asquith",
    "1914": "H.H. Asquith",
    "1918": "David Lloyd George",
    "1932": "Ramsay MacDonald",
    "1936": "Stanley Baldwin",
    "1939": "Neville Chamberlain"
}

spare_pms = ["Duncan Pirie", "Henry Cowan", "Harold Baker", "James Calmont", "Ellis Ellis-Griffith",
             "Charles Craig", "William Jones", "Alfred Scott", "Sir Charles Hunter"]

spare_1900_1950_monarchs = ["Louis", "Prince Arthur", "Beatrice", "Prince Henry", "Alexander Ramsay", "Alexander Cambridge",
                            "Albert Victor", "Victoria II", "George VI"]

# population variables and dictionaries
population = {
    """Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""

    "1910": 44915900,
    "1914": 42956900,
    "1918": 39582000,
    "1932": 46335000,
    "1936": 47081300,
    "1939": 46029200
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}

tax_rate = {
    "1910": 10.0,
    "1914": 50.0,
    "1918": 80.0,
    "1932": 60.0,
    "1936": 60.0,
    "1939": 80.0
}

business_cycle = ["recession", "recovery", "expansion", "depression"]

"""Event functions"""
def political_events(britain):
    if britain.date == datetime(1936, 1, 20):
        """Date for George V's death"""
        print(f"{britain.monarch} is dead!!!")
        britain.monarch = "Edward VIII"
        print(f"{britain.monarch} is your new king. All hail Brittania.\n")

    if britain.date == datetime(1910, 5, 6):
        """Date for when Edward VII dies"""
        print(f"{britain.monarch} is dead!!")
        britain.monarch = "George V"
        print(f"{britain.monarch} is your new king. All hail Brittania.\n")

    if britain.date == datetime(1936, 12, 11):
        """Date for when Edward VIII abdicates"""
        print(f"{britain.monarch} has abdicated the throne.")
        britain.monarch = "George VI"
        print(f"{britain.monarch} is your new king. All hail Brittania.\n")

def economic_events(britain):
    if britain.date == datetime(1929, 10, 24):
        print("Britain has fallen into a severe depression.\n"
              "It is being reported that nations across the globe are experiencing similar events.\n")
        time.sleep(3)

    if britain.date > datetime(1929, 10, 24) and britain.date < datetime(1937, 1, 1):
        decrease_happiness = round(random.uniform(0.01, 0.05), 2)
        decrease_stability = round(random.uniform(0.01, 0.05), 2)
        if (britain.happiness - decrease_happiness) > 5:
            britain.happiness -= decrease_happiness
        elif (britain.stability - decrease_stability) > 5:
            britain.happiness -= decrease_stability

def social_events(britain):
    if britain.date == datetime(britain.date.year, 3, 17):
        print("Today is St. Patrick's Day in Britain.\n")
        time.sleep(3)

def events(britain):
    political_events(britain)
    economic_events(britain)
    social_events(britain)

"""Population functions"""
def population_change(britain):
    if britain.past_year < britain.date.year:
        britain.population_change = (britain.current_pop - britain.past_pop / ((britain.current_pop + britain.past_pop) / 2)) * 100

        britain.past_pop = britain.population
        """Resetting of current population(past)"""
        if britain.population_change <= 1.5:
            """Incorporation of what happens when population growth becomes too small"""
            print(f"Your population growth for {britain.current_year} was {britain.population_change}%\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == 'y':
                britain.viagra_subsidy = True

                if britain.condom_subsidy == True:
                    """Checking to see if condom subsidies exist"""
                    britain.condom_subsidy = False

        elif britain.population_change >= 10.5:
            """Incorporation of what happens when population growth becomes too large"""
            print(f"Your population growth for {britain.current_year} was {britain.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                britain.condom_subsidy = True

                if britain.viagra_subsidy == True:
                    """Checking to see if viagra subsidies exist"""
                    britain.viagra_subsidy = False

    else:
        if britain.viagra_subsidy:
            births = random.randrange(300, 600)
            britain.births += births
            britain.current_pop += births
            for i in range(0, births):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp += 1

                elif chance == 1:
                    britain.liberal += 1

                elif chance == 2:
                    britain.clup += 1

                elif chance == 3:
                    britain.independents += 1

            deaths = random.randrange(200, 400)
            britain.deaths += deaths
            britain.current_pop -= deaths

            for i in range(0, deaths):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp -= 1

                elif chance == 1:
                    britain.liberal -= 1

                elif chance == 2:
                    britain.clup -= 1

                elif chance == 3:
                    britain.independents -= 1

        elif britain.condom_subsidy:
            births = random.randrange(100, 300)
            britain.births += births
            britain.current_pop += births

            for i in range(0, births):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp += 1

                elif chance == 1:
                    britain.liberal += 1

                elif chance == 2:
                    britain.clup += 1

                elif chance == 3:
                    britain.independents += 1

            deaths = random.randrange(100, 200)
            britain.deaths += deaths
            britain.current_pop -= deaths

            for i in range(0, deaths):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp -= 1

                elif chance == 1:
                    britain.liberal -= 1

                elif chance == 2:
                    britain.clup -= 1

                elif chance == 3:
                    britain.independents -= 1

        else:
            births = random.randrange(200, 400)
            britain.births += births
            britain.current_pop += births

            for i in range(0, births):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp += 1

                elif chance == 1:
                    britain.liberal += 1

                elif chance == 2:
                    britain.clup += 1

                elif chance == 3:
                    britain.independents += 1

            deaths = random.randrange(150, 300)
            britain.deaths += deaths
            britain.current_pop -= deaths

            for i in range(0, deaths):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp -= 1

                elif chance == 1:
                    britain.liberal -= 1

                elif chance == 2:
                    britain.clup -= 1

                elif chance == 3:
                    britain.independents -= 1

"""Economic Functions"""
def recovery(britain):
    if britain.economic_stimulus:
        """Depression with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:

            britain.consumer_spending = round(random.uniform(1000, 20000), 2)
            britain.investment = round(random.uniform(1000, 45000), 2)
            britain.government_spending = round(random.uniform(1000, 46000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.05), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.055), 4), 2))

            britain.exports = round(random.uniform(300000, 800000), 2)
            britain.imports = round(random.uniform(200000, 660000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))

        elif britain.tax_rate > 25.00:
            britain.consumer_spending = round(random.uniform(1000, 15000), 2)
            britain.investment = round(random.uniform(1500, 35000), 2)
            britain.government_spending = round(random.uniform(4000, 66000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.05), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.05), 4), 2))

            britain.exports = round(random.uniform(300000, 600000), 2)
            britain.imports = round(random.uniform(120000, 560000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
    else:
        """Recovery without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:
            britain.consumer_spending = round(random.uniform(1000, 15000), 2)
            britain.investment = round(random.uniform(1000, 20000), 2)
            britain.government_spending = round(random.uniform(10000, 25000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.0011, 0.05), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.05), 4), 2))

            britain.exports = round(random.uniform(320000, 700000), 2)
            britain.imports = round(random.uniform(300000, 560000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = round(random.uniform(1000, 10000), 2)
            britain.investment = round(random.uniform(1000, 15000), 2)
            britain.government_spending = round(random.uniform(30000, 70000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.05), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.05), 4), 2))

            britain.exports = round(random.uniform(220000, 450000), 2)
            britain.imports = round(random.uniform(220000, 420000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
def expansion(britain):
    if britain.economic_stimulus:
        """Expansion with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:

            britain.consumer_spending = round(random.uniform(1000, 60000), 2)
            britain.investment = round(random.uniform(1000, 65000), 2)
            britain.government_spending = round(random.uniform(1000, 200000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.01, 0.095), 4), 2))

            britain.exports = round(random.uniform(120000, 1500000), 2)
            britain.imports = round(random.uniform(120000, 950000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))

        elif britain.tax_rate > 25.00:
            britain.consumer_spending = round(random.uniform(1000, 45000), 2)
            britain.investment = round(random.uniform(1000, 45000), 2)
            britain.government_spending = round(random.uniform(1000, 300000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.009), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.01, 0.095), 4), 2))

            britain.exports = round(random.uniform(120000, 750000), 2)
            britain.imports = round(random.uniform(120000, 650000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
    else:
        """Expansion without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:
            britain.consumer_spending = round(random.uniform(1000, 40000), 2)
            britain.investment = round(random.uniform(1000, 45000), 2)
            britain.government_spending = round(random.uniform(1000, 300000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.01), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.0095), 4), 2))

            britain.exports = round(random.uniform(120000, 1300000), 2)
            britain.imports = round(random.uniform(120000, 900000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = round(random.uniform(1000, 4500), 2)
            britain.investment = round(random.uniform(1000, 3500), 2)
            britain.government_spending = round(random.uniform(1000, 55000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.01), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))

            britain.exports = round(random.uniform(120000, 1100000), 2)
            britain.imports = round(random.uniform(120000, 950000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
def recession(britain):
    """Recession simulation based upon stimulus and tax rate"""
    if britain.economic_stimulus:
        """Recession with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:

            britain.consumer_spending = -round(random.uniform(1000, 6000), 2)
            britain.investment = -round(random.uniform(1000, 4000), 2)
            britain.government_spending = round(random.uniform(1000, 16000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.01, 0.09), 4), 2))

            britain.exports = round(random.uniform(120000, 750000), 2)
            britain.imports = round(random.uniform(120000, 1100000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 4000), 2)
            britain.investment = -round(random.uniform(1000, 3000), 2)
            britain.government_spending = round(random.uniform(20000, 60000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.01, 0.09), 4), 2))

            britain.exports = round(random.uniform(120000, 560000), 2)
            britain.imports = round(random.uniform(120000, 1100000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
    else:
        """Recession without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 2500), 2)
            britain.investment = -round(random.uniform(1000, 4000), 2)
            britain.government_spending = round(random.uniform(1000, 25000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.01, 0.09), 4), 2))

            britain.exports = round(random.uniform(120000, 560000), 2)
            britain.imports = round(random.uniform(120000, 1100000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 6000), 2)
            britain.investment = -round(random.uniform(1000, 6000), 2)
            britain.government_spending = round(random.uniform(1000, 35000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.01, 0.09), 4), 2))

            britain.exports = round(random.uniform(120000, 860000), 2)
            britain.imports = round(random.uniform(120000, 1100000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
def depression(britain):
    if britain.economic_stimulus:
        """Depression with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:

            britain.consumer_spending = -round(random.uniform(1000, 9000), 2)
            britain.investment = -round(random.uniform(1000, 6000), 2)
            britain.government_spending = round(random.uniform(1000, 25000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.15), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))
            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment)

            britain.exports = round(random.uniform(240000, 800000), 2)
            britain.imports = round(random.uniform(300000, 2000000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 11000), 2)
            britain.investment = -round(random.uniform(1000, 8000), 2)
            britain.government_spending = round(random.uniform(1000, 40000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.11), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))
            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment)


            britain.exports = round(random.uniform(120000, 800000), 2)
            britain.imports = round(random.uniform(120000, 1400000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
    else:
        """Depression without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 2500), 2)
            britain.investment = -round(random.uniform(1000, 4000), 2)
            britain.government_spending = round(random.uniform(1000, 25000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.11), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))
            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment)

            britain.exports = round(random.uniform(120000, 750000), 2)
            britain.imports = round(random.uniform(120000, 1400000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 10000), 2)
            britain.investment = -round(random.uniform(1000, 16000), 2)
            britain.government_spending = round(random.uniform(1000, 35000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.21), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))

            britain.exports = round(random.uniform(120000, 590000), 2)
            britain.imports = round(random.uniform(120000, 1400000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
def gdp_changes(britain):
    if britain.economic_state == "recovery":
        recovery(britain)
    elif britain.economic_state == "expansion":
        expansion(britain)
    elif britain.economic_state == "recession":
        recession(britain)
    elif britain.economic_state == "depression":
        depression(britain)
def economic_state(britain):
    if britain.date >= britain.economic_change_date:
        """Comparing current date to when Italy's economic state could change"""
        chance = random.randrange(0, 2000)
        if chance % 37 == 10:
            """Making potential for economic disaster really low"""
            if britain.current_gdp < britain.past_gdp:
                """Comparison of current gdp to past gdp"""
                if britain.economic_state == "expansion" or britain.economic_state == "recovery":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "recession":
                            print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                            time.sleep(3)
                            britain.economic_state = business_cycle[i]
                            britain.economic_change_date = britain.date + timedelta(days=240)
                            economic_stimulus(britain)
                            """increasing amount of time to check up on GDP
                            Time is average amount(6 months cycle)
                            """
                elif britain.economic_state == "recession":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "depression":
                            print("Your economy has entered into a depression "
                                  "after exceeding 6 months of decayed growth.\n")
                            time.sleep(3)
                            britain.economic_state = business_cycle[i]
                            britain.economic_change_date = britain.date + timedelta(days=270)
                            economic_stimulus(britain)
                            """
                            Since it takes awhile to escape a depression, amount of time on change date is increased
                            """

        if chance % 40 == 37:
            """making potential for economic expansion or recovery very low"""
            if britain.economic_state == "depression" or britain.economic_state == "recession":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recovery":
                        print("Your economy hs finally entered its recovery period\n")
                        time.sleep(3)
                        britain.economic_state = business_cycle[i]
                        britain.economic_change_date = britain.date + timedelta(days=240)
                        """increasing amount of time to check up on GDP
                        Time is average amount(6 months cycle)
                        """

            elif britain.economic_state == "recovery":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("Your economy has blasted into an expansionary period. Woo!\n")
                        time.sleep(3)
                        britain.economic_state = business_cycle[i]
                        britain.economic_change_date = britain.date + timedelta(days=270)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """
def economic_stimulus(britain):
    britain.economic_stimulus = True

    if britain.economic_state == "recession":
        choice = input("Do you want to increase the tax rate in order to support increased spending?\n"
                       "(Remember this will apply to the entire population): ")

        if choice.lower() == "yes" or choice.lower() == "y":
            valid_choice = False

            while valid_choice:

                tax_hike = float(input("By how much do you to increase taxes(max cap is 10)?: "))
                if tax_hike <= 10 and tax_hike >= 1.0:
                    britain.tax_rate += tax_hike
                    print(f"{britain.tax_rate}% is your new tax rate.\n")
                    time.sleep(3)
                    decrease = round(random.uniform(0.25, 1.45), 2)

                    if (britain.happiness - decrease) < 5:
                        britain.happiness -= decrease

                    valid_choice = True

                elif tax_hike <= 0 or tax_hike > 10:
                    print(f"New tax hike of {tax_hike}% is improper.\n"
                          f"Try again.")
                    time.sleep(3)

                else:
                    print("Not a valid tax rate")
                    time.sleep(3)

    elif britain.economic_state == "depression":
        tax_hike = round(random.uniform(0.5, 10), 2)
        if (britain.tax_rate + tax_hike) <= 68.00:
            if britain.date.year <= 1922 or britain.date.year >= 1946:
                print(f"Parliament has enacted a tax hike of {tax_hike}%\n")

            if britain.date.year > 1922 and britain.date.year < 1946:
                print(f"Il Duce has enacted a tax hike of {tax_hike}%\n")
            time.sleep(3)
def economic_decisions(britain):
    if britain.past_year < britain.date.year:
        britain.economic_growth = round((britain.current_gdp - britain.past_gdp / ((britain.past_gdp + britain.current_gdp) / 2)) * 100, 2)
        """Calculation of yearly economic growth"""
        if britain.economic_growth <= 2.0:
            if not britain.economic_stimulus:
                choice = input(f"Your GDP grew {britain.economic_growth}% last year.\n")
                if choice.lower() == "y" or choice.lower() == "yes":
                    pass
                    economic_stimulus(britain)

        elif britain.economic_growth >= 15.00:
            if britain.economic_stimulus:
                britain.economic_stimulus = False
    else:
        gdp_changes(britain)
        economic_state(britain)

"""Political functions"""
def politics_change(britain):
    if britain.date > britain.political_census:

        chance = random.randrange(0, 4)
        if chance == 0:
            """Chance that the labour party loses support"""
            loss = round(britain.lp * round(random.uniform(0.001, 0.09), 4), 0)
            britain.lp -= loss

            chance = random.randrange(0, 3)
            if chance == 0:
                """Chance that the CLUP party picks up support"""
                britain.clup += loss

            elif chance == 1:
                britain.liberal += loss

            elif chance == 2:
                britain.independents += loss

            britain.political_census = britain.date + timedelta(days=3)
            """Resetting of check in regards to political censuses"""

        elif chance == 1:
            """Chance that Conservative Labour unionist party loses support"""
            loss = round(britain.clup * round(random.uniform(0.01, 0.09), 4), 0)
            britain.clup -= loss
            chance = random.randrange(0, 3)
            if chance == 0:
                """Chance that the Labour party picks up support"""
                britain.lp += loss

            elif chance == 1:
                """Chance that liberals pick up support"""
                britain.liberal += loss

            elif chance == 2:
                """Chance that independent parties pick up support"""
                britain.independents += loss

            britain.political_census = britain.date + timedelta(days=3)
            """Resetting of check in regards to political censuses"""

        elif chance == 2:
            """Chance that independents lose support"""
            loss = round(britain.independents * round(random.uniform(0.01, 0.09), 4), 0)
            britain.independents -= loss

            chance = random.randrange(0, 3)
            if chance == 0:
                """Chance that the CLUP party picks up support"""
                britain.clup += loss

            elif chance == 1:
                """Chance that liberals pick up support"""
                britain.liberal += loss

            elif chance == 2:
                """Chance that the labour party pick up support"""
                britain.lp += loss

            britain.political_census = britain.date + timedelta(days=3)
            """Resetting of check in regards to political censuses"""

        elif chance == 3:
            """Chance that liberal party loses support"""
            loss = round(britain.liberal * round(random.uniform(0.01, 0.09), 4), 0)
            britain.liberal -= loss

            chance = random.randrange(0, 3)
            if chance == 0:
                """Chance that the CLUP party picks up support"""
                britain.clup += loss

            elif chance == 1:
                """Chance that the Labour party picks up support"""
                britain.lp += loss

            elif chance == 2:
                """Chance that Independent parties picks up support"""
                britain.independents += loss

            britain.political_census = britain.date + timedelta(days=3)
            """Resetting of check in regards to political censuses"""

"""Stats function"""
def social_stats(britain):
    print(f"Your current happiness level is {britain.happiness}%.")
    time.sleep(3)
    if britain.happiness < 35.45 and not britain.improve_happiness:
        choice = input(f"{britain.happiness}% doesnt represent a healthy civilian relationship with the government.\n"
                       f"A low happiness could lead to potential rebellions occurring.\n"
                       f"Would you like to improve your citizens' happiness over a course of 30 days?(y or n): ")
        if choice.lower() == "y":
            britain.improve_happiness = britain.date + timedelta(days=30)
    print(f"Your current population {britain.current_pop}.\n")
    time.sleep(3)
    print(f"There have been {britain.births} births in {britain.date.year}.\n")
    time.sleep(3)
    print(f"There have been {britain.deaths} deaths in {britain.date.year}.\n")
    time.sleep(3)

def political_stats(britain):
    print(f"Your current political stability is {britain.stability}%.\n")
    time.sleep(3)
    if britain.stability < 45.45 and not britain.improve_stability:
        choice = input(f"{britain.stability}% doesnt represent a functional government.\n"
                       f"Would you like to improve your government's stability for a course of 30 days?(y or n): ")
        if choice.lower() == "y":
            britain.improve_stability = britain.date + timedelta(days=30)
    print(f"Britain's current monarch is {britain.monarch}\n")
    time.sleep(3)
    print(f"Britain's current prime minister is {britain.pm}\n")
    time.sleep(3)

    print(f"Britain's liberal party makes up {round(round(britain.liberal / britain.current_pop, 4) * 100, 4)}% of the population.\n")
    time.sleep(3)
    print(f"The conservative and liberal unionist party makes up {round(round(britain.clup / britain.current_pop, 4) * 100, 4)}% of the population.\n")
    time.sleep(3)
    print(f"The Labour Party makes up {round(round(britain.lp / britain.current_pop, 4) * 100, 4)}% of the population.\n")
    time.sleep(3)
    print(f"Independents make up {round(round(britain.independents / britain.current_pop, 4) * 100, 4)}% of the population.\n")
    time.sleep(3)

def economic_stats(britain):
    print(f"Your current GDP is ${round(britain.current_gdp, 2)}.\n")
    time.sleep(3)
    print(f"Your current yearly gdp growth is {round(((britain.current_gdp - britain.past_gdp) / ((britain.past_gdp + britain.current_gdp) / 2)) * 100, 5)}%\n")
    time.sleep(3)
    print(f"Your current national debt is ${round(britain.national_debt, 2)}.\n")
    time.sleep(3)

    if britain.national_debt > 1000000000 and not britain.debt_repayment:
        choice = input(f"You are going to want to pay back some of your debt before it outpaces your assets.\n"
              f"Would you like to pay back some of your debt for 120 days?(y or n): ")
        if choice.lower() == "y":
            britain.debt_repayment = britain.date + timedelta(days=120)
def daily_decisions(britain):
    done = True
    while done:
        choice = input("Would you like to view your political, social, or economic stats?(enter quit to quit): ")
        if choice.lower() == "political":
            political_stats(britain)
        elif choice.lower() == "economic":
            economic_stats(britain)
        elif choice.lower() == "social":
            social_stats(britain)
        elif choice.lower() == "quit":
            done = False
            britain.check_stats = britain.date + timedelta(days=3)
def manual_game(britain):
    while britain.current_pop > 500000:
        # establishment of check upon game status
        print(f"Current Date: {britain.date.date()}\n")
        population_change(britain)
        politics_change(britain)
        economic_decisions(britain)
        if britain.date > britain.check_stats:
            daily_decisions(britain)
        britain.date += timedelta(days=1)
        time.sleep(3)

class Britain:
    def __init__(self, time):
        """time variables"""
        self.date = datetime(int(time), 1, 1)
        self.past_year = self.date.year
        self.political_census = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        """Variable for improving stability of nation over given time"""
        self.improve_stability = None
        """Ditto to improve stability"""
        self.improve_happiness = None
        """variable for repaying debt over given time"""
        self.debt_repayment = None
        self.check_stats = self.date + timedelta(days=3)
        """population variables"""
        self.current_pop = population[time]
        self.births = 0
        self.deaths = 0
        self.past_pop = self.current_pop
        self.population_change = None
        self.viagra_subsidy = False
        self.condom_subsidy = False
        """Political variables"""
        self.monarch = monarchs[time]
        self.pm = pm[time]
        self.stability = 90.00
        self.lp = round(self.current_pop * round(random.uniform(0.09, 0.35), 4), 0)
        # labour party
        self.clup = round((self.current_pop - self.lp) * round(random.uniform(0.09, 0.35), 4), 0)
        # conservative and liberal unionist party
        self.liberal = round((self.current_pop - self.lp - self.clup) * round(random.uniform(0.09, 0.35), 4), 0)
        # liberal party
        self.independents = self.current_pop - self.clup - self.lp - self.liberal
        """economic variables"""
        self.current_gdp = gdp[time]
        self.past_gdp = self.current_gdp
        self.national_debt = 0
        self.economic_growth = None
        self.economic_state = "recovery"
        self.economic_stimulus = False
        self.tax_rate = tax_rate[time]
        """Social variables"""
        self.happiness = 90.00
britain = Britain("1918")
manual_game(britain)