import random
import time

population = {
    "1910": 2142069,
    "1914": 2225741,
    "1918": 2311503,
    "1932": 2689523,
    "1936": 2761094,
    "1939": 2817169
}

gdp = {
    "1910": 250000,
    "1914": 259374,
    "1918": 289009,
    "1932": 298998,
    "1936": 321035,
    "1939": 339003
}
def population_growth(alaska):
    births = random.randrange(1, 15)
    deaths = random.randrange(1, 10)
    alaska.population += (births - deaths)
    alaska.nation.current_pop += (births - deaths)
    alaska.nation.births += births
    alaska.nation.deaths += deaths


def random_social(alaska):
    chance = random.randrange(10, 20000)
    if chance % 5 == 4:
        """Chance that a moose attack occurs"""
        print("A moose attack just occurred in Alaska.\n")
        time.sleep(3)

    elif chance % 8 == 7:
        """Chance that parade occurs"""
        print("A parade just occurred in Alaska.\n")
        time.sleep(3)

    elif chance % 10 == 7:
        """chance that someone has a surprise birthday thrown for them"""
        print("Someone just had a surprise birthday thrown for them.\n")
        time.sleep(3)

def random_crime(alaska):
    chance = random.randrange(10, 20000)
    if chance % 5 == 3:
        """Chance that rape occurs
        - decrease in happiness
        """
        print("A rape just occurred in Alaska.\n")
        time.sleep(3)
        decrease = round(random.uniform(0.75, 1.75), 2)
        if (alaska.happiness - decrease) > 7.56 and (alaska.nation.happiness - decrease) > 5:
            alaska.happiness -= decrease
            alaska.nation.happiness -= decrease

    elif chance % 8 == 7:
        """Chance that a stabbing occurs
        - no chance of survival
        - decrease in population and happiness
        """
        print("A fatal stabbing just occurred in Alaska.\n")
        time.sleep(3)
        decrease = round(random.uniform(0.75, 1.75), 2)
        if (alaska.happiness - decrease) > 7.56 and (alaska.nation.happiness - decrease) > 5:
            alaska.happiness -= decrease
            alaska.nation.happiness -= decrease

    elif chance % 12 == 9:
        """chance that a homicide occurs
        - decrease in population and happiness
        """
        homicide = random.randrange(10, 100)
        print(f"A homicide ring has been uncovered in Alabama, with {homicide} victims.\n.")
        time.sleep(3)
        alaska.population -= homicide
        alaska.nation.current_pop -= homicide
        decrease = round(random.uniform(0.25, 1.00), 2)
        if (alaska.happiness - decrease) > 5 and (alaska.nation.happiness - decrease) > 5:
            alaska.happiness -= decrease
            alaska.nation.happiness -= decrease

    elif chance % 40 == 25:
        """Chance for bank robbery
        - internal chance of death
        - decrease in gdp(national and regional)
        - decrease in happiness and stability
        """
        loss = round(alaska.current_gdp * round(random.uniform(0.001, 0.009), 5), 2)
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance that people die in robbery"""
            deaths = random.randrange(13, 50)
            print(f"A bank robbery just occurred in Alabama, with {deaths} dead and ${loss} lost.\n")
            time.sleep(3)
            alaska.population -= deaths
            alaska.nation.current_pop -= deaths
            alaska.nation.current_gdp -= loss
            alaska.current_gdp -= loss

        else:
            print(f"A bank robbery just occurred in Alabama, nobody was hurt, but ${loss} was lost.\n")
            time.sleep(3)
        decrease = round(random.uniform(0.25, 1.00), 2)
        if (alaska.happiness - decrease) > 5 and (alaska.nation.happiness - decrease) > 5:
            alaska.happiness -= decrease
            alaska.nation.happiness -= decrease

        if (alaska.stability - decrease) > 7.56 and (alaska.nation.stability - decrease) > 5:
            alaska.stability -= decrease
            alaska.nation.stability -= decrease
def random_events(alabama):
    random_social(alabama)
    random_crime(alabama)
"""economic_functions"""
def recovery(alaska):
    if alaska.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        alaska.consumer_spending = round(random.uniform(10, 55), 2)
        alaska.investment = round(random.uniform(25, 100), 2)

        alaska.government_spending = round(random.uniform(100, 500), 2)

        alaska.debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        alaska.nation.national_debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alaska.exports = round(random.uniform(150, 450), 2)
        alaska.imports = round(random.uniform(20, 250), 2)
        alaska.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                             (alaska.exports - alaska.imports))
        """implementing two ways of expanding regional and national gdp"""
        alaska.nation.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                                      (alaska.exports - alaska.imports))

    else:
        """If United States has implemented an economic stimulus"""
        alaska.consumer_spending = round(random.uniform(10, 35), 2)
        alaska.investment = round(random.uniform(25, 80), 2)

        alaska.government_spending = round(random.uniform(100, 850), 2)

        """alaska.debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))"""

        alaska.nation.national_debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alaska.exports = round(random.uniform(150, 350), 2)
        alaska.imports = round(random.uniform(20, 300), 2)
        alaska.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                             (alaska.exports - alaska.imports))
        """implementing two ways of expanding regional and national gdp"""
        alaska.nation.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                                      (alaska.exports - alaska.imports))
def expansion(alaska):
    if alaska.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        alaska.consumer_spending = round(random.uniform(10, 255), 2)
        alaska.investment = round(random.uniform(25, 450), 2)

        alaska.government_spending = round(random.uniform(100, 1000), 2)

        alaska.nation.national_debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alaska.exports = round(random.uniform(450, 1150), 2)
        alaska.imports = round(random.uniform(320, 760), 2)
        alaska.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                             (alaska.exports - alaska.imports))
        """implementing two ways of expanding regional and national gdp"""
        alaska.nation.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                                      (alaska.exports - alaska.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alaska.consumer_spending = round(random.uniform(10, 150), 2)
        alaska.investment = round(random.uniform(25, 400), 2)

        alaska.government_spending = round(random.uniform(100, 1200), 2)

        alaska.nation.national_debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alaska.exports = round(random.uniform(450, 950), 2)
        alaska.imports = round(random.uniform(320, 760), 2)
        alaska.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                             (alaska.exports - alaska.imports))
        """implementing two ways of expanding regional and national gdp"""
        alaska.nation.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                                      (alaska.exports - alaska.imports))

def recession(alaska):
    if alaska.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        alaska.consumer_spending = -round(random.uniform(10, 25), 2)
        alaska.investment = -round(random.uniform(25, 35), 2)

        alaska.government_spending = round(random.uniform(100, 300), 2)

        alaska.nation.national_debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alaska.exports = round(random.uniform(250, 450), 2)
        alaska.imports = round(random.uniform(320, 760), 2)
        alaska.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                             (alaska.exports - alaska.imports))
        """implementing two ways of expanding regional and national gdp"""
        alaska.nation.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                                      (alaska.exports - alaska.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alaska.consumer_spending = -round(random.uniform(10, 55), 2)
        alaska.investment = -round(random.uniform(25, 75), 2)

        alaska.government_spending = round(random.uniform(100, 500), 2)

        alaska.nation.national_debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alaska.exports = round(random.uniform(250, 550), 2)
        alaska.imports = round(random.uniform(320, 860), 2)
        alaska.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                             (alaska.exports - alaska.imports))
        """implementing two ways of expanding regional and national gdp"""
        alaska.nation.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                                      (alaska.exports - alaska.imports))

def depression(alaska):
    if alaska.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        alaska.consumer_spending = -round(random.uniform(10, 250), 2)
        alaska.investment = -round(random.uniform(25, 350), 2)

        alaska.government_spending = round(random.uniform(100, 1400), 2)

        alaska.nation.national_debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alaska.exports = round(random.uniform(250, 550), 2)
        alaska.imports = round(random.uniform(320, 760), 2)
        alaska.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                             (alaska.exports - alaska.imports))
        """implementing two ways of expanding regional and national gdp"""
        alaska.nation.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                                      (alaska.exports - alaska.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        alaska.consumer_spending = -round(random.uniform(10, 350), 2)
        alaska.investment = -round(random.uniform(25, 550), 2)

        alaska.government_spending = round(random.uniform(100, 1500), 2)

        alaska.nation.national_debt += (alaska.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alaska.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alaska.exports = round(random.uniform(250, 850), 2)
        alaska.imports = round(random.uniform(320, 1200), 2)
        alaska.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                             (alaska.exports - alaska.imports))
        """implementing two ways of expanding regional and national gdp"""
        alaska.nation.current_gdp += (alaska.consumer_spending + alaska.investment + alaska.government_spending +
                (alaska.exports - alaska.imports))

def economic_growth(alaska):
    """Economic growth of iowa as individual state"""
    if alaska.economic_state == "recovery":
        recovery(alaska)

    elif alaska.economic_state == "depression":
        depression(alaska)

    elif alaska.economic_state == "recession":
        recession(alaska)

    elif alaska.economic_state == "expansion":
        expansion(alaska)

class Alaska:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Alaska"
        # establishment of connection to United States
        self.nation = us
        """Population variables"""
        self.population = population[str(year)]
        """economic variables"""
        self.current_gdp = gdp[str(year)]
        self.consumer_spending = None
        self.government_spending = None
        self.investment = None
        self.exports = None
        self.imports = None
        self.economic_state = "recovery"
        self.debt = 0
        """Union variables"""
        self.union_favorability = 90.45