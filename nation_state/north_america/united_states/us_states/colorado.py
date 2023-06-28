import random

population = {
    "1910": 799024,
    "1914": 808232,
    "1918": 819238,
    "1932": 852390,
    "1936": 864933,
    "1939": 872362
}

gdp = {
    "1910": 498549,
    "1914": 512492,
    "1918": 532428,
    "1932": 501284,
    "1936": 545873,
    "1939": 567348
}
def population_growth(colorado):
    births = random.randrange(1, 9)
    deaths = random.randrange(1, 5)
    colorado.population += (births - deaths)
    colorado.nation.current_pop += (births - deaths)
    colorado.nation.births += births
    colorado.nation.deaths += deaths

"""economic_functions"""
def recovery(colorado):
    if colorado.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        colorado.consumer_spending = round(random.uniform(10, 55), 2)
        colorado.investment = round(random.uniform(25, 50), 2)

        colorado.government_spending = round(random.uniform(100, 500), 2)

        colorado.debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        colorado.nation.national_debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        colorado.exports = round(random.uniform(150, 350), 2)
        colorado.imports = round(random.uniform(20, 160), 2)
        colorado.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                             (colorado.exports - colorado.imports))
        """implementing two ways of expanding regional and national gdp"""
        colorado.nation.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                                      (colorado.exports - colorado.imports))

    else:
        """If United States has implemented an economic stimulus"""
        colorado.consumer_spending = round(random.uniform(10, 35), 2)
        colorado.investment = round(random.uniform(25, 40), 2)

        colorado.government_spending = round(random.uniform(100, 750), 2)

        colorado.debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))

        colorado.nation.national_debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        colorado.exports = round(random.uniform(150, 350), 2)
        colorado.imports = round(random.uniform(20, 260), 2)
        colorado.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                             (colorado.exports - colorado.imports))
        """implementing two ways of expanding regional and national gdp"""
        colorado.nation.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                                      (colorado.exports - colorado.imports))
def expansion(colorado):
    if colorado.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        colorado.consumer_spending = round(random.uniform(10, 250), 2)
        colorado.investment = round(random.uniform(25, 350), 2)

        colorado.government_spending = round(random.uniform(100, 1000), 2)

        colorado.nation.national_debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        colorado.exports = round(random.uniform(450, 1150), 2)
        colorado.imports = round(random.uniform(320, 760), 2)
        colorado.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                             (colorado.exports - colorado.imports))
        """implementing two ways of expanding regional and national gdp"""
        colorado.nation.current_gdp += (
                    colorado.consumer_spending + colorado.investment + colorado.government_spending +
                    (colorado.exports - colorado.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        colorado.consumer_spending = round(random.uniform(10, 150), 2)
        colorado.investment = round(random.uniform(25, 250), 2)

        colorado.government_spending = round(random.uniform(100, 1200), 2)

        colorado.nation.national_debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        colorado.exports = round(random.uniform(450, 1150), 2)
        colorado.imports = round(random.uniform(320, 760), 2)
        colorado.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                             (colorado.exports - colorado.imports))
        """implementing two ways of expanding regional and national gdp"""
        colorado.nation.current_gdp += (
                    colorado.consumer_spending + colorado.investment + colorado.government_spending +
                    (colorado.exports - colorado.imports))

def recession(colorado):
    if colorado.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        colorado.consumer_spending = -round(random.uniform(10, 250), 2)
        colorado.investment = -round(random.uniform(25, 350), 2)

        colorado.government_spending = round(random.uniform(100, 300), 2)

        colorado.nation.national_debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        colorado.exports = round(random.uniform(250, 450), 2)
        colorado.imports = round(random.uniform(320, 760), 2)
        colorado.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                             (colorado.exports - colorado.imports))
        """implementing two ways of expanding regional and national gdp"""
        colorado.nation.current_gdp += (
                    colorado.consumer_spending + colorado.investment + colorado.government_spending +
                    (colorado.exports - colorado.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        colorado.consumer_spending = -round(random.uniform(10, 350), 2)
        colorado.investment = -round(random.uniform(25, 550), 2)

        colorado.government_spending = round(random.uniform(100, 500), 2)

        colorado.nation.national_debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        colorado.exports = round(random.uniform(250, 350), 2)
        colorado.imports = round(random.uniform(320, 860), 2)
        colorado.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                             (colorado.exports - colorado.imports))
        """implementing two ways of expanding regional and national gdp"""
        colorado.nation.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                                      (colorado.exports - colorado.imports))

def depression(colorado):
    if colorado.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        colorado.consumer_spending = -round(random.uniform(10, 550), 2)
        colorado.investment = -round(random.uniform(25, 750), 2)

        colorado.government_spending = round(random.uniform(100, 1400), 2)

        colorado.nation.national_debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        colorado.exports = round(random.uniform(250, 750), 2)
        colorado.imports = round(random.uniform(320, 760), 2)
        colorado.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                             (colorado.exports - colorado.imports))
        """implementing two ways of expanding regional and national gdp"""
        colorado.nation.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                                      (colorado.exports - colorado.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        colorado.consumer_spending = -round(random.uniform(10, 350), 2)
        colorado.investment = -round(random.uniform(25, 550), 2)

        colorado.government_spending = round(random.uniform(100, 500), 2)

        colorado.nation.national_debt += (colorado.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -colorado.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        colorado.exports = round(random.uniform(250, 350), 2)
        colorado.imports = round(random.uniform(320, 1200), 2)
        colorado.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                             (colorado.exports - colorado.imports))
        """implementing two ways of expanding regional and national gdp"""
        colorado.nation.current_gdp += (colorado.consumer_spending + colorado.investment + colorado.government_spending +
                (colorado.exports - colorado.imports))

def economic_growth(colorado):
    """Economic growth of iowa as individual state"""
    if colorado.economic_state == "recovery":
        recovery(colorado)

    elif colorado.economic_state == "depression":
        depression(colorado)

    elif colorado.economic_state == "recession":
        recession(colorado)

    elif colorado.economic_state == "expansion":
        expansion(colorado)

class Colorado:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Colorado"
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