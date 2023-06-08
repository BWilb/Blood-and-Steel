import random
import time
from datetime import datetime, timedelta

dictators = {
    "1910": "Nicolaus II",
    "1914": "Nicolaus II",
    "1918": "Vladimir Lenin",
    "1932": "Joseph Stalin",
    "1936": "Joseph Stalin",
    "1939": "Joseph Stalin"
}

population = {
    "1910": 126200000,
    "1914": 130000000,
    "1918": 136800000,
    "1932": 126000000,
    "1936": 104900000,
    "1939": 109397463
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

business_cycle = ["recession", "recovery", "expansion", "depression"]
"""Political Functions"""


def political_change(russia):
    """function for redrawing political lines"""
    if russia.date > russia.political_census:
        """If date exceeds census"""
        chance = random.randrange(0, 2)
        if chance == 0:
            loss = round(russia.pe * round(random.uniform(0.001, 0.009), 5), 0)
            russia.pe -= loss
            russia.ae += loss
        else:
            loss = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
            russia.ae -= loss
            russia.pe += loss

    if round((russia.ae / russia.current_pop) * 100, 2) > 10.00:
        """Checking if anti-establishment parties have grown to powerful/influential"""
        if russia.date < datetime(1917, 3, 1):
            choice = input("Anti-Tsarist parties are flourishing, should we do something about it?(y or n): ")

            if choice.lower() == "yes" or choice.lower() == "y":
                options = random.randrange(0, 3)
                # choice of death, internment in Siberia, or deportation
                if options == 0:
                    """if options = 0, a small amount of people are sent to siberia"""
                    people = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
                    print(f"{people} anti-tsarists were sent to Siberia\n")
                    time.sleep(3)
                    russia.siberians += people

                elif options == 1:
                    """if options = 1, a small amount of people are killed"""
                    people = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
                    print(f"{people} anti-tsarists were killed for treason.\n")
                    time.sleep(3)
                    russia.deaths += people
                    russia.current_pop -= people
                    russia.ae -= people

                elif options == 2:
                    """if options = 2, a small amount of people are deported"""
                    people = round(russia.ae * round(random.uniform(0.001, 0.02), 5), 0)
                    print(f"{people} anti-tsarists were deported.\n")
                    time.sleep(3)
                    russia.current_pop -= people
                    russia.deportees += people


"""population functions"""


def population_change(russia):
    if russia.past_year < russia.date.year:
        russia.pop_change = (russia.current_pop - russia.past_pop / (
                (russia.current_pop + russia.current_pop) / 2)) * 100

        russia.past_pop = russia.current_pop

        if russia.pop_change <= 5.50:
            """possible implementation of viagra with somewhat moderate growth, due to low population"""
            print(f"Your population growth for {russia.past_year} was {russia.population_change}%.\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                russia.viagra_subsidy = True

                if russia.condom_subsidy:
                    """Checking to see if condom subsidies exist"""
                    russia.condom_subsidy = False

        elif russia.pop_change >= 15.50:
            print(f"Your population growth for {russia.past_year} was {russia.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == 'y' or choice.lower() == "yes":
                russia.condom_subsidy = True

                if russia.viagra_subsidy:
                    russia.viagra_subsidy = False

        else:
            if russia.date < datetime(1914, 7, 28):
                births = random.randrange(100, 1000)
                deaths = random.randrange(100, 950)

                for i in range(0, births):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe += 1
                    else:
                        russia.ae += 1

                russia.current_pop += births
                russia.births += births

                russia.current_pop -= deaths
                russia.deaths += deaths

                for i in range(0, deaths):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe -= 1
                    else:
                        russia.ae -= 1

            elif russia.date > datetime(1914, 7, 28) and russia.date < datetime(1923, 6, 16):
                births = random.randrange(100, 800)
                deaths = random.randrange(100, 750)

                russia.current_pop += births
                russia.births += births

                for i in range(0, births):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe += 1
                    else:
                        russia.ae += 1

                russia.current_pop -= deaths
                russia.deaths += deaths
                for i in range(0, deaths):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe -= 1
                    else:
                        russia.ae -= 1

            elif russia.date > datetime(1923, 6, 16) and russia.date < datetime(1941, 6, 22):
                births = random.randrange(100, 500)
                deaths = random.randrange(100, 450)

                russia.current_pop += births
                russia.births += births

                for i in range(0, births):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe += 1
                    else:
                        russia.ae += 1

                russia.current_pop -= deaths
                russia.deaths += deaths

                for i in range(0, deaths):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe -= 1
                    else:
                        russia.ae -= 1

            elif russia.date > datetime(1941, 6, 22) and russia.date < datetime(1945, 5, 8):
                births = random.randrange(100, 1300)
                deaths = random.randrange(100, 1250)

                russia.current_pop += births
                russia.births += births

                for i in range(0, births):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe += 1
                    else:
                        russia.ae += 1

                russia.current_pop -= deaths
                russia.deaths += deaths

                for i in range(0, deaths):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe -= 1
                    else:
                        russia.ae -= 1

            elif russia.date > datetime(1945, 5, 8):
                births = random.randrange(100, 600)
                deaths = random.randrange(100, 550)

                russia.current_pop += births
                russia.births += births

                for i in range(0, births):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe += 1
                    else:
                        russia.ae += 1

                russia.current_pop -= deaths
                russia.deaths += deaths

                for i in range(0, deaths):
                    chance = random.randrange(0, 2)
                    if chance == 0:
                        russia.pe -= 1
                    else:
                        russia.ae -= 1


def recession(russia):
    """changes based upon whether an economic stimulus is in place and what year plan is in place
    extremity of losses or gains, based upon stimulus and year plans
    """
    if russia.economic_stimulus:
        if russia.year_plans == 0:

            russia.consumer_spending = -round(random.uniform(100, 90000), 2)
            russia.investment = -round(random.uniform(100, 500000), 2)
            russia.government_spending = round(random.uniform(1000, 500000), 2)

            russia.exports = round(random.uniform(10000, 400000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = -round(random.uniform(100, 80000), 2)
            russia.investment = -round(random.uniform(100, 350000), 2)
            russia.government_spending = round(random.uniform(1000, 600000), 2)

            russia.exports = round(random.uniform(10000, 500000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = -round(random.uniform(100, 70000), 2)
            russia.investment = -round(random.uniform(100, 300000), 2)
            russia.government_spending = round(random.uniform(1000, 700000), 2)

            russia.exports = round(random.uniform(10000, 550000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = -round(random.uniform(100, 50000), 2)
            russia.investment = -round(random.uniform(100, 200000), 2)
            russia.government_spending = round(random.uniform(1000, 750000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 4:

            russia.consumer_spending = -round(random.uniform(100, 30000), 2)
            russia.investment = -round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(1000, 850000), 2)

            russia.exports = round(random.uniform(10000, 900000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

    else:
        if russia.year_plans == 0:

            russia.consumer_spending = -round(random.uniform(100, 70000), 2)
            russia.investment = -round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(1000, 750000), 2)

            russia.exports = round(random.uniform(10000, 550000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = -round(random.uniform(100, 60000), 2)
            russia.investment = -round(random.uniform(100, 90000), 2)
            russia.government_spending = round(random.uniform(1000, 850000), 2)

            russia.exports = round(random.uniform(10000, 600000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = -round(random.uniform(100, 50000), 2)
            russia.investment = -round(random.uniform(100, 190000), 2)
            russia.government_spending = round(random.uniform(1000, 900000), 2)

            russia.exports = round(random.uniform(10000, 650000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = -round(random.uniform(100, 40000), 2)
            russia.investment = -round(random.uniform(100, 90000), 2)
            russia.government_spending = round(random.uniform(1000, 950000), 2)

            russia.exports = round(random.uniform(10000, 700000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 4:

            russia.consumer_spending = -round(random.uniform(100, 30000), 2)
            russia.investment = -round(random.uniform(100, 80000), 2)
            russia.government_spending = round(random.uniform(1000, 1000000), 2)

            russia.exports = round(random.uniform(10000, 800000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)


def depression(russia):
    if russia.economic_stimulus:
        if russia.year_plans == 0:

            russia.consumer_spending = -round(random.uniform(100, 500000), 2)
            russia.investment = -round(random.uniform(100, 500000), 2)
            russia.government_spending = round(random.uniform(1000, 650000), 2)

            russia.exports = round(random.uniform(10000, 550000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = -round(random.uniform(100, 400000), 2)
            russia.investment = -round(random.uniform(100, 400000), 2)
            russia.government_spending = round(random.uniform(1000, 750000), 2)

            russia.exports = round(random.uniform(10000, 650000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = -round(random.uniform(100, 300000), 2)
            russia.investment = -round(random.uniform(100, 300000), 2)
            russia.government_spending = round(random.uniform(1000, 850000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = -round(random.uniform(100, 200000), 2)
            russia.investment = -round(random.uniform(100, 200000), 2)
            russia.government_spending = round(random.uniform(1000, 950000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 4:

            russia.consumer_spending = -round(random.uniform(100, 100000), 2)
            russia.investment = -round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(1000, 1050000), 2)

            russia.exports = round(random.uniform(10000, 900000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

    else:
        if russia.year_plans == 0:

            russia.consumer_spending = -round(random.uniform(100, 700000), 2)
            russia.investment = -round(random.uniform(100, 700000), 2)
            russia.government_spending = round(random.uniform(1000, 650000), 2)

            russia.exports = round(random.uniform(10000, 550000), 2)
            russia.imports = round(random.uniform(10000, 1050000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = -round(random.uniform(100, 600000), 2)
            russia.investment = -round(random.uniform(100, 600000), 2)
            russia.government_spending = round(random.uniform(1000, 750000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = -round(random.uniform(100, 500000), 2)
            russia.investment = -round(random.uniform(100, 500000), 2)
            russia.government_spending = round(random.uniform(1000, 850000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 850000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = -round(random.uniform(100, 400000), 2)
            russia.investment = -round(random.uniform(100, 400000), 2)
            russia.government_spending = round(random.uniform(1000, 950000), 2)

            russia.exports = round(random.uniform(10000, 950000), 2)
            russia.imports = round(random.uniform(10000, 750000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 4:
            russia.consumer_spending = -round(random.uniform(100, 300000), 2)
            russia.investment = -round(random.uniform(100, 300000), 2)
            russia.government_spending = round(random.uniform(1000, 1050000), 2)

            russia.exports = round(random.uniform(10000, 1100000), 2)
            russia.imports = round(random.uniform(10000, 650000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)


def recovery(russia):
    if russia.economic_stimulus:
        if russia.year_plans == 0:
            russia.consumer_spending = round(random.uniform(100, 10000), 2)
            russia.investment = round(random.uniform(100, 5000), 2)
            russia.government_spending = round(random.uniform(1000, 50000), 2)

            russia.exports = round(random.uniform(10000, 500000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)
        elif russia.year_plans == 1:
            russia.consumer_spending = round(random.uniform(100, 20000), 2)
            russia.investment = round(random.uniform(100, 10000), 2)
            russia.government_spending = round(random.uniform(1000, 60000), 2)

            russia.exports = round(random.uniform(10000, 650000), 2)
            russia.imports = round(random.uniform(10000, 750000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:
            russia.consumer_spending = round(random.uniform(100, 45000), 2)
            russia.investment = round(random.uniform(100, 20000), 2)
            russia.government_spending = round(random.uniform(1000, 55000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 450000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 3:
            russia.consumer_spending = round(random.uniform(100, 65000), 2)
            russia.investment = round(random.uniform(100, 30000), 2)
            russia.government_spending = round(random.uniform(1000, 225000), 2)

            russia.exports = round(random.uniform(10000, 1000000), 2)
            russia.imports = round(random.uniform(10000, 350000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 4:
            russia.consumer_spending = round(random.uniform(100, 80000), 2)
            russia.investment = round(random.uniform(100, 50000), 2)
            russia.government_spending = round(random.uniform(1000, 455000), 2)

            russia.exports = round(random.uniform(10000, 1200000), 2)
            russia.imports = round(random.uniform(10000, 325000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)
    else:
        if russia.year_plans == 0:
            russia.consumer_spending = round(random.uniform(100, 5000), 2)
            russia.investment = round(random.uniform(100, 2500), 2)
            russia.government_spending = round(random.uniform(1000, 350000), 2)

            russia.exports = round(random.uniform(10000, 450000), 2)
            russia.imports = round(random.uniform(10000, 1500000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)
        elif russia.year_plans == 1:
            russia.consumer_spending = round(random.uniform(100, 10000), 2)
            russia.investment = round(random.uniform(100, 5500), 2)
            russia.government_spending = round(random.uniform(1000, 500000), 2)

            russia.exports = round(random.uniform(10000, 650000), 2)
            russia.imports = round(random.uniform(10000, 1250000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:
            russia.consumer_spending = round(random.uniform(100, 35000), 2)
            russia.investment = round(random.uniform(100, 15000), 2)
            russia.government_spending = round(random.uniform(1000, 650000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 1000000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 3:
            russia.consumer_spending = round(random.uniform(100, 65000), 2)
            russia.investment = round(random.uniform(100, 30000), 2)
            russia.government_spending = round(random.uniform(1000, 755000), 2)

            russia.exports = round(random.uniform(10000, 1000000), 2)
            russia.imports = round(random.uniform(10000, 900000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 4:
            russia.consumer_spending = round(random.uniform(100, 80000), 2)
            russia.investment = round(random.uniform(100, 50000), 2)
            russia.government_spending = round(random.uniform(1000, 1000000), 2)

            russia.exports = round(random.uniform(10000, 1200000), 2)
            russia.imports = round(random.uniform(10000, 850000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)


def expansion(russia):
    if russia.economic_stimulus:
        if russia.year_plans == 0:

            russia.consumer_spending = round(random.uniform(100, 100000), 2)
            russia.investment = round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(100, 300000), 2)

            russia.exports = round(random.uniform(10000, 700000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = round(random.uniform(100, 200000), 2)
            russia.investment = round(random.uniform(100, 200000), 2)
            russia.government_spending = round(random.uniform(100, 400000), 2)

            russia.exports = round(random.uniform(10000, 800000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = round(random.uniform(100, 200000), 2)
            russia.investment = round(random.uniform(100, 200000), 2)
            russia.government_spending = round(random.uniform(1000, 450000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = round(random.uniform(100, 300000), 2)
            russia.investment = round(random.uniform(100, 300000), 2)
            russia.government_spending = round(random.uniform(1000, 500000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 4:
            russia.consumer_spending = round(random.uniform(100, 400000), 2)
            russia.investment = round(random.uniform(100, 400000), 2)
            russia.government_spending = round(random.uniform(1000, 600000), 2)

            russia.exports = round(random.uniform(10000, 1500000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

    else:
        if russia.year_plans == 0:

            russia.consumer_spending = round(random.uniform(100, 100000), 2)
            russia.investment = round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(100, 300000), 2)

            russia.exports = round(random.uniform(10000, 700000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = round(random.uniform(100, 150000), 2)
            russia.investment = round(random.uniform(100, 150000), 2)
            russia.government_spending = round(random.uniform(100, 325000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = round(random.uniform(100, 250000), 2)
            russia.investment = round(random.uniform(100, 250000), 2)
            russia.government_spending = round(random.uniform(100, 425000), 2)

            russia.exports = round(random.uniform(10000, 770000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 3:
            russia.consumer_spending = round(random.uniform(100, 150000), 2)
            russia.investment = round(random.uniform(100, 150000), 2)
            russia.government_spending = round(random.uniform(100, 625000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)
        elif russia.year_plans == 4:
            russia.consumer_spending = round(random.uniform(100, 250000), 2)
            russia.investment = round(random.uniform(100, 250000), 2)
            russia.government_spending = round(random.uniform(100, 725000), 2)

            russia.exports = round(random.uniform(10000, 1050000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)


def economic_stimulus(russia):
    pass


def gdp_changes(russia):
    if russia.economic_state == "recovery":
        recovery(russia)
    elif russia.economic_state == "recession":
        recession(russia)
    elif russia.economic_state == "depression":
        depression(russia)
    elif russia.economic_state == "expansion":
        expansion(russia)


def economic_state(russia):
    if russia.date >= russia.economic_change_date:
        if russia.date >= russia.economic_change_date:
            """Comparing current date to when Italy's economic state could change"""
            chance = random.randrange(0, 2000)
            if chance % 37 == 10:
                """Making potential for economic disaster really low"""
                if russia.current_gdp < russia.past_gdp:
                    """Comparison of current gdp to past gdp"""
                    if russia.economic_state == "expansion" or russia.economic_state == "recovery":
                        for i in range(0, len(business_cycle) - 1):
                            if business_cycle[i] == "recession":
                                print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                                time.sleep(3)
                                russia.economic_state = business_cycle[i]
                                russia.economic_change_date = russia.date + timedelta(days=240)
                                economic_stimulus(russia)
                                """increasing amount of time to check up on GDP
                                Time is average amount(6 months cycle)
                                """
                    elif russia.economic_state == "recession":
                        for i in range(0, len(business_cycle) - 1):
                            if business_cycle[i] == "depression":
                                print("Your economy has entered into a depression "
                                      "after exceeding 6 months of decayed growth.\n")
                                time.sleep(3)
                                russia.economic_state = business_cycle[i]
                                russia.economic_change_date = russia.date + timedelta(days=270)
                                economic_stimulus(russia)
                                """
                                Since it takes awhile to escape a depression, amount of time on change date is increased
                                """

            if chance % 40 == 37:
                """making potential for economic expansion or recovery very low"""
                if russia.economic_state == "depression" or russia.economic_state == "recession":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "recovery":
                            print("Your economy hs finally entered its recovery period\n")
                            time.sleep(3)
                            russia.economic_state = business_cycle[i]
                            russia.economic_change_date = russia.date + timedelta(days=240)
                            """increasing amount of time to check up on GDP
                            Time is average amount(6 months cycle)
                            """

                elif russia.economic_state == "recovery":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "expansion":
                            print("Your economy has blasted into an expansionary period. Woo!\n")
                            time.sleep(3)
                            russia.economic_state = business_cycle[i]
                            russia.economic_change_date = russia.date + timedelta(days=270)
                            """
                            Since it takes awhile to escape a depression, amount of time on change date is increased
                            """


def economic_decisions(russia):
    if russia.past_year < russia.date.year:
        russia.economic_growth = (russia.current_gdp - russia.past_gdp /
                                  ((russia.past_gdp + russia.current_gdp) / 2)) * 100

        """Calculation of yearly economic growth"""
        if russia.economic_growth <= 3.35:
            if not russia.economic_stimulus:
                choice = input(f"Your GDP grew {russia.economic_growth}% last year.\n"
                               f"Would you like to apply a stimulus?: ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    economic_stimulus(russia)

        elif russia.economic_growth >= 9.56:
            if russia.economic_stimulus:
                russia.economic_stimulus = False
    else:
        gdp_changes(russia)
        economic_state(russia)


"""Stats functions"""


def stats(russia):
    print(f"Your current leader is {russia.leader}.\n"
          f"{round((russia.pe / russia.current_pop) * 100, 4)}% of your population support your regime.\n"
          f"{round((russia.ae / russia.current_pop) * 100, 4)}% of your population are against your regime.\n"
          f"Your national debt is ${russia.national_debt}.\n"
          f"Your current GDP is ${russia.current_gdp}.\n"
          f"Your current GDP growth rate is {round((russia.current_gdp - russia.past_gdp) / ((russia.current_gdp + russia.past_gdp) / 2) * 100, 5)}%\n"
          f"Your current debt to GDP ratio is {round((russia.national_debt / russia.current_gdp), 2)}%\n"
          f"Your current population is {russia.current_pop}.\n"
          f"There have been {russia.births} in {russia.date.year}.\n"
          f"There have been {russia.deaths} in {russia.date.year}.\n")


def manual_game(year):
    russia = Russia(year)
    while russia.current_pop > 3000000:
        print("hi")
        population_change(russia)
        political_change(russia)
        economic_decisions(russia)
        answer = input("would you like to view your stats?: ")
        if answer.lower() == "y" or answer.lower() == "yes":
            stats(russia)
        time.sleep(3)


class Russia:
    def __init__(self, year):
        """Time variables"""
        self.date = datetime(int(year), 1, 1)
        self.past_year = self.date.year
        self.economic_change_date = self.date + timedelta(days=60)
        self.political_census = self.date + timedelta(days=3)
        self.year_plan_date = None
        """Population Variables"""
        self.current_pop = population[year]
        self.past_pop = self.current_pop
        self.deaths = None
        self.births = None
        self.pop_change = None
        self.condom_subsidy = None
        self.viagra_subsidy = None
        self.siberians = None
        self.deportees = None
        """Political Variables"""
        self.leader = dictators[year]
        self.pe = self.current_pop * 0.99
        self.ae = self.current_pop - self.pe
        """Economic Variables"""
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.economic_state = "recovery"
        self.economic_growth = None
        self.economic_stimulus = None
        # political economic variables
        self.national_debt = 0
        self.government_spending = None
        self.economic_stimulus = None
        if self.date < datetime(1923, 6, 16):
            self.year_plans = 0
        else:
            self.year_plans = 1
        # GDP components
        self.consumer_spending = None
        self.investment = None
        self.exports = None
        self.imports = None


manual_game("1914")
