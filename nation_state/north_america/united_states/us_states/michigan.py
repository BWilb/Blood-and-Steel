import random

population = {
    "1910": 2816416,
    "1914": 3168028,
    "1918": 3500657,
    "1932": 4930343,
    "1936": 5114263,
    "1939": 5225067
}

gdp = {
    "1910": 30500000000,
    "1914": 35093747000,
    "1918": 38900098000,
    "1932": 37890984000,
    "1936": 42103059000,
    "1939": 43900309000
}
def population_growth(michigan):
    births = random.randrange(10, 20)
    deaths = random.randrange(5, 15)
    michigan.population += (births - deaths)
    michigan.nation.current_pop += (births - deaths)

"""economic_functions"""
def recovery(michigan):
    if michigan.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        michigan.consumer_spending = round(random.uniform(10, 75), 2)
        michigan.investment = round(random.uniform(25, 250), 2)

        michigan.government_spending = round(random.uniform(100, 500), 2)

        michigan.nation.national_debt += (michigan.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             michigan.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        michigan.exports = round(random.uniform(450, 750), 2)
        michigan.imports = round(random.uniform(320, 560), 2)
        michigan.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                             (michigan.exports - michigan.imports))
        """implementing two ways of expanding regional and national gdp"""
        michigan.nation.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                                       (michigan.exports - michigan.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        michigan.consumer_spending = round(random.uniform(10, 250), 2)
        michigan.investment = round(random.uniform(25, 350), 2)

        michigan.government_spending = round(random.uniform(100, 800), 2)

        michigan.nation.national_debt += (michigan.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               michigan.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        michigan.exports = round(random.uniform(450, 750), 2)
        michigan.imports = round(random.uniform(320, 560), 2)
        michigan.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                             (michigan.exports - michigan.imports))
        """implementing two ways of expanding regional and national gdp"""
        michigan.nation.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                                       (michigan.exports - michigan.imports))
def expansion(michigan):
    if michigan.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        michigan.consumer_spending = round(random.uniform(10, 550), 2)
        michigan.investment = round(random.uniform(25, 750), 2)

        michigan.government_spending = round(random.uniform(100, 1000), 2)

        michigan.nation.national_debt += (michigan.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               michigan.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        michigan.exports = round(random.uniform(450, 1150), 2)
        michigan.imports = round(random.uniform(320, 760), 2)
        michigan.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                             (michigan.exports - michigan.imports))
        """implementing two ways of expanding regional and national gdp"""
        michigan.nation.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                                       (michigan.exports - michigan.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        michigan.consumer_spending = round(random.uniform(10, 550), 2)
        michigan.investment = round(random.uniform(25, 750), 2)

        michigan.government_spending = round(random.uniform(100, 1200), 2)

        michigan.nation.national_debt += (michigan.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               michigan.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        michigan.exports = round(random.uniform(450, 1150), 2)
        michigan.imports = round(random.uniform(320, 760), 2)
        michigan.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                             (michigan.exports - michigan.imports))
        """implementing two ways of expanding regional and national gdp"""
        michigan.nation.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                                       (michigan.exports - michigan.imports))

def recession(michigan):
    if michigan.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        michigan.consumer_spending = -round(random.uniform(10, 250), 2)
        michigan.investment = -round(random.uniform(25, 350), 2)

        michigan.government_spending = round(random.uniform(100, 300), 2)

        michigan.nation.national_debt += (michigan.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -michigan.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        michigan.exports = round(random.uniform(250, 450), 2)
        michigan.imports = round(random.uniform(320, 760), 2)
        michigan.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                             (michigan.exports - michigan.imports))
        """implementing two ways of expanding regional and national gdp"""
        michigan.nation.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                                       (michigan.exports - michigan.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        michigan.consumer_spending = -round(random.uniform(10, 350), 2)
        michigan.investment = -round(random.uniform(25, 550), 2)

        michigan.government_spending = round(random.uniform(100, 500), 2)

        michigan.nation.national_debt += (michigan.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -michigan.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        michigan.exports = round(random.uniform(250, 350), 2)
        michigan.imports = round(random.uniform(320, 860), 2)
        michigan.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                             (michigan.exports - michigan.imports))
        """implementing two ways of expanding regional and national gdp"""
        michigan.nation.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                                       (michigan.exports - michigan.imports))

def depression(michigan):
    if michigan.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        michigan.consumer_spending = -round(random.uniform(10, 550), 2)
        michigan.investment = -round(random.uniform(25, 750), 2)

        michigan.government_spending = round(random.uniform(100, 1400), 2)

        michigan.nation.national_debt += (michigan.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -michigan.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        michigan.exports = round(random.uniform(250, 750), 2)
        michigan.imports = round(random.uniform(320, 760), 2)
        michigan.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                             (michigan.exports - michigan.imports))
        """implementing two ways of expanding regional and national gdp"""
        michigan.nation.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                                       (michigan.exports - michigan.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        michigan.consumer_spending = -round(random.uniform(10, 350), 2)
        michigan.investment = -round(random.uniform(25, 550), 2)

        michigan.government_spending = round(random.uniform(100, 500), 2)

        michigan.nation.national_debt += (michigan.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -michigan.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        michigan.exports = round(random.uniform(250, 350), 2)
        michigan.imports = round(random.uniform(320, 1200), 2)
        michigan.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                             (michigan.exports - michigan.imports))
        """implementing two ways of expanding regional and national gdp"""
        michigan.nation.current_gdp += (michigan.consumer_spending + michigan.investment + michigan.government_spending +
                (michigan.exports - michigan.imports))

def economic_growth(michigan):
    """Economic growth of iowa as individual state"""
    if michigan.economic_state == "recovery":
        recovery(michigan)

    elif michigan.economic_state == "depression":
        depression(michigan)

    elif michigan.economic_state == "recession":
        recession(michigan)

    elif michigan.economic_state == "expansion":
        expansion(michigan)

class Michigan:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Michigan"
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