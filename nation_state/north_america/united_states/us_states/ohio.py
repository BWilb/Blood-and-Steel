import random

population = {
    "1910": 4825093,
    "1914": 5170318,
    "1918": 5592461,
    "1932": 6703628,
    "1936": 6803983,
    "1939": 6885543
}

gdp = {
    "1910": 43503480000,
    "1914": 43937447400,
    "1918": 44002350900,
    "1932": 43822399800,
    "1936": 44106353500,
    "1939": 44904530300
}
def population_growth(ohio):
    births = random.randrange(1, 20)
    deaths = random.randrange(1, 18)
    ohio.population += (births - deaths)
    ohio.nation.current_pop += (births - deaths)
    ohio.nation.births += births
    ohio.nation.deaths += deaths

"""economic_functions"""
def recovery(alabama):
    if alabama.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 75), 2)
        alabama.investment = round(random.uniform(25, 250), 2)

        alabama.government_spending = round(random.uniform(100, 500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 750), 2)
        alabama.imports = round(random.uniform(320, 560), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 250), 2)
        alabama.investment = round(random.uniform(25, 350), 2)

        alabama.government_spending = round(random.uniform(100, 800), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 750), 2)
        alabama.imports = round(random.uniform(320, 560), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))
def expansion(alabama):
    if alabama.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 550), 2)
        alabama.investment = round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1000), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 1150), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 550), 2)
        alabama.investment = round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1200), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 1150), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

def recession(alabama):
    if alabama.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 250), 2)
        alabama.investment = -round(random.uniform(25, 350), 2)

        alabama.government_spending = round(random.uniform(100, 300), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 450), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 350), 2)
        alabama.investment = -round(random.uniform(25, 550), 2)

        alabama.government_spending = round(random.uniform(100, 500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 350), 2)
        alabama.imports = round(random.uniform(320, 860), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

def depression(alabama):
    if alabama.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 550), 2)
        alabama.investment = -round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1400), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 750), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 350), 2)
        alabama.investment = -round(random.uniform(25, 550), 2)

        alabama.government_spending = round(random.uniform(100, 500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 350), 2)
        alabama.imports = round(random.uniform(320, 1200), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                (alabama.exports - alabama.imports))

def economic_growth(alabama):
    """Economic growth of iowa as individual state"""
    if alabama.economic_state == "recovery":
        recovery(alabama)

    elif alabama.economic_state == "depression":
        depression(alabama)

    elif alabama.economic_state == "recession":
        recession(alabama)

    elif alabama.economic_state == "expansion":
        expansion(alabama)

class Ohio:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Ohio"
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