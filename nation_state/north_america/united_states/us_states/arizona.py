import random
import time

population = {
    "1910": 605844,
    "1914": 612394,
    "1918": 623184,
    "1932": 634573,
    "1936": 648673,
    "1939": 668372
}

gdp = {
    "1910": 569875,
    "1914": 648291,
    "1918": 782723,
    "1932": 792382,
    "1936": 803223,
    "1939": 820121
}
def population_growth(arizona):
    births = random.randrange(1, 9)
    deaths = random.randrange(1, 9)
    arizona.population += (births - deaths)
    arizona.nation.current_pop += (births - deaths)
    arizona.nation.births += births
    arizona.nation.deaths += deaths

"""Random"""
def random_social(arizona):
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

"""def random_events(alabama):
    random_social(alabama)
    random_crime(alabama)"""
"""economic_functions"""
def recovery(arizona):
    if arizona.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        arizona.consumer_spending = round(random.uniform(10, 125), 2)
        arizona.investment = round(random.uniform(25, 220), 2)

        arizona.government_spending = round(random.uniform(100, 600), 2)

        arizona.debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        arizona.nation.national_debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arizona.exports = round(random.uniform(150, 550), 2)
        arizona.imports = round(random.uniform(20, 360), 2)
        arizona.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                             (arizona.exports - arizona.imports))
        """implementing two ways of expanding regional and national gdp"""
        arizona.nation.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                                      (arizona.exports - arizona.imports))

    else:
        """If United States has implemented an economic stimulus"""
        arizona.consumer_spending = round(random.uniform(10, 100), 2)
        arizona.investment = round(random.uniform(25, 200), 2)

        arizona.government_spending = round(random.uniform(100, 800), 2)

        arizona.debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))

        arizona.nation.national_debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arizona.exports = round(random.uniform(150, 500), 2)
        arizona.imports = round(random.uniform(20, 360), 2)
        arizona.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                             (arizona.exports - arizona.imports))
        """implementing two ways of expanding regional and national gdp"""
        arizona.nation.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                                      (arizona.exports - arizona.imports))
def expansion(arizona):
    if arizona.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        arizona.consumer_spending = round(random.uniform(10, 550), 2)
        arizona.investment = round(random.uniform(25, 650), 2)

        arizona.government_spending = round(random.uniform(100, 1000), 2)

        arizona.nation.national_debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arizona.exports = round(random.uniform(450, 1350), 2)
        arizona.imports = round(random.uniform(320, 760), 2)
        arizona.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                             (arizona.exports - arizona.imports))
        """implementing two ways of expanding regional and national gdp"""
        arizona.nation.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                                       (arizona.exports - arizona.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        arizona.consumer_spending = round(random.uniform(10, 400), 2)
        arizona.investment = round(random.uniform(25, 550), 2)

        arizona.government_spending = round(random.uniform(100, 1200), 2)

        arizona.nation.national_debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arizona.exports = round(random.uniform(450, 1150), 2)
        arizona.imports = round(random.uniform(320, 760), 2)
        arizona.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                             (arizona.exports - arizona.imports))
        """implementing two ways of expanding regional and national gdp"""
        arizona.nation.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                                       (arizona.exports - arizona.imports))

def recession(arizona):
    if arizona.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        arizona.consumer_spending = -round(random.uniform(10, 150), 2)
        arizona.investment = -round(random.uniform(25, 250), 2)

        arizona.government_spending = round(random.uniform(100, 300), 2)

        arizona.nation.national_debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arizona.exports = round(random.uniform(250, 450), 2)
        arizona.imports = round(random.uniform(320, 760), 2)
        arizona.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                             (arizona.exports - arizona.imports))
        """implementing two ways of expanding regional and national gdp"""
        arizona.nation.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                                       (arizona.exports - arizona.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        arizona.consumer_spending = -round(random.uniform(10, 200), 2)
        arizona.investment = -round(random.uniform(25, 300), 2)

        arizona.government_spending = round(random.uniform(100, 500), 2)

        arizona.nation.national_debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arizona.exports = round(random.uniform(250, 350), 2)
        arizona.imports = round(random.uniform(320, 760), 2)
        arizona.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                             (arizona.exports - arizona.imports))
        """implementing two ways of expanding regional and national gdp"""
        arizona.nation.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                                      (arizona.exports - arizona.imports))

def depression(arizona):
    if arizona.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        arizona.consumer_spending = -round(random.uniform(10, 450), 2)
        arizona.investment = -round(random.uniform(25, 550), 2)

        arizona.government_spending = round(random.uniform(100, 1400), 2)

        arizona.nation.national_debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arizona.exports = round(random.uniform(250, 750), 2)
        arizona.imports = round(random.uniform(320, 760), 2)
        arizona.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                             (arizona.exports - arizona.imports))
        """implementing two ways of expanding regional and national gdp"""
        arizona.nation.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                                      (arizona.exports - arizona.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        arizona.consumer_spending = -round(random.uniform(10, 750), 2)
        arizona.investment = -round(random.uniform(25, 750), 2)

        arizona.government_spending = round(random.uniform(100, 1500), 2)

        arizona.nation.national_debt += (arizona.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -arizona.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arizona.exports = round(random.uniform(250, 850), 2)
        arizona.imports = round(random.uniform(320, 1200), 2)
        arizona.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                             (arizona.exports - arizona.imports))
        """implementing two ways of expanding regional and national gdp"""
        arizona.nation.current_gdp += (arizona.consumer_spending + arizona.investment + arizona.government_spending +
                (arizona.exports - arizona.imports))

def economic_growth(arizona):
    """Economic growth of iowa as individual state"""
    if arizona.economic_state == "recovery":
        recovery(arizona)

    elif arizona.economic_state == "depression":
        depression(arizona)

    elif arizona.economic_state == "recession":
        recession(arizona)

    elif arizona.economic_state == "expansion":
        expansion(arizona)

class Arizona:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Arizona"
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
        self.union_favorability = 90.45