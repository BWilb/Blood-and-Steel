import random

population = {
    "1910": 745000,
    "1914": 772000,
    "1918": 760000,
    "1932": 815000,
    "1936": 840000,
    "1939": 846000
}

gdp = {
    "1910": 2500000,
    "1914": 2593747,
    "1918": 2890098,
    "1932": 2989984,
    "1936": 3210359,
    "1939": 3390039
}
def population_growth(maine):
    births = random.randrange(10, 20)
    deaths = random.randrange(5, 10)
    maine.population += (births - deaths)
    maine.nation.current_pop += (births - deaths)
    maine.nation.births += births
    maine.nation.deaths += deaths

"""economic_functions"""
def recovery(maine):
    if maine.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        maine.consumer_spending = round(random.uniform(10, 75), 2)
        maine.investment = round(random.uniform(25, 250), 2)

        maine.government_spending = round(random.uniform(100, 500), 2)

        maine.nation.national_debt += (maine.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             maine.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maine.exports = round(random.uniform(450, 750), 2)
        maine.imports = round(random.uniform(320, 560), 2)
        maine.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                             (maine.exports - maine.imports))
        """implementing two ways of expanding regional and national gdp"""
        maine.nation.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                                       (maine.exports - maine.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        maine.consumer_spending = round(random.uniform(10, 250), 2)
        maine.investment = round(random.uniform(25, 350), 2)

        maine.government_spending = round(random.uniform(100, 800), 2)

        maine.nation.national_debt += (maine.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               maine.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maine.exports = round(random.uniform(450, 750), 2)
        maine.imports = round(random.uniform(320, 560), 2)
        maine.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                             (maine.exports - maine.imports))
        """implementing two ways of expanding regional and national gdp"""
        maine.nation.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                                       (maine.exports - maine.imports))
def expansion(maine):
    if maine.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        maine.consumer_spending = round(random.uniform(10, 550), 2)
        maine.investment = round(random.uniform(25, 750), 2)

        maine.government_spending = round(random.uniform(100, 1000), 2)

        maine.nation.national_debt += (maine.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               maine.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maine.exports = round(random.uniform(450, 1150), 2)
        maine.imports = round(random.uniform(320, 760), 2)
        maine.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                             (maine.exports - maine.imports))
        """implementing two ways of expanding regional and national gdp"""
        maine.nation.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                                       (maine.exports - maine.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        maine.consumer_spending = round(random.uniform(10, 550), 2)
        maine.investment = round(random.uniform(25, 750), 2)

        maine.government_spending = round(random.uniform(100, 1200), 2)

        maine.nation.national_debt += (maine.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               maine.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maine.exports = round(random.uniform(450, 1150), 2)
        maine.imports = round(random.uniform(320, 760), 2)
        maine.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                             (maine.exports - maine.imports))
        """implementing two ways of expanding regional and national gdp"""
        maine.nation.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                                       (maine.exports - maine.imports))

def recession(maine):
    if maine.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        maine.consumer_spending = -round(random.uniform(10, 250), 2)
        maine.investment = -round(random.uniform(25, 350), 2)

        maine.government_spending = round(random.uniform(100, 300), 2)

        maine.nation.national_debt += (maine.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -maine.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maine.exports = round(random.uniform(250, 450), 2)
        maine.imports = round(random.uniform(320, 760), 2)
        maine.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                             (maine.exports - maine.imports))
        """implementing two ways of expanding regional and national gdp"""
        maine.nation.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                                       (maine.exports - maine.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        maine.consumer_spending = -round(random.uniform(10, 350), 2)
        maine.investment = -round(random.uniform(25, 550), 2)

        maine.government_spending = round(random.uniform(100, 500), 2)

        maine.nation.national_debt += (maine.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -maine.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maine.exports = round(random.uniform(250, 350), 2)
        maine.imports = round(random.uniform(320, 860), 2)
        maine.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                             (maine.exports - maine.imports))
        """implementing two ways of expanding regional and national gdp"""
        maine.nation.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                                       (maine.exports - maine.imports))

def depression(maine):
    if maine.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        maine.consumer_spending = -round(random.uniform(10, 550), 2)
        maine.investment = -round(random.uniform(25, 750), 2)

        maine.government_spending = round(random.uniform(100, 1400), 2)

        maine.nation.national_debt += (maine.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -maine.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maine.exports = round(random.uniform(250, 750), 2)
        maine.imports = round(random.uniform(320, 760), 2)
        maine.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                             (maine.exports - maine.imports))
        """implementing two ways of expanding regional and national gdp"""
        maine.nation.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                                       (maine.exports - maine.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        maine.consumer_spending = -round(random.uniform(10, 350), 2)
        maine.investment = -round(random.uniform(25, 550), 2)

        maine.government_spending = round(random.uniform(100, 500), 2)

        maine.nation.national_debt += (maine.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -maine.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maine.exports = round(random.uniform(250, 350), 2)
        maine.imports = round(random.uniform(320, 1200), 2)
        maine.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                             (maine.exports - maine.imports))
        """implementing two ways of expanding regional and national gdp"""
        maine.nation.current_gdp += (maine.consumer_spending + maine.investment + maine.government_spending +
                (maine.exports - maine.imports))

def economic_growth(maine):
    """Economic growth of iowa as individual state"""
    if maine.economic_state == "recovery":
        recovery(maine)

    elif maine.economic_state == "depression":
        depression(maine)

    elif maine.economic_state == "recession":
        recession(maine)

    elif maine.economic_state == "expansion":
        expansion(maine)

class Maine:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Maine"
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