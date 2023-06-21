import random

population = {
    "1910": 405844,
    "1914": 412394,
    "1918": 423184,
    "1932": 434573,
    "1936": 448673,
    "1939": 468372
}

gdp = {
    "1910": 369875,
    "1914": 448291,
    "1918": 682723,
    "1932": 592382,
    "1936": 613223,
    "1939": 630121
}
def population_growth(arkansas):
    births = random.randrange(7, 25)
    deaths = random.randrange(2, 18)
    arkansas.population += (births - deaths)
    arkansas.nation.current_pop += (births - deaths)
    arkansas.nation.births += births
    arkansas.nation.deaths += deaths

"""economic_functions"""
def recovery(arkansas):
    if arkansas.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        arkansas.consumer_spending = round(random.uniform(10, 75), 2)
        arkansas.investment = round(random.uniform(25, 250), 2)

        arkansas.government_spending = round(random.uniform(100, 450), 2)

        arkansas.nation.national_debt += (arkansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                                         arkansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arkansas.exports = round(random.uniform(450, 750), 2)
        arkansas.imports = round(random.uniform(320, 560), 2)
        arkansas.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                (arkansas.exports - arkansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        arkansas.nation.current_gdp += (alabama.consumer_spending + arkansas.investment + arkansas.government_spending +
                                       (arkansas.exports - arkansas.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        arkansas.consumer_spending = round(random.uniform(10, 250), 2)
        arkansas.investment = round(random.uniform(25, 350), 2)

        arkansas.government_spending = round(random.uniform(100, 800), 2)

        arkansas.nation.national_debt += (arkansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                                         arkansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arkansas.exports = round(random.uniform(450, 750), 2)
        arkansas.imports = round(random.uniform(320, 560), 2)
        arkansas.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                (arkansas.exports - arkansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        arkansas.nation.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                       (arkansas.exports - arkansas.imports))
def expansion(arkansas):
    if arkansas.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        arkansas.consumer_spending = round(random.uniform(10, 550), 2)
        arkansas.investment = round(random.uniform(25, 750), 2)

        arkansas.government_spending = round(random.uniform(100, 1000), 2)

        arkansas.nation.national_debt += (arkansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                                         arkansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arkansas.exports = round(random.uniform(450, 1150), 2)
        arkansas.imports = round(random.uniform(320, 760), 2)
        arkansas.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                (arkansas.exports - arkansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        arkansas.nation.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                       (arkansas.exports - arkansas.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        arkansas.consumer_spending = round(random.uniform(10, 550), 2)
        arkansas.investment = round(random.uniform(25, 750), 2)

        arkansas.government_spending = round(random.uniform(100, 1200), 2)

        arkansas.nation.national_debt += (arkansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                                         arkansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arkansas.exports = round(random.uniform(450, 1150), 2)
        arkansas.imports = round(random.uniform(320, 760), 2)
        arkansas.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                (arkansas.exports - arkansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        arkansas.nation.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                       (arkansas.exports - arkansas.imports))

def recession(arkansas):
    if arkansas.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        arkansas.consumer_spending = -round(random.uniform(10, 250), 2)
        arkansas.investment = -round(random.uniform(25, 350), 2)

        arkansas.government_spending = round(random.uniform(100, 300), 2)

        arkansas.nation.national_debt += (arkansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                                         -arkansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arkansas.exports = round(random.uniform(250, 450), 2)
        arkansas.imports = round(random.uniform(320, 760), 2)
        arkansas.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                (arkansas.exports - arkansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        arkansas.nation.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                       (arkansas.exports - arkansas.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        arkansas.consumer_spending = -round(random.uniform(10, 350), 2)
        arkansas.investment = -round(random.uniform(25, 550), 2)

        arkansas.government_spending = round(random.uniform(100, 500), 2)

        arkansas.nation.national_debt += (arkansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                                         -arkansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arkansas.exports = round(random.uniform(250, 350), 2)
        arkansas.imports = round(random.uniform(320, 860), 2)
        arkansas.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                (arkansas.exports - arkansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        arkansas.nation.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                       (arkansas.exports - arkansas.imports))

def depression(arkansas):
    if arkansas.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        arkansas.consumer_spending = -round(random.uniform(10, 550), 2)
        arkansas.investment = -round(random.uniform(25, 750), 2)

        arkansas.government_spending = round(random.uniform(100, 1500), 2)

        arkansas.nation.national_debt += (arkansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                                         -arkansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arkansas.exports = round(random.uniform(250, 550), 2)
        arkansas.imports = round(random.uniform(320, 760), 2)
        arkansas.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                (arkansas.exports - arkansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        arkansas.nation.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                       (arkansas.exports - arkansas.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        arkansas.consumer_spending = -round(random.uniform(10, 350), 2)
        arkansas.investment = -round(random.uniform(25, 550), 2)

        arkansas.government_spending = round(random.uniform(100, 500), 2)

        arkansas.nation.national_debt += (arkansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                                         -arkansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        arkansas.exports = round(random.uniform(250, 750), 2)
        arkansas.imports = round(random.uniform(320, 1200), 2)
        arkansas.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                (arkansas.exports - arkansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        arkansas.nation.current_gdp += (arkansas.consumer_spending + arkansas.investment + arkansas.government_spending +
                                       (arkansas.exports - arkansas.imports))

def economic_growth(arkansas):
    """Economic growth of iowa as individual state"""
    if arkansas.economic_state == "recovery":
        recovery(arkansas)

    elif arkansas.economic_state == "depression":
        depression(arkansas)

    elif arkansas.economic_state == "recession":
        recession(arkansas)

    elif arkansas.economic_state == "expansion":
        expansion(arkansas)

class Arkansas:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Arkansas"
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