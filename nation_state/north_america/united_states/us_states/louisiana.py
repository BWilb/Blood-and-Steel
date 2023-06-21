import random

population = {
    "1910": 1667000,
    "1914": 1740000,
    "1918": 1746000,
    "1932": 2155000,
    "1936": 2246000,
    "1939": 2334000
}

gdp = {
    "1910": 8034090,
    "1914": 8390290,
    "1918": 8586480,
    "1932": 8375730,
    "1936": 8398240,
    "1939": 8423580
}
def population_growth(louisiana):
    births = random.randrange(1, 10)
    deaths = random.randrange(1, 10)
    louisiana.population += (births - deaths)
    louisiana.nation.current_pop += (births - deaths)
    louisiana.nation.births += births
    louisiana.nation.deaths += deaths

"""economic_functions"""
def recovery(louisiana):
    if louisiana.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        louisiana.consumer_spending = round(random.uniform(10, 75), 2)
        louisiana.investment = round(random.uniform(25, 250), 2)

        louisiana.government_spending = round(random.uniform(100, 500), 2)

        louisiana.nation.national_debt += (louisiana.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             louisiana.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        louisiana.exports = round(random.uniform(450, 750), 2)
        louisiana.imports = round(random.uniform(320, 560), 2)
        louisiana.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                             (louisiana.exports - louisiana.imports))
        """implementing two ways of expanding regional and national gdp"""
        louisiana.nation.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                                       (louisiana.exports - louisiana.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        louisiana.consumer_spending = round(random.uniform(10, 250), 2)
        louisiana.investment = round(random.uniform(25, 350), 2)

        louisiana.government_spending = round(random.uniform(100, 800), 2)

        louisiana.nation.national_debt += (louisiana.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               louisiana.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        louisiana.exports = round(random.uniform(450, 750), 2)
        louisiana.imports = round(random.uniform(320, 560), 2)
        louisiana.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                             (louisiana.exports - louisiana.imports))
        """implementing two ways of expanding regional and national gdp"""
        louisiana.nation.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                                       (louisiana.exports - louisiana.imports))
def expansion(louisiana):
    if louisiana.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        louisiana.consumer_spending = round(random.uniform(10, 550), 2)
        louisiana.investment = round(random.uniform(25, 750), 2)

        louisiana.government_spending = round(random.uniform(100, 1000), 2)

        louisiana.nation.national_debt += (louisiana.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               louisiana.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        louisiana.exports = round(random.uniform(450, 1150), 2)
        louisiana.imports = round(random.uniform(320, 760), 2)
        louisiana.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                             (louisiana.exports - louisiana.imports))
        """implementing two ways of expanding regional and national gdp"""
        louisiana.nation.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                                       (louisiana.exports - louisiana.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        louisiana.consumer_spending = round(random.uniform(10, 550), 2)
        louisiana.investment = round(random.uniform(25, 750), 2)

        louisiana.government_spending = round(random.uniform(100, 1200), 2)

        louisiana.nation.national_debt += (louisiana.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               louisiana.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        louisiana.exports = round(random.uniform(450, 1150), 2)
        louisiana.imports = round(random.uniform(320, 760), 2)
        louisiana.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                             (louisiana.exports - louisiana.imports))
        """implementing two ways of expanding regional and national gdp"""
        louisiana.nation.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                                       (louisiana.exports - louisiana.imports))

def recession(louisiana):
    if louisiana.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        louisiana.consumer_spending = -round(random.uniform(10, 250), 2)
        louisiana.investment = -round(random.uniform(25, 350), 2)

        louisiana.government_spending = round(random.uniform(100, 300), 2)

        louisiana.nation.national_debt += (louisiana.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -louisiana.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        louisiana.exports = round(random.uniform(250, 450), 2)
        louisiana.imports = round(random.uniform(320, 760), 2)
        louisiana.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                             (louisiana.exports - louisiana.imports))
        """implementing two ways of expanding regional and national gdp"""
        louisiana.nation.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                                       (louisiana.exports - louisiana.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        louisiana.consumer_spending = -round(random.uniform(10, 350), 2)
        louisiana.investment = -round(random.uniform(25, 550), 2)

        louisiana.government_spending = round(random.uniform(100, 500), 2)

        louisiana.nation.national_debt += (louisiana.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -louisiana.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        louisiana.exports = round(random.uniform(250, 350), 2)
        louisiana.imports = round(random.uniform(320, 860), 2)
        louisiana.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                             (louisiana.exports - louisiana.imports))
        """implementing two ways of expanding regional and national gdp"""
        louisiana.nation.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                                       (louisiana.exports - louisiana.imports))

def depression(louisiana):
    if louisiana.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        louisiana.consumer_spending = -round(random.uniform(10, 550), 2)
        louisiana.investment = -round(random.uniform(25, 750), 2)

        louisiana.government_spending = round(random.uniform(100, 1400), 2)

        louisiana.nation.national_debt += (louisiana.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -louisiana.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        louisiana.exports = round(random.uniform(250, 750), 2)
        louisiana.imports = round(random.uniform(320, 760), 2)
        louisiana.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                             (louisiana.exports - louisiana.imports))
        """implementing two ways of expanding regional and national gdp"""
        louisiana.nation.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                                       (louisiana.exports - louisiana.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        louisiana.consumer_spending = -round(random.uniform(10, 350), 2)
        louisiana.investment = -round(random.uniform(25, 550), 2)

        louisiana.government_spending = round(random.uniform(100, 500), 2)

        louisiana.nation.national_debt += (louisiana.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -louisiana.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        louisiana.exports = round(random.uniform(250, 350), 2)
        louisiana.imports = round(random.uniform(320, 1200), 2)
        louisiana.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                             (louisiana.exports - louisiana.imports))
        """implementing two ways of expanding regional and national gdp"""
        louisiana.nation.current_gdp += (louisiana.consumer_spending + louisiana.investment + louisiana.government_spending +
                (louisiana.exports - louisiana.imports))

def economic_growth(louisiana):
    """Economic growth of iowa as individual state"""
    if louisiana.economic_state == "recovery":
        recovery(louisiana)

    elif louisiana.economic_state == "depression":
        depression(louisiana)

    elif louisiana.economic_state == "recession":
        recession(louisiana)

    elif louisiana.economic_state == "expansion":
        expansion(louisiana)

class Louisiana:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Louisiana"
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