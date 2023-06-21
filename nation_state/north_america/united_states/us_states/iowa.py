import random

population = {
    "1910": 2229146,
    "1914": 2301256,
    "1918": 2382629,
    "1932": 2488741,
    "1936": 2513360,
    "1939": 2532942
}

gdp = {
    "1910": 6000000,
    "1914": 6193245,
    "1918": 6509000,
    "1932": 6734500,
    "1936": 6796700,
    "1939": 6850000
}
def population_growth(iowa):
    births = random.randrange(1, 15)
    deaths = random.randrange(1, 12)
    iowa.population += (births - deaths)
    iowa.nation.current_pop += (births - deaths)
    iowa.nation.births += births
    iowa.nation.deaths += deaths

"""economic_functions"""
def recovery(iowa):
    if iowa.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        iowa.consumer_spending = round(random.uniform(10, 250), 2)
        iowa.investment = round(random.uniform(25, 350), 2)

        iowa.government_spending = round(random.uniform(100, 500), 2)

        iowa.nation.national_debt += (iowa.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             iowa.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        iowa.exports = round(random.uniform(450, 750), 2)
        iowa.imports = round(random.uniform(320, 560), 2)
        iowa.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                             (iowa.exports - iowa.imports))
        """implementing two ways of expanding regional and national gdp"""
        iowa.nation.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                                    (iowa.exports - iowa.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        iowa.consumer_spending = round(random.uniform(10, 250), 2)
        iowa.investment = round(random.uniform(25, 350), 2)

        iowa.government_spending = round(random.uniform(100, 800), 2)

        iowa.nation.national_debt += (iowa.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               iowa.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        iowa.exports = round(random.uniform(450, 750), 2)
        iowa.imports = round(random.uniform(320, 560), 2)
        iowa.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                             (iowa.exports - iowa.imports))
        """implementing two ways of expanding regional and national gdp"""
        iowa.nation.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                                    (iowa.exports - iowa.imports))

def expansion(iowa):
    if iowa.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        iowa.consumer_spending = round(random.uniform(10, 550), 2)
        iowa.investment = round(random.uniform(25, 750), 2)

        iowa.government_spending = round(random.uniform(100, 1000), 2)

        iowa.nation.national_debt += (iowa.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               iowa.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        iowa.exports = round(random.uniform(450, 1150), 2)
        iowa.imports = round(random.uniform(320, 760), 2)
        iowa.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                             (iowa.exports - iowa.imports))
        """implementing two ways of expanding regional and national gdp"""
        iowa.nation.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                                    (iowa.exports - iowa.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        iowa.consumer_spending = round(random.uniform(10, 550), 2)
        iowa.investment = round(random.uniform(25, 750), 2)

        iowa.government_spending = round(random.uniform(100, 1200), 2)

        iowa.nation.national_debt += (iowa.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               iowa.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        iowa.exports = round(random.uniform(450, 1150), 2)
        iowa.imports = round(random.uniform(320, 760), 2)
        iowa.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                             (iowa.exports - iowa.imports))
        """implementing two ways of expanding regional and national gdp"""
        iowa.nation.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                                    (iowa.exports - iowa.imports))

def recession(iowa):
    if iowa.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        iowa.consumer_spending = -round(random.uniform(10, 250), 2)
        iowa.investment = -round(random.uniform(25, 350), 2)

        iowa.government_spending = round(random.uniform(100, 300), 2)

        iowa.nation.national_debt += (iowa.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -iowa.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        iowa.exports = round(random.uniform(250, 450), 2)
        iowa.imports = round(random.uniform(320, 760), 2)
        iowa.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                             (iowa.exports - iowa.imports))
        """implementing two ways of expanding regional and national gdp"""
        iowa.nation.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                                    (iowa.exports - iowa.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        iowa.consumer_spending = -round(random.uniform(10, 350), 2)
        iowa.investment = -round(random.uniform(25, 550), 2)

        iowa.government_spending = round(random.uniform(100, 500), 2)

        iowa.nation.national_debt += (iowa.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -iowa.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        iowa.exports = round(random.uniform(250, 350), 2)
        iowa.imports = round(random.uniform(320, 860), 2)
        iowa.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                             (iowa.exports - iowa.imports))
        """implementing two ways of expanding regional and national gdp"""
        iowa.nation.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                                    (iowa.exports - iowa.imports))

def depression(iowa):
    if iowa.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        iowa.consumer_spending = -round(random.uniform(10, 550), 2)
        iowa.investment = -round(random.uniform(25, 750), 2)

        iowa.government_spending = round(random.uniform(100, 1400), 2)

        iowa.nation.national_debt += (iowa.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -iowa.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        iowa.exports = round(random.uniform(250, 750), 2)
        iowa.imports = round(random.uniform(320, 760), 2)
        iowa.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                             (iowa.exports - iowa.imports))
        """implementing two ways of expanding regional and national gdp"""
        iowa.nation.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                                    (iowa.exports - iowa.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        iowa.consumer_spending = -round(random.uniform(10, 350), 2)
        iowa.investment = -round(random.uniform(25, 550), 2)

        iowa.government_spending = round(random.uniform(100, 500), 2)

        iowa.national_debt += (iowa.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -iowa.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        iowa.exports = round(random.uniform(250, 350), 2)
        iowa.imports = round(random.uniform(320, 1200), 2)
        iowa.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                             (iowa.exports - iowa.imports))
        """implementing two ways of expanding regional and national gdp"""
        iowa.nation.current_gdp += (iowa.consumer_spending + iowa.investment + iowa.government_spending +
                                    (iowa.exports - iowa.imports))

def economic_growth(iowa):
    """Economic growth of iowa as individual state"""
    if iowa.economic_state == "recovery":
        recovery(iowa)

    elif iowa.economic_state == "depression":
        depression(iowa)

    elif iowa.economic_state == "recession":
        recession(iowa)

    elif iowa.economic_state == "expansion":
        expansion(iowa)

class Iowa:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Iowa"
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