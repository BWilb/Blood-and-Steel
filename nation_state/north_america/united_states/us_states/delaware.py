import random

population = {
    "1910": 202322,
    "1914": 204964,
    "1918": 208949,
    "1932": 223923,
    "1936": 226593,
    "1939": 229938
}

gdp = {
    "1910": 310190,
    "1914": 318332,
    "1918": 349458,
    "1932": 323493,
    "1936": 345923,
    "1939": 356934
}
def population_growth(delaware):
    births = random.randrange(1, 12)
    deaths = random.randrange(1, 8)
    delaware.population += (births - deaths)
    delaware.nation.current_pop += (births - deaths)
    delaware.nation.births += births
    delaware.nation.deaths += deaths

"""economic_functions"""
def recovery(delaware):
    if delaware.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        delaware.consumer_spending = round(random.uniform(10, 75), 2)
        delaware.investment = round(random.uniform(25, 100), 2)

        delaware.government_spending = round(random.uniform(100, 500), 2)

        delaware.debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        delaware.nation.national_debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        delaware.exports = round(random.uniform(150, 350), 2)
        delaware.imports = round(random.uniform(20, 260), 2)
        delaware.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                             (delaware.exports - delaware.imports))
        """implementing two ways of expanding regional and national gdp"""
        delaware.nation.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                                      (delaware.exports - delaware.imports))

    else:
        """If United States has implemented an economic stimulus"""
        delaware.consumer_spending = round(random.uniform(10, 55), 2)
        delaware.investment = round(random.uniform(25, 80), 2)

        delaware.government_spending = round(random.uniform(100, 750), 2)

        delaware.debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))

        delaware.nation.national_debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        delaware.exports = round(random.uniform(150, 250), 2)
        delaware.imports = round(random.uniform(20, 160), 2)
        delaware.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                             (delaware.exports - delaware.imports))
        """implementing two ways of expanding regional and national gdp"""
        delaware.nation.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                                      (delaware.exports - delaware.imports))
def expansion(delaware):
    if delaware.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        delaware.consumer_spending = round(random.uniform(10, 450), 2)
        delaware.investment = round(random.uniform(25, 350), 2)

        delaware.government_spending = round(random.uniform(100, 1000), 2)

        delaware.nation.national_debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        delaware.exports = round(random.uniform(450, 1150), 2)
        delaware.imports = round(random.uniform(320, 760), 2)
        delaware.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                             (delaware.exports - delaware.imports))
        """implementing two ways of expanding regional and national gdp"""
        delaware.nation.current_gdp += (
                    delaware.consumer_spending + delaware.investment + delaware.government_spending +
                    (delaware.exports - delaware.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        delaware.consumer_spending = round(random.uniform(10, 550), 2)
        delaware.investment = round(random.uniform(25, 750), 2)

        delaware.government_spending = round(random.uniform(100, 1200), 2)

        delaware.nation.national_debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        delaware.exports = round(random.uniform(450, 1150), 2)
        delaware.imports = round(random.uniform(320, 760), 2)
        delaware.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                             (delaware.exports - delaware.imports))
        """implementing two ways of expanding regional and national gdp"""
        delaware.nation.current_gdp += (
                    delaware.consumer_spending + delaware.investment + delaware.government_spending +
                    (delaware.exports - delaware.imports))

def recession(delaware):
    if delaware.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        delaware.consumer_spending = -round(random.uniform(10, 250), 2)
        delaware.investment = -round(random.uniform(25, 350), 2)

        delaware.government_spending = round(random.uniform(100, 300), 2)

        delaware.nation.national_debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        delaware.exports = round(random.uniform(250, 450), 2)
        delaware.imports = round(random.uniform(320, 760), 2)
        delaware.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                             (delaware.exports - delaware.imports))
        """implementing two ways of expanding regional and national gdp"""
        delaware.nation.current_gdp += (
                    delaware.consumer_spending + delaware.investment + delaware.government_spending +
                    (delaware.exports - delaware.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        delaware.consumer_spending = -round(random.uniform(10, 350), 2)
        delaware.investment = -round(random.uniform(25, 550), 2)

        delaware.government_spending = round(random.uniform(100, 500), 2)

        delaware.nation.national_debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        delaware.exports = round(random.uniform(250, 350), 2)
        delaware.imports = round(random.uniform(320, 860), 2)
        delaware.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                             (delaware.exports - delaware.imports))
        """implementing two ways of expanding regional and national gdp"""
        delaware.nation.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                                      (delaware.exports - delaware.imports))

def depression(delaware):
    if delaware.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        delaware.consumer_spending = -round(random.uniform(10, 550), 2)
        delaware.investment = -round(random.uniform(25, 750), 2)

        delaware.government_spending = round(random.uniform(100, 1400), 2)

        delaware.nation.national_debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        delaware.exports = round(random.uniform(250, 550), 2)
        delaware.imports = round(random.uniform(320, 760), 2)
        delaware.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                             (delaware.exports - delaware.imports))
        """implementing two ways of expanding regional and national gdp"""
        delaware.nation.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                                      (delaware.exportsconnecticutcticut.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        delaware.consumer_spending = -round(random.uniform(10, 350), 2)
        delaware.investment = -round(random.uniform(25, 550), 2)

        delaware.government_spending = round(random.uniform(100, 500), 2)

        delaware.nation.national_debt += (delaware.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -delaware.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        delaware.exports = round(random.uniform(250, 350), 2)
        delaware.imports = round(random.uniform(320, 1200), 2)
        delaware.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                             (delaware.exports - delaware.imports))
        """implementing two ways of expanding regional and national gdp"""
        delaware.nation.current_gdp += (delaware.consumer_spending + delaware.investment + delaware.government_spending +
                (delaware.exports - delaware.imports))

def economic_growth(delaware):
    """Economic growth of iowa as individual state"""
    if delaware.economic_state == "recovery":
        recovery(delaware)

    elif delaware.economic_state == "depression":
        depression(delaware)

    elif delaware.economic_state == "recession":
        recession(delaware)

    elif delaware.economic_state == "expansion":
        expansion(delaware)

class Delaware:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Delaware"
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