# political variables and dictionaries
import random
import time
from datetime import datetime, timedelta

monarchs = {
    """Dictionary for english monarchs
    Leader selection will be in sync with time frame selection
    Unlike population, leader dictionary will be setup to be as historically accurate as possible"""

    "1910": "Edward VII",
    "1914": "George V",
    "1918": "George V",
    "1932": "George V",
    "1936": "Edward VIII",
    "1939": "George VI"
}

pm = {
    "1910": "H.H. Asquith",
    "1914": "H.H. Asquith",
    "1918": "David Lloyd George",
    "1932": "Ramsay MacDonald",
    "1936": "Stanley Baldwin",
    "1939": "Neville Chamberlain"
}

spare_pms = ["Duncan Pirie", "Henry Cowan", "Harold Baker", "James Calmont", "Ellis Ellis-Griffith",
             "Charles Craig", "William Jones", "Alfred Scott", "Sir Charles Hunter"]

spare_1900_1950_monarchs = ["Louis", "Prince Arthur", "Beatrice", "Prince Henry", "Alexander Ramsay", "Alexander Cambridge",
                            "Albert Victor", "Victoria II", "George VI"]

# population variables and dictionaries
population = {
    """Dictionary for population
    Population selection will be in sync with time frame selection
    Population will then be set up to grow or shrink in random amounts"""

    "1910": 44915900,
    "1914": 42956900,
    "1918": 39582000,
    "1932": 46335000,
    "1936": 47081300,
    "1939": 46029200
}

# economic variables and dictionaries
gdp = {
    "1910": 15783763158,
    "1914": 17856842105,
    "1918": 23873207895,
    "1932": 44371994737,
    "1936": 53157368421,
    "1939": 54936947368
}

tax_rate = {
    "1910": 10.0,
    "1914": 50.0,
    "1918": 80.0,
    "1932": 60.0,
    "1936": 60.0,
    "1939": 80.0
}

business_cycle = ["recession", "recovery", "expansion", "depression"]

"""Event functions"""
def political_events(britain):
    if britain.date == datetime(1936, 1, 20):
        """Date for George V's death"""
        print(f"{britain.monarch} is dead!!!")
        britain.monarch = "Edward VIII"
        print(f"{britain.monarch} is your new king. All hail Brittania.\n")

    if britain.date == datetime(1910, 5, 6):
        """Date for when Edward VII dies"""
        print(f"{britain.monarch} is dead!!")
        britain.monarch = "George V"
        print(f"{britain.monarch} is your new king. All hail Brittania.\n")

    if britain.date == datetime(1936, 12, 11):
        """Date for when Edward VIII abdicates"""
        print(f"{britain.monarch} has abdicated the throne.")
        britain.monarch = "George VI"
        print(f"{britain.monarch} is your new king. All hail Brittania.\n")

def economic_events(britain):
    if britain.date == datetime(1929, 10, 24):
        print("Britain has fallen into a severe depression.\n"
              "It is being reported that nations across the globe are experiencing similar events.\n")
        time.sleep(3)

    if britain.date > datetime(1929, 10, 24) and britain.date < datetime(1937, 1, 1):
        decrease_happiness = round(random.uniform(0.01, 0.05), 2)
        decrease_stability = round(random.uniform(0.01, 0.05), 2)
        if (britain.happiness - decrease_happiness) > 5:
            britain.happiness -= decrease_happiness
        elif (britain.stability - decrease_stability) > 5:
            britain.happiness -= decrease_stability

def social_events(britain):
    if britain.date == datetime(britain.date.year, 3, 17):
        print("Today is St. Patrick's Day in Britain.\n")
        time.sleep(3)

def events(britain):
    political_events(britain)
    economic_events(britain)
    social_events(britain)

def random_crime(britain):
    chance = random.randrange(10, 20000)
    if chance % 5 == 4:
        """Chance that a stabbing occurs
        * chance that victim dies
            -> decrease in population
        - decrease in happiness
        """
        chance = random.randrange(0, 2)
        if chance == 0:
            print("A stabbing just occurred. However the victim survived.\n")
            time.sleep(3)
            decrease_happiness = round(random.uniform(0.25, 0.75), 2)
            if (britain.happiness - decrease_happiness) > 5:
                britain.happiness -= decrease_happiness
        elif chance == 1:
            print("A stabbing just occurred, which the victim died.\n")
            time.sleep(3)
            britain.current_pop -= 1
            decrease_happiness = round(random.uniform(0.25, 0.75), 2)
            if (britain.happiness - decrease_happiness) > 5:
                britain.happiness -= decrease_happiness

    elif chance % 8 == 6:
        """Chance that a raping occurs
        * decrease in happiness
        """
        print("A rape just occurred.\n")
        time.sleep(3)
        decrease_happiness = round(random.uniform(0.25, 0.75), 2)
        if (britain.happiness - decrease_happiness) > 5:
            britain.happiness -= decrease_happiness

    elif chance % 12 == 5:
        """Chance that a homicide occurs
        - reduction in population and political influences
        - decrease in happiness and stability
        """
        losses = random.randrange(2, 35)
        print(f"A homicide just occurred. {losses} people were killed.\n")
        britain.current_pop -= losses
        britain.deaths += losses
        for i in range(0, losses):
            """Assigning births to political parties"""
            chance = random.randrange(0, 4)
            if chance == 0:
                britain.lp -= 1

            elif chance == 1:
                britain.liberal -= 1

            elif chance == 2:
                britain.clup -= 1

            elif chance == 3:
                britain.independents -= 1

    elif chance % 16 == 12:
        """Chance that bank robbery occurs
        - internal chance of success
        - internal chance of potential deaths
            -> decrease in population
        - decrease in stability and happiness
        """
        chance = random.randrange(0, 2)
        if chance == 0:
            print("There was an unsuccessful attempt at robbing a bank\n")

            chance = random.randrange(0, 2)
            if chance == 0:
                print("Nobody was harmed in the process")

            elif chance == 1:
                losses = random.randrange(2, 35)
                print(f"{losses} people were killed in the process though.\n")
                britain.current_pop -= losses
                britain.deaths += losses
                for i in range(0, losses):
                    """Assigning births to political parties"""
                    chance = random.randrange(0, 4)
                    if chance == 0:
                        britain.lp -= 1

                    elif chance == 1:
                        britain.liberal -= 1

                    elif chance == 2:
                        britain.clup -= 1

                    elif chance == 3:
                        britain.independents -= 1

        elif chance == 1:
            thievery = round(random.uniform(10000, 300000), 2)
            print(f"A bank robbery just occurred. ${thievery} was stolen.")
            britain.current_gdp -= thievery
            """Loss in gdp"""
            britain.national_debt += round(thievery * round(random.uniform(0.009, 0.09), 5), 2)

            chance = random.randrange(0, 2)
            if chance == 0:
                print("Nobody was harmed in the process")

            elif chance == 1:
                losses = random.randrange(2, 35)
                print(f"{losses} people were killed in the process though.\n")
                britain.current_pop -= losses
                britain.deaths += losses
                for i in range(0, losses):
                    """Assigning births to political parties"""
                    chance = random.randrange(0, 4)
                    if chance == 0:
                        britain.lp -= 1

                    elif chance == 1:
                        britain.liberal -= 1

                    elif chance == 2:
                        britain.clup -= 1

                    elif chance == 3:
                        britain.independents -= 1
def random_economics(britain):
    chance = random.randrange(10, 20000)
    if chance % 6 == 5:
        """Chance that somebody begins to invest
        - very slight increase in GDP
        - increase in happiness
        """
        invest = round(random.uniform(1000, 100000), 2)
        print(f"Somebody started to invest with an amount of ${invest}. What a smart lad.\n")
        time.sleep(3)
        britain.current_gdp += invest
        increase_happiness = round(random.uniform(0.25, 0.75), 2)
        if (britain.happiness + increase_happiness) < 98:
            britain.happiness += increase_happiness

    elif chance % 10 == 7:
        """Chance that somebody loses at their local casino
        - loss in GDP
        - decrease in happiness
        """
        loss = round(random.uniform(10000, 1000000), 2)
        print(f"Somebody just lost ${loss} at their casino.\n")
        time.sleep(3)
        britain.current_gdp -= loss
        decrease_happiness = round(random.uniform(0.25, 0.75), 2)
        if (britain.happiness - decrease_happiness) > 5:
            britain.happiness -= decrease_happiness

    elif chance % 16 == 11:
        """Chance that somebody or government takes out a loan on a specific item(house, car, etc)
        - increase in GDP
        - increase in National debt
        """
        objects = ["car", "home", "boat", "store", "PC", "college degree"]
        loan = round(random.uniform(1000, 1000000), 2)
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance that individual defaults"""
            print(f"Somebody just took a ${loan} loan out for a new {objects[random.randrange(0, len(objects) - 1)]}.\n")
            britain.current_gdp += loan
            britain.national_debt += round(loan * round(random.uniform(0.001, 0.09), 4), 2)
            increase_happiness = round(random.uniform(0.25, 0.75), 2)
            if (britain.happiness + increase_happiness) < 98:
                britain.happiness += increase_happiness

        elif chance == 1:
            """Chance that the government defaults"""
            programs_objects = ["social program", "economic program", "debt paying program", "immigration program",
                                "colonial program"]
            print(f"Our government just took out a ${loan} for a new {programs_objects[random.randrange(0, len(programs_objects) - 1)]}\n")
            britain.current_gdp += loan
            britain.national_debt += round(loan * round(random.uniform(0.001, 0.09), 4), 2)
            increase_happiness = round(random.uniform(0.25, 0.75), 2)
            increase_stability = round(random.uniform(0.01, 0.25), 2)

            if (britain.happiness + increase_happiness) < 98:
                britain.happiness += increase_happiness
            if (britain.stability + increase_stability) < 98:
                britain.stability += increase_stability

    elif chance % 28 == 16:
        """Chance that somebody wins National Lottery
        - increase in GDP
        - increase in national debt
        - decrease in happiness and stability
        """
        lottery = round(random.uniform(1000, 500000), 2)
        print(f"Somebody just won ${lottery} in our national lottery")
        britain.current_gdp += lottery
        britain.national_debt += round(lottery * round(random.uniform(0.001, 0.09), 4), 2)

        increase_happiness = round(random.uniform(0.25, 0.75), 2)
        increase_stability = round(random.uniform(0.01, 0.25), 2)
        if (britain.happiness + increase_happiness) < 98:
            britain.happiness += increase_happiness
        if (britain.stability + increase_stability) < 98:
            britain.stability += increase_stability

    elif chance % 36 == 23:
        """Chance that somebody or government defaults on their loan
        - decrease in GDP
        - increase in national debt if government
        - decrease in happiness and stability
        """
        default = round(random.uniform(1000, 1000000), 2)
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance that individual defaults"""
            print(f"Somebody just defaulted on their loan of ${default}.\n")
            britain.current_gdp -= default
            decrease_happiness = round(random.uniform(0.25, 0.75), 2)
            if (britain.happiness - decrease_happiness) > 5:
                britain.happiness -= decrease_happiness

        elif chance == 1:
            """Chance that the government defaults"""
            print(f"Our government just defaulted on one of our loans of ${default}.\n")
            britain.current_gdp -= default
            decrease_happiness = round(random.uniform(0.25, 0.75), 2)
            decrease_stability = round(random.uniform(0.01, 0.25), 2)
            if (britain.happiness - decrease_happiness) > 5:
                britain.happiness -= decrease_happiness
            if (britain.stability - decrease_stability) > 5:
                britain.stability -= decrease_stability

    elif chance % 44 == 34:
        """Chance that a random amount of banks collapse
        - internal chance of either recession or depression(depends upon severity)-> economic stimulus function is called
        - decrease in GDP
        - increase in National Debt(government spending)
        - decrease in happiness and stability
        """
        banks = random.randrange(2, 45)
        if banks <= 20:
            loss = round(random.uniform(100000, 500000), 2)
            britain.current_gdp -= loss
            britain.national_debt += round(loss * round(random.uniform(0.001, 0.09), 4), 2)
            print(f"{banks} banks just collapsed, resulting in a loss of ${loss}.")

            decrease_happiness = round(random.uniform(0.25, 0.75), 2)
            decrease_stability = round(random.uniform(0.01, 0.25), 2)
            if (britain.happiness - decrease_happiness) > 5:
                britain.happiness -= decrease_happiness
            if (britain.stability - decrease_stability) > 5:
                britain.stability -= decrease_stability

        elif banks > 20 and banks < 35:
            loss = round(random.uniform(1.25, 2.25), 2)
            gdp_loss = britain.current_gdp - (britain.current_gdp / loss)
            britain.current_gdp /= loss
            britain.national_debt += round(gdp_loss * round(random.uniform(0.001, 0.09), 4), 2)
            print(f"{banks} banks just collapsed, resulting in a loss of ${gdp_loss}.")
            print("Your economy has also fallen into a recession from the severity of the collapse.\n")
            britain.economic_state = "recession"
            economic_stimulus(britain)

            decrease_happiness = round(random.uniform(1.25, 2.75), 2)
            decrease_stability = round(random.uniform(0.25, 1.25), 2)
            if (britain.happiness - decrease_happiness) > 5:
                britain.happiness -= decrease_happiness
            if (britain.stability - decrease_stability) > 5:
                britain.stability -= decrease_stability

        elif banks > 35:
            loss = round(random.uniform(2.25, 4.25), 2)
            gdp_loss = britain.current_gdp - (britain.current_gdp / loss)
            britain.current_gdp /= loss
            britain.national_debt += round(gdp_loss * round(random.uniform(0.001, 0.09), 4), 2)
            print(f"{banks} banks just collapsed, resulting in a loss of ${gdp_loss}.")
            print("Your economy has also fallen into a depression from the severity of the collapse.\n")
            britain.economic_state = "depression"
            economic_stimulus(britain)
            decrease_happiness = round(random.uniform(3.25, 4.75), 2)
            decrease_stability = round(random.uniform(1.25, 2.25), 2)
            if (britain.happiness - decrease_happiness) > 5:
                britain.happiness -= decrease_happiness
            if (britain.stability - decrease_stability) > 5:
                britain.stability -= decrease_stability

    elif chance % 67 == 43 and britain.date > britain.econonmic_change_date:
        """Chance that britain falls into a depression
        - decrease in happiness and stability
        - economy slashed by factor of ten
        - potential for monarch or prime minister to be assassinated
        - later on, potential for britain to break up and lose empire
        """
        print("The English economy has randomly fallen into a depression, which the economy has been slashed by 10.\n")
        economic_stimulus(britain)
        britain.economic_state = "depression"
        britain.current_gdp /= 10

        decrease_happiness = round(random.uniform(6.25, 11.75), 2)
        decrease_stability = round(random.uniform(3.25, 6.25), 2)
        if (britain.happiness - decrease_happiness) > 5:
            britain.happiness -= decrease_happiness
        if (britain.stability - decrease_stability) > 5:
            britain.stability -= decrease_stability

        chance = random.randrange(0, 11)
        if chance % 5 == 0:
            """Chance that an assassination occurs"""

            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that monarch gets assassinated"""
                print(f"{britain.monarch} has also been assassinated.")
                britain.monarch = spare_1900_1950_monarchs[random.randrange(0, len(spare_1900_1950_monarchs) - 1)]
                print(f"{britain.monarch} is your new monarch.\n")

            elif chance == 1:
                """Chance that prime minister gets assassinated"""
                print(f"{britain.pm} has also been assassinated.")
                britain.monarch = spare_pms[random.randrange(0, len(spare_pms) - 1)]
                print(f"{britain.pm} is your new prime minister.\n")
        britain.economic_change_date = britain.date + timedelta(days=100)

    elif chance % 78 == 65 and britain.date > britain.econonmic_change_date:
        """Chance that britain falls into an expansion
        - increase in happiness and stability
        - economy multiplied by factor of ten
        """
        print("The English economy has randomly fallen into an expansion, which the economy has been multiplied by 10.\n")
        britain.economic_state = "expansion"
        britain.current_gdp *= 10

        increase_happiness = round(random.uniform(6.25, 11.75), 2)
        increase_stability = round(random.uniform(3.25, 6.25), 2)
        if (britain.happiness + increase_happiness) < 98:
            britain.happiness += increase_happiness
        if (britain.stability + increase_stability) < 98:
            britain.stability += increase_stability

        britain.economic_change_date = britain.date + timedelta(days=100)
def random_social(britain):
    chance = random.randrange(20, 20000)
    if chance % 6 == 8:
        """chance that someone throws a surprise birthday party
        - increase in happiness
        """
        print("Somebody just threw a surprise party.\n")
        time.sleep(3)
        increase_happiness = round(random.uniform(0.25, 0.75), 2)
        if (britain.happiness + increase_happiness) < 98:
            britain.happiness += increase_happiness

    elif chance % 8 == 5:
        """Chance that a parade occurs
        - increase in happiness
        """
        print("A parade just occurred.\n")
        time.sleep(3)
        increase_happiness = round(random.uniform(0.25, 0.75), 2)
        if (britain.happiness + increase_happiness) < 98:
            britain.happiness += increase_happiness

    elif chance % 13 == 11:
        """Chance that somebody gets married
        - increase in happiness and stability
        """
        print("Someone just got married.\n")
        time.sleep(3)

        increase_happiness = round(random.uniform(0.25, 0.75), 2)
        increase_stability = round(random.uniform(0.01, 0.25), 2)
        if (britain.happiness + increase_happiness) < 98:
            britain.happiness += increase_happiness
        if (britain.stability + increase_stability) < 98:
            britain.stability += increase_stability

def random_politics(britain):
    pass
def random_functions(britain):
    random_economics(britain)
    random_social(britain)
    random_politics(britain)
    random_crime(britain)
"""Population functions"""
def population_change(britain):
    if britain.past_year < britain.date.year:
        britain.population_change = (britain.current_pop - britain.past_pop / ((britain.current_pop + britain.past_pop) / 2)) * 100

        britain.past_pop = britain.population
        """Resetting of current population(past)"""
        if britain.population_change <= 1.5:
            """Incorporation of what happens when population growth becomes too small"""
            print(f"Your population growth for {britain.current_year} was {britain.population_change}%\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == 'y':
                britain.viagra_subsidy = True

                if britain.condom_subsidy == True:
                    """Checking to see if condom subsidies exist"""
                    britain.condom_subsidy = False

        elif britain.population_change >= 10.5:
            """Incorporation of what happens when population growth becomes too large"""
            print(f"Your population growth for {britain.current_year} was {britain.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                britain.condom_subsidy = True

                if britain.viagra_subsidy == True:
                    """Checking to see if viagra subsidies exist"""
                    britain.viagra_subsidy = False

    else:
        if britain.viagra_subsidy:
            births = random.randrange(300, 600)
            britain.births += births
            britain.current_pop += births
            for i in range(0, births):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp += 1

                elif chance == 1:
                    britain.liberal += 1

                elif chance == 2:
                    britain.clup += 1

                elif chance == 3:
                    britain.independents += 1

            deaths = random.randrange(200, 400)
            britain.deaths += deaths
            britain.current_pop -= deaths

            for i in range(0, deaths):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp -= 1

                elif chance == 1:
                    britain.liberal -= 1

                elif chance == 2:
                    britain.clup -= 1

                elif chance == 3:
                    britain.independents -= 1

        elif britain.condom_subsidy:
            births = random.randrange(100, 300)
            britain.births += births
            britain.current_pop += births

            for i in range(0, births):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp += 1

                elif chance == 1:
                    britain.liberal += 1

                elif chance == 2:
                    britain.clup += 1

                elif chance == 3:
                    britain.independents += 1

            deaths = random.randrange(100, 200)
            britain.deaths += deaths
            britain.current_pop -= deaths

            for i in range(0, deaths):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp -= 1

                elif chance == 1:
                    britain.liberal -= 1

                elif chance == 2:
                    britain.clup -= 1

                elif chance == 3:
                    britain.independents -= 1

        else:
            births = random.randrange(200, 400)
            britain.births += births
            britain.current_pop += births

            for i in range(0, births):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp += 1

                elif chance == 1:
                    britain.liberal += 1

                elif chance == 2:
                    britain.clup += 1

                elif chance == 3:
                    britain.independents += 1

            deaths = random.randrange(150, 300)
            britain.deaths += deaths
            britain.current_pop -= deaths

            for i in range(0, deaths):
                """Assigning births to political parties"""
                chance = random.randrange(0, 4)
                if chance == 0:
                    britain.lp -= 1

                elif chance == 1:
                    britain.liberal -= 1

                elif chance == 2:
                    britain.clup -= 1

                elif chance == 3:
                    britain.independents -= 1

"""Economic Functions"""
def recovery(britain):
    if britain.economic_stimulus:
        """Depression with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:

            britain.consumer_spending = round(random.uniform(1000, 20000), 2)
            britain.investment = round(random.uniform(1000, 45000), 2)
            britain.government_spending = round(random.uniform(1000, 46000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.05), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.055), 4), 2))

            britain.exports = round(random.uniform(300000, 800000), 2)
            britain.imports = round(random.uniform(200000, 660000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))

        elif britain.tax_rate > 25.00:
            britain.consumer_spending = round(random.uniform(1000, 15000), 2)
            britain.investment = round(random.uniform(1500, 35000), 2)
            britain.government_spending = round(random.uniform(4000, 66000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.05), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.05), 4), 2))

            britain.exports = round(random.uniform(300000, 600000), 2)
            britain.imports = round(random.uniform(120000, 560000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
    else:
        """Recovery without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:
            britain.consumer_spending = round(random.uniform(1000, 15000), 2)
            britain.investment = round(random.uniform(1000, 20000), 2)
            britain.government_spending = round(random.uniform(10000, 25000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.0011, 0.05), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.05), 4), 2))

            britain.exports = round(random.uniform(320000, 700000), 2)
            britain.imports = round(random.uniform(300000, 560000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = round(random.uniform(1000, 10000), 2)
            britain.investment = round(random.uniform(1000, 15000), 2)
            britain.government_spending = round(random.uniform(30000, 70000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.05), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.05), 4), 2))

            britain.exports = round(random.uniform(220000, 450000), 2)
            britain.imports = round(random.uniform(220000, 420000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
def expansion(britain):
    if britain.economic_stimulus:
        """Expansion with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:

            britain.consumer_spending = round(random.uniform(1000, 60000), 2)
            britain.investment = round(random.uniform(1000, 65000), 2)
            britain.government_spending = round(random.uniform(1000, 200000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.01, 0.095), 4), 2))

            britain.exports = round(random.uniform(120000, 1500000), 2)
            britain.imports = round(random.uniform(120000, 950000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))

        elif britain.tax_rate > 25.00:
            britain.consumer_spending = round(random.uniform(1000, 45000), 2)
            britain.investment = round(random.uniform(1000, 45000), 2)
            britain.government_spending = round(random.uniform(1000, 300000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.009), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.01, 0.095), 4), 2))

            britain.exports = round(random.uniform(120000, 750000), 2)
            britain.imports = round(random.uniform(120000, 650000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
    else:
        """Expansion without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:
            britain.consumer_spending = round(random.uniform(1000, 40000), 2)
            britain.investment = round(random.uniform(1000, 45000), 2)
            britain.government_spending = round(random.uniform(1000, 300000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.01), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.0095), 4), 2))

            britain.exports = round(random.uniform(120000, 1300000), 2)
            britain.imports = round(random.uniform(120000, 900000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = round(random.uniform(1000, 4500), 2)
            britain.investment = round(random.uniform(1000, 3500), 2)
            britain.government_spending = round(random.uniform(1000, 55000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.01), 4), 2) +
                                    round(britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))

            britain.exports = round(random.uniform(120000, 1100000), 2)
            britain.imports = round(random.uniform(120000, 950000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
def recession(britain):
    """Recession simulation based upon stimulus and tax rate"""
    if britain.economic_stimulus:
        """Recession with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:

            britain.consumer_spending = -round(random.uniform(1000, 6000), 2)
            britain.investment = -round(random.uniform(1000, 4000), 2)
            britain.government_spending = round(random.uniform(1000, 16000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.01, 0.09), 4), 2))

            britain.exports = round(random.uniform(120000, 750000), 2)
            britain.imports = round(random.uniform(120000, 1100000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 4000), 2)
            britain.investment = -round(random.uniform(1000, 3000), 2)
            britain.government_spending = round(random.uniform(20000, 60000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.01, 0.09), 4), 2))

            britain.exports = round(random.uniform(120000, 560000), 2)
            britain.imports = round(random.uniform(120000, 1100000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
    else:
        """Recession without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 2500), 2)
            britain.investment = -round(random.uniform(1000, 4000), 2)
            britain.government_spending = round(random.uniform(1000, 25000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.01, 0.09), 4), 2))

            britain.exports = round(random.uniform(120000, 560000), 2)
            britain.imports = round(random.uniform(120000, 1100000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 6000), 2)
            britain.investment = -round(random.uniform(1000, 6000), 2)
            britain.government_spending = round(random.uniform(1000, 35000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.09), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.01, 0.09), 4), 2))

            britain.exports = round(random.uniform(120000, 860000), 2)
            britain.imports = round(random.uniform(120000, 1100000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
def depression(britain):
    if britain.economic_stimulus:
        """Depression with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:

            britain.consumer_spending = -round(random.uniform(1000, 9000), 2)
            britain.investment = -round(random.uniform(1000, 6000), 2)
            britain.government_spending = round(random.uniform(1000, 25000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.001, 0.15), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))
            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment)

            britain.exports = round(random.uniform(240000, 800000), 2)
            britain.imports = round(random.uniform(300000, 2000000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 11000), 2)
            britain.investment = -round(random.uniform(1000, 8000), 2)
            britain.government_spending = round(random.uniform(1000, 40000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.11), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))
            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment)


            britain.exports = round(random.uniform(120000, 800000), 2)
            britain.imports = round(random.uniform(120000, 1400000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
    else:
        """Depression without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if britain.tax_rate < 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 2500), 2)
            britain.investment = -round(random.uniform(1000, 4000), 2)
            britain.government_spending = round(random.uniform(1000, 25000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.11), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))
            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment)

            britain.exports = round(random.uniform(120000, 750000), 2)
            britain.imports = round(random.uniform(120000, 1400000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
        elif britain.tax_rate > 25.00:
            britain.consumer_spending = -round(random.uniform(1000, 10000), 2)
            britain.investment = -round(random.uniform(1000, 16000), 2)
            britain.government_spending = round(random.uniform(1000, 35000), 2)
            britain.national_debt += (round(britain.government_spending * round(random.uniform(0.01, 0.21), 4), 2) +
                                    round(-britain.consumer_spending * round(random.uniform(0.001, 0.009), 4), 2))

            britain.exports = round(random.uniform(120000, 590000), 2)
            britain.imports = round(random.uniform(120000, 1400000), 2)

            britain.current_gdp += (britain.consumer_spending + britain.government_spending + britain.investment +
                                  (britain.exports - britain.imports))
def gdp_changes(britain):
    if britain.economic_state == "recovery":
        recovery(britain)
    elif britain.economic_state == "expansion":
        expansion(britain)
    elif britain.economic_state == "recession":
        recession(britain)
    elif britain.economic_state == "depression":
        depression(britain)
def economic_state(britain):
    if britain.date >= britain.economic_change_date:
        """Comparing current date to when Italy's economic state could change"""
        chance = random.randrange(0, 2000)
        if chance % 37 == 10:
            """Making potential for economic disaster really low"""
            if britain.current_gdp < britain.past_gdp:
                """Comparison of current gdp to past gdp"""
                if britain.economic_state == "expansion" or britain.economic_state == "recovery":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "recession":
                            print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                            time.sleep(3)
                            britain.economic_state = business_cycle[i]
                            britain.economic_change_date = britain.date + timedelta(days=240)
                            economic_stimulus(britain)
                            """increasing amount of time to check up on GDP
                            Time is average amount(6 months cycle)
                            """
                elif britain.economic_state == "recession":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "depression":
                            print("Your economy has entered into a depression "
                                  "after exceeding 6 months of decayed growth.\n")
                            time.sleep(3)
                            britain.economic_state = business_cycle[i]
                            britain.economic_change_date = britain.date + timedelta(days=270)
                            economic_stimulus(britain)
                            """
                            Since it takes awhile to escape a depression, amount of time on change date is increased
                            """

        if chance % 40 == 37:
            """making potential for economic expansion or recovery very low"""
            if britain.economic_state == "depression" or britain.economic_state == "recession":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recovery":
                        print("Your economy hs finally entered its recovery period\n")
                        time.sleep(3)
                        britain.economic_state = business_cycle[i]
                        britain.economic_change_date = britain.date + timedelta(days=240)
                        """increasing amount of time to check up on GDP
                        Time is average amount(6 months cycle)
                        """

            elif britain.economic_state == "recovery":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("Your economy has blasted into an expansionary period. Woo!\n")
                        time.sleep(3)
                        britain.economic_state = business_cycle[i]
                        britain.economic_change_date = britain.date + timedelta(days=270)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """
def economic_stimulus(britain):
    britain.economic_stimulus = True

    if britain.economic_state == "recession":
        choice = input("Do you want to increase the tax rate in order to support increased spending?\n"
                       "(Remember this will apply to the entire population): ")

        if choice.lower() == "yes" or choice.lower() == "y":
            valid_choice = False

            while valid_choice:

                tax_hike = float(input("By how much do you to increase taxes(max cap is 10)?: "))
                if tax_hike <= 10 and tax_hike >= 1.0:
                    britain.tax_rate += tax_hike
                    print(f"{britain.tax_rate}% is your new tax rate.\n")
                    time.sleep(3)
                    decrease = round(random.uniform(0.25, 1.45), 2)

                    if (britain.happiness - decrease) < 5:
                        britain.happiness -= decrease

                    valid_choice = True

                elif tax_hike <= 0 or tax_hike > 10:
                    print(f"New tax hike of {tax_hike}% is improper.\n"
                          f"Try again.")
                    time.sleep(3)

                else:
                    print("Not a valid tax rate")
                    time.sleep(3)

    elif britain.economic_state == "depression":
        tax_hike = round(random.uniform(0.5, 10), 2)
        if (britain.tax_rate + tax_hike) <= 68.00:
            if britain.date.year <= 1922 or britain.date.year >= 1946:
                print(f"Parliament has enacted a tax hike of {tax_hike}%\n")

            if britain.date.year > 1922 and britain.date.year < 1946:
                print(f"Il Duce has enacted a tax hike of {tax_hike}%\n")
            time.sleep(3)
def economic_decisions(britain):
    if britain.past_year < britain.date.year:
        britain.economic_growth = round((britain.current_gdp - britain.past_gdp / ((britain.past_gdp + britain.current_gdp) / 2)) * 100, 2)
        """Calculation of yearly economic growth"""
        if britain.economic_growth <= 2.0:
            if not britain.economic_stimulus:
                choice = input(f"Your GDP grew {britain.economic_growth}% last year.\n")
                if choice.lower() == "y" or choice.lower() == "yes":
                    pass
                    economic_stimulus(britain)

        elif britain.economic_growth >= 15.00:
            if britain.economic_stimulus:
                britain.economic_stimulus = False
    else:
        gdp_changes(britain)
        economic_state(britain)

"""Political functions"""
def politics_change(britain):
    if britain.date > britain.political_census:

        chance = random.randrange(0, 4)
        if chance == 0:
            """Chance that the labour party loses support"""
            loss = round(britain.lp * round(random.uniform(0.001, 0.09), 4), 0)
            britain.lp -= loss

            chance = random.randrange(0, 3)
            if chance == 0:
                """Chance that the CLUP party picks up support"""
                britain.clup += loss

            elif chance == 1:
                britain.liberal += loss

            elif chance == 2:
                britain.independents += loss

            britain.political_census = britain.date + timedelta(days=3)
            """Resetting of check in regards to political censuses"""

        elif chance == 1:
            """Chance that Conservative Labour unionist party loses support"""
            loss = round(britain.clup * round(random.uniform(0.01, 0.09), 4), 0)
            britain.clup -= loss
            chance = random.randrange(0, 3)
            if chance == 0:
                """Chance that the Labour party picks up support"""
                britain.lp += loss

            elif chance == 1:
                """Chance that liberals pick up support"""
                britain.liberal += loss

            elif chance == 2:
                """Chance that independent parties pick up support"""
                britain.independents += loss

            britain.political_census = britain.date + timedelta(days=3)
            """Resetting of check in regards to political censuses"""

        elif chance == 2:
            """Chance that independents lose support"""
            loss = round(britain.independents * round(random.uniform(0.01, 0.09), 4), 0)
            britain.independents -= loss

            chance = random.randrange(0, 3)
            if chance == 0:
                """Chance that the CLUP party picks up support"""
                britain.clup += loss

            elif chance == 1:
                """Chance that liberals pick up support"""
                britain.liberal += loss

            elif chance == 2:
                """Chance that the labour party pick up support"""
                britain.lp += loss

            britain.political_census = britain.date + timedelta(days=3)
            """Resetting of check in regards to political censuses"""

        elif chance == 3:
            """Chance that liberal party loses support"""
            loss = round(britain.liberal * round(random.uniform(0.01, 0.09), 4), 0)
            britain.liberal -= loss

            chance = random.randrange(0, 3)
            if chance == 0:
                """Chance that the CLUP party picks up support"""
                britain.clup += loss

            elif chance == 1:
                """Chance that the Labour party picks up support"""
                britain.lp += loss

            elif chance == 2:
                """Chance that Independent parties picks up support"""
                britain.independents += loss

            britain.political_census = britain.date + timedelta(days=3)
            """Resetting of check in regards to political censuses"""

"""Stats function"""
def stats(britain):
    """stats function
    1. population
    2. political
    3. economic
    4. social
    5. others
    """
    print(f"Your current population is {britain.current_pop}.\n"
          f"There have been {britain.births} births in {britain.past_year}.\n"
          f"There have been {britain.deaths} deaths in {britain.past_year}.\n"
          f"Your current prime minister is {britain.pm}.\n"
          f"Your current monarch is {britain.monarch}.\n"
          f"The liberal party makes up {round(round(britain.liberal / britain.current_pop, 4) * 100, 4)}% of the population.\n"
          f"The conservative and liberal unionist party makes up {round(round(britain.clup / britain.current_pop, 4) * 100, 4)}% of the population.\n"
          f"The Labour Party makes up {round(round(britain.lp / britain.current_pop, 4) * 100, 4)}% of the population.\n"
          f"Independents make up {round(round(britain.independents / britain.current_pop, 4) * 100, 4)}% of the population.\n"
          f"Your current GDP is ${britain.current_gdp}.\n"
          f"Your current GDP growth is {round((britain.current_gdp - britain.past_gdp) / ((britain.current_gdp + britain.current_gdp)/2) * 100, 6)}%\n")
def manual_game(britain):
    while britain.current_pop > 500000:
        # establishment of check upon game status
        print(britain.date)
        population_change(britain)
        politics_change(britain)
        random_functions(britain)
        economic_decisions(britain)
        if britain.stability > 5:
            choice = input("Would you like to view your stats?: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                stats(britain)
        britain.date += timedelta(days=1)
        time.sleep(3)

class Britain:
    def __init__(self, time):
        """time variables"""
        self.date = datetime(int(time), 1, 1)
        self.past_year = self.date.year
        self.political_census = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        """population variables"""
        self.current_pop = population[time]
        self.births = 0
        self.deaths = 0
        self.past_pop = self.current_pop
        self.population_change = None
        self.viagra_subsidy = False
        self.condom_subsidy = False
        """Political variables"""
        self.monarch = monarchs[time]
        self.pm = pm[time]
        self.stability = 90.00
        self.lp = round(self.current_pop * round(random.uniform(0.09, 0.35), 4), 0)
        # labour party
        self.clup = round((self.current_pop - self.lp) * round(random.uniform(0.09, 0.35), 4), 0)
        # conservative and liberal unionist party
        self.liberal = round((self.current_pop - self.lp - self.clup) * round(random.uniform(0.09, 0.35), 4), 0)
        # liberal party
        self.independents = self.current_pop - self.clup - self.lp - self.liberal
        """economic variables"""
        self.current_gdp = gdp[time]
        self.past_gdp = self.current_gdp
        self.national_debt = 0
        self.economic_growth = None
        self.economic_state = "recovery"
        self.economic_stimulus = False
        self.tax_rate = tax_rate[time]
        """Social variables"""
        self.happiness = 90.00