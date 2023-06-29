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
        print(f"{britain.monarch} is Britain's new king.\n")

    if britain.date == datetime(1910, 5, 6):
        """Date for when Edward VII dies"""
        print(f"{britain.monarch} is dead!!")
        britain.monarch = "George V"
        print(f"{britain.monarch} is Britain's new king\n")

    if britain.date == datetime(1936, 12, 11):
        """Date for when Edward VIII abdicates"""
        print(f"{britain.monarch} of Britain has abdicated the throne.")
        britain.monarch = "George VI"
        print(f"{britain.monarch} is Britain's new king\n")

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

            choice = random.randrange(0, 2)
            if choice == 0:
                britain.viagra_subsidy = True

                if britain.condom_subsidy == True:
                    """Checking to see if condom subsidies exist"""
                    britain.condom_subsidy = False

        elif britain.population_change >= 10.5:
            """Incorporation of what happens when population growth becomes too large"""
            choice = random.randrange(0, 2)
            if choice == 0:
                britain.condom_subsidy = True

                if britain.viagra_subsidy == True:
                    """Checking to see if viagra subsidies exist"""
                    britain.viagra_subsidy = False

    else:
        if britain.viagra_subsidy:
            births = random.randrange(300, 600)
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
                            print("The British economy into a recession after 6 months of decayed growth.\n")
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
                            print("The British economy has entered into a depression\n")
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
                        print("The British economy has entered into a recovery period\n")
                        time.sleep(3)
                        britain.economic_state = business_cycle[i]
                        britain.economic_change_date = britain.date + timedelta(days=240)
                        """increasing amount of time to check up on GDP
                        Time is average amount(6 months cycle)
                        """

            elif britain.economic_state == "recovery":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("The British economy has blasted into an expansionary period.\n")
                        time.sleep(3)
                        britain.economic_state = business_cycle[i]
                        britain.economic_change_date = britain.date + timedelta(days=270)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """
def economic_stimulus(britain):
    britain.economic_stimulus = True

    if britain.economic_state == "recession":
        choice = random.randrange(0, 2)

        if choice == 0:
            tax_hike = float(input("By how much do you to increase taxes(max cap is 10)?: "))
            if tax_hike <= 10 and tax_hike >= 1.0:
                britain.tax_rate += tax_hike
                print(f"{britain.tax_rate}% is your new tax rate.\n")
                time.sleep(3)
                decrease = round(random.uniform(0.25, 1.45), 2)

                if (britain.happiness - decrease) < 5:
                    britain.happiness -= decrease

    elif britain.economic_state == "depression":
        tax_hike = round(random.uniform(0.5, 10), 2)
        if (britain.tax_rate + tax_hike) <= 68.00:
            print(f"The British Parliament has enacted a tax hike of {tax_hike}%\n")
            decrease = round(random.uniform(0.25, 1.45), 2)

            if (britain.happiness - decrease) < 5:
                britain.happiness -= decrease
def economic_decisions(britain):
    if britain.past_year < britain.date.year:
        britain.economic_growth = round((britain.current_gdp - britain.past_gdp / ((britain.past_gdp + britain.current_gdp) / 2)) * 100, 2)
        """Calculation of yearly economic growth"""
        if britain.economic_growth <= 2.0:
            if not britain.economic_stimulus:
                choice = random.randrange(0, 2)
                if choice == 0:
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
    if britain.happiness < 35.45 and not britain.improve_happiness:
        choice = random.randrange(0, 2)
        if choice == 0:
            britain.improve_happiness = britain.date + timedelta(days=30)
            print("The British parliament has decided to improve their relations with citizens.\n")
            time.sleep(3)
def political_stats(britain):
    if britain.stability < 45.45 and not britain.improve_stability:
        choice = random.randrange(0, 2)
        if choice == 0:
            britain.improve_stability = britain.date + timedelta(days=30)
            print("The British parliament has decided to improve their political capital over a period of 120 days.\n")
            time.sleep(3)
def economic_stats(britain):
    if britain.national_debt > 3560000 and not britain.debt_repayment:
        choice = random.randrange(0, 2)
        if choice == 0:
            britain.debt_repayment = britain.date + timedelta(days=120)
            print("The British parliament has decided to pay back some of their national debt for a period of 120 days.\n")
            time.sleep(3)
def daily_decisions(britain):
    political_stats(britain)
    economic_stats(britain)
    social_stats(britain)
    britain.check_stats = britain.date + timedelta(days=3)

def improvements(britain):
    if britain.date < britain.debt_repayment:
        payment = round(britain.national_debt * round(random.uniform(0.001, 0.009), 5), 2)
        britain.national_debt -= payment
        britain.current_gdp -= payment

    if britain.date < britain.improve_stability:
        increase = round(random.uniform(0.01, 1.25), 2)
        if (increase + britain.stability) < 100:
            britain.stability += increase

    if britain.date < britain.improve_happiness:
        increase = round(random.uniform(0.01, 1.25), 2)
        if (increase + britain.happiness) < 100:
            britain.happiness += increase

"""International functions"""

def alternate_options(us, britain, globe):
    """passes to this function, if German government doesn't accept original terms, but is open to dialogue"""
    is_not_mediated = True
    while is_not_mediated:
        print("The Italian government did not accept your offer, however they could be willing to...")
        time.sleep(3)
        responses = ["1. Improve trade between your two nations(improve both economies)",
                     "2. Improve relations over period of 15 days(1.5 political power per day)",
                     "3. Accept a possible alliance(or accept your entry into an existing alliance)",
                     "4. Improve relations over a period of 20 days(1.5 political power per day)",
                     "5. Trade students and train each others workers(improve both economies)"]

        for i in responses:
            print(f"{i}\n")
            time.sleep(1)
        response_choice = int(input("Which one do you choose(1-5)?: "))
        chance = random.randrange(0, 7)
        # choice variable utilized for all response choices
        if response_choice == 1:
            """Improvement of trade"""

            if chance % 2 == 0:
                """57% chance of acceptance"""
                print("The Italian government has agreed to improve trade between our two nations.")
                time.sleep(3)
                us.improve_italian_trade = us.date + timedelta(days=30)
                is_not_mediated = False

            elif chance % 3 == 1:
                """28.5% chance of refusal to acknowledge"""
                print("The Italian government has not agreed to our terms\n")
                is_not_mediated = False
                time.sleep(3)

            elif chance % 4 == 2:
                """28.5% chance of diplomats getting kicked out of Reichstag"""
                print("Our diplomats have been kicked out of the Italian Parliament.\n")
                time.sleep(3)
                is_not_mediated = False

            else:
                print("Your offer died in the midst of geopolitics.\n")
                time.sleep(3)

        elif response_choice == 2:
            """Response for 15 day period"""
            if chance % 2 == 0:
                """57% chance of acceptance"""
                print("The Italian government has agreed to improve relations over a 15 day period.\n")
                time.sleep(3)
                us.improve_italian_relations = us.date + timedelta(days=15)
                is_not_mediated = False

            elif chance % 3 == 1:
                """28.5% chance of refusal to acknowledge"""
                print("The Italian government has not agreed to our terms\n")
                is_not_mediated = False
                time.sleep(3)

            elif chance % 4 == 2:
                """28.5% chance of diplomats getting kicked out of Parliament"""
                print("Our diplomats have been kicked out of the Italian parliament.\n")
                time.sleep(3)
                globe.tension += 1.5
                is_not_mediated = False

            else:
                print("Your offer died in the midst of geopolitics.\n")
                time.sleep(3)

        elif response_choice == 3:
            if britain.alliance:
                choice = input(f"Italy has invited us to join the {britain.alliance}.\n"
                               f"Do you accept?(y or n): ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    print(f"you have successfully entered into the {britain.alliance}.\n")
                    time.sleep(3)

        elif response_choice == 4:
            """Response for 20 day period"""

            if chance % 2 == 0:
                """57% chance of acceptance"""
                print("The Italian government has agreed to improve relations over a 20 day period.\n")
                time.sleep(3)
                us.improve_italian_relations = us.date + timedelta(days=20)
                is_not_mediated = False

            elif chance % 3 == 1:
                """28.5% chance of refusal to acknowledge"""
                print("The Italian government has not agreed to our terms\n")
                is_not_mediated = False
                time.sleep(3)

            elif chance % 4 == 2:
                """28.5% chance of diplomats getting kicked out of Reichstag"""
                print("Our diplomats have been kicked out of the Italian Parliament.\n")
                time.sleep(3)
                globe.tension += 1.5
                is_not_mediated = False

            else:
                print("Your offer died in the midst of geopolitics.\n")
                time.sleep(3)

        elif response_choice == 5:

            if chance % 2 == 0:
                """57% chance of acceptance"""
                print("The Italian government has agreed for us to train each others workers and students.\n")
                time.sleep(3)
                britain.improve_us_trade = britain.date + timedelta(days=20)
                us.improve_german_trade = us.date + timedelta(days=20)
                is_not_mediated = False

            elif chance % 3 == 1:
                """28.5% chance of refusal to acknowledge"""
                print("The Italian government has not agreed to our terms\n")
                is_not_mediated = False
                time.sleep(3)

            elif chance % 4 == 2:
                """28.5% chance of diplomats getting kicked out of Reichstag"""
                print("Our diplomats have been kicked out of the Italian Parliament.\n")
                time.sleep(3)
                globe.tension += 1.5
                is_not_mediated = False

            else:
                print("Your offer died in the midst of geopolitics.\n")
                time.sleep(3)

def kill_diplomats(us, globe):
    print("The British government has killed our diplomats on claims of espionage.\n")
    time.sleep(3)
    deaths = random.randrange(3, 20)
    us.current_pop -= deaths
    us.deaths += deaths
    globe.tension += round(random.uniform(1.0, 3.0), 2)

def manual_us_relations(us, britain, globe):
    """Function is called from new_usa if user wants to improve relations with Britain(You can also worsen relations)
        - if you worsen relations, you increase global tensions
        """
    positive = ["1. increase trade(5 political power per day, lasts 50 days)",
                "2. improve relations(1.5 political power per day, lasts 30 days)",
                "3. establish an embassy",
                "4. Guarantee British Independence(Decreases potential for political power growth, 25 political power)",
                "5. Establish An Alliance(join alliance, if Italy is in one already)"]

    negative = ["1. Subvert British government(50 political power)", "2. Embargo Britain(hurts British economy)",
                "3. Impose tariffs on british goods(hurts both british and US economies)",
                "4. Expel legal Britain residents within the US(20 political power)",
                "5. Imprison some legal Britain residents within the US(20 political power)",
                "6. Kill Britain Nationals(15 political power)",
                "7. Declare War against Britain(May bring British allies into war)",
                "8. Dissolve alliance with Britain(10 political power)",
                "9. Expel British diplomats(10 political power)"]

    not_finished = True
    while not_finished:
        choice = input("Would you like to improve or hinder relations with Britain?(Enter quit to leave relations): ")

        if choice.lower() == "improve":
            for pos in range(0, len(positive)):
                print(f"{positive[pos]}\n")
                time.sleep(3)

            choice = int(input("Which number do you choose(1-5)?: "))

            if globe.tension < 50 and us.british_relations > 50:
                """All choices for when tension is low and relations are great"""

                if choice == 1:
                    chance = random.randrange(0, 11)
                    if chance % 2 == 0:
                        """54.5% chance that Italian government accepts proposal"""
                        print("The British government has agreed to improve relations over a period of 50 days.\n")
                        time.sleep(3)

                        us.improve_british_relations = us.date + timedelta(days=50)

                    elif chance % 3 == 0:
                        """36.3% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """18.1% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)
                        not_finished = False

                    elif chance % 9 == 5:
                        """9.09% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)
                        not_finished = False

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 2:
                    chance = random.randrange(0, 11)
                    if chance % 2 == 0:
                        """54.5% chance that Italian government accepts proposal"""
                        print("The British government has agreed to improve trade over a period of 30 days.\n")
                        time.sleep(3)

                        us.improve_british_trade = us.date + timedelta(days=30)

                    elif chance % 3 == 0:
                        """36.3% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """18.1% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)
                        not_finished = False

                    elif chance % 9 == 5:
                        """9.09% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)
                        not_finished = False
                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 3:
                    chance = random.randrange(0, 20)
                    if chance % 2 == 0 and not us.british_embassy:
                        """54.5% chance that Italian government accepts proposal"""
                        print("The British government has approved of our building of an embassy in London\n")
                        time.sleep(3)
                        us.british_embassy = True

                    elif chance % 3 == 0:
                        """36.3% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """18.1% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)
                        not_finished = False

                    elif chance % 9 == 5:
                        """9.09% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)
                        not_finished = False

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 4:
                    chance = random.randrange(0, 20)
                    if chance % 2 == 0:
                        """54.5% chance that Italian government accepts proposal"""
                        print("The British government has accepted our guarantee of independence.\n")
                        time.sleep(3)

                    elif chance % 3 == 0:
                        """36.3% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """18.1% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)
                        not_finished = False

                    elif chance % 9 == 5:
                        """9.09% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)
                        not_finished = False

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 5:
                    chance = random.randrange(0, 20)
                    if chance % 2 == 0:
                        """54.5% chance that Italian government accepts proposal"""
                        if us.britain.alliance:
                            print(f"The British government has accepted our entry into the {britain.alliance}.\n")
                            time.sleep(3)

                        else:
                            print("The British government has accepted our proposal of creating an alliance.\n")
                            time.sleep(3)
                            alliance = input("What would you like your alliance to be called?: ")
                            britain.alliance = alliance
                            us.alliance = alliance

                    elif chance % 3 == 0:
                        """36.3% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """18.1% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)
                        not_finished = False

                    elif chance % 9 == 5:
                        """9.09% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)
                        not_finished = False

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

            elif globe.tension < 50 and us.british_relations < 50:

                if choice == 1:
                    chance = random.randrange(0, 30)
                    if chance % 3 == 2:
                        """33% chance that Italian government accepts proposal"""
                        print("The British government has agreed to improve relations over a period of 50 days.\n")
                        time.sleep(3)

                        us.improve_british_relations = us.date + timedelta(days=50)

                    elif chance % 2 == 0:
                        """50% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """16.6% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 7 == 2:
                        """13.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 2:
                    chance = random.randrange(0, 30)
                    if chance % 3 == 2:
                        """33% chance that Italian government accepts proposal"""
                        print("The British government has agreed to improve trade over a period of 30 days.\n")
                        time.sleep(3)

                        us.improve_britain_trade = us.date + timedelta(days=30)

                    elif chance % 2 == 0:
                        """50% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """16.6% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 7 == 2:
                        """13.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 3:
                    chance = random.randrange(0, 30)
                    if chance % 3 == 0 and not us.british_embassy:
                        """33.3% chance that Italian government accepts proposal"""
                        print("The British government has approved of our building of an embassy in London\n")
                        time.sleep(3)
                        us.british_embassy = True

                    elif chance % 2 == 0:
                        """50% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """16.6% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 7 == 2:
                        """13.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 4:
                    chance = random.randrange(0, 30)
                    if chance % 3 == 0:
                        """33.3% chance that Italian government accepts proposal"""
                        print("The British government has accepted our guarantee of independence.\n")
                        time.sleep(3)

                    elif chance % 2 == 0:
                        """50% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """16.6% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 7 == 2:
                        """13.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 5:
                    chance = random.randrange(0, 30)
                    if chance % 3 == 0:
                        """33.3% chance that Italian government accepts proposal"""
                        if britain.alliance:
                            print(f"The British government has accepted our entry into the {britain.alliance}.\n")
                            time.sleep(3)

                        else:
                            print("The British government has accepted our proposal of creating an alliance.\n")
                            time.sleep(3)
                            alliance = input("What would you like your alliance to be called?: ")
                            britain.alliance = alliance
                            us.alliance = alliance

                    elif chance % 2 == 0:
                        """50% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 6 == 2:
                        """16.6% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 7 == 2:
                        """13.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

            elif globe.tension > 50 and us.british_relations < 50:
                if choice == 1:
                    chance = random.randrange(0, 60)
                    if chance % 6 == 2:
                        """16.6% chance that Italian government accepts proposal"""
                        print("The British government has agreed to improve relations over a period of 50 days.\n")
                        time.sleep(3)

                        us.improve_british_relations = us.date + timedelta(days=50)

                    elif chance % 5 == 3:
                        """20% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 4 == 1:
                        """25% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 2:
                    chance = random.randrange(0, 60)
                    if chance % 6 == 2:
                        """16.6% chance that Italian government accepts proposal"""
                        print("The British government has agreed to improve trade over a period of 30 days.\n")
                        time.sleep(3)

                        us.improve_british_trade = us.date + timedelta(days=30)

                    elif chance % 5 == 3:
                        """20% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 4 == 1:
                        """25% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 3:
                    chance = random.randrange(0, 60)
                    if chance % 6 == 2 and not us.britain.embassy:
                        """16.6% chance that Italian government accepts proposal"""
                        print("The British government has approved of our building of an embassy in London\n")
                        time.sleep(3)
                        us.british_embassy = True

                    elif chance % 5 == 3:
                        """20% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 4 == 1:
                        """25% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 4:
                    chance = random.randrange(0, 60)
                    if chance % 6 == 2:
                        """16.6% chance that Italian government accepts proposal"""
                        print("The British government has accepted our guarantee of independence.\n")
                        time.sleep(3)

                    elif chance % 5 == 3:
                        """20% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 4 == 1:
                        """25% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 5:
                    chance = random.randrange(0, 60)
                    if chance % 6 == 2:
                        """16.6% chance that Italian government accepts proposal"""
                        if britain.alliance:
                            print(f"The British government has accepted our entry into the {britain.alliance}.\n")
                            time.sleep(3)
                            us.alliance = britain.alliance

                        else:
                            print("The Italian government has accepted our proposal of creating an alliance.\n")
                            time.sleep(3)
                            alliance = input("What would you like your alliance to be called?: ")
                            britain.alliance = alliance
                            us.alliance = alliance

                    elif chance % 5 == 3:
                        """20% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 4 == 1:
                        """25% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

            elif globe.tension > 50 and us.british_relations > 50:
                if choice == 1:
                    chance = random.randrange(0, 45)
                    if chance % 4 == 2:
                        """24.4% chance that Italian government accepts proposal"""
                        print("The British government has agreed to improve relations over a period of 50 days.\n")
                        time.sleep(3)

                        us.improve_british_relations = us.date + timedelta(days=50)

                    elif chance % 2 == 0:
                        """51.1% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 2 == 1:
                        """48.89% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 2:
                    chance = random.randrange(0, 45)
                    if chance % 4 == 2:
                        """24.4% chance that Italian government accepts proposal"""
                        print("The British government has agreed to improve trade over a period of 30 days.\n")
                        time.sleep(3)
                        us.improve_british_trade = us.date + timedelta(days=30)

                    elif chance % 2 == 0:
                        """51.1% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 2 == 1:
                        """48.89% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 3:
                    chance = random.randrange(0, 45)
                    if chance % 4 == 2 and not us.british.embassy:
                        """24.4% chance that Italian government accepts proposal"""
                        print("The British government has approved of our building of an embassy in London\n")
                        time.sleep(3)
                        us.british_embassy = True

                    elif chance % 2 == 0:
                        """51.1% chance that British government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 2 == 1:
                        """48.89% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 4:
                    chance = random.randrange(0, 45)
                    if chance % 4 == 2:
                        """24.4% chance that Italian government accepts proposal"""
                        print("The British government has accepted our guarantee of independence.\n")
                        time.sleep(3)

                    elif chance % 2 == 0:
                        """51.1% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 2 == 1:
                        """48.89% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

                elif choice == 5:
                    chance = random.randrange(0, 45)
                    if chance % 4 == 2:
                        """24.4% chance that Italian government accepts proposal"""
                        if britain.alliance:
                            print(f"The British government has accepted our entry into the {britain.alliance}.\n")
                            time.sleep(3)
                            us.alliance = britain.alliance

                        else:
                            print("The British government has accepted our proposal of creating an alliance.\n")
                            time.sleep(3)
                            alliance = input("What would you like your alliance to be called?: ")
                            britain.alliance = alliance
                            us.alliance = alliance

                    elif chance % 2 == 0:
                        """51.1% chance that Italian government doesn't accept proposal, but may accept another proposal"""
                        alternate_options(us, britain, globe)

                    elif chance % 2 == 1:
                        """48.89% chance that Italy kicks diplomats out of Italian Parliament"""
                        print("Our diplomats have been kicked out of the British Parliament.\n")
                        globe.tension += 1.5
                        time.sleep(3)

                    elif chance % 3 == 1:
                        """33.3% chance that Italy kills your diplomats"""
                        kill_diplomats(us, globe)

                    else:
                        print("Your proposal died in the midst of Geopolitics.\n")
                        time.sleep(3)

        elif choice.lower() == "quit":
            not_finished = False

def ai_game(britain, globe):
    while britain.current_pop > 500000:
        # establishment of check upon game status
        population_change(britain)
        politics_change(britain)
        economic_decisions(britain)
        improvements(britain)
        if britain.date > britain.check_stats:
            daily_decisions(britain)
        britain.date += timedelta(days=1)
        break

    if britain.current_pop < 500000:
        print("britain has collapsed")
class BritainAI:
    def __init__(self, time):
        self.name = "Britain"
        """time variables"""
        self.date = datetime(int(time), 1, 1)
        self.past_year = self.date.year
        self.political_census = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        """Variable for improving stability of nation over given time"""
        self.improve_stability = self.date
        """Ditto to improve stability"""
        self.improve_happiness = self.date
        """variable for repaying debt over given time"""
        self.debt_repayment = self.date
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
