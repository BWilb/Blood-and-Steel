import random
import time

population = {
    "1910": 2142069,
    "1914": 2225741,
    "1918": 2311503,
    "1932": 2689523,
    "1936": 2761094,
    "1939": 2817169
}

gdp = {
    "1910": 2500000,
    "1914": 2593747,
    "1918": 2890098,
    "1932": 2989984,
    "1936": 3210359,
    "1939": 3390039
}
def population_growth(alabama):
    births = random.randrange(1, 16)
    deaths = random.randrange(1, 14)
    alabama.population += (births - deaths)
    alabama.nation.current_pop += (births - deaths)
    alabama.nation.births += births
    alabama.nation.deaths += deaths

"""random functions"""
def random_social(alabama):
    chance = random.randrange(10, 20000)
    if chance % 5 == 0:
       """chance that someone has a surprise birthday thrown for them
       - increase in happiness
       """
       print("Someone in Alabama had a surprise birthday thrown for them.\n")
       time.sleep(3)
       increase = round(random.uniform(0.25, 1.00), 2)
       if (alabama.happiness + increase) < 98:
           alabama.happiness += increase

    elif chance % 8 == 7:
        """chance that a lynching occurs(could be one or more)
        - decrease in population, stability and happiness
        - decrease in Union favorability
        """
        blacks = random.randrange(1, 16)
        print(f"{blacks} blacks were just lynched in Alabama.\n")
        time.sleep(3)
        alabama.population -= blacks
        alabama.nation.current_pop -= blacks
        alabama.nation.deaths += blacks

        decrease = round(random.uniform(0.25, 1.00), 2)
        if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
            alabama.happiness -= decrease
            alabama.nation.happiness -= decrease

        if (alabama.stability - decrease) > 7.56 and (alabama.nation.stability - decrease) > 5:
            alabama.stability -= decrease
            alabama.nation.stability -= decrease

    elif chance % 10 == 7:
        """Chance that a KKK march occurs
        - decrease in stability and happiness
        """
        print("A KKK march just occurred in Alabama.\n")
        time.sleep(3)
        decrease = round(random.uniform(0.25, 1.00), 2)
        if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
            alabama.happiness -= decrease
            alabama.nation.happiness -= decrease

        if (alabama.stability - decrease) > 7.56 and (alabama.nation.stability - decrease) > 5:
            alabama.stability -= decrease
            alabama.nation.stability -= decrease

def random_crime(alabama):
    chance = random.randrange(10, 20000)
    if chance % 5 == 3:
        """Chance that a stabbing occurs
        - internal chance that person survives or not
        -> potential decrease in population
        -> decrease in happiness
        """
        print("someone just got stabbed in Alabama.\n")
        time.sleep(3)
        chance = random.randrange(0, 2)
        if chance == 0:
            print("the victim did not survive\n")
            time.sleep(3)
            decrease = round(random.uniform(0.25, 1.00), 2)
            if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
                alabama.happiness -= decrease
                alabama.nation.happiness -= decrease

        else:
            print("The victim survived.\n")
            decrease = round(random.uniform(0.25, 1.00), 2)
            if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
                alabama.happiness -= decrease
                alabama.nation.happiness -= decrease

    elif chance % 8 == 7:
        """Chance that a KKK establishment gets raided
        - no reporting, unless death occurs 
        - decrease gdp(nationally and regionally) 
        - decrease in stability and union favorability
        """
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance that gets swept under rug if no death"""
            loss = round(alabama.current_gdp * round(random.uniform(0.001, 0.009), 5), 2)
            alabama.current_gdp -= loss
            alabama.nation.current_gdp -= loss

            decrease = round(random.uniform(0.25, 1.00), 2)
            if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
                alabama.happiness -= decrease
                alabama.nation.happiness -= decrease

            if (alabama.union_favorability - decrease) > 5.56:
                alabama.union_favorability -= decrease

        else:
            deaths = random.randrange(2, 100)
            print(f"Federal troops just raided a KKK outpost in Alabama. {deaths} KKK agents were killed in the process.\n")
            time.sleep(3)
            loss = round(alabama.current_gdp * round(random.uniform(0.001, 0.009), 5), 2)
            alabama.current_gdp -= loss
            alabama.nation.current_gdp -= loss

            decrease = round(random.uniform(0.25, 1.00), 2)
            if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
                alabama.happiness -= decrease
                alabama.nation.happiness -= decrease

            if (alabama.union_favorability - decrease) > 5.56:
                alabama.union_favorability -= decrease

            alabama.population -= deaths
            alabama.nation.current_pop -= deaths

    elif chance % 12 == 9:
        """chance that a homicide occurs
        - decrease in population and happiness
        """
        homicide = random.randrange(10, 100)
        print(f"A homicide ring has been uncovered in Alabama, with {homicide} victims.\n.")
        time.sleep(3)
        alabama.population -= homicide
        alabama.nation.current_pop -= homicide
        decrease = round(random.uniform(0.25, 1.00), 2)
        if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
            alabama.happiness -= decrease
            alabama.nation.happiness -= decrease

    elif chance % 20 == 19:
        """Chance that a rape occurs
        - decrease in stability and happiness
        """
        print("Somebody was just raped in Alabama.\n")
        time.sleep(3)
        decrease = round(random.uniform(0.25, 1.00), 2)
        if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
            alabama.happiness -= decrease
            alabama.nation.happiness -= decrease

    elif chance % 30 == 25:
        """Chance for bank robbery
        - internal chance of death
        - decrease in gdp(national and regional)
        - decrease in happiness and stability
        """
        loss = round(alabama.current_gdp * round(random.uniform(0.001, 0.009), 5), 2)
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance that people die in robbery"""
            deaths = random.randrange(13, 50)
            print(f"A bank robbery just occurred in Alabama, with {deaths} dead and ${loss} lost.\n")
            time.sleep(3)
            alabama.population -= deaths
            alabama.nation.current_pop -= deaths
            alabama.nation.current_gdp -= loss
            alabama.current_gdp -= loss

        else:
            print(f"A bank robbery just occurred in Alabama, nobody was hurt, but ${loss} was lost.\n")
            time.sleep(3)
        decrease = round(random.uniform(0.25, 1.00), 2)
        if (alabama.happiness - decrease) > 5 and (alabama.nation.happiness - decrease) > 5:
            alabama.happiness -= decrease
            alabama.nation.happiness -= decrease

        if (alabama.stability - decrease) > 7.56 and (alabama.nation.stability - decrease) > 5:
            alabama.stability -= decrease
            alabama.nation.stability -= decrease

def random_events(alabama):
    random_social(alabama)
    random_crime(alabama)

"""economic_functions"""
def recovery(alabama):
    if alabama.nation.economic_stimulus:
        """If United States has implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 75), 2)
        alabama.investment = round(random.uniform(25, 250), 2)

        alabama.government_spending = round(random.uniform(100, 450), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                             alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 750), 2)
        alabama.imports = round(random.uniform(320, 560), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 250), 2)
        alabama.investment = round(random.uniform(25, 350), 2)

        alabama.government_spending = round(random.uniform(100, 800), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 750), 2)
        alabama.imports = round(random.uniform(320, 560), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))
def expansion(alabama):
    if alabama.nation.economic_stimulus:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 550), 2)
        alabama.investment = round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1000), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 1150), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = round(random.uniform(10, 550), 2)
        alabama.investment = round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1200), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(450, 1150), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

def recession(alabama):
    if alabama.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 250), 2)
        alabama.investment = -round(random.uniform(25, 350), 2)

        alabama.government_spending = round(random.uniform(100, 300), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 450), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:
        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 350), 2)
        alabama.investment = -round(random.uniform(25, 550), 2)

        alabama.government_spending = round(random.uniform(100, 500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 350), 2)
        alabama.imports = round(random.uniform(320, 860), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

def depression(alabama):
    if alabama.nation.economic_stimulus:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 550), 2)
        alabama.investment = -round(random.uniform(25, 750), 2)

        alabama.government_spending = round(random.uniform(100, 1500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 550), 2)
        alabama.imports = round(random.uniform(320, 760), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                                       (alabama.exports - alabama.imports))

    else:

        """If United States hasn't implemented an economic stimulus"""
        alabama.consumer_spending = -round(random.uniform(10, 350), 2)
        alabama.investment = -round(random.uniform(25, 550), 2)

        alabama.government_spending = round(random.uniform(100, 500), 2)

        alabama.nation.national_debt += (alabama.government_spending * round(random.uniform(0.001, 0.009), 5) +
                               -alabama.consumer_spending * round(random.uniform(0.001, 0.009), 5))
        """
        National debt includes both portions of US government spending and consumer spending.
        The portions are comprised of the loans and bonds that are bought and sold
        """

        alabama.exports = round(random.uniform(250, 750), 2)
        alabama.imports = round(random.uniform(320, 1200), 2)
        alabama.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                             (alabama.exports - alabama.imports))
        """implementing two ways of expanding regional and national gdp"""
        alabama.nation.current_gdp += (alabama.consumer_spending + alabama.investment + alabama.government_spending +
                (alabama.exports - alabama.imports))

def economic_growth(alabama):
    """Economic growth of iowa as individual state"""
    if alabama.economic_state == "recovery":
        recovery(alabama)

    elif alabama.economic_state == "depression":
        depression(alabama)

    elif alabama.economic_state == "recession":
        recession(alabama)

    elif alabama.economic_state == "expansion":
        expansion(alabama)

class Alabama:
    def __init__(self, year, us):
        """regional variables"""
        self.name = "Alabama"
        # establishment of connection to United States
        self.nation = us
        """Population variables"""
        self.population = population[str(year)]
        self.happiness = 90.00
        """economic variables"""
        self.current_gdp = gdp[str(year)]
        self.consumer_spending = None
        self.government_spending = None
        self.investment = None
        self.exports = None
        self.imports = None
        self.economic_state = "recovery"
        self.debt = 0
        """political variables"""
        self.stability = 85.56
        self.union_favorability = 90.45
        # if union favorability falls below 20%, potential for secession