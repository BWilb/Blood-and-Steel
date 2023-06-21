import random

population = {
    "1910": 5658078,
    "1914": 6001048,
    "1918": 6339377,
    "1932": 7693160,
    "1936": 7794630,
    "1939": 7880490
}

gdp = {
    "1910": 834736370,
    "1914": 839029472,
    "1918": 858648373,
    "1932": 837573626,
    "1936": 839824723,
    "1939": 842358373
}
def population_growth(illinois):
    births = random.randrange(1, 30)
    deaths = random.randrange(1, 25)
    illinois.population += (births - deaths)
    illinois.nation.current_pop += (births - deaths)
    illinois.nation.births += births
    illinois.nation.deaths += deaths

"""economic_functions"""
def recovery(illinois):
    if illinois.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        illinois.consumer_spending = round(random.uniform(10, 75), 2)
        illinois.investment = round(random.uniform(25, 250), 2)

        illinois.government_spending = round(random.uniform(100, 500), 2)

        illinois.nation.national_debt += (illinois.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             illinois.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        illinois.exports = round(random.uniform(450, 750), 2)
        illinois.imports = round(random.uniform(320, 560), 2)
        illinois.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                             (illinois.exports - illinois.imports))
        """implementing two ways of expanding regional and national gdp"""
        illinois.nation.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                                       (illinois.exports - illinois.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        illinois.consumer_spending = round(random.uniform(10, 250), 2)
        illinois.investment = round(random.uniform(25, 350), 2)

        illinois.government_spending = round(random.uniform(100, 800), 2)

        illinois.nation.national_debt += (illinois.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               illinois.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        illinois.exports = round(random.uniform(450, 750), 2)
        illinois.imports = round(random.uniform(320, 560), 2)
        illinois.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                             (illinois.exports - illinois.imports))
        """implementing two ways of expanding regional and national gdp"""
        illinois.nation.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                                       (illinois.exports - illinois.imports))
def expansion(illinois):
    if illinois.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        illinois.consumer_spending = round(random.uniform(10, 550), 2)
        illinois.investment = round(random.uniform(25, 750), 2)

        illinois.government_spending = round(random.uniform(100, 1000), 2)

        illinois.nation.national_debt += (illinois.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               illinois.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        illinois.exports = round(random.uniform(450, 1150), 2)
        illinois.imports = round(random.uniform(320, 760), 2)
        illinois.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                             (illinois.exports - illinois.imports))
        """implementing two ways of expanding regional and national gdp"""
        illinois.nation.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                                       (illinois.exports - illinois.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        illinois.consumer_spending = round(random.uniform(10, 550), 2)
        illinois.investment = round(random.uniform(25, 750), 2)

        illinois.government_spending = round(random.uniform(100, 1200), 2)

        illinois.nation.national_debt += (illinois.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               illinois.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        illinois.exports = round(random.uniform(450, 1150), 2)
        illinois.imports = round(random.uniform(320, 760), 2)
        illinois.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                             (illinois.exports - illinois.imports))
        """implementing two ways of expanding regional and national gdp"""
        illinois.nation.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                                       (illinois.exports - illinois.imports))

def recession(illinois):
    if illinois.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        illinois.consumer_spending = -round(random.uniform(10, 250), 2)
        illinois.investment = -round(random.uniform(25, 350), 2)

        illinois.government_spending = round(random.uniform(100, 300), 2)

        illinois.nation.national_debt += (illinois.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -illinois.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        illinois.exports = round(random.uniform(250, 450), 2)
        illinois.imports = round(random.uniform(320, 760), 2)
        illinois.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                             (illinois.exports - illinois.imports))
        """implementing two ways of expanding regional and national gdp"""
        illinois.nation.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                                       (illinois.exports - illinois.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        illinois.consumer_spending = -round(random.uniform(10, 350), 2)
        illinois.investment = -round(random.uniform(25, 550), 2)

        illinois.government_spending = round(random.uniform(100, 500), 2)

        illinois.nation.national_debt += (illinois.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -illinois.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        illinois.exports = round(random.uniform(250, 350), 2)
        illinois.imports = round(random.uniform(320, 860), 2)
        illinois.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                             (illinois.exports - illinois.imports))
        """implementing two ways of expanding regional and national gdp"""
        illinois.nation.current_gdp += (illinois.consumer_spending + illinois.investment + illinois.government_spending +
                                       (illinois.exports - illinois.imports))

def depression(illionis):
    if illionis.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        illionis.consumer_spending = -round(random.uniform(10, 550), 2)
        illionis.investment = -round(random.uniform(25, 750), 2)

        illionis.government_spending = round(random.uniform(100, 1400), 2)

        illionis.nation.national_debt += (illionis.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -illionis.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        illionis.exports = round(random.uniform(250, 750), 2)
        illionis.imports = round(random.uniform(320, 760), 2)
        illionis.current_gdp += (illionis.consumer_spending + illionis.investment + illionis.government_spending +
                             (illionis.exports - illionis.imports))
        """implementing two ways of expanding regional and national gdp"""
        illionis.nation.current_gdp += (illionis.consumer_spending + illionis.investment + illionis.government_spending +
                                       (illionis.exports - illionis.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        illionis.consumer_spending = -round(random.uniform(10, 350), 2)
        illionis.investment = -round(random.uniform(25, 550), 2)

        illionis.government_spending = round(random.uniform(100, 500), 2)

        illionis.nation.national_debt += (illionis.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -illionis.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        illionis.exports = round(random.uniform(250, 350), 2)
        illionis.imports = round(random.uniform(320, 1200), 2)
        illionis.current_gdp += (illionis.consumer_spending + illionis.investment + illionis.government_spending +
                             (illionis.exports - illionis.imports))
        """implementing two ways of expanding regional and national gdp"""
        illionis.nation.current_gdp += (illionis.consumer_spending + illionis.investment + illionis.government_spending +
                (illionis.exports - illionis.imports))

def economic_growth(illinois):
    """Economic growth of iowa as individual state"""
    if illinois.economic_state == "recovery":
        recovery(illinois)

    elif illinois.economic_state == "depression":
        depression(illinois)

    elif illinois.economic_state == "recession":
        recession(illinois)

    elif illinois.economic_state == "expansion":
        expansion(illinois)

class Illinois:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Illinois"
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