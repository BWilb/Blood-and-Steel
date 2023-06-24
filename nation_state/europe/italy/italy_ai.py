"""Political variables and dictionaries"""
import random
from datetime import datetime, timedelta
import time

prime_ministers = {
    "1910": "Luigi Luzzatti",
    "1914": "Antonio Salandra",
    "1918": "Vittorio Emanuele Orlando",
    "1932": "Benito Mussolini",
    "1936": "Benito Mussolini",
    "1939": "Benito Mussolini"
}

monarchs = {
    "1910": "Victor Emmanuel III",
    "1914": "Victor Emmanuel III",
    "1918": "Victor Emmanuel III",
    "1932": "Victor Emmanuel III",
    "1936": "Victor Emmanuel III",
    "1939": "Victor Emmanuel III"
}
"""Economic variables and dictionaries"""
gdp = {
    "1910": 7243560000,
    "1914": 7294052632,
    "1918": 7318292632,
    "1932": 12072684211,
    "1936": 15920315789,
    "1939": 19837894737
}
tax_rate = {
    "1910": 18.00,
    "1914": 18.00,
    "1918": 36.00,
    "1932": 10.00,
    "1936": 8.00,
    "1939": 12.00
}

business_cycle = ["recovery", "expansion", "recession", "depression"]

"""Population variables and dictionaries"""
population = {
    "1910": 36100000,
    "1914": 36500000,
    "1918": 36800000,
    "1932": 41000000,
    "1936": 42400000,
    "1939": 43500000
}
"""Military variables and dictionaries"""

army_size = {
    "1910": 252169,
    "1914": 497219,
    "1918": 2700000,
    "1932": 354169,
    "1936": 381336,
    "1939": 645000
}
"""Stability and happiness functions"""
def stability_happiness(italy):
    chance = random.randrange(0, 2)

    if chance == 0:
        increase_happiness = round(random.uniform(0.001, 0.09), 3)
        increase_stability = round(random.uniform(0.001, 0.009), 3)

        if (italy.happiness + increase_happiness) < 98:
            italy.happiness += increase_happiness
        if (italy.stability + increase_stability) < 98:
            italy.stability += increase_stability

    elif chance == 1:
        decrease_happiness = round(random.uniform(0.001, 0.09), 3)
        decrease_stability = round(random.uniform(0.001, 0.009), 3)

        if (italy.happiness - decrease_happiness) > 5:
            italy.happiness -= decrease_happiness
        if (italy.stability - decrease_stability) > 5:
            italy.stability -= decrease_stability
def retire_soldiers(italy):
    """function for retiring old, wounded, or stupid soldiers"""
    italy.army -= random.randrange(2, 100)
def increase_army(italy):
    increase = round(italy.conscripts * round(random.uniform(0.0001, 0.0005), 6), 0)
    italy.army += increase
    italy.conscripts -= increase
def increase_conscripts(italy):
    if italy.conscription_status == "volunteer":
        if italy.date == italy.conscript_census:
            """Amount of population that is eligible under volunteering draft"""
            italy.conscripts = round(italy.current_pop * round(random.uniform(0.0001, 0.0009), 5), 0)
            italy.conscript_census = italy.date + timedelta(days=15)

    elif italy.conscription_status == "limited":
        if italy.date == italy.conscript_census:
            """Amount of population that is eligible under limited draft"""
            italy.conscripts = round(italy.current_pop * round(random.uniform(0.0001, 0.002), 5), 0)
            italy.conscript_census = italy.date + timedelta(days=20)

    elif italy.conscript_status == "extensive":
        if italy.date == italy.conscript_census:
            """Amount of population that is eligible under extensive draft"""
            italy.conscripts = round(italy.current_pop * round(random.uniform(0.0001, 0.005), 5), 0)
            italy.conscript_census = italy.date + timedelta(days=25)

    elif italy.conscript_status == "required":
        if italy.date == italy.conscript_census:
            """Amount of population that is eligible under required drafting"""
            italy.conscripts = round(italy.current_pop * round(random.uniform(0.0001, 0.02), 5), 0)
            italy.conscript_census = italy.date + timedelta(days=30)
def military_functions(italy):
    increase_conscripts(italy)
    increase_army(italy)
    retire_soldiers(italy)

"""population functions"""
def population_change(italy):
    if italy.past_year < italy.date.year:
        italy.population_change = (italy.current_pop - italy.past_pop / (
                    (italy.current_pop + italy.current_pop) / 2)) * 100
        italy.past_pop = italy.current_pop

        if italy.population_change <= 2.1:
            """possible implementation of viagra with somewhat moderate growth, due to low population"""

            choice = random.randrange(0, 2)
            if choice == 1:
                italy.viagra_subsidy = True

                if italy.condom_subsidy:
                    """Checking to see if condom subsidies exist"""
                    italy.condom_subsidy = False

        elif italy.population_change >= 12.5:
            choice = random.randrange(0, 2)
            if choice == 0:
                italy.condom_subsidy = True

                if italy.viagra_subsidy:
                    italy.viagra_subsidy = False
    else:
        if italy.viagra_subsidy:
            births = random.randrange(50, 600)
            italy.current_pop += births

            for i in range(0, births):
                """Looping through births to assign to political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party += 1

                elif chance == 1:
                    italy.italian_liberal_party += 1

                elif chance == 2:
                    italy.italian_peoples_party += 1

                elif chance == 3:
                    italy.italian_republican_party += 1

            deaths = random.randrange(25, 150)
            italy.current_pop -= deaths

            for i in range(0, births):
                """Looping through deaths to un-assign political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party -= 1

                elif chance == 1:
                    italy.italian_liberal_party -= 1

                elif chance == 2:
                    italy.italian_peoples_party -= 1

                elif chance == 3:
                    italy.italian_republican_party -= 1

        elif italy.condom_subsidy:
            births = random.randrange(50, 200)
            italy.current_pop += births

            for i in range(0, births):
                """Looping through births to assign to political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party += 1

                elif chance == 1:
                    italy.italian_liberal_party += 1

                elif chance == 2:
                    italy.italian_peoples_party += 1

                elif chance == 3:
                    italy.italian_republican_party += 1

            deaths = random.randrange(25, 150)
            italy.current_pop -= deaths

            for i in range(0, deaths):
                """Looping through deaths to un-assign political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party -= 1

                elif chance == 1:
                    italy.italian_liberal_party -= 1

                elif chance == 2:
                    italy.italian_peoples_party -= 1

                elif chance == 3:
                    italy.italian_republican_party -= 1

        else:
            births = random.randrange(50, 300)
            italy.current_pop += births
            for i in range(0, births):
                """Looping through births to assign to political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party += 1

                elif chance == 1:
                    italy.italian_liberal_party += 1

                elif chance == 2:
                    italy.italian_peoples_party += 1

                elif chance == 3:
                    italy.italian_republican_party += 1

            deaths = random.randrange(25, 150)
            italy.current_pop -= deaths

            for i in range(0, deaths):
                """Looping through deaths to un-assign political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party -= 1

                elif chance == 1:
                    italy.italian_liberal_party -= 1

                elif chance == 2:
                    italy.italian_peoples_party -= 1

                elif chance == 3:
                    italy.italian_republican_party -= 1

"""Economic Functions"""
def economic_state(italy):
    if italy.date >= italy.economic_change_date:
        """Comparing current date to when Italy's economic state could change"""
        chance = random.randrange(0, 2000)
        if chance % 37 == 10:
            """Making potential for economic disaster really low"""
            if italy.current_gdp < italy.past_gdp:
                """Comparison of current gdp to past gdp"""
                if italy.economic_state == "expansion" or italy.economic_state == "recovery":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "recession":
                            print("The Italian economy has entered into a recession after 6 months of decayed growth.\n")
                            time.sleep(3)
                            italy.economic_state = business_cycle[i]
                            italy.economic_change_date = italy.date + timedelta(days=240)
                            economic_stimulus(italy)
                            """increasing amount of time to check up on GDP
                            Time is average amount(6 months cycle)
                            """
                elif italy.economic_state == "recession":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "depression":
                            print("The Italian Economy has entered into a depression\n")
                            time.sleep(3)
                            italy.economic_state = business_cycle[i]
                            italy.economic_change_date = italy.date + timedelta(days=270)
                            economic_stimulus(italy)
                            """
                            Since it takes awhile to escape a depression, amount of time on change date is increased
                            """

        if chance % 40 == 37:
            """making potential for economic expansion or recovery very low"""
            if italy.economic_state == "depression" or italy.economic_state == "recession":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recovery":
                        print("The Italian economy has entered into a recovery period\n")
                        time.sleep(3)
                        italy.economic_state = business_cycle[i]
                        italy.economic_change_date = italy.date + timedelta(days=240)
                        """increasing amount of time to check up on GDP
                        Time is average amount(6 months cycle)
                        """

            elif italy.economic_state == "recovery":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("The Italian economy has begun to rapidly expand\n")
                        time.sleep(3)
                        italy.economic_state = business_cycle[i]
                        italy.economic_change_date = italy.date + timedelta(days=270)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """
def economic_stimulus(italy):
    italy.economic_stimulus = True

    if italy.economic_state == "recession":
        choice = random.randrange(0, 2)

        if choice == 1:
            valid_choice = False

            while valid_choice:

                tax_hike = round(random.uniform(1, 10), 2)
                if tax_hike <= 10 and tax_hike >= 1.0:
                    italy.tax_rate += tax_hike
                    print(f"The Italian government has decide to raise their taxes by {tax_hike}.\n")
                    time.sleep(3)
                    decrease = round(random.uniform(0.25, 1.45), 2)

                    if (italy.happiness - decrease) < 5:
                        italy.happiness -= decrease

                    valid_choice = True

    elif italy.economic_state == "depression":
        tax_hike = round(random.uniform(0.5, 10), 2)
        if (italy.tax_rate + tax_hike) <= 68.00:
            if italy.date.year <= 1922 or italy.date.year >= 1946:
                print(f"The Italian Parliament has enacted a tax hike of {tax_hike}%\n")

            if italy.date.year > 1922 and italy.date.year < 1946:
                print(f"Il Duce of Italy has enacted a tax hike of {tax_hike}%\n")
            time.sleep(3)
def recession(italy):
    """Recession simulation based upon stimulus and tax rate"""
    if italy.economic_stimulus:
        """Recession with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:

            italy.consumer_spending = -round(random.uniform(100, 1000), 2)
            italy.investment = -round(random.uniform(100, 2000), 2)
            italy.government_spending = round(random.uniform(1000, 3000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.01, 0.09), 2), 2))

            italy.exports = round(random.uniform(120000, 750000), 2)
            italy.imports = round(random.uniform(120000, 1100000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 4000), 2)
            italy.investment = -round(random.uniform(1000, 3000), 2)
            italy.government_spending = round(random.uniform(1000, 9000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.01, 0.09), 2), 2))

            italy.exports = round(random.uniform(120000, 560000), 2)
            italy.imports = round(random.uniform(120000, 1100000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
    else:
        """Recession without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 2500), 2)
            italy.investment = -round(random.uniform(1000, 4000), 2)
            italy.government_spending = round(random.uniform(1000, 5000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.01, 0.09), 2), 2))

            italy.exports = round(random.uniform(120000, 560000), 2)
            italy.imports = round(random.uniform(120000, 1100000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 6000), 2)
            italy.investment = -round(random.uniform(1000, 6000), 2)
            italy.government_spending = round(random.uniform(1000, 12000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.01, 0.09), 2), 2))

            italy.exports = round(random.uniform(120000, 460000), 2)
            italy.imports = round(random.uniform(120000, 1100000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))

def depression(italy):
    """Recession simulation based upon stimulus and tax rate"""
    if italy.economic_stimulus:
        """Depression with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:

            italy.consumer_spending = -round(random.uniform(1000, 3000), 2)
            italy.investment = -round(random.uniform(1000, 4000), 2)
            italy.government_spending = round(random.uniform(1000, 16000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.15), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))
            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment)

            italy.exports = round(random.uniform(120000, 690000), 2)
            italy.imports = round(random.uniform(120000, 1400000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 6000), 2)
            italy.investment = -round(random.uniform(1000, 8000), 2)
            italy.government_spending = round(random.uniform(1000, 19000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.11), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))
            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment)


            italy.exports = round(random.uniform(120000, 590000), 2)
            italy.imports = round(random.uniform(120000, 1400000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
    else:
        """Depression without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 2500), 2)
            italy.investment = -round(random.uniform(1000, 4000), 2)
            italy.government_spending = round(random.uniform(1000, 25000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.11), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))
            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment)

            italy.exports = round(random.uniform(120000, 750000), 2)
            italy.imports = round(random.uniform(120000, 1400000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 10000), 2)
            italy.investment = -round(random.uniform(1000, 16000), 2)
            italy.government_spending = round(random.uniform(1000, 35000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.21), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))

            italy.exports = round(random.uniform(120000, 590000), 2)
            italy.imports = round(random.uniform(120000, 1400000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
def recovery(italy):
    """Recession simulation based upon stimulus and tax rate"""
    if italy.economic_stimulus:
        """Depression with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:

            italy.consumer_spending = round(random.uniform(100, 2000), 2)
            italy.investment = round(random.uniform(100, 2500), 2)
            italy.government_spending = round(random.uniform(1000, 16000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.001, 0.05), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.055), 2), 2))

            italy.exports = round(random.uniform(120000, 690000), 2)
            italy.imports = round(random.uniform(120000, 660000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))

        elif italy.tax_rate > 25.00:
            italy.consumer_spending = round(random.uniform(100, 1000), 2)
            italy.investment = round(random.uniform(1000, 2000), 2)
            italy.government_spending = round(random.uniform(1000, 19000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.001, 0.05), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.05), 2), 2))

            italy.exports = round(random.uniform(120000, 590000), 2)
            italy.imports = round(random.uniform(120000, 560000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
    else:
        """Recovery without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:
            italy.consumer_spending = round(random.uniform(100, 1500), 2)
            italy.investment = round(random.uniform(100, 2000), 2)
            italy.government_spending = round(random.uniform(1000, 25000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.0011, 0.05), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.05), 2), 2))

            italy.exports = round(random.uniform(120000, 590000), 2)
            italy.imports = round(random.uniform(120000, 560000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = round(random.uniform(100, 1000), 2)
            italy.investment = round(random.uniform(100, 1500), 2)
            italy.government_spending = round(random.uniform(1000, 35000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.001, 0.05), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.05), 2), 2))

            italy.exports = round(random.uniform(120000, 450000), 2)
            italy.imports = round(random.uniform(120000, 420000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
def expansion(italy):
    """Recession simulation based upon stimulus and tax rate"""
    if italy.economic_stimulus:
        """Expansion with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:

            italy.consumer_spending = round(random.uniform(100, 4000), 2)
            italy.investment = round(random.uniform(100, 6500), 2)
            italy.government_spending = round(random.uniform(1000, 20000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.01, 0.095), 2), 2))

            italy.exports = round(random.uniform(120000, 1000000), 2)
            italy.imports = round(random.uniform(120000, 750000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))

        elif italy.tax_rate > 25.00:
            italy.consumer_spending = round(random.uniform(100, 2500), 2)
            italy.investment = round(random.uniform(100, 4500), 2)
            italy.government_spending = round(random.uniform(1000, 30000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.01, 0.095), 2), 2))

            italy.exports = round(random.uniform(120000, 750000), 2)
            italy.imports = round(random.uniform(120000, 650000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
    else:
        """Expansion without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:
            italy.consumer_spending = round(random.uniform(100, 6000), 2)
            italy.investment = round(random.uniform(100, 8000), 2)
            italy.government_spending = round(random.uniform(1000, 30000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.11), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.01, 0.095), 2), 2))

            italy.exports = round(random.uniform(120000, 750000), 2)
            italy.imports = round(random.uniform(120000, 650000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = round(random.uniform(100, 4500), 2)
            italy.investment = round(random.uniform(100, 3500), 2)
            italy.government_spending = round(random.uniform(1000, 55000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.21), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))

            italy.exports = round(random.uniform(120000, 560000), 2)
            italy.imports = round(random.uniform(120000, 340000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
def gdp_changes(italy):
    if italy.economic_state == "recovery":
        recovery(italy)
    elif italy.economic_state == "expansion":
        expansion(italy)
    elif italy.economic_state == "recession":
        recession(italy)
    elif italy.economic_state == "depression":
        depression(italy)
def economic_decisions(italy):
    if italy.past_year < italy.date.year:

        italy.economic_growth = (italy.current_gdp - italy.past_gdp / ((italy.past_gdp + italy.current_gdp) / 2)) * 100
        """Calculation of yearly economic growth"""
        if italy.economic_growth <= 1.5:
            if not italy.economic_stimulus:
                choice = random.randrange(0, 2)
                if choice == 0:
                    economic_stimulus(italy)

        elif italy.economic_growth >= 10.5:
            if italy.economic_stimulus:
                italy.economic_stimulus = False
    else:
        gdp_changes(italy)
        economic_state(italy)

"""international functions"""
def us_relations(us, italy):
    # function isn't called from AI file, is called from new_usa file
    done = False
    while done:
        choices = ["improve relations", "establish an alliance", "increase trade", "declare war", "establish an embassy"]
        # potential choices for user to select
        for i in choices:
            print(i, end="\n")

"""stats functions"""
def social_stats(italy):
    time.sleep(3)
    if italy.happiness < 35.45 and not italy.improve_happiness:
        choice = random.randrange(0, 2)
        if choice == 0:
            italy.improve_happiness = italy.date + timedelta(days=30)
            print("The Italian government decided their relations with the Italian people")

def political_stats(italy):
    if italy.stability < 45.45 and not italy.improve_stability:
        choice = random.randrange(0, 2)
        if choice == 0:
            italy.improve_stability = italy.date + timedelta(days=30)
            print("The Italian government decided to improve Italy's political stability for a period of 30 days")
    time.sleep(3)

def economic_stats(italy):
    if italy.national_debt > 100000 and not italy.debt_repayment:
        choice = random.randrange(0, 2)
        if choice == 0:
            italy.debt_repayment = italy.date + timedelta(days=120)
            print("The Italian government has decided to repay part of their national debt over a period of 120 days")
            time.sleep(3)
def daily_decisions(italy):
    political_stats(italy)
    economic_stats(italy)
    social_stats(italy)
    italy.check_stats = italy.date + timedelta(days=3)

def social_events(italy):
    if italy.date.year > 1945 and italy.date == datetime(italy.year, 4, 25):
        print("Italy is celebrating freedom from Fascism day\n")
        italy.happiness += round(random.uniform(0.25, 1.25), 2)
        time.sleep(3)
def economic_events(italy):
    if italy.date > datetime(1922, 10, 24) and italy.date < datetime(1929, 10, 24):
        increment = round(random.uniform(1000, 10000), 2)
        italy.curent_gdp += increment
        italy.national_debt += round(increment * round(random.uniform(0.001, 0.009), 2), 2)

    if italy.date == datetime(1929, 10, 24):
        print("The Italian economy has fallen into a Depression.\n"
              "It is being reported that their economy has been slashed by a factor of 5\n"
              )
        time.sleep(3)
        italy.current_gdp /= 5
        italy.government_spending = round(random.uniform(100000, 5000000), 2)
        italy.national_debt = round(italy.government_spending * round(random.uniform(0.001, 0.05), 2), 2)
def political_events(italy):
    if italy.date == datetime(1922, 10, 27):
        print(f"Benito Mussolini has stormed Rome, forcing {italy.monarch} to elect him as PM.\n")
        time.sleep(3)
        italy.pm = "Benito Mussolini"

    elif italy.date == datetime(1940, 10, 28):
        print("Italy has entered world war 2 alongside Hitler, bonding them together.\n")
        italy.alliance = "Axis"
        time.sleep(3)
def events(italy):
    political_events(italy)
    economic_events(italy)
    social_events(italy)
def ai_game(italy, globe):
    while italy.current_pop > 150000:
        # incrementing of time
        stability_happiness(italy)
        events(italy)
        population_change(italy)
        economic_decisions(italy)
        military_functions(italy)
        if italy.date > italy.check_stats:
            daily_decisions(italy)
        italy.date += timedelta(days=1)
        break
class Italy:
    def __init__(self, year):
        self.name = "Italy"
        """Time variables"""
        self.date = datetime(int(year), 1, 1)
        self.past_year = self.date.year
        """Variable for improving stability of nation over given time"""
        self.improve_stability = None
        """Ditto to improve stability"""
        self.improve_happiness = None
        """variable for repaying debt over given time"""
        self.debt_repayment = None
        self.check_stats = self.date + timedelta(days=3)
        """Population variables"""
        self.current_pop = population[year]
        self.population_change = 0
        self.past_pop = self.current_pop
        self.happiness = 95.56
        # population controller if birth rate gets out of hand
        self.condom_subsidy = False
        # population controller if birth rate flops
        self.viagra_subsidy = False
        """Political variables"""
        self.pm = prime_ministers[year]
        self.monarch = monarchs[year]
        self.stability = 90.00
        self.anti_establishment = 0
        # political parties based upon time frame
        if self.date < datetime(1922, 10, 27):
            self.italian_socialist_party = round(self.current_pop * round(random.uniform(0.1, 0.25), 2), 0)

            self.italian_republican_party = round((self.current_pop - self.italian_socialist_party) *
                                                  round(random.uniform(0.1, 0.25), 2), 0)


            self.italian_peoples_party = round((self.current_pop - self.italian_socialist_party -
                                                self.italian_republican_party) *
                                                round(random.uniform(0.1, 0.25), 2), 0)

            self.italian_liberal_party = round((self.current_pop - self.italian_socialist_party -
                                                self.italian_republican_party - self.italian_peoples_party))
        """Economic_variables"""
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.economic_state = "recovery"
        self.tax_rate = tax_rate[year]
        self.economic_stimulus = False
        self.economic_growth = 0
        self.economic_change_date = self.date + timedelta(days=60)
        # gdp components
        self.consumer_spending = 0
        self.investment = 0
        self.exports = 0
        self.imports = 0
        # political economic variables
        self.government_spending = 0
        self.national_debt = 0
        """international variables"""
        self.us_relations = 45.56
        """military variables"""
        self.army = army_size[year]
        self.conscripts = round(self.current_pop * round(random.uniform(0.001, 0.009), 5), 0)
        self.conscription_status = "limited"
        self.conscript_census = self.date + timedelta(days=15)
        self.war_deaths = 0