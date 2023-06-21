import random

population = {
    "1910": 9146310,
    "1914": 9657975,
    "1918": 10166100,
    "1932": 12827307,
    "1936": 13136161,
    "1939": 13418346
}

gdp = {
    "1910": 645503480000,
    "1914": 654593744740,
    "1918": 658690235090,
    "1932": 649682239980,
    "1936": 652410635350,
    "1939": 663490453030
}
def population_growth(n_y):
    births = random.randrange(10, 20)
    deaths = random.randrange(5, 10)
    n_y.population += (births - deaths)
    n_y.nation.current_pop += (births - deaths)
    n_y.nation.births += births
    n_y.nation.deaths += deaths

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

class NewYork:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "New York"
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