import random

population = {
    "1910": 2093902,
    "1914": 2207315,
    "1918": 3500657,
    "1932": 2332621,
    "1936": 2617493,
    "1939": 2770204
}

gdp = {
    "1910": 30500000000,
    "1914": 35093747000,
    "1918": 38900098000,
    "1932": 37890984000,
    "1936": 42103059000,
    "1939": 43900309000
}
def population_growth(minnesota):
    births = random.randrange(1, 20)
    deaths = random.randrange(1, 15)
    minnesota.population += (births - deaths)
    minnesota.nation.current_pop += (births - deaths)
    minnesota.nation.births += births
    minnesota.nation.deaths += deaths

"""economic_functions"""
def recovery(minnesota):
    if minnesota.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        minnesota.consumer_spending = round(random.uniform(10, 75), 2)
        minnesota.investment = round(random.uniform(25, 250), 2)

        minnesota.government_spending = round(random.uniform(100, 500), 2)

        minnesota.nation.national_debt += (minnesota.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             minnesota.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        minnesota.exports = round(random.uniform(450, 750), 2)
        minnesota.imports = round(random.uniform(320, 560), 2)
        minnesota.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                             (minnesota.exports - minnesota.imports))
        """implementing two ways of expanding regional and national gdp"""
        minnesota.nation.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                                       (minnesota.exports - minnesota.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        minnesota.consumer_spending = round(random.uniform(10, 250), 2)
        minnesota.investment = round(random.uniform(25, 350), 2)

        minnesota.government_spending = round(random.uniform(100, 800), 2)

        minnesota.nation.national_debt += (minnesota.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               minnesota.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        minnesota.exports = round(random.uniform(450, 750), 2)
        minnesota.imports = round(random.uniform(320, 560), 2)
        minnesota.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                             (minnesota.exports - minnesota.imports))
        """implementing two ways of expanding regional and national gdp"""
        minnesota.nation.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                                       (minnesota.exports - minnesota.imports))
def expansion(minnesota):
    if minnesota.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        minnesota.consumer_spending = round(random.uniform(10, 550), 2)
        minnesota.investment = round(random.uniform(25, 750), 2)

        minnesota.government_spending = round(random.uniform(100, 1000), 2)

        minnesota.nation.national_debt += (minnesota.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               minnesota.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        minnesota.exports = round(random.uniform(450, 1150), 2)
        minnesota.imports = round(random.uniform(320, 760), 2)
        minnesota.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                             (minnesota.exports - minnesota.imports))
        """implementing two ways of expanding regional and national gdp"""
        minnesota.nation.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                                       (minnesota.exports - minnesota.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        minnesota.consumer_spending = round(random.uniform(10, 550), 2)
        minnesota.investment = round(random.uniform(25, 750), 2)

        minnesota.government_spending = round(random.uniform(100, 1200), 2)

        minnesota.nation.national_debt += (minnesota.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               minnesota.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        minnesota.exports = round(random.uniform(450, 1150), 2)
        minnesota.imports = round(random.uniform(320, 760), 2)
        minnesota.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                             (minnesota.exports - minnesota.imports))
        """implementing two ways of expanding regional and national gdp"""
        minnesota.nation.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                                       (minnesota.exports - minnesota.imports))

def recession(minnesota):
    if minnesota.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        minnesota.consumer_spending = -round(random.uniform(10, 250), 2)
        minnesota.investment = -round(random.uniform(25, 350), 2)

        minnesota.government_spending = round(random.uniform(100, 300), 2)

        minnesota.nation.national_debt += (minnesota.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -minnesota.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        minnesota.exports = round(random.uniform(250, 450), 2)
        minnesota.imports = round(random.uniform(320, 760), 2)
        minnesota.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                             (minnesota.exports - minnesota.imports))
        """implementing two ways of expanding regional and national gdp"""
        minnesota.nation.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                                       (minnesota.exports - minnesota.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        minnesota.consumer_spending = -round(random.uniform(10, 350), 2)
        minnesota.investment = -round(random.uniform(25, 550), 2)

        minnesota.government_spending = round(random.uniform(100, 500), 2)

        minnesota.nation.national_debt += (minnesota.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -minnesota.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        minnesota.exports = round(random.uniform(250, 350), 2)
        minnesota.imports = round(random.uniform(320, 860), 2)
        minnesota.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                             (minnesota.exports - minnesota.imports))
        """implementing two ways of expanding regional and national gdp"""
        minnesota.nation.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                                       (minnesota.exports - minnesota.imports))

def depression(minnesota):
    if minnesota.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        minnesota.consumer_spending = -round(random.uniform(10, 550), 2)
        minnesota.investment = -round(random.uniform(25, 750), 2)

        minnesota.government_spending = round(random.uniform(100, 1400), 2)

        minnesota.nation.national_debt += (minnesota.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -minnesota.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        minnesota.exports = round(random.uniform(250, 750), 2)
        minnesota.imports = round(random.uniform(320, 760), 2)
        minnesota.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                             (minnesota.exports - minnesota.imports))
        """implementing two ways of expanding regional and national gdp"""
        minnesota.nation.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                                       (minnesota.exports - minnesota.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        minnesota.consumer_spending = -round(random.uniform(10, 350), 2)
        minnesota.investment = -round(random.uniform(25, 550), 2)

        minnesota.government_spending = round(random.uniform(100, 500), 2)

        minnesota.nation.national_debt += (minnesota.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -minnesota.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        minnesota.exports = round(random.uniform(250, 350), 2)
        minnesota.imports = round(random.uniform(320, 1200), 2)
        minnesota.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                             (minnesota.exports - minnesota.imports))
        """implementing two ways of expanding regional and national gdp"""
        minnesota.nation.current_gdp += (minnesota.consumer_spending + minnesota.investment + minnesota.government_spending +
                (minnesota.exports - minnesota.imports))

def economic_growth(minnesota):
    """Economic growth of iowa as individual state"""
    if minnesota.economic_state == "recovery":
        recovery(minnesota)

    elif minnesota.economic_state == "depression":
        depression(minnesota)

    elif minnesota.economic_state == "recession":
        recession(minnesota)

    elif minnesota.economic_state == "expansion":
        expansion(minnesota)

class Minnesota:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Minnesota"
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