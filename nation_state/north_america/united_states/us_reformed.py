import random
import time
from datetime import datetime, timedelta
import arcade
"""Population Dictionaries"""
population = {
    # population will be set up to increase or decrease randomly throughout every year
    "1910": 92410000,
    "1914": 99110000,
    "1918": 103210000,
    "1932": 124840000,
    "1936": 128050000,
    "1939": 130880000
}
"""Political Dictionaries"""
presidents = {
    "1910": "William Howard Taft",
    "1914": "Woodrow Wilson",
    "1918": "Woodrow Wilson",
    "1932": "Herbert Hoover",
    "1936": "Franklin D. Roosevelt",
    "1939": "Franklin D. Roosevelt"
}

vice_presidents = {
    # dictionary of vice presidents incase president gets assassinated
    "1910": "James S. Sherman",
    "1914": "Thomas R. Marshall",
    "1918": "Thomas R. Marshall",
    "1932": "Charles Curtis",
    "1936": "John Garner",
    "1939": "Henry Wallace"
}
"""Economic dictionaries & Variables"""
business_cycle = ["recovery", "expansion", "recession", "depression"]
gdp = {
    "1910": 520000000000,
    "1914": 500000000000,
    "1918": 550000000000,
    "1932": 550000000000,
    "1936": 575000000000,
    "1939": 1100000000000
}

tax_rate = {
    "1910": 0,
    "1914": 1.00,
    "1918": 6.00,
    "1932": 4.00,
    "1936": 4.00,
    "1939": 4.00
}

"""Subsidiary functions of game"""

"""Happiness and Stability functions"""

def happiness_and_stability(us):
    """
    Function controls the stability and happiness of the nation.
    Happiness & stability are based upon...
    1. Each other
    2. The Economy
    """
    chance = random.randrange(0, 2)
    if us.economic_state == "recession":
        """if economy is in recession. moderate decrease"""
        if us.tax_rate >= 25.00:

            if not us.happiness <= 4.00:
                """
                Setting constraint upon happiness.
                In order to prevent falling into negative range
                * chance also plays part(some people may become happier) * 
                """
                if chance == 0:
                    us.happiness -= round(random.uniform(0.56, 1.23), 2)

                elif chance == 1:
                    us.happiness += round(random.uniform(0.26, 0.57), 2)

            if not us.stability <= 15:
                us.stability -= round(random.uniform(0.25, 0.75), 2)

    elif us.economic_state == "depression":
        """if economy is in depression. extreme decrease"""
        if us.tax_rate >= 30.00:

            if not us.happiness <= 10.00:
                """
                Setting constraint upon happiness.
                In order to prevent falling into negative range
                """

                if chance == 0:
                    us.happiness -= round(random.uniform(1.56, 7.35), 2)

                elif chance == 1:
                    us.happiness += round(random.uniform(1.25, 5.54), 2)

            if not us.stability <= 20:
                us.stability -= round(random.uniform(1.25, 5.45), 2)

    elif us.economic_state == "recovery":
        """if economy is in recovery. moderate increase"""
        if us.tax_rate >= 20.00:

            if not us.happiness >= 98.56:
                """
                Setting constraint upon happiness.
                In order to prevent falling into negative range
                """
                if chance == 0:
                    us.happiness -= round(random.uniform(0.35, 2.34), 2)

                    if not us.stability <= 14.65:
                        us.stability -= round(random.uniform(0.10, 1.14), 2)

                elif chance == 1:
                    us.happiness += round(random.uniform(0.45, 3.33), 2)

                    if not us.stability >= 97.85:
                        us.stability += round(random.uniform(0.23, 2.34), 2)

    elif us.economic_state == "expansion":
        """if economy is in expansion. extreme increase"""
        if us.tax_rate >= 15.00:

            if not us.happiness >= 98.56:
                """
                Setting constraint upon happiness.
                In order to prevent falling into negative range
                """
                if chance == 0:
                    us.happiness -= round(random.uniform(1.45, 5.67), 2)

                    if not us.stability <= 14.65:
                        us.stability -= round(random.uniform(0.95, 4.96), 2)

                elif chance == 1:
                    us.happiness += round(random.uniform(0.85, 5.33), 2)

                    if not us.stability >= 97.85:
                        us.stability += round(random.uniform(0.75, 4.34), 2)

    if us.happiness < 50.00:
        """
        Just as with the economy, overall happiness can affect the stability
        of a nation.
        """
        chance = random.randrange(0, 2)

        if chance == 0:
            us.stability += round(random.uniform(1.34, 5.56), 2)

        elif chance == 1:
            us.stability -= round(random.uniform(2.45, 6.56), 2)

    if us.stability < 45.00:
        """
        Just as with the economy, overall stability can affect the happiness
        of a nation.
        """
        chance = random.randrange(0, 2)

        if chance == 0:
            us.happiness += round(random.uniform(1.34, 5.56), 2)

        elif chance == 1:
            us.happiness -= round(random.uniform(2.45, 6.56), 2)
"""population functions"""
def population_change(us):
    if us.current_year < us.date.year:
        us.population_change = (us.population - us.current_pop / ((us.population + us.current_pop) / 2)) * 100

        us.current_pop = us.population

        if us.population_change <= 1.5:
            """Incorporation of what happens when population growth becomes too small"""
            print(f"Your population growth for {us.current_year} was {us.population_change}%")
            choice = input("Would you like to subsidize viagra?: ")

            if choice.lower() == "yes" or choice.lower() == "y":
                us.viagra_subsidy = True
                us.condom_subsidy = False

        elif us.population_change >= 8:
            """Incorporation of what happens when population growth becomes too large"""
            print(f"Your population growth for {us.current_year} was {us.population_change}%")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == "yes" or choice.lower():
                us.condom_subsidy = True
                us.viagra_subsidy = False

    else:
        if us.viagra_subsidy:
            """incorporation of births and deaths under viagra subsidies"""
            births = random.randrange(700, 2400)
            us.births += births
            us.population += births

            deaths = random.randrange(300, 1200)
            us.deaths += deaths
            us.population -= deaths

        elif us.condom_subsidy:
            """incorporation of births and deaths under condom subsidies"""
            births = random.randrange(500, 2000)
            us.births += births
            us.population += births

            deaths = random.randrange(400, 1800)
            us.deaths += deaths
            us.population -= deaths

        else:
            """Incorporation of births and deaths under regular circumstances"""
            births = random.randrange(600, 2200)
            us.births += births
            us.population += births

            deaths = random.randrange(500, 1500)
            us.deaths += deaths
            us.population -= deaths

"""political functions"""

def political_changes(us):
    chance = random.randrange(0, 2)
    if chance == 0:
        change = us.republicans * random.uniform(0.05, 0.25)
        us.republicans -= change
        us.democrats += change

    else:
        change = us.democrats * random.uniform(0.05, 0.25)
        us.democrats -= change
        us.republicans += change

"""Random functions"""
def random_politics(us):
    """Function based upon random political events"""
    chance = random.randrange(10, 20000)
    if chance % 12 == 5:
        issues = ["Abortion", "Immigration", "Guns", "Women's Rights"]
        print(f"A(n) {issues[random.randrange(0, len(issues) - 1)]} protest occurred in DC.")

def random_economics(us):
    """Function based upon random economic events"""
    chance = random.randrange(10, 20000)
    if chance % 5 == 3:
        """Chance that Congress spends a bit of money"""
        money = round(random.uniform(14500, 150000), 2)
        print(f"Congress decided to spend ${money} today")
        us.current_gdp += money
        us.national_debt += round((money * random.uniform(0.25, 0.75)), 2)

    elif chance % 8 == 3:
        """Chance that congress raises tax rate"""

        if us.tax_rate < 10.00 and us.date >= us.tax_change_date:
            """chance that congress raises taxes, has time constraint on it"""
            increase = round(random.uniform(0.25, 2.25), 2)
            print(f"Congress decided to raise taxes by {increase}%")
            us.investment -= round(random.uniform(120000, 1020000), 2)
            us.consumer_spending -= round(random.uniform(20000, 400000), 2)
            us.happiness -= round(random.uniform(0.25, 1.25), 2)
            time.sleep(3)
            us.tax_rate += increase
            us.tax_change_date = us.date

    elif chance % 10 == 6 and us.date >= us.tax_change_date:
        """chance that congress lowers tax rate, has time constraint"""
        decrease = round(random.uniform(0.25, 2.25), 2)
        if us.tax_rate - decrease >= 0.25:
            print(f"Congress decided to lower taxes by {decrease}%")
            us.happiness += round(random.uniform(0.25, 1.25), 2)
            time.sleep(3)
            us.tax_rate -= decrease
            us.tax_change_date = us.date
            
        else:
            print(f"Congress attempted to lower taxes by {decrease}%.\n"
                  f"However this decrease wouldn't've been sustainable.")
            time.sleep(3)

    elif chance % 35 == 3:
        """Chance the economy goes for a run"""
        growth = round(random.uniform(3.56, 8.56), 2)
        print(f"The economy has whipped itself into a frenzy of extreme growth has taken place!!\n"
              f"Numbers indicate that it is beginning to grow at {growth}%.")
        time.sleep(3)
        us.gdp *= growth
        us.stability += round(random.uniform(0.95, 4.56), 2)
        us.happiness += round(random.uniform(0.56, 20.45), 2)

    elif chance % 45 == 4:
        """Chance that the economy goes into a tailspin"""
        retraction = round(random.uniform(5.56, 10.00), 2)
        print("OH FUCK, the economy has fallen into a tailspin.\n"
              f"It is being reported that it is beginning to shrink at {retraction}%")
        time.sleep(3)
        us.gdp = us.gdp / retraction
        us.happiness -= round(random.uniform(10.45, 34.56), 2)
        us.stability -= round(random.uniform(12.56, 50.55), 2)
        if us.economic_state != "depression":
            us.economic_state = "depression"


def random_social(us):
    """Random events based upon a social aspect"""
    chance = random.randrange(10, 20000)
    if chance % 4 == 0:
        print("Someone threw a surprise birthday for their child!")
        time.sleep(3)
        us.happiness += round(random.uniform(0.5, 2), 2)

    elif chance % 8 == 3:
        print("A parade occurred")
        time.sleep(3)
        us.happiness += round(random.uniform(0.5, 2), 2)

    elif chance % 10 == 4:
        print("Someone just got married!!")
        time.sleep(3)
        us.happiness += round(random.uniform(0.5, 2), 2)

    elif chance % 12 == 5:
        money = random.randrange(1000, 1000000)
        print(f"Someone just won ${money} at their local lottery")

    elif chance % 15 == 2:
        people = random.randrange(3, 25)
        print(f"Someone lost control of their car and ran into a group of people.\n"
              f"{people} people died.")
        us.deaths += people
        time.sleep(3)
        us.happiness -= round(random.uniform(0.5, 2), 2)
        
    elif chance % 16 == 3:
        partner = ["wife", "husband", "boyfriend" "girlfriend", "fiance"]
        print(f"Someone just broke up with their {partner[random.randrange(0, len(partner) - 1)]}")
        us.happiness -= round(random.uniform(0.5, 1.25), 2)
        time.sleep(3)

    elif chance % 24 == 5:
        locations = ["School", "Bank", "Store", "Parade"]
        people = random.randrange(0, 50)
        print(f"Someone decided to shoot up a {locations[random.randrange(0, len(locations) - 1)]}.\n"
              f"{people} people died")
        us.deaths += people
        time.sleep(3)
        us.population -= people
        us.stability -= round(random.uniform(0.5, 5), 2)
        us.happiness -= round(random.uniform(0.5, 14), 2)

def random_weather(us):
    """Function covers random weather events"""
    print()

def random_international(us):
    """
    Function deals with un-anticipated international events.
    These events will include terrorism, pre-emptive strikes,
    trade(possibly), international aid, and many more
    """
    print()
def randomized_functions(us):
    """Function that deviates to other subsidiary functions"""
    random_politics(us)
    random_social(us)
    random_economics(us)
    random_weather(us)
    random_international(us)

"""Economic Functions"""
def economic_state(us):
    if us.date >= us.economic_change_date:
        """comparing current date with possible shift in business cycle, based upon 3 month cycle"""
        if us.past_gdp > us.current_gdp:
            """comparing past gdp to current gdp"""
            if us.economic_state == "expansion" or us.economic_state == "recovery":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recession":
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=150)
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif us.economic_state == "recession":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "depression":
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=210)
                        # economic_stimulus(us)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """

            elif us.economic_state == "depression":
                """if statement handling depression cycle going to recovery or expansion cycle"""
                chance = random.randrange(0, 2)
                if chance == 0:
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "recovery":
                            us.economic_state = business_cycle[i]
                            us.economic_change_date = us.date + timedelta(days=365)
                            """
                            Allowance of a recovery to last an entire year
                            """

                elif chance == 1:
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "expansion":
                            us.economic_state = business_cycle[i]
                            us.economic_change_date = us.date + timedelta(days=240)
                            """
                            Unlike depressions, expansions can only last for a short time
                            """
def slow_growth(us):
    us.consumer_spending = round(random.uniform(3000, 7500), 2)
    us.investment = round(random.uniform(2000, 5400), 2)
    print(us.consumer_spending, '\n', us.investment)
    us.government_spending = round(random.uniform(3000, 5000), 2)

    us.national_debt += (us.government_spending * round(random.uniform(0.05, 0.45), 2) +
                         us.consumer_spending * round(random.uniform(0.05, 0.30), 2))
    """
    National debt includes both portions of US government spending and consumer spending.
    The portions are comprised of the loans and bonds that are bought and sold
    """

    us.exports = round(random.uniform(4500, 75000), 2)
    us.imports = round(random.uniform(3200, 56000), 2)
    us.current_gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    us.happiness += 0.15

def fast_growth(us):
    us.consumer_spending = round(random.uniform(80000, 150000), 2)
    us.investment = round(random.uniform(60000, 150000), 2)
    print(us.consumer_spending, '\n', us.investment)
    us.government_spending = round(random.uniform(50000, 175000), 2)

    us.national_debt += (us.government_spending * round(random.uniform(0.05, 0.45), 2) +
                         us.consumer_spending * round(random.uniform(0.05, 0.30), 2))
    """
    National debt includes both portions of US government spending and consumer spending.
    The portions are comprised of the loans and bonds that are bought and sold
    """

    us.exports = round(random.uniform(15000, 170000), 2)
    us.imports = round(random.uniform(14000, 100000), 2)
    us.current_gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    us.happiness += 0.25

def slow_fall(us):
    us.consumer_spending = -(round(random.uniform(3500, 10250), 2))
    us.investment = -(round(random.uniform(3000, 40000), 2))
    print(us.consumer_spending, '\n', us.investment)
    if us.economic_stimulus:
        us.government_spending = round(random.uniform(75000, 3250000), 2)

    else:
        us.government_spending = round(random.uniform(50000, 7650000), 2)

    us.national_debt += (us.government_spending * round(random.uniform(0.05, 0.45), 2) +
                         -(us.consumer_spending) * round(random.uniform(0.05, 0.30), 2))
    """
    National debt includes both portions of US government spending and consumer spending.
    The portions are comprised of the loans and bonds that are bought and sold
    """

    us.exports = round(random.uniform(14000, 65000), 2)
    us.imports = round(random.uniform(14000, 140000), 2)
    us.current_gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    us.happiness -= 0.15
    us.stability -= round(random.uniform(0.15, 1.05), 2)

def fast_fall(us):
    us.consumer_spending = -(round(random.uniform(6000, 455000), 2))
    us.investment = -(round(random.uniform(6000, 560000), 2))
    print(us.consumer_spending, '\n', us.investment)
    if us.economic_stimulus:
        us.government_spending = round(random.uniform(500000, 12500000), 2)

    else:
        us.government_spending = round(random.uniform(50000, 1250000), 2)

    us.national_debt += (us.government_spending * round(random.uniform(0.05, 0.45), 2) +
                         -(us.consumer_spending) * round(random.uniform(0.05, 0.30), 2))
    """
    National debt includes both portions of US government spending and consumer spending.
    The portions are comprised of the loans and bonds that are bought and sold
    """

    us.exports = round(random.uniform(1200, 420000), 2)
    us.imports = round(random.uniform(140000, 1400000), 2)
    us.current_gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    us.happiness -= 0.25
    us.stability -= round(random.uniform(0.25, 1.25), 2)

def gdp_change(us):
    if us.economic_state == "recovery":
        slow_growth(us)

    elif us.economic_state == "expansion":
        fast_growth(us)

    elif us.economic_state == "recession":
        slow_fall(us)

    elif us.economic_state == "depression":
        fast_fall(us)

def economic_stimulus(us):
    us.stimulus = True

    if us.economic_state.lower() == "recession":
        choice = input("\nDo you want to increase the tax rate in order to support increased spending"
                       "(Remember this applies to the entire population)?:")
        """Prompting user to choose if they want to increase taxes"""

        if choice.lower() == "yes" or choice.lower() == "y":
            valid_choice = False

            while valid_choice:
                tax_hike = float(input("By how much do you want to increase taxes(max cap is 25)?: "))

                if tax_hike <= 25 and tax_hike >= 0.5:
                    """if statement covering if tax hike meets criteria"""
                    us.tax_rate += round(tax_hike, 2)
                    print(f"{us.tax_rate}% is your new tax rate")
                    us.happiness -= round(random.uniform(0.25, 3.45), 2)
                    us.stability -= round(random.uniform(0.25, 1.45), 2)
                    valid_choice = True

                elif tax_hike <= 0 or tax_hike > 25:
                    print(f"New tax hike of {tax_hike} is improper./n"
                          f"try again")
                    time.sleep(3)

                else:
                    print("Not a valid tax rate")
                    time.sleep(3)

    elif us.economic_state.lower() == "depression":

        tax_hike = round(random.uniform(10, 25), 2)
        if (us.tax_rate + tax_hike) <= 86.00:
            print(f"Congress has enacted a tax hike of {tax_hike} points")

def economic_decisions(us):
    if us.current_year < us.date.year:
        us.economic_growth = (us.current_gdp - us.past_gdp / ((us.past_gdp + us.current_gdp) / 2)) * 100

        if us.economic_growth <= 1.5:
            choice = input(f"Your GDP grew {us.economic_growth}% last year.\n"
                           f"Would you like to apply a stimulus?: ")

            if choice.lower() == "yes" or choice.lower() == "y":
                economic_stimulus(us)

            elif choice.lower() == "n" or choice.lower() == "no":
                if us.recess_years > 3 and us.economic_grwoth <= 0.5:
                    print("Your economy has been been declining for three years.\n"
                          "An economic stimulus has been implemented by Congress.")
                    time.sleep(3)
                    economic_stimulus(us)
    else:
        gdp_change(us)

"""Function designed to check stats"""
def check_stats(us):
    """Stats organized by...
    1. Politics
    2. Economics
    3. Social aspects
    4. Others
    """
    print(f"Your current President is {us.president}\n"
          f"Your current Vice President is {us.vice_president}\n"
          f"Democrats make up {round((us.democrats / us.population) * 100, 2)}% of the population\n"
          f"Republicans make up {round((us.republicans / us.population) * 100, 2)}% of the population\n"
          f"Your current political stability is {round(us.stability, 2)}%\n"
          f"Your current GDP is ${round(us.current_gdp, 2)}\n"
          f"Your economy is currently in a(n) {us.economic_state} period\n"
          f"Your current yearly gdp growth is {round(((us.current_gdp - us.past_gdp) / ((us.past_gdp + us.current_gdp) / 2)) * 100, 5 )}%\n"
          f"Your current national debt is ${round(us.national_debt, 2)}\n"
          f"Your current tax rate is {round(us.tax_rate, 2)}%\n"
          f"There have been {us.deaths} deaths that have occurred in {us.current_year}\n"
          f"There have been {us.births} births that have occurred in {us.current_year}\n"
          f"The current happiness rating of the United States is {round(us.happiness, 2)}%\n")

"""Main function of US_Version of game"""
def manual_game(us):
    # Establishment of date variable
    while us.population > 2000000:
        us.date = us.date + timedelta(days=1)
        print(f"Date: {us.date}")
        # function will incorporate daily changes in us population
        population_change(us)
        political_changes(us)
        economic_decisions(us)
        economic_state(us)
        randomized_functions(us)
        # chance variable for depicting US political stability

        if us.stability >= 50:
            choice = input("Important!!! view your stats: ")
            if choice == "y" or choice == "yes":
                check_stats(us)

class UnitedStates:
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
        """Leaders of US"""
        self.president = presidents[year]
        self.vice_president = vice_presidents[year]
        """Political parties of US"""
        self.republicans = self.population * 0.5
        self.democrats = self.population - self.republicans
        """Other political variables"""
        self.stability = 95.00
        # economic variables
        self.economic_state = business_cycle[0]
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
        # international variables
        self.alliance = ""
        # time variables
        self.date = datetime(int(year), 1, 1)
        self.tax_change_date = self.date + timedelta(days=30)
        self.economic_change_date = self.date + timedelta(days=60)
        self.current_year = self.date.year

def main(time):
    united_states = UnitedStates(time)
    manual_game(united_states)