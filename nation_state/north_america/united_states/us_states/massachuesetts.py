import random

population = {
    "1910": 1032000,
    "1914": 1389000,
    "1918": 1467000,
    "1932": 1678000,
    "1936": 1745000,
    "1939": 1793000
}

gdp = {
    "1910": 2500000000,
    "1914": 2593747000,
    "1918": 2890098000,
    "1932": 2989984000,
    "1936": 3210359000,
    "1939": 3390039000
}
def population_growth(massachuesetts):
    births = random.randrange(1, 20)
    deaths = random.randrange(1, 15)
    massachuesetts.population += (births - deaths)
    massachuesetts.nation.current_pop += (births - deaths)
    massachuesetts.nation.births += births
    massachuesetts.nation.deaths += deaths

"""economic_functions"""
def recovery(maryland):
    if maryland.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        maryland.consumer_spending = round(random.uniform(10, 75), 2)
        maryland.investment = round(random.uniform(25, 250), 2)

        maryland.government_spending = round(random.uniform(100, 500), 2)

        maryland.nation.national_debt += (maryland.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             maryland.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maryland.exports = round(random.uniform(450, 750), 2)
        maryland.imports = round(random.uniform(320, 560), 2)
        maryland.current_gdp += (maryland.consumer_spending + maryland.investment + maryland.government_spending +
                             (maryland.exports - maryland.imports))
        """implementing two ways of expanding regional and national gdp"""
        maryland.nation.current_gdp += (maryland.consumer_spending + maryland.investment + maryland.government_spending +
                                       (maryland.exports - maryland.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        maryland.consumer_spending = round(random.uniform(10, 250), 2)
        maryland.investment = round(random.uniform(25, 350), 2)

        maryland.government_spending = round(random.uniform(100, 800), 2)

        maryland.nation.national_debt += (maryland.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               maryland.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        maryland.exports = round(random.uniform(450, 750), 2)
        maryland.imports = round(random.uniform(320, 560), 2)
        maryland.current_gdp += (maryland.consumer_spending + maryland.investment + maryland.government_spending +
                             (maryland.exports - maryland.imports))
        """implementing two ways of expanding regional and national gdp"""
        maryland.nation.current_gdp += (maryland.consumer_spending + maryland.investment + maryland.government_spending +
                                       (maryland.exports - maryland.imports))
def expansion(massachuesetts):
    if massachuesetts.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        massachuesetts.consumer_spending = round(random.uniform(10, 550), 2)
        massachuesetts.investment = round(random.uniform(25, 750), 2)

        massachuesetts.government_spending = round(random.uniform(100, 1000), 2)

        massachuesetts.nation.national_debt += (massachuesetts.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               massachuesetts.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        massachuesetts.exports = round(random.uniform(450, 1150), 2)
        massachuesetts.imports = round(random.uniform(320, 760), 2)
        massachuesetts.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                             (massachuesetts.exports - massachuesetts.imports))
        """implementing two ways of expanding regional and national gdp"""
        massachuesetts.nation.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                                       (massachuesetts.exports - massachuesetts.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        massachuesetts.consumer_spending = round(random.uniform(10, 550), 2)
        massachuesetts.investment = round(random.uniform(25, 750), 2)

        massachuesetts.government_spending = round(random.uniform(100, 1200), 2)

        massachuesetts.nation.national_debt += (massachuesetts.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               massachuesetts.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        massachuesetts.exports = round(random.uniform(450, 1150), 2)
        massachuesetts.imports = round(random.uniform(320, 760), 2)
        massachuesetts.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                             (massachuesetts.exports - massachuesetts.imports))
        """implementing two ways of expanding regional and national gdp"""
        massachuesetts.nation.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                                       (massachuesetts.exports - massachuesetts.imports))

def recession(massachuesetts):
    if massachuesetts.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        massachuesetts.consumer_spending = -round(random.uniform(10, 250), 2)
        massachuesetts.investment = -round(random.uniform(25, 350), 2)

        massachuesetts.government_spending = round(random.uniform(100, 300), 2)

        massachuesetts.nation.national_debt += (massachuesetts.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -massachuesetts.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        massachuesetts.exports = round(random.uniform(250, 450), 2)
        massachuesetts.imports = round(random.uniform(320, 760), 2)
        massachuesetts.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                             (massachuesetts.exports - massachuesetts.imports))
        """implementing two ways of expanding regional and national gdp"""
        massachuesetts.nation.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                                       (massachuesetts.exports - massachuesetts.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        massachuesetts.consumer_spending = -round(random.uniform(10, 350), 2)
        massachuesetts.investment = -round(random.uniform(25, 550), 2)

        massachuesetts.government_spending = round(random.uniform(100, 500), 2)

        massachuesetts.nation.national_debt += (massachuesetts.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -massachuesetts.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        massachuesetts.exports = round(random.uniform(250, 350), 2)
        massachuesetts.imports = round(random.uniform(320, 860), 2)
        massachuesetts.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                             (massachuesetts.exports - massachuesetts.imports))
        """implementing two ways of expanding regional and national gdp"""
        massachuesetts.nation.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                                       (massachuesetts.exports - massachuesetts.imports))

def depression(massachuesetts):
    if massachuesetts.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        massachuesetts.consumer_spending = -round(random.uniform(10, 550), 2)
        massachuesetts.investment = -round(random.uniform(25, 750), 2)

        massachuesetts.government_spending = round(random.uniform(100, 1400), 2)

        massachuesetts.nation.national_debt += (massachuesetts.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -massachuesetts.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        massachuesetts.exports = round(random.uniform(250, 750), 2)
        massachuesetts.imports = round(random.uniform(320, 760), 2)
        massachuesetts.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                             (massachuesetts.exports - massachuesetts.imports))
        """implementing two ways of expanding regional and national gdp"""
        massachuesetts.nation.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                                       (massachuesetts.exports - massachuesetts.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        massachuesetts.consumer_spending = -round(random.uniform(10, 350), 2)
        massachuesetts.investment = -round(random.uniform(25, 550), 2)

        massachuesetts.government_spending = round(random.uniform(100, 500), 2)

        massachuesetts.nation.national_debt += (massachuesetts.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -massachuesetts.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        massachuesetts.exports = round(random.uniform(250, 350), 2)
        massachuesetts.imports = round(random.uniform(320, 1200), 2)
        massachuesetts.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                             (massachuesetts.exports - massachuesetts.imports))
        """implementing two ways of expanding regional and national gdp"""
        massachuesetts.nation.current_gdp += (massachuesetts.consumer_spending + massachuesetts.investment + massachuesetts.government_spending +
                (massachuesetts.exports - massachuesetts.imports))

def economic_growth(massachuesetts):
    """Economic growth of iowa as individual state"""
    if massachuesetts.economic_state == "recovery":
        recovery(massachuesetts)

    elif massachuesetts.economic_state == "depression":
        depression(massachuesetts)

    elif massachuesetts.economic_state == "recession":
        recession(massachuesetts)

    elif massachuesetts.economic_state == "expansion":
        expansion(massachuesetts)

class Massachuesetts:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Massachuesetts"
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