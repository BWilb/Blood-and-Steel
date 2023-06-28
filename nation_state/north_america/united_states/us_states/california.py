import random

population = {
    "1910": 2401699,
    "1914": 2819625,
    "1918": 3240291,
    "1932": 5942241,
    "1936": 6450595,
    "1939": 6815111
}

gdp = {
    "1910": 898549,
    "1914": 912492,
    "1918": 932428,
    "1932": 901284,
    "1936": 945873,
    "1939": 967348
}
def population_growth(california):
    births = random.randrange(1, 45)
    deaths = random.randrange(1, 42)
    california.population += (births - deaths)
    california.nation.current_pop += (births - deaths)
    california.nation.births += births
    california.nation.deaths += deaths

"""economic_functions"""
def recovery(california):
    if california.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        california.consumer_spending = round(random.uniform(10, 225), 2)
        california.investment = round(random.uniform(25, 200), 2)

        california.government_spending = round(random.uniform(100, 600), 2)

        california.debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        california.nation.national_debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        california.exports = round(random.uniform(150, 650), 2)
        california.imports = round(random.uniform(20, 360), 2)
        california.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                             (california.exports - california.imports))
        """implementing two ways of expanding regional and national gdp"""
        california.nation.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                                      (california.exports - california.imports))

    else:
        """If United States has implemented an economic stimulus"""
        california.consumer_spending = round(random.uniform(10, 175), 2)
        california.investment = round(random.uniform(25, 150), 2)

        california.government_spending = round(random.uniform(100, 750), 2)

        california.debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             california.consumer_spending * round(random.uniform(0.001, 0.009), 5))

        california.nation.national_debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        california.exports = round(random.uniform(150, 550), 2)
        california.imports = round(random.uniform(20, 360), 2)
        california.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                             (california.exports - california.imports))
        """implementing two ways of expanding regional and national gdp"""
        california.nation.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                                      (california.exports - california.imports))
def expansion(california):
    if california.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        california.consumer_spending = round(random.uniform(10, 550), 2)
        california.investment = round(random.uniform(25, 750), 2)

        california.government_spending = round(random.uniform(100, 1000), 2)

        california.nation.national_debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        california.exports = round(random.uniform(450, 1450), 2)
        california.imports = round(random.uniform(320, 760), 2)
        california.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                             (california.exports - california.imports))
        """implementing two ways of expanding regional and national gdp"""
        california.nation.current_gdp += (
                    california.consumer_spending + california.investment + california.government_spending +
                    (california.exports - california.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        california.consumer_spending = round(random.uniform(10, 550), 2)
        california.investment = round(random.uniform(25, 750), 2)

        california.government_spending = round(random.uniform(100, 1800), 2)

        california.nation.national_debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        california.exports = round(random.uniform(450, 1150), 2)
        california.imports = round(random.uniform(320, 760), 2)
        california.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                             (california.exports - california.imports))
        """implementing two ways of expanding regional and national gdp"""
        california.nation.current_gdp += (
                    california.consumer_spending + california.investment + california.government_spending +
                    (california.exports - california.imports))

def recession(california):
    if california.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        california.consumer_spending = -round(random.uniform(10, 250), 2)
        california.investment = -round(random.uniform(25, 350), 2)

        california.government_spending = round(random.uniform(100, 300), 2)

        california.nation.national_debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        california.exports = round(random.uniform(250, 450), 2)
        california.imports = round(random.uniform(320, 760), 2)
        california.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                             (california.exports - california.imports))
        """implementing two ways of expanding regional and national gdp"""
        california.nation.current_gdp += (
                    california.consumer_spending + california.investment + california.government_spending +
                    (california.exports - california.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        california.consumer_spending = -round(random.uniform(10, 350), 2)
        california.investment = -round(random.uniform(25, 550), 2)

        california.government_spending = round(random.uniform(100, 500), 2)

        california.nation.national_debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        california.exports = round(random.uniform(250, 350), 2)
        california.imports = round(random.uniform(320, 860), 2)
        california.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                             (california.exports - california.imports))
        """implementing two ways of expanding regional and national gdp"""
        california.nation.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                                      (california.exports - california.imports))

def depression(california):
    if california.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        california.consumer_spending = -round(random.uniform(10, 550), 2)
        california.investment = -round(random.uniform(25, 750), 2)

        california.government_spending = round(random.uniform(100, 1400), 2)

        california.nation.national_debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        california.exports = round(random.uniform(250, 750), 2)
        california.imports = round(random.uniform(320, 760), 2)
        california.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                             (california.exports - california.imports))
        """implementing two ways of expanding regional and national gdp"""
        california.nation.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                                      (california.exports - california.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        california.consumer_spending = -round(random.uniform(10, 750), 2)
        california.investment = -round(random.uniform(25, 1050), 2)

        california.government_spending = round(random.uniform(100, 1900), 2)

        california.nation.national_debt += (california.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -california.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        california.exports = round(random.uniform(250, 350), 2)
        california.imports = round(random.uniform(320, 1200), 2)
        california.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                             (california.exports - california.imports))
        """implementing two ways of expanding regional and national gdp"""
        california.nation.current_gdp += (california.consumer_spending + california.investment + california.government_spending +
                (california.exports - california.imports))

def economic_growth(california):
    """Economic growth of iowa as individual state"""
    if california.economic_state == "recovery":
        recovery(california)

    elif california.economic_state == "depression":
        depression(california)

    elif california.economic_state == "recession":
        recession(california)

    elif california.economic_state == "expansion":
        expansion(california)

class California:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "California"
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