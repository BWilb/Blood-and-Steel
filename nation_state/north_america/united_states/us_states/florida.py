import random

population = {
    "1910": 384206,
    "1914": 332574,
    "1918": 401150,
    "1932": 428952,
    "1936": 436109,
    "1939": 441716
}

gdp = {
    "1910": 2900000,
    "1914": 2993747,
    "1918": 3890098,
    "1932": 3689984,
    "1936": 3710359,
    "1939": 3890039
}
def population_growth(florida):
    births = random.randrange(10, 30)
    deaths = random.randrange(5, 20)
    florida.population += (births - deaths)
    florida.nation.current_pop += (births - deaths)
    florida.nation.births += births
    florida.nation.deaths += deaths

"""economic_functions"""
def recovery(florida):
    if florida.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        florida.consumer_spending = round(random.uniform(10, 75), 2)
        florida.investment = round(random.uniform(25, 250), 2)

        florida.government_spending = round(random.uniform(100, 500), 2)

        florida.nation.national_debt += (florida.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             florida.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        florida.exports = round(random.uniform(450, 750), 2)
        florida.imports = round(random.uniform(320, 560), 2)
        florida.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                             (florida.exports - florida.imports))
        """implementing two ways of expanding regional and national gdp"""
        florida.nation.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                                       (florida.exports - florida.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        florida.consumer_spending = round(random.uniform(10, 250), 2)
        florida.investment = round(random.uniform(25, 350), 2)

        florida.government_spending = round(random.uniform(100, 800), 2)

        florida.nation.national_debt += (florida.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               florida.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        florida.exports = round(random.uniform(450, 750), 2)
        florida.imports = round(random.uniform(320, 560), 2)
        florida.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                             (florida.exports - florida.imports))
        """implementing two ways of expanding regional and national gdp"""
        florida.nation.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                                       (florida.exports - florida.imports))
def expansion(florida):
    if florida.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        florida.consumer_spending = round(random.uniform(10, 550), 2)
        florida.investment = round(random.uniform(25, 750), 2)

        florida.government_spending = round(random.uniform(100, 1000), 2)

        florida.nation.national_debt += (florida.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               florida.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        florida.exports = round(random.uniform(450, 1150), 2)
        florida.imports = round(random.uniform(320, 760), 2)
        florida.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                             (florida.exports - florida.imports))
        """implementing two ways of expanding regional and national gdp"""
        florida.nation.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                                       (florida.exports - florida.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        florida.consumer_spending = round(random.uniform(10, 550), 2)
        florida.investment = round(random.uniform(25, 750), 2)

        florida.government_spending = round(random.uniform(100, 1200), 2)

        florida.nation.national_debt += (florida.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               florida.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        florida.exports = round(random.uniform(450, 1150), 2)
        florida.imports = round(random.uniform(320, 760), 2)
        florida.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                             (florida.exports - florida.imports))
        """implementing two ways of expanding regional and national gdp"""
        florida.nation.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                                       (florida.exports - florida.imports))

def recession(florida):
    if florida.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        florida.consumer_spending = -round(random.uniform(10, 250), 2)
        florida.investment = -round(random.uniform(25, 350), 2)

        florida.government_spending = round(random.uniform(100, 300), 2)

        florida.nation.national_debt += (florida.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -florida.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        florida.exports = round(random.uniform(250, 450), 2)
        florida.imports = round(random.uniform(320, 760), 2)
        florida.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                             (florida.exports - florida.imports))
        """implementing two ways of expanding regional and national gdp"""
        florida.nation.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                                       (florida.exports - florida.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        florida.consumer_spending = -round(random.uniform(10, 350), 2)
        florida.investment = -round(random.uniform(25, 550), 2)

        florida.government_spending = round(random.uniform(100, 500), 2)

        florida.nation.national_debt += (florida.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -florida.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        florida.exports = round(random.uniform(250, 350), 2)
        florida.imports = round(random.uniform(320, 860), 2)
        florida.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                             (florida.exports - florida.imports))
        """implementing two ways of expanding regional and national gdp"""
        florida.nation.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                                       (florida.exports - florida.imports))

def depression(florida):
    if florida.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        florida.consumer_spending = -round(random.uniform(10, 550), 2)
        florida.investment = -round(random.uniform(25, 750), 2)

        florida.government_spending = round(random.uniform(100, 1400), 2)

        florida.nation.national_debt += (florida.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -florida.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        florida.exports = round(random.uniform(250, 750), 2)
        florida.imports = round(random.uniform(320, 760), 2)
        florida.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                             (florida.exports - florida.imports))
        """implementing two ways of expanding regional and national gdp"""
        florida.nation.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                                       (florida.exports - florida.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        florida.consumer_spending = -round(random.uniform(10, 350), 2)
        florida.investment = -round(random.uniform(25, 550), 2)

        florida.government_spending = round(random.uniform(100, 500), 2)

        florida.nation.national_debt += (florida.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -florida.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        florida.exports = round(random.uniform(250, 350), 2)
        florida.imports = round(random.uniform(320, 1200), 2)
        florida.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                             (florida.exports - florida.imports))
        """implementing two ways of expanding regional and national gdp"""
        florida.nation.current_gdp += (florida.consumer_spending + florida.investment + florida.government_spending +
                (florida.exports - florida.imports))

def economic_growth(florida):
    """Economic growth of iowa as individual state"""
    if florida.economic_state == "recovery":
        recovery(florida)

    elif florida.economic_state == "depression":
        depression(florida)

    elif florida.economic_state == "recession":
        recession(florida)

    elif florida.economic_state == "expansion":
        expansion(florida)

class Florida:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Florida"
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