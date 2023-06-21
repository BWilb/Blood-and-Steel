import random

population = {
    "1910": 370492,
    "1914": 379599,
    "1918": 388552,
    "1932": 428288,
    "1936": 435595,
    "1939": 441282
}

gdp = {
    "1910": 603409,
    "1914": 639029,
    "1918": 658648,
    "1932": 637573,
    "1936": 639824,
    "1939": 642358
}
def population_growth(kansas):
    births = random.randrange(1, 10)
    deaths = random.randrange(1, 10)
    kansas.population += (births - deaths)
    kansas.nation.current_pop += (births - deaths)
    kansas.nation.births += births
    kansas.nation.deaths += deaths

"""economic_functions"""
def recovery(kansas):
    if kansas.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        kansas.consumer_spending = round(random.uniform(10, 75), 2)
        kansas.investment = round(random.uniform(25, 250), 2)

        kansas.government_spending = round(random.uniform(100, 500), 2)

        kansas.nation.national_debt += (kansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             kansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kansas.exports = round(random.uniform(450, 750), 2)
        kansas.imports = round(random.uniform(320, 560), 2)
        kansas.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                             (kansas.exports - kansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        kansas.nation.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                                       (kansas.exports - kansas.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        kansas.consumer_spending = round(random.uniform(10, 250), 2)
        kansas.investment = round(random.uniform(25, 350), 2)

        kansas.government_spending = round(random.uniform(100, 800), 2)

        kansas.nation.national_debt += (kansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               kansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kansas.exports = round(random.uniform(450, 750), 2)
        kansas.imports = round(random.uniform(320, 560), 2)
        kansas.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                             (kansas.exports - kansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        kansas.nation.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                                       (kansas.exports - kansas.imports))
def expansion(kansas):
    if kansas.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        kansas.consumer_spending = round(random.uniform(10, 550), 2)
        kansas.investment = round(random.uniform(25, 750), 2)

        kansas.government_spending = round(random.uniform(100, 1000), 2)

        kansas.nation.national_debt += (kansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               kansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kansas.exports = round(random.uniform(450, 1150), 2)
        kansas.imports = round(random.uniform(320, 760), 2)
        kansas.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                             (kansas.exports - kansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        kansas.nation.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                                       (kansas.exports - kansas.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        kansas.consumer_spending = round(random.uniform(10, 550), 2)
        kansas.investment = round(random.uniform(25, 750), 2)

        kansas.government_spending = round(random.uniform(100, 1200), 2)

        kansas.nation.national_debt += (kansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               kansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kansas.exports = round(random.uniform(450, 1150), 2)
        kansas.imports = round(random.uniform(320, 760), 2)
        kansas.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                             (kansas.exports - kansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        kansas.nation.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                                       (kansas.exports - kansas.imports))

def recession(kansas):
    if kansas.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        kansas.consumer_spending = -round(random.uniform(10, 250), 2)
        kansas.investment = -round(random.uniform(25, 350), 2)

        kansas.government_spending = round(random.uniform(100, 300), 2)

        kansas.nation.national_debt += (kansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -kansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kansas.exports = round(random.uniform(250, 450), 2)
        kansas.imports = round(random.uniform(320, 760), 2)
        kansas.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                             (kansas.exports - kansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        kansas.nation.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                                       (kansas.exports - kansas.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        kansas.consumer_spending = -round(random.uniform(10, 350), 2)
        kansas.investment = -round(random.uniform(25, 550), 2)

        kansas.government_spending = round(random.uniform(100, 500), 2)

        kansas.nation.national_debt += (kansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -kansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kansas.exports = round(random.uniform(250, 350), 2)
        kansas.imports = round(random.uniform(320, 860), 2)
        kansas.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                             (kansas.exports - kansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        kansas.nation.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                                       (kansas.exports - kansas.imports))

def depression(kansas):
    if kansas.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        kansas.consumer_spending = -round(random.uniform(10, 550), 2)
        kansas.investment = -round(random.uniform(25, 750), 2)

        kansas.government_spending = round(random.uniform(100, 1400), 2)

        kansas.nation.national_debt += (kansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -kansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kansas.exports = round(random.uniform(250, 750), 2)
        kansas.imports = round(random.uniform(320, 760), 2)
        kansas.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                             (kansas.exports - kansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        kansas.nation.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                                       (kansas.exports - kansas.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        kansas.consumer_spending = -round(random.uniform(10, 350), 2)
        kansas.investment = -round(random.uniform(25, 550), 2)

        kansas.government_spending = round(random.uniform(100, 500), 2)

        kansas.nation.national_debt += (kansas.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -kansas.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kansas.exports = round(random.uniform(250, 350), 2)
        kansas.imports = round(random.uniform(320, 1200), 2)
        kansas.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                             (kansas.exports - kansas.imports))
        """implementing two ways of expanding regional and national gdp"""
        kansas.nation.current_gdp += (kansas.consumer_spending + kansas.investment + kansas.government_spending +
                (kansas.exports - kansas.imports))

def economic_growth(kansas):
    """Economic growth of iowa as individual state"""
    if kansas.economic_state == "recovery":
        recovery(kansas)

    elif kansas.economic_state == "depression":
        depression(kansas)

    elif kansas.economic_state == "recession":
        recession(kansas)

    elif kansas.economic_state == "expansion":
        expansion(kansas)

class Kansas:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Kansas"
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