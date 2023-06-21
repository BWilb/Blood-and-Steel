import random

population = {
    "1910": 16246,
    "1914": 17302,
    "1918": 18448,
    "1932": 29542,
    "1936": 30438,
    "1939": 34011
}

gdp = {
    "1910": 29000,
    "1914": 29937,
    "1918": 38900,
    "1932": 36899,
    "1936": 37103,
    "1939": 38904
}
def population_growth(idaho):
    births = random.randrange(1, 9)
    deaths = random.randrange(1, 8)
    idaho.population += (births - deaths)
    idaho.nation.current_pop += (births - deaths)
    idaho.nation.births += births
    idaho.nation.deaths += deaths

"""economic_functions"""
def recovery(idaho):
    if idaho.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        idaho.consumer_spending = round(random.uniform(10, 75), 2)
        idaho.investment = round(random.uniform(25, 250), 2)

        idaho.government_spending = round(random.uniform(100, 500), 2)

        idaho.nation.national_debt += (idaho.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             idaho.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        idaho.exports = round(random.uniform(450, 750), 2)
        idaho.imports = round(random.uniform(320, 560), 2)
        idaho.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                             (idaho.exports - idaho.imports))
        """implementing two ways of expanding regional and national gdp"""
        idaho.nation.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                                       (idaho.exports - idaho.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        idaho.consumer_spending = round(random.uniform(10, 250), 2)
        idaho.investment = round(random.uniform(25, 350), 2)

        idaho.government_spending = round(random.uniform(100, 800), 2)

        idaho.nation.national_debt += (idaho.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               idaho.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        idaho.exports = round(random.uniform(450, 750), 2)
        idaho.imports = round(random.uniform(320, 560), 2)
        idaho.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                             (idaho.exports - idaho.imports))
        """implementing two ways of expanding regional and national gdp"""
        idaho.nation.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                                       (idaho.exports - idaho.imports))
def expansion(idaho):
    if idaho.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        idaho.consumer_spending = round(random.uniform(10, 550), 2)
        idaho.investment = round(random.uniform(25, 750), 2)

        idaho.government_spending = round(random.uniform(100, 1000), 2)

        idaho.nation.national_debt += (idaho.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               idaho.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        idaho.exports = round(random.uniform(450, 1150), 2)
        idaho.imports = round(random.uniform(320, 760), 2)
        idaho.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                             (idaho.exports - idaho.imports))
        """implementing two ways of expanding regional and national gdp"""
        idaho.nation.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                                       (idaho.exports - idaho.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        idaho.consumer_spending = round(random.uniform(10, 550), 2)
        idaho.investment = round(random.uniform(25, 750), 2)

        idaho.government_spending = round(random.uniform(100, 1200), 2)

        idaho.nation.national_debt += (idaho.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               idaho.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        idaho.exports = round(random.uniform(450, 1150), 2)
        idaho.imports = round(random.uniform(320, 760), 2)
        idaho.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                             (idaho.exports - idaho.imports))
        """implementing two ways of expanding regional and national gdp"""
        idaho.nation.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                                       (idaho.exports - idaho.imports))

def recession(idaho):
    if idaho.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        idaho.consumer_spending = -round(random.uniform(10, 250), 2)
        idaho.investment = -round(random.uniform(25, 350), 2)

        idaho.government_spending = round(random.uniform(100, 300), 2)

        idaho.nation.national_debt += (idaho.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -idaho.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        idaho.exports = round(random.uniform(250, 450), 2)
        idaho.imports = round(random.uniform(320, 760), 2)
        idaho.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                             (idaho.exports - idaho.imports))
        """implementing two ways of expanding regional and national gdp"""
        idaho.nation.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                                       (idaho.exports - idaho.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        idaho.consumer_spending = -round(random.uniform(10, 350), 2)
        idaho.investment = -round(random.uniform(25, 550), 2)

        idaho.government_spending = round(random.uniform(100, 500), 2)

        idaho.nation.national_debt += (idaho.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -idaho.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        idaho.exports = round(random.uniform(250, 350), 2)
        idaho.imports = round(random.uniform(320, 860), 2)
        idaho.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                             (idaho.exports - idaho.imports))
        """implementing two ways of expanding regional and national gdp"""
        idaho.nation.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                                       (idaho.exports - idaho.imports))

def depression(idaho):
    if idaho.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        idaho.consumer_spending = -round(random.uniform(10, 550), 2)
        idaho.investment = -round(random.uniform(25, 750), 2)

        idaho.government_spending = round(random.uniform(100, 1400), 2)

        idaho.nation.national_debt += (idaho.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -idaho.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        idaho.exports = round(random.uniform(250, 750), 2)
        idaho.imports = round(random.uniform(320, 760), 2)
        idaho.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                             (idaho.exports - idaho.imports))
        """implementing two ways of expanding regional and national gdp"""
        idaho.nation.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                                       (idaho.exports - idaho.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        idaho.consumer_spending = -round(random.uniform(10, 350), 2)
        idaho.investment = -round(random.uniform(25, 550), 2)

        idaho.government_spending = round(random.uniform(100, 500), 2)

        idaho.nation.national_debt += (idaho.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -idaho.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        idaho.exports = round(random.uniform(250, 350), 2)
        idaho.imports = round(random.uniform(320, 1200), 2)
        idaho.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                             (idaho.exports - idaho.imports))
        """implementing two ways of expanding regional and national gdp"""
        idaho.nation.current_gdp += (idaho.consumer_spending + idaho.investment + idaho.government_spending +
                (idaho.exports - idaho.imports))

def economic_growth(idaho):
    """Economic growth of iowa as individual state"""
    if idaho.economic_state == "recovery":
        recovery(idaho)

    elif idaho.economic_state == "depression":
        depression(idaho)

    elif idaho.economic_state == "recession":
        recession(idaho)

    elif idaho.economic_state == "expansion":
        expansion(idaho)

class Idaho:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Idaho"
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