import random

population = {
    "1910": 26246,
    "1914": 27302,
    "1918": 28448,
    "1932": 29542,
    "1936": 30438,
    "1939": 29011
}

gdp = {
    "1910": 29000,
    "1914": 29937,
    "1918": 38900,
    "1932": 36899,
    "1936": 37103,
    "1939": 38904
}
def population_growth(hawaii):
    births = random.randrange(1, 5)
    deaths = random.randrange(0, 3)
    hawaii.population += (births - deaths)
    hawaii.nation.current_pop += (births - deaths)

"""economic_functions"""
def recovery(hawaii):
    if hawaii.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        hawaii.consumer_spending = round(random.uniform(10, 75), 2)
        hawaii.investment = round(random.uniform(25, 250), 2)

        hawaii.government_spending = round(random.uniform(100, 500), 2)

        hawaii.nation.national_debt += (hawaii.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             hawaii.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        hawaii.exports = round(random.uniform(450, 750), 2)
        hawaii.imports = round(random.uniform(320, 560), 2)
        hawaii.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                             (hawaii.exports - hawaii.imports))
        """implementing two ways of expanding regional and national gdp"""
        hawaii.nation.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                                       (hawaii.exports - hawaii.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        hawaii.consumer_spending = round(random.uniform(10, 250), 2)
        hawaii.investment = round(random.uniform(25, 350), 2)

        hawaii.government_spending = round(random.uniform(100, 800), 2)

        hawaii.nation.national_debt += (hawaii.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               hawaii.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        hawaii.exports = round(random.uniform(450, 750), 2)
        hawaii.imports = round(random.uniform(320, 560), 2)
        hawaii.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                             (hawaii.exports - hawaii.imports))
        """implementing two ways of expanding regional and national gdp"""
        hawaii.nation.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                                       (hawaii.exports - hawaii.imports))
def expansion(hawaii):
    if hawaii.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        hawaii.consumer_spending = round(random.uniform(10, 550), 2)
        hawaii.investment = round(random.uniform(25, 750), 2)

        hawaii.government_spending = round(random.uniform(100, 1000), 2)

        hawaii.nation.national_debt += (hawaii.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               hawaii.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        hawaii.exports = round(random.uniform(450, 1150), 2)
        hawaii.imports = round(random.uniform(320, 760), 2)
        hawaii.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                             (hawaii.exports - hawaii.imports))
        """implementing two ways of expanding regional and national gdp"""
        hawaii.nation.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                                       (hawaii.exports - hawaii.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        hawaii.consumer_spending = round(random.uniform(10, 550), 2)
        hawaii.investment = round(random.uniform(25, 750), 2)

        hawaii.government_spending = round(random.uniform(100, 1200), 2)

        hawaii.nation.national_debt += (hawaii.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               hawaii.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        hawaii.exports = round(random.uniform(450, 1150), 2)
        hawaii.imports = round(random.uniform(320, 760), 2)
        hawaii.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                             (hawaii.exports - hawaii.imports))
        """implementing two ways of expanding regional and national gdp"""
        hawaii.nation.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                                       (hawaii.exports - hawaii.imports))

def recession(hawaii):
    if hawaii.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        hawaii.consumer_spending = -round(random.uniform(10, 250), 2)
        hawaii.investment = -round(random.uniform(25, 350), 2)

        hawaii.government_spending = round(random.uniform(100, 300), 2)

        hawaii.nation.national_debt += (hawaii.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -hawaii.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        hawaii.exports = round(random.uniform(250, 450), 2)
        hawaii.imports = round(random.uniform(320, 760), 2)
        hawaii.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                             (hawaii.exports - hawaii.imports))
        """implementing two ways of expanding regional and national gdp"""
        hawaii.nation.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                                       (hawaii.exports - hawaii.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        hawaii.consumer_spending = -round(random.uniform(10, 350), 2)
        hawaii.investment = -round(random.uniform(25, 550), 2)

        hawaii.government_spending = round(random.uniform(100, 500), 2)

        hawaii.nation.national_debt += (hawaii.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -hawaii.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        hawaii.exports = round(random.uniform(250, 350), 2)
        hawaii.imports = round(random.uniform(320, 860), 2)
        hawaii.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                             (hawaii.exports - hawaii.imports))
        """implementing two ways of expanding regional and national gdp"""
        hawaii.nation.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                                       (hawaii.exports - hawaii.imports))

def depression(hawaii):
    if hawaii.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        hawaii.consumer_spending = -round(random.uniform(10, 550), 2)
        hawaii.investment = -round(random.uniform(25, 750), 2)

        hawaii.government_spending = round(random.uniform(100, 1400), 2)

        hawaii.nation.national_debt += (hawaii.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -hawaii.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        hawaii.exports = round(random.uniform(250, 750), 2)
        hawaii.imports = round(random.uniform(320, 760), 2)
        hawaii.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                             (hawaii.exports - hawaii.imports))
        """implementing two ways of expanding regional and national gdp"""
        hawaii.nation.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                                       (hawaii.exports - hawaii.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        hawaii.consumer_spending = -round(random.uniform(10, 350), 2)
        hawaii.investment = -round(random.uniform(25, 550), 2)

        hawaii.government_spending = round(random.uniform(100, 500), 2)

        hawaii.nation.national_debt += (hawaii.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -hawaii.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        hawaii.exports = round(random.uniform(250, 350), 2)
        hawaii.imports = round(random.uniform(320, 1200), 2)
        hawaii.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                             (hawaii.exports - hawaii.imports))
        """implementing two ways of expanding regional and national gdp"""
        hawaii.nation.current_gdp += (hawaii.consumer_spending + hawaii.investment + hawaii.government_spending +
                (hawaii.exports - hawaii.imports))

def economic_growth(hawaii):
    """Economic growth of iowa as individual state"""
    if hawaii.economic_state == "recovery":
        recovery(hawaii)

    elif hawaii.economic_state == "depression":
        depression(hawaii)

    elif hawaii.economic_state == "recession":
        recession(hawaii)

    elif hawaii.economic_state == "expansion":
        expansion(hawaii)

class Hawaii:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Hawaii"
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