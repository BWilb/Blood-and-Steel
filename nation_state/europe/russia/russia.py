import random
import time
from datetime import datetime, timedelta
dictators = {
    "1910" : "Nicolaus II",
    "1914" : "Nicolaus II",
    "1918" : "Vladimir Lenin",
    "1932" : "Joseph Stalin",
    "1936" : "Joseph Stalin",
    "1939" : "Joseph Stalin"
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

def manual_game(year):
    russia = Russia(year)
    while russia.current_pop > 3000000:
        print("hi")
        population_change(russia)
        political_change(russia)
        time.sleep(3)
class Russia:
    def __init__(self, year):
        """Time variables"""
        self.date = datetime(int(year), 1, 1)
        self.past_year = self.date.year
        self.economic_change_date = self.date + timedelta(days=60)
        self.political_census = self.date + timedelta(days=3)
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
        self.tax_rate = None
        self.economic_growth = None
        self.economic_stimulus = None
        # political economic variables
        self.national_debt = 0
        self.government_spending = None
        # GDP components
        self.consumer_spending = None
        self.investment = None
        self.exports = None
        self.imports = None