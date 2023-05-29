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

"""Population variables and dictionaries"""
population = {
    "1910": 36100000,
    "1914": 36500000,
    "1918": 36800000,
    "1932": 41000000,
    "1936": 42400000,
    "1939": 43500000
}

"""population functions"""
def population_change(italy):
    if italy.past_year > italy.date.year:
        italy.population_change = (italy.current_pop - italy.past_pop / (
                    (italy.current_pop + italy.current_pop) / 2)) * 100
        italy.past_pop = italy.current_pop

        if italy.population_change <= 2.1:
            """possible implementation of viagra with somewhat moderate growth, due to low population"""
            print(f"Your population growth for {italy.past_year} was {italy.population_change}%.\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                italy.viagra_subsidy = True

                if italy.condom_subsidy:
                    """Checking to see if condom subsidies exist"""
                    italy.condom_subsidy = False

        elif italy.population_change >= 12.5:
            print(f"Your population growth for {italy.past_year} was {italy.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == 'y' or choice.lower() == "yes":
                italy.condom_subsidy = True

                if italy.viagra_subsidy:
                    italy.viagra_subsidy = False
    else:
        if italy.viagra_subsidy:
            births = random.randrange(200, 600)
            italy.births += births
            italy.current_pop += births

            deaths = random.randrange(25, 150)
            italy.deaths += deaths
            italy.current_pop -= deaths

        elif italy.condom_subsidy:
            births = random.randrange(50, 200)
            italy.births += births
            italy.current_pop += births

            deaths = random.randrange(25, 150)
            italy.deaths += deaths
            italy.current_pop -= deaths

        else:
            births = random.randrange(100, 300)
            italy.births += births
            italy.current_pop += births

            deaths = random.randrange(25, 150)
            italy.deaths += deaths
            italy.current_pop -= deaths

"""Economic Functions"""
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

        if italy.economic_growth <= 1.5:
            choice = input(f"Your GDP grew {italy.economic_growth} last year.\n"
                           f"Would you like to apply a stimulus?: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                # economic_stimulus(italy)
                pass
    else:
        gdp_changes(italy)

"""stats functions"""
def stats(italy):
    """Stats go from...
    1. Political
    2. Population
    3. Economic
    4. Social???
    5. Other
    """
    print(f"Your current monarch is {italy.monarch}\n"
          f"Your current prime minister is {italy.pm}\n"
          f"Your current stability is {italy.stability}\n"
          f"Your current population is {italy.current_pop}\n"
          f"Your current happiness level is {italy.happiness}\n"
          f"There have been {italy.births} births in {italy.past_year}\n"
          f"There have been {italy.deaths} deaths in {italy.past_year}\n"
          f"Your current GDP is ${round(italy.current_gdp, 2)}\n"
          f"Your current GDP growth rate is {round((italy.current_gdp - italy.past_gdp) / ((italy.current_gdp + italy.past_gdp)/2) * 100, 5)}%\n"
          f"Your economy is currently in a(n) {italy.economic_state}\n"
          f"Your current national debt it ${round(italy.national_debt, 2)}.\n"
          f"Your current tax rate is {italy.tax_rate}%\n")
def manual_game(italy):
    while italy.current_pop > 150000:
        print(f"Date: {italy.date}")
        italy.date += timedelta(days=1)
        print(italy.stability)
        # incrementing of time
        population_change(italy)
        economic_decisions(italy)
        if italy.stability > 50:
            choice = input("view stats: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                stats(italy)
        time.sleep(3)
class Italy:
    def __init__(self, year):
        """Political variables"""
        self.pm = prime_ministers[year]
        self.monarch = monarchs[year]
        self.stability = 90.00
        self.anti_establishment = 0
        """Population variables"""
        self.current_pop = population[year]
        self.population_change = 0
        self.past_pop = self.current_pop
        self.births = 0
        self.deaths = 0
        self.happiness = 95.56
        # population controller if birth rate gets out of hand
        self.condom_subsidy = False
        # population controller if birth rate flops
        self.viagra_subsidy = False
        """Economic_variables"""
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.economic_state = "recovery"
        self.tax_rate = tax_rate[year]
        self.economic_stimulus = False
        self.economic_growth = 0
        # gdp components
        self.consumer_spending = 0
        self.investment = 0
        self.exports = 0
        self.imports = 0
        # political economic variables
        self.government_spending = 0
        self.national_debt = 0
        """Time variables"""
        self.date = datetime(int(year), 1, 1)

        self.past_year = self.date.year
