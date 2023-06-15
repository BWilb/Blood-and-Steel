import random

population = {
    "1910": 1114756,
    "1914": 1234567,
    "1918": 1323535,
    "1932": 1511224,
    "1936": 1592324,
    "1939": 1612435
}

gdp = {
    "1910": 1101927,
    "1914": 1129384,
    "1918": 1243474,
    "1932": 1112892,
    "1936": 1191872,
    "1939": 1304838
}
def population_growth(connecticut):
    births = random.randrange(7, 19)
    deaths = random.randrange(2, 15)
    connecticut.population += (births - deaths)
    connecticut.nation.current_pop += (births - deaths)

"""economic_functions"""
def recovery(connecticut):
    if connecticut.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        connecticut.consumer_spending = round(random.uniform(10, 75), 2)
        connecticut.investment = round(random.uniform(25, 100), 2)

        connecticut.government_spending = round(random.uniform(100, 500), 2)

        connecticut.debt += (connecticut.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             connecticut.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        connecticut.nation.national_debt += (connecticut.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             connecticut.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        connecticut.exports = round(random.uniform(150, 350), 2)
        connecticut.imports = round(random.uniform(20, 360), 2)
        connecticut.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                             (connecticut.exports - connecticut.imports))
        """implementing two ways of expanding regional and national gdp"""
        connecticut.nation.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                                      (connecticut.exports - connecticut.imports))

    else:
        """If United States has implemented an economic stimulus"""
        connecticut.consumer_spending = round(random.uniform(10, 55), 2)
        connecticut.investment = round(random.uniform(25, 80), 2)

        connecticut.government_spending = round(random.uniform(100, 750), 2)

        connecticut.debt += (connecticut.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             connecticut.consumer_spending * round(random.uniform(0.001, 0.009), 5))

        connecticut.nation.national_debt += (connecticut.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             connecticut.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        connecticut.exports = round(random.uniform(150, 350), 2)
        connecticut.imports = round(random.uniform(20, 360), 2)
        connecticut.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                             (connecticut.exports - connecticut.imports))
        """implementing two ways of expanding regional and national gdp"""
        connecticut.nation.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                                      (connecticut.exports - connecticut.imports))
def expansion(connecticut):
    if connecticut.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        connecticut.consumer_spending = round(random.uniform(10, 550), 2)
        connecticut.investment = round(random.uniform(25, 750), 2)

        connecticut.government_spending = round(random.uniform(100, 1000), 2)

        connecticut.nation.national_debt += (connecticut.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               connecticut.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        connecticut.exports = round(random.uniform(450, 1150), 2)
        connecticut.imports = round(random.uniform(320, 760), 2)
        connecticut.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                             (connecticut.exports - connecticut.imports))
        """implementing two ways of expanding regional and national gdp"""
        connecticut.nation.current_gdp += (
                    connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                    (connecticut.exports - connecticut.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        connecticut.consumer_spending = round(random.uniform(10, 550), 2)
        connecticut.investment = round(random.uniform(25, 750), 2)

        connecticut.government_spending = round(random.uniform(100, 1200), 2)

        connecticut.nation.national_debt += (connecticut.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               connecticut.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        connecticut.exports = round(random.uniform(450, 1150), 2)
        connecticut.imports = round(random.uniform(320, 760), 2)
        connecticut.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                             (connecticut.exports - connecticut.imports))
        """implementing two ways of expanding regional and national gdp"""
        connecticut.nation.current_gdp += (
                    connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                    (connecticut.exports - connecticut.imports))

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

def depression(connecticut):
    if connecticut.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        connecticut.consumer_spending = -round(random.uniform(10, 550), 2)
        connecticut.investment = -round(random.uniform(25, 750), 2)

        connecticut.government_spending = round(random.uniform(100, 1400), 2)

        connecticut.nation.national_debt += (connecticut.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -connecticut.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        connecticut.exports = round(random.uniform(250, 750), 2)
        connecticut.imports = round(random.uniform(320, 760), 2)
        connecticut.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                             (connecticut.exports - connecticut.imports))
        """implementing two ways of expanding regional and national gdp"""
        connecticut.nation.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                                      (connecticut.exportsconnecticutcticut.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        connecticut.consumer_spending = -round(random.uniform(10, 350), 2)
        connecticut.investment = -round(random.uniform(25, 550), 2)

        connecticut.government_spending = round(random.uniform(100, 500), 2)

        connecticut.nation.national_debt += (connecticut.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -connecticut.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        connecticut.exports = round(random.uniform(250, 350), 2)
        connecticut.imports = round(random.uniform(320, 1200), 2)
        connecticut.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                             (connecticut.exports - connecticut.imports))
        """implementing two ways of expanding regional and national gdp"""
        connecticut.nation.current_gdp += (connecticut.consumer_spending + connecticut.investment + connecticut.government_spending +
                (connecticut.exports - connecticut.imports))

def economic_growth(connecticut):
    """Economic growth of iowa as individual state"""
    if connecticut.economic_state == "recovery":
        recovery(connecticut)

    elif connecticut.economic_state == "depression":
        depression(connecticut)

    elif connecticut.economic_state == "recession":
        recession(connecticut)

    elif connecticut.economic_state == "expansion":
        expansion(connecticut)

class Conneticut:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Connecticut"
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