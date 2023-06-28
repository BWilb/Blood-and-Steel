import random

population = {
    "1910": 2624674,
    "1914": 2730287,
    "1918": 2844854,
    "1932": 2954286,
    "1936": 3043805,
    "1939": 2901124
}

gdp = {
    "1910": 29000000,
    "1914": 29937473,
    "1918": 38900983,
    "1932": 36899849,
    "1936": 37103595,
    "1939": 38900394
}
def population_growth(georgia):
    births = random.randrange(1, 20)
    deaths = random.randrange(1, 15)
    georgia.population += (births - deaths)
    georgia.nation.current_pop += (births - deaths)
    georgia.nation.births += births
    georgia.nation.deaths += deaths

"""economic_functions"""
def recovery(georgia):
    if georgia.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        georgia.consumer_spending = round(random.uniform(10, 75), 2)
        georgia.investment = round(random.uniform(25, 250), 2)

        georgia.government_spending = round(random.uniform(100, 500), 2)

        georgia.nation.national_debt += (georgia.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             georgia.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        georgia.exports = round(random.uniform(450, 750), 2)
        georgia.imports = round(random.uniform(320, 560), 2)
        georgia.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                             (georgia.exports - georgia.imports))
        """implementing two ways of expanding regional and national gdp"""
        georgia.nation.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                                       (georgia.exports - georgia.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        georgia.consumer_spending = round(random.uniform(10, 250), 2)
        georgia.investment = round(random.uniform(25, 350), 2)

        georgia.government_spending = round(random.uniform(100, 800), 2)

        georgia.nation.national_debt += (georgia.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               georgia.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        georgia.exports = round(random.uniform(450, 750), 2)
        georgia.imports = round(random.uniform(320, 560), 2)
        georgia.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                             (georgia.exports - georgia.imports))
        """implementing two ways of expanding regional and national gdp"""
        georgia.nation.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                                       (georgia.exports - georgia.imports))
def expansion(georgia):
    if georgia.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        georgia.consumer_spending = round(random.uniform(10, 550), 2)
        georgia.investment = round(random.uniform(25, 750), 2)

        georgia.government_spending = round(random.uniform(100, 1000), 2)

        georgia.nation.national_debt += (georgia.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               georgia.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        georgia.exports = round(random.uniform(450, 1150), 2)
        georgia.imports = round(random.uniform(320, 760), 2)
        georgia.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                             (georgia.exports - georgia.imports))
        """implementing two ways of expanding regional and national gdp"""
        georgia.nation.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                                       (georgia.exports - georgia.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        georgia.consumer_spending = round(random.uniform(10, 550), 2)
        georgia.investment = round(random.uniform(25, 750), 2)

        georgia.government_spending = round(random.uniform(100, 1200), 2)

        georgia.nation.national_debt += (georgia.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               georgia.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        georgia.exports = round(random.uniform(450, 1150), 2)
        georgia.imports = round(random.uniform(320, 760), 2)
        georgia.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                             (georgia.exports - georgia.imports))
        """implementing two ways of expanding regional and national gdp"""
        georgia.nation.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                                       (georgia.exports - georgia.imports))

def recession(georgia):
    if georgia.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        georgia.consumer_spending = -round(random.uniform(10, 250), 2)
        georgia.investment = -round(random.uniform(25, 350), 2)

        georgia.government_spending = round(random.uniform(100, 300), 2)

        georgia.nation.national_debt += (georgia.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -georgia.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        georgia.exports = round(random.uniform(250, 450), 2)
        georgia.imports = round(random.uniform(320, 760), 2)
        georgia.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                             (georgia.exports - georgia.imports))
        """implementing two ways of expanding regional and national gdp"""
        georgia.nation.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                                       (georgia.exports - georgia.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        georgia.consumer_spending = -round(random.uniform(10, 350), 2)
        georgia.investment = -round(random.uniform(25, 550), 2)

        georgia.government_spending = round(random.uniform(100, 500), 2)

        georgia.nation.national_debt += (georgia.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -georgia.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        georgia.exports = round(random.uniform(250, 350), 2)
        georgia.imports = round(random.uniform(320, 860), 2)
        georgia.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                             (georgia.exports - georgia.imports))
        """implementing two ways of expanding regional and national gdp"""
        georgia.nation.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                                       (georgia.exports - georgia.imports))

def depression(georgia):
    if georgia.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        georgia.consumer_spending = -round(random.uniform(10, 550), 2)
        georgia.investment = -round(random.uniform(25, 750), 2)

        georgia.government_spending = round(random.uniform(100, 1400), 2)

        georgia.nation.national_debt += (georgia.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -georgia.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        georgia.exports = round(random.uniform(250, 750), 2)
        georgia.imports = round(random.uniform(320, 760), 2)
        georgia.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                             (georgia.exports - georgia.imports))
        """implementing two ways of expanding regional and national gdp"""
        georgia.nation.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                                       (georgia.exports - georgia.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        georgia.consumer_spending = -round(random.uniform(10, 350), 2)
        georgia.investment = -round(random.uniform(25, 550), 2)

        georgia.government_spending = round(random.uniform(100, 500), 2)

        georgia.nation.national_debt += (georgia.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -georgia.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        georgia.exports = round(random.uniform(250, 350), 2)
        georgia.imports = round(random.uniform(320, 1200), 2)
        georgia.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                             (georgia.exports - georgia.imports))
        """implementing two ways of expanding regional and national gdp"""
        georgia.nation.current_gdp += (georgia.consumer_spending + georgia.investment + georgia.government_spending +
                (georgia.exports - georgia.imports))

def economic_growth(georgia):
    """Economic growth of iowa as individual state"""
    if georgia.economic_state == "recovery":
        recovery(georgia)

    elif georgia.economic_state == "depression":
        depression(georgia)

    elif georgia.economic_state == "recession":
        recession(georgia)

    elif georgia.economic_state == "expansion":
        expansion(georgia)

class Georgia:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Georgia"
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