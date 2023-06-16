import random

population = {
    "1910": 2293163,
    "1914": 2342062,
    "1918": 2395829,
    "1932": 2686780,
    "1936": 2761403,
    "1939": 2826728
}

gdp = {
    "1910": 703409,
    "1914": 739029,
    "1918": 758648,
    "1932": 737573,
    "1936": 739824,
    "1939": 742358
}
def population_growth(kentucky):
    births = random.randrange(1, 10)
    deaths = random.randrange(1, 10)
    kentucky.population += (births - deaths)
    kentucky.nation.current_pop += (births - deaths)

"""economic_functions"""
def recovery(kentucky):
    if kentucky.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        kentucky.consumer_spending = round(random.uniform(10, 75), 2)
        kentucky.investment = round(random.uniform(25, 250), 2)

        kentucky.government_spending = round(random.uniform(100, 500), 2)

        kentucky.nation.national_debt += (kentucky.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             kentucky.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kentucky.exports = round(random.uniform(450, 750), 2)
        kentucky.imports = round(random.uniform(320, 560), 2)
        kentucky.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                             (kentucky.exports - kentucky.imports))
        """implementing two ways of expanding regional and national gdp"""
        kentucky.nation.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                                       (kentucky.exports - kentucky.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        kentucky.consumer_spending = round(random.uniform(10, 250), 2)
        kentucky.investment = round(random.uniform(25, 350), 2)

        kentucky.government_spending = round(random.uniform(100, 800), 2)

        kentucky.nation.national_debt += (kentucky.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               kentucky.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kentucky.exports = round(random.uniform(450, 750), 2)
        kentucky.imports = round(random.uniform(320, 560), 2)
        kentucky.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                             (kentucky.exports - kentucky.imports))
        """implementing two ways of expanding regional and national gdp"""
        kentucky.nation.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                                       (kentucky.exports - kentucky.imports))
def expansion(kentucky):
    if kentucky.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        kentucky.consumer_spending = round(random.uniform(10, 550), 2)
        kentucky.investment = round(random.uniform(25, 750), 2)

        kentucky.government_spending = round(random.uniform(100, 1000), 2)

        kentucky.nation.national_debt += (kentucky.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               kentucky.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kentucky.exports = round(random.uniform(450, 1150), 2)
        kentucky.imports = round(random.uniform(320, 760), 2)
        kentucky.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                             (kentucky.exports - kentucky.imports))
        """implementing two ways of expanding regional and national gdp"""
        kentucky.nation.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                                       (kentucky.exports - kentucky.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        kentucky.consumer_spending = round(random.uniform(10, 550), 2)
        kentucky.investment = round(random.uniform(25, 750), 2)

        kentucky.government_spending = round(random.uniform(100, 1200), 2)

        kentucky.nation.national_debt += (kentucky.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               kentucky.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kentucky.exports = round(random.uniform(450, 1150), 2)
        kentucky.imports = round(random.uniform(320, 760), 2)
        kentucky.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                             (kentucky.exports - kentucky.imports))
        """implementing two ways of expanding regional and national gdp"""
        kentucky.nation.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                                       (kentucky.exports - kentucky.imports))

def recession(kentucky):
    if kentucky.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        kentucky.consumer_spending = -round(random.uniform(10, 250), 2)
        kentucky.investment = -round(random.uniform(25, 350), 2)

        kentucky.government_spending = round(random.uniform(100, 300), 2)

        kentucky.nation.national_debt += (kentucky.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -kentucky.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kentucky.exports = round(random.uniform(250, 450), 2)
        kentucky.imports = round(random.uniform(320, 760), 2)
        kentucky.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                             (kentucky.exports - kentucky.imports))
        """implementing two ways of expanding regional and national gdp"""
        kentucky.nation.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                                       (kentucky.exports - kentucky.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        kentucky.consumer_spending = -round(random.uniform(10, 350), 2)
        kentucky.investment = -round(random.uniform(25, 550), 2)

        kentucky.government_spending = round(random.uniform(100, 500), 2)

        kentucky.nation.national_debt += (kentucky.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -kentucky.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kentucky.exports = round(random.uniform(250, 350), 2)
        kentucky.imports = round(random.uniform(320, 860), 2)
        kentucky.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                             (kentucky.exports - kentucky.imports))
        """implementing two ways of expanding regional and national gdp"""
        kentucky.nation.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                                       (kentucky.exports - kentucky.imports))

def depression(kentucky):
    if kentucky.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        kentucky.consumer_spending = -round(random.uniform(10, 550), 2)
        kentucky.investment = -round(random.uniform(25, 750), 2)

        kentucky.government_spending = round(random.uniform(100, 1400), 2)

        kentucky.nation.national_debt += (kentucky.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -kentucky.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kentucky.exports = round(random.uniform(250, 750), 2)
        kentucky.imports = round(random.uniform(320, 760), 2)
        kentucky.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                             (kentucky.exports - kentucky.imports))
        """implementing two ways of expanding regional and national gdp"""
        kentucky.nation.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                                       (kentucky.exports - kentucky.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        kentucky.consumer_spending = -round(random.uniform(10, 350), 2)
        kentucky.investment = -round(random.uniform(25, 550), 2)

        kentucky.government_spending = round(random.uniform(100, 500), 2)

        kentucky.nation.national_debt += (kentucky.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -kentucky.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        kentucky.exports = round(random.uniform(250, 350), 2)
        kentucky.imports = round(random.uniform(320, 1200), 2)
        kentucky.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                             (kentucky.exports - kentucky.imports))
        """implementing two ways of expanding regional and national gdp"""
        kentucky.nation.current_gdp += (kentucky.consumer_spending + kentucky.investment + kentucky.government_spending +
                (kentucky.exports - kentucky.imports))

def economic_growth(kentucky):
    """Economic growth of iowa as individual state"""
    if kentucky.economic_state == "recovery":
        recovery(kentucky)

    elif kentucky.economic_state == "depression":
        depression(kentucky)

    elif kentucky.economic_state == "recession":
        recession(kentucky)

    elif kentucky.economic_state == "expansion":
        expansion(kentucky)

class Kentucky:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Kentucky"
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