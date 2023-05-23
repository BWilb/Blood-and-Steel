import random
import time
from datetime import datetime, timedelta
import arcade
"""Population Dictionaries"""
population = {
    # population will be set up to increase or decrease randomly throughout every year
    "1910": 92410000,
    "1914": 99110000,
    "1918": 103210000,
    "1932": 124840000,
    "1936": 128050000,
    "1939": 130880000
}
"""Political Dictionaries"""
presidents = {
    "1910": "William Howard Taft",
    "1914": "Woodrow Wilson",
    "1918": "Woodrow Wilson",
    "1932": "Herbert Hoover",
    "1936": "Franklin D. Roosevelt",
    "1939": "Franklin D. Roosevelt"
}

vice_presidents = {
    # dictionary of vice presidents incase president gets assassinated
    "1910": "James S. Sherman",
    "1914": "Thomas R. Marshall",
    "1918": "Thomas R. Marshall",
    "1932": "Charles Curtis",
    "1936": "John Garner",
    "1939": "Henry Wallace"
}
"""Economic dictionaries & Variables"""
business_cycle = ["recovery", "expansion", "recession", "depression"]
gdp = {
    "1910": 520000000000,
    "1914": 500000000000,
    "1918": 550000000000,
    "1932": 550000000000,
    "1936": 575000000000,
    "1939": 1100000000000
}

tax_rate = {
    "1910": 0,
    "1914": 1.00,
    "1918": 6.00,
    "1932": 4.00,
    "1936": 4.00,
    "1939": 4.00
}

"""Subsidiary functions of game"""

"""Weather functions"""
def blackout(us):
    if us.date < us.blackout_date:
        us.population -= random.randrange(1, 34)
        loss = round(random.uniform(2000, 50000), 2)
        """Representing loss in consumer spending"""
        us.gdp -= loss
        us.national_debt += loss * 0.75
        spending = round(random.uniform(10000, 100000), 2)
        us.gdp += round(random.uniform(10000, 100000), 2)
        """representing government spending to support nation and/or communities"""
        us.national_debt += spending * 0.75
        us.happiness -= round(random.uniform(0.01, 0.25), 2)
        us.stability -= round(random.uniform(0.01, 0.1), 2)
    else:
        us.blackout = False

"""Happiness and Stability functions"""

def happiness_and_stability(us):
    """
    Function controls the stability and happiness of the nation.
    Happiness & stability are based upon...
    1. Each other
    2. The Economy
    """
    chance = random.randrange(0, 2)
    if us.economic_state == "recession":
        """if economy is in recession. moderate decrease"""
        if us.tax_rate >= 25.00:

            if not us.happiness <= 4.00:
                """
                Setting constraint upon happiness.
                In order to prevent falling into negative range
                * chance also plays part(some people may become happier) * 
                """
                if chance == 0:
                    us.happiness -= round(random.uniform(0.56, 1.23), 2)

                elif chance == 1:
                    us.happiness += round(random.uniform(0.26, 0.57), 2)

            if not us.stability <= 15:
                us.stability -= round(random.uniform(0.25, 0.75), 2)

    elif us.economic_state == "depression":
        """if economy is in depression. extreme decrease"""
        if us.tax_rate >= 30.00:

            if not us.happiness <= 10.00:
                """
                Setting constraint upon happiness.
                In order to prevent falling into negative range
                """

                if chance == 0:
                    us.happiness -= round(random.uniform(1.56, 7.35), 2)

                elif chance == 1:
                    us.happiness += round(random.uniform(1.25, 5.54), 2)

            if not us.stability <= 20:
                us.stability -= round(random.uniform(1.25, 5.45), 2)

    elif us.economic_state == "recovery":
        """if economy is in recovery. moderate increase"""
        if us.tax_rate >= 20.00:

            if not us.happiness >= 98.56:
                """
                Setting constraint upon happiness.
                In order to prevent falling into negative range
                """
                if chance == 0:
                    us.happiness -= round(random.uniform(0.35, 2.34), 2)

                    if not us.stability <= 14.65:
                        us.stability -= round(random.uniform(0.10, 1.14), 2)

                elif chance == 1:
                    us.happiness += round(random.uniform(0.45, 3.33), 2)

                    if not us.stability >= 97.85:
                        us.stability += round(random.uniform(0.23, 2.34), 2)

    elif us.economic_state == "expansion":
        """if economy is in expansion. extreme increase"""
        if us.tax_rate >= 15.00:

            if not us.happiness >= 98.56:
                """
                Setting constraint upon happiness.
                In order to prevent falling into negative range
                """
                if chance == 0:
                    us.happiness -= round(random.uniform(1.45, 5.67), 2)

                    if not us.stability <= 14.65:
                        us.stability -= round(random.uniform(0.95, 4.96), 2)

                elif chance == 1:
                    us.happiness += round(random.uniform(0.85, 5.33), 2)

                    if not us.stability >= 97.85:
                        us.stability += round(random.uniform(0.75, 4.34), 2)

    if us.happiness < 50.00:
        """
        Just as with the economy, overall happiness can affect the stability
        of a nation.
        """
        chance = random.randrange(0, 2)

        if chance == 0:
            us.stability += round(random.uniform(1.34, 5.56), 2)

        elif chance == 1:
            us.stability -= round(random.uniform(2.45, 6.56), 2)

    if us.stability < 45.00:
        """
        Just as with the economy, overall stability can affect the happiness
        of a nation.
        """
        chance = random.randrange(0, 2)

        if chance == 0:
            us.happiness += round(random.uniform(1.34, 5.56), 2)

        elif chance == 1:
            us.happiness -= round(random.uniform(2.45, 6.56), 2)
"""population functions"""
def population_change(us):
    if us.current_year < us.date.year:
        us.population_change = (us.population - us.current_pop / ((us.population + us.current_pop) / 2)) * 100

        us.current_pop = us.population

        if us.population_change <= 1.5:
            """Incorporation of what happens when population growth becomes too small"""
            print(f"Your population growth for {us.current_year} was {us.population_change}%")
            choice = input("Would you like to subsidize viagra?: ")

            if choice.lower() == "yes" or choice.lower() == "y":
                us.viagra_subsidy = True
                us.condom_subsidy = False

        elif us.population_change >= 8:
            """Incorporation of what happens when population growth becomes too large"""
            print(f"Your population growth for {us.current_year} was {us.population_change}%")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == "yes" or choice.lower():
                us.condom_subsidy = True
                us.viagra_subsidy = False

    else:
        if us.viagra_subsidy:
            """incorporation of births and deaths under viagra subsidies"""
            births = random.randrange(700, 2400)
            us.births += births
            us.population += births

            deaths = random.randrange(300, 1200)
            us.deaths += deaths
            us.population -= deaths

        elif us.condom_subsidy:
            """incorporation of births and deaths under condom subsidies"""
            births = random.randrange(500, 2000)
            us.births += births
            us.population += births

            deaths = random.randrange(400, 1800)
            us.deaths += deaths
            us.population -= deaths

        else:
            """Incorporation of births and deaths under regular circumstances"""
            births = random.randrange(600, 2200)
            us.births += births
            us.population += births

            deaths = random.randrange(500, 1500)
            us.deaths += deaths
            us.population -= deaths

"""political functions"""

def political_changes(us):
    chance = random.randrange(0, 2)
    if chance == 0:
        change = us.republicans * random.uniform(0.05, 0.25)
        us.republicans -= change
        us.democrats += change

    else:
        change = us.democrats * random.uniform(0.05, 0.25)
        us.democrats -= change
        us.republicans += change

"""Random functions"""


def random_economics(us):
    chance = random.randrange(10, 20000)

    if chance % 8 == 5:
        """chance that someone loses their savings @ a casino
        - decrease in happiness
        """
        loss = round(random.uniform(10000, 900000), 2)
        print(f"Someone just lost ${loss} at their local Casino\n")

        decrease = round(random.uniform(0.55, 2.00), 2)
        if (us.happiness - decrease) > 5:
            us.happiness -= decrease

        us.current_gdp -= round(loss * round(random.uniform(0.1, 0.65), 2), 2)
        time.sleep(3)

    elif chance % 12 == 7:
        """chance that somebody gets robbed
        - potential for death
        - decrease in happiness
        """
        death = random.randrange(0, 2)
        if death == 0:
            print("Someone just got mugged. They were left unharmed though!\n")
            decrease = round(random.uniform(0.55, 1.55), 2)
            if (us.happiness - decrease) > 5:
                us.happiness -= decrease
            time.sleep(3)

        elif death == 1:
            print("Someone just got mugged. The mugging resulted in the victims death\n")
            us.population -= 1
            decrease = round(random.uniform(0.55, 1.25), 2)
            if (us.happiness - decrease) > 5:
                us.happiness -= decrease
            time.sleep(3)

    elif chance % 15 == 6:
        """chance that a bank gets robbed
        - loss in GDP
            -> investment
        - potential death(s)
        - decrease in happiness
        - decrease in stability
        - increase in government and consumer(bank owner) debt to cover bank losses
        """
        robbery = round(random.uniform(756000, 50000000), 2)
        death_chance = random.randrange(0, 2)
        deaths = random.randrange(10, 40)
        if death_chance == 0:
            print(f"A bank robbery just occurred. The bank lost ${robbery} in assets\n")
        if death_chance == 1:
            print(f"A bank robbery just occurred. The bank lost ${robbery} in assets.\n"
                  f"The robber was also armed, killing {deaths} people.\n")
            us.deaths += deaths

            decrease = round(random.uniform(0.25, 5.56), 2)
            if (us.happiness - decrease) > 5:
                us.happiness -= decrease
            """Checks upon both happiness and stability"""
            if us.stability > 10:
                us.stability -= decrease

        us.current_gdp -= robbery
        us.national_debt += round(robbery * round(random.uniform(0.25, 0.65), 2), 2)
        # partial government and consumer(bank) spending in order to replace stolen assets
        time.sleep(3)

    elif chance % 17 == 2:
        """Chance that Congress decides to spend extra money
        - increase in government debt
        - increase in GDP
        - increase in stability
        """
        money = round(random.uniform(345000, 1000000), 2)
        print(f"Congress decided to spend an extra ${money} today.\n")
        us.national_debt += round(money * round(random.uniform(0.25, 0.65), 2), 2)
        us.current_gdp += money
        time.sleep(3)

    elif chance % 20 == 3:
        """Chance that a bank or multiple banks collapse
        - decrease in GDP
            -> loss in investment
            -> increase in government spending
                -> increase in national debt
        - decrease in stability and happiness
        """
        amount = random.randrange(1, 30)
        loss = round(random.uniform(645000, 3000000), 2)
        us.current_gdp -= loss
        # GDP decreases in wake of loss

        decrease = round(random.uniform(1.25, 10.56), 2)
        if (us.happiness - decrease) > 5:
            us.happiness -= decrease
        """Checks upon both happiness and stability"""
        if us.stability > 10:
            us.stability -= decrease

        print(f"{amount} banks just collapsed. There has been an estimated ${loss} lost\n")
        time.sleep(3)

    elif chance % 28 == 6 and us.date > us.tax_change_date:
        """Chance that congress decides to raise taxes
        - decrease in happiness
        - decrease in stability
        - increase of government spending and national debt(other functions)
        - increase in democratic support
        - decrease in republican support
        """
        tax_hike = round(random.uniform(1.25, 10.5), 2)
        if (us.tax_rate + tax_hike) <= 50:
            print(f"Congress has decided to raise taxes by {tax_hike}%\n")
            us.tax_rate += tax_hike

            decrease = round(random.uniform(0.45, 5.56), 2)
            if (us.happiness - decrease) > 5:
                us.happiness -= decrease

            if us.stability > 10:
                us.stability -= decrease

            us.tax_change_date = us.date + timedelta(days=75)

            rep_loss = us.republicans * round(random.uniform(0.01, 0.25), 2)
            if us.democrats + rep_loss < 100:
                us.democrats += rep_loss

            if us.republicans - rep_loss > 0:
                us.republicans -= rep_loss
        time.sleep(3)

    if chance % 33 == 2:
        """Chance that someone wins the lottery
        - increase in happiness
        - increase in consumer debt
        """
        lottery = round(random.uniform(125000, 956000), 2)
        us.national_debt += round(lottery * round(random.uniform(0.10, 0.35), 2), 2)
        happy = round(random.uniform(0.25, 1.00))
        if us.happiness + happy < 98:
            us.happiness += happy

        print(f"Someone just won ${lottery} in their local lottery\n")
        time.sleep(3)

    elif chance % 35 == 12 and us.date > us.tax_change_date:
        """chance that congress decides to lower taxes
        - increase in happiness
        - increase in stability 
        - increase of consumer spending
        - decrease of government spending and increase of national debt(consumer spending)
        - increase in republican support
        - decrease of democratic support
        """
        tax_cut = round(random.uniform(1.25, 10.5))
        if (us.tax_rate + tax_cut) >= 50:
            print(f"Congress has decided to raise taxes by {tax_cut}%\n")
            us.tax_rate += tax_cut

            increase = round(random.uniform(0.45, 5.56), 2)
            if (us.happiness + increase) < 98:
                us.happiness += increase
            """Checks upon both happiness and stability"""
            if (us.stability + increase) < 95:
                us.stability += increase

            us.tax_change_date = us.date + timedelta(days=75)
            dem_loss = us.democrats * round(random.uniform(0.01, 0.25), 2)

            if us.republicans + dem_loss < 100:
                us.republicans += dem_loss

            if us.democrats - dem_loss > 0:
                us.democrats -= dem_loss
        time.sleep(3)

    elif (chance % 42 == 9 and us.date >= us.economic_change_date) and \
            us.economic_state != "recession":
        """chance that economy collapses into depression
        - stimulus function gets called
        - gdp gets slashed by a factor of 5
            -> time for potential cycle change is reset
        - stability and happiness decrease
        - government spending increases and national debt increases
        - later on, potential for pieces of the Union to break off
        """
        for i in range(0, len(business_cycle) - 1):
            if business_cycle[i] == "recession":
                us.economic_state = business_cycle[i]

        print("It seems like your economy has fallen into a recession.\n"
              "Your current GDP has been slashed by 2.\n")
        time.sleep(3)
        us.current_gdp /= 2
        economic_stimulus(us)
        decrease = round(random.uniform(10.56, 25), 2)
        if (us.happiness - decrease) > 5:
            us.happiness -= decrease
        """Checks upon both happiness and stability"""
        if us.stability > 10:
            us.stability -= decrease
        recovery_spending = round(random.uniform(120000, 900000), 2)
        us.current_gdp += recovery_spending
        us.national_debt += round(recovery_spending * round(random.uniform(0.25, 0.75), 2), 2)
        us.economic_change_date = us.date + timedelta(days=120)
        time.sleep(3)

    elif (chance % 48 == 5 and us.date >= us.economic_change_date) and \
            us.economic_state != "recovery":
        """chance that economy experiences boom
        - tax rate decreases
        - gdp gets multiplied by 2
        - investment increases
        - national debt increases
            -> consumer spending increases
        - stability and happiness increase
        """
        print("Very Interesting...the US economy has suddenly experienced a recovery.\n"
              "This recovery has increased the US GDP by a factor of 2\n")

        for i in range(0, len(business_cycle) - 1):
            if business_cycle[i] == "recovery":
                us.economic_state = business_cycle[i]
        us.current_gdp *= 2

        increase = round(random.uniform(2.56, 20), 2)
        if (us.happiness + increase) < 98:
            us.happiness += increase
            """Checks upon both happiness and stability"""
        if (us.stability + increase) < 95:
            us.stability += increase

        increased_consumer = round(random.uniform(120000, 900000), 2)
        us.current_gdp += increased_consumer * 1.25
        # increase in consumer spending is multiplied by 1.25 in order to represent increase in spending
        us.national_debt += round(increased_consumer * round(random.uniform(0.25, 0.75), 2), 2)
        us.economic_change_date = us.date + timedelta(days=120)
        time.sleep(3)

    elif (chance % 59 == 18 and us.date >= us.economic_change_date) and \
            us.economic_state != "expansion":

        """chance that economy experiences boom
        - tax rate decreases
        - gdp gets multiplied by 2
        - investment increases
        - national debt increases
            -> consumer spending increases
        - stability and happiness increase
        """
        print("Very Interesting...the US economy has suddenly experienced an expansion.\n"
              "This recovery has increased the US GDP by a factor of 5\n")

        for i in range(0, len(business_cycle) - 1):
            if business_cycle[i] == "expansion":
                us.economic_state = business_cycle[i]
        us.current_gdp *= 5

        increase = round(random.uniform(2.56, 20), 2)
        if (us.happiness + increase) < 98:
            us.happiness += increase
            """Checks upon both happiness and stability"""
        if (us.stability + increase) < 95:
            us.stability += increase

        increased_consumer = round(random.uniform(1200000, 9000000), 2)
        us.current_gdp += increased_consumer * 1.5
        # increase in consumer spending is multiplied by 1.5 in order to represent increase in spending
        us.national_debt += round(increased_consumer * round(random.uniform(0.25, 0.75), 2), 2)
        us.economic_change_date = us.date + timedelta(days=120)
        time.sleep(3)

    elif (chance % 67 == 12 and us.date >= us.economic_change_date) and \
            us.economic_state != "depression":
        """chance that economy collapses into depression
        - stimulus function gets called
        - gdp gets slashed by a factor of 5
            -> time for potential cycle change is reset
        - stability and happiness decrease
        - government spending increases and national debt increases
        - later on, potential for entire Union to break apart
        """
        for i in range(0, len(business_cycle) - 1):
            if business_cycle[i] == "depression":
                us.economic_state = business_cycle[i]

        print("It seems like your economy has fallen into a recession.\n"
              "Your current GDP has been slashed by 5.\n")
        time.sleep(3)
        us.current_gdp /= 5
        economic_stimulus(us)
        decrease = round(random.uniform(10.56, 25), 2)
        if (us.happiness - decrease) > 5:
            us.happiness -= decrease

        if us.stability > 10:
            us.stability -= decrease

        recovery_spending = round(random.uniform(1200000, 9000000), 2)
        us.current_gdp += recovery_spending
        us.national_debt += round(recovery_spending * round(random.uniform(0.25, 0.75), 2), 2)
        us.economic_change_date = us.date + timedelta(days=120)
        time.sleep(3)

def random_social(us):
    chance = random.randrange(10, 20000)
    if chance % 5 == 0:
        """Very likely chance that a college dorm party occurs
        within this chance, there will be a probability of deaths from drunkenness
        - increase in happiness 
            -> decrease in happiness if death
        """
        print("A college dorm is throwing a wild party\n")
        time.sleep(3)
        chance = random.randrange(0, 2)
        if chance == 1:
            people = random.randrange(1, 30)
            print(f"Well bad news...{people} people died from partying a little to hard.\n")
            us.population -= people
            us.deaths += people
            time.sleep(3)
            us.happiness -= random.randrange(1, 4)
        else:
            increase = round(random.uniform(0.25, 7), 2)

            us.happiness += random.randrange(2, 7)

    elif chance % 8 == 0:
        """Chance that a high school party occurs
        within this chance, there will be a probability of deaths from drunkenness(possibly murder later on)
        - increase in happiness 
            -> decrease in happiness if death
        """
        print("A popular high school cheerleader is throwing a wild party\n")
        time.sleep(3)
        chance = random.randrange(0, 2)
        if chance == 1:
            people = random.randrange(1, 30)
            print(f"Well bad news...{people} people died from partying a little to hard.\n")
            us.population -= people
            us.deaths += people
            time.sleep(3)
            us.happiness -= random.randrange(1, 4)
        else:
            us.happiness += random.randrange(2, 7)

    elif chance % 10 == 3:
        """Chance that someone throws a surprise birthday party for their child
        - increase in happiness
        """
        print("Someone just threw their child a surprise party\n")
        us.happiness += round(random.uniform(0.25, 1.25), 2)
        time.sleep(3)

    elif chance % 12 == 5:
        """Chance that someone gets married
        - increase in happiness and stability
        """
        print("someone just got married\n")
        time.sleep(3)
        us.stability += round(random.uniform(0.25, 0.75), 2)
        us.happiness += round(random.uniform(0.25, 1.75), 2)

    elif chance % 15 == 4:
        """Chance that somebody converts and begins to believe in God
        -> Christian, Islamic, Jewish, or other
        - increase in happiness and stability
        """
        religions = ["Jewish", "Christian", "Islamic"]
        print(
            f"An Atheist just converted to believing in the {religions[random.randrange(0, len(religions) - 1)]} God\n")
        us.stability += round(random.uniform(0.25, 0.75), 2)
        us.happiness += round(random.uniform(0.25, 1.75), 2)
        time.sleep(3)

    elif chance % 18 == 4:
        """Chance that a parade occurs
        - increase in happiness
        """
        print("A parade occurred, Huzzah.\n")
        us.happiness += round(random.uniform(0.25, 1.75), 2)
        time.sleep(3)

    elif chance % 21 == 2:
        """Chance that a random place gets shot up
        - decrease in population, happiness, and stability
        """
        locations = ["School", "Library", "Restaurant", "Bakery", "Courthouse", "Bank"]
        deaths = random.randrange(6, 100)
        print(f"Oh no there was a shooting at a local {locations[random.randrange(0, len(locations) - 1)]}.\n"
              f"This shooting resulted in the deaths of {deaths} people.\n")
        us.stability += round(random.uniform(0.25, 1.75), 2)
        us.happiness += round(random.uniform(0.25, 4.75), 2)
        us.population -= deaths
        time.sleep(3)

    elif chance % 26 == 3:
        """Chance that someone rolls their car into a group of people
        decrease in population
        """
        deaths = random.randrange(3, 25)
        print(f"Someone just rolled their car into a group of people. {deaths} people died.\n")
        us.population -= deaths
        time.sleep(3)

def random_politics(us):
    chance = random.randrange(10, 20000)
    if chance % 5 == 0:
        """Chance that a protest occurs
        - stability decreases
        """
        protests = ["Abortion", "Gun", "Free Speech", "Women's Rights",
                    "Men's Rights", "Immigration"]
        print(f"A(n) {protests[random.randrange(0, len(protests) - 1)]} protest occurred\n")
        us.stability -= round(random.uniform(0.25, 0.75), 2)
        time.sleep(3)

    elif chance % 8 == 3:
        """Chance that political parties are reversed in amount of support
        """
        republicans = us.democrats
        us.democrats = us.republicans
        us.republicans = republicans
        print("Both Republicans and Democrats swapped popularity\n")
        time.sleep(3)

    elif chance % 16 == 5:
        """chance that a special interest group gets sued
        - decrease in stability
        - decrease in GDP
            -> investment
        """
        spig = ["BLM", "NRA", "NAACP", "GOA", "FreedomWorks", "Common Cause", "RNC", "DNC"]
        lawsuit = round(random.uniform(200000, 800000), 2)
        print(f"{spig[random.randrange(0, len(spig) - 1)]} experienced a lawsuit of ${lawsuit}\n")
        us.current_gdp -= lawsuit

    elif chance % 21 == 8:
        """Chance that congressman is assassinated 
        - stability decreases
        - chance that they're replaced with republican or democrat
        """
        kill = random.randrange(0, 2)
        if kill == 0:
            print("Oh no, a democratic congressman was just assassinated.")
            replacement = random.randrange(0, 2)
            if replacement == 0:
                print("A republican congressman has replaced the dead congressman place\n")
            elif replacement == 1:
                print("A democratic congressman has replaced the dead congressman place\n")

        elif kill == 1:
            print("Oh no, a republican congressman was just assassinated.")
            replacement = random.randrange(0, 2)
            if replacement == 0:
                print("A republican congressman has replaced the dead congressman place\n")
            elif replacement == 1:
                print("A democratic congressman has replaced the dead congressman place\n")

    elif chance % 48 == 5:
        """Chance that the speaker of the house gets assassinated(will be filled in later)
        - decrease in stability and happiness
        - Decrease in population
        """
    elif chance % 60 == 8:
        """Chance that the Vice president gets assassinated(will be filled in later)
        - decrease in stability and happiness
        - decrease in consumer spending and GDP
        - Decrease in population
        """

    elif chance % 78 == 4:
        """Chance that the President gets assassinated(will be filled in later)
        - Decrease in stability and happiness
        - Potential for Economic Recession or Depression to occur
        - Potential for the US to dissolve
        - Decrease in population
        """
    elif chance % 90 == 7:
        """Chance for a revolt/revolution against the government to occur(will be filled in later)
        -> potential factions will include hyper-nationalists, communists, socialists, monarchists, foreign actors
        - decrease in stability and happiness
        - GDP gets slashed by factor of 12
        - Any alliance the US is in, will have the US kicked out
        - Decrease in population as civil war ensues
        """

def random_weather(us):
    chance = random.randrange(10, 20000)
    if us.date == datetime(us.date.year, 4, 1):
        print("Tornado Season has begun!!!\n")
        time.sleep(3)

    elif us.date == datetime(us.date.year, 8, 1):
        print("Tornado Season has ended.\n")

    elif us.date == datetime(us.date.year, 6, 1):
        print("Hurricane Season has begun!!!\n")
        time.sleep(3)
    elif us.date == datetime(us.date.year, 11, 1):
        print("Hurricane Season has ended.\n")
        time.sleep(3)

    if chance % 7 == 0:
        """Chance for a thunderstorm
        later on will increase the amount of food resources for specific time period
        """
        print("A thunderstorm has occurred\n")
        us.happiness += round(random.uniform(0.10, 0.80), 2)
        time.sleep(3)

    elif chance % 12 == 5:
        """chance for lightning to strike personal property
        - very slight decrease in GDP
        - decrease in happiness
        """
        property = ["Car", "Home", "Swimming Pool", "Barbecue", "Deck", "Garden",
                    "Trailer", "Camper"]
        print(f"Lightning just struck someone's {property[random.randrange(0, len(property) - 1)]}\n")

        us.happiness -= round(random.uniform(0.10, 0.80), 2)
        us.current_gdp -= round(random.uniform(1000, 10000), 2)

    elif chance % 14 == 3 and (us.date.month <= 4 or us.date.month >= 1):
        """Chance for ice storm
        - internal chance for blackouts
            -> if black severe loss in...
                - life
                - GDP
                - increase in government spending and national debt
                - decrease in stability and happiness
        - if no blackout
        - potential for death
        - decrease in happiness
        """
        chance = random.randrange(0, 20)
        if chance % 19 == 0 and us.blackout != True:
            print("A major ice storm just occurred across the nation, knocking out power and causing a blackout.\n"
                  "It is being reported that the black out will be fixed within the next 15 - 60 days\n")
            time.sleep(3)
            us.blackout_date = us.date + timedelta(days=random.randrange(15, 60))
            us.blackout = True
        else:
            print("A major ice storm just occurred within the nation.\n"
                  "Fortunately nothing major occurred.\n")
            us.happiness -= round(random.uniform(0.25, 2.25), 2)
            us.stability -= round(random.uniform(0.25, 1.25), 2)
        pass

    elif chance % 16 == 3 and (us.date.month <= 8 and us.date.month >= 4):
        """Chance that tornado forms
        internal chance whether tornado is EF0-EF5
        - Decrease in GDP
        - Decrease in Population if deaths occur
            -> based upon another chance
        - Decrease in happiness
        **Decrements based upon severity of tornado
        """
        time.sleep(3)
        scale = random.randrange(0, 6)
        if scale == 0:
            print("An EF0 tornado just struck a local town.\n")
            death_chance = random.randrange(0, 2)
            if death_chance == 1:
                deaths = random.randrange(1, 16)
                us.population -= deaths
                us.deaths += deaths
                print(f"This has resulted in {deaths} death(s)")

            property_damage = round(random.uniform(1000, 20000), 2)
            print(f"Overall there has been ${property_damage} in damage\n")
            us.gdp -= property_damage
            decrease_happiness = round(random.uniform(0.76, 1.45), 2)
            decrease_stability = round(random.uniform(0.10, 0.75), 2)
            if (us.happiness - decrease_happiness) >= 3.5:
                us.happiness -= decrease_happiness
            if (us.happiness - decrease_stability) >= 5:
                us.stability -= decrease_stability
            time.sleep(3)

        elif scale == 1:
            print("An EF1 tornado just struck a local town.\n")
            death_chance = random.randrange(0, 2)
            if death_chance == 1:
                deaths = random.randrange(1, 30)
                us.population -= deaths
                us.deaths += deaths
                print(f"This has resulted in {deaths} death(s)")

            property_damage = round(random.uniform(6000, 40000), 2)
            print(f"Overall there has been ${property_damage} in damage\n")
            us.gdp -= property_damage
            decrease_happiness = round(random.uniform(0.76, 2.45), 2)
            decrease_stability = round(random.uniform(0.10, 1.25), 2)
            if (us.happiness - decrease_happiness) >= 3.5:
                us.happiness -= decrease_happiness
            if (us.happiness - decrease_stability) >= 5:
                us.stability -= decrease_stability
            time.sleep(3)

        elif scale == 2:
            print("An EF2 tornado just struck a local town.\n")
            death_chance = random.randrange(0, 2)
            if death_chance == 1:
                deaths = random.randrange(1, 50)
                us.population -= deaths
                us.deaths += deaths
                print(f"This has resulted in {deaths} death(s)")

            property_damage = round(random.uniform(7000, 500000), 2)
            print(f"Overall there has been ${property_damage} in damage\n")
            us.gdp -= property_damage
            decrease_happiness = round(random.uniform(0.76, 3.45), 2)
            decrease_stability = round(random.uniform(0.10, 2.25), 2)
            if (us.happiness - decrease_happiness) >= 3.5:
                us.happiness -= decrease_happiness
            if (us.happiness - decrease_stability) >= 5:
                us.stability -= decrease_stability
            time.sleep(3)

        elif scale == 3:
            print("An EF3 tornado just struck a local town.\n")
            death_chance = random.randrange(0, 2)
            if death_chance == 1:
                deaths = random.randrange(1, 75)
                us.population -= deaths
                us.deaths += deaths
                print(f"This has resulted in {deaths} death(s)")

            property_damage = round(random.uniform(24000, 1200000), 2)
            print(f"Overall there has been ${property_damage} in damage\n")
            us.gdp -= property_damage
            decrease_happiness = round(random.uniform(0.76, 4.45), 2)
            decrease_stability = round(random.uniform(0.10, 3.25), 2)
            if (us.happiness - decrease_happiness) >= 3.5:
                us.happiness -= decrease_happiness
            if (us.happiness - decrease_stability) >= 5:
                us.stability -= decrease_stability
            time.sleep(3)

        elif scale == 4:
            print("An EF4 tornado just struck a local town.\n")
            death_chance = random.randrange(0, 2)
            if death_chance == 1:
                deaths = random.randrange(1, 100)
                us.population -= deaths
                us.deaths += deaths
                print(f"This has resulted in {deaths} death(s)")

            property_damage = round(random.uniform(500000, 3400000), 2)
            print(f"Overall there has been ${property_damage} in damage\n")
            us.gdp -= property_damage
            decrease_happiness = round(random.uniform(0.76, 6.45), 2)
            decrease_stability = round(random.uniform(0.10, 4.25), 2)
            if (us.happiness - decrease_happiness) >= 3.5:
                us.happiness -= decrease_happiness
            if (us.happiness - decrease_stability) >= 5:
                us.stability -= decrease_stability
            time.sleep(3)

        elif scale == 5:
            print("An EF5 tornado just struck a local town.\n")
            death_chance = random.randrange(0, 2)
            if death_chance == 1:
                deaths = random.randrange(1, 200)
                us.population -= deaths
                us.deaths += deaths
                print(f"This has resulted in {deaths} death(s)")

            property_damage = round(random.uniform(700000, 6000000), 2)
            print(f"Overall there has been ${property_damage} in damage\n")
            us.gdp -= property_damage

            decrease_happiness = round(random.uniform(0.76, 8.45), 2)
            decrease_stability = round(random.uniform(0.10, 6.25), 2)
            if (us.happiness - decrease_happiness) >= 3.5:
                us.happiness -= decrease_happiness
            if (us.happiness - decrease_stability) >= 5:
                us.stability -= decrease_stability
            time.sleep(3)

    elif chance % 18 == 5 and (us.date.month <= 4 or us.date.month >= 1):
        """Chance that a blizzard occurs
        -> internal chance of death
            - decrease in population
        - decrease in stability 
        - decrease in happiness
        """
        print("A blizzard just occurred\n")
        chance = random.randrange(0, 2)
        if chance == 1:
            deaths = random.randrange(1, 100)
            damages = round(random.uniform(10000, 1000000), 2)
            print(f"{deaths} deaths occurred and there was ${damages} in damage\n")
            us.current_gdp -= damages
            us.population -= deaths
            us.deaths += deaths
            decrease_happiness = round(random.uniform(0.76, 3.45), 2)
            decrease_stability = round(random.uniform(0.10, 1.25), 2)
            if (us.happiness - decrease_happiness) >= 3.5:
                us.happiness -= decrease_happiness
            if (us.happiness - decrease_stability) >= 5:
                us.stability -= decrease_stability
            time.sleep(3)
        pass

    elif chance % 20 == 6 and (us.date.month <= 11 and us.date.month >= 6):
        """Chance that a hurricane occurs
        - Decrease in stability
        - Decrease in happiness
        - Internal chance of death
            -> decrease in population
        - Decrease in GDP
        """

        category = random.randrange(1, 6)
        if category == 1:
            print(f"A Category {category} hurricane is occurring now\n")
            death_chance = random.randrange(0, 2)
            damages = round(random.uniform(10000, 300000), 2)
            if death_chance == 1:
                """If death is true"""
                deaths = random.randrange(2, 90)
                us.population -= deaths
                us.deaths += deaths
                print(f"{deaths} people died and there were ${damages} in damages\n")
                time.sleep(3)

            else:
                print(f"nobody was harmed, however there were ${damages} in damages\n")
                time.sleep(3)
                us.gdp -= damages
                decrease_happiness = round(random.uniform(0.76, 6.45), 2)
                decrease_stability = round(random.uniform(0.10, 4.25), 2)
                if (us.happiness - decrease_happiness) >= 3.5:
                    us.happiness -= decrease_happiness
                if (us.happiness - decrease_stability) >= 5:
                    us.stability -= decrease_stability

        if category == 2:
            print(f"A Category {category} hurricane is occurring now\n")
            death_chance = random.randrange(0, 2)
            damages = round(random.uniform(50000, 600000), 2)
            if death_chance == 1:
                """If death is true"""
                deaths = random.randrange(2, 200)
                us.population -= deaths
                us.deaths += deaths
                print(f"{deaths} people died and there were ${damages} in damages\n")
                time.sleep(3)

            else:
                print(f"nobody was harmed, however there were ${damages} in damages\n")
                time.sleep(3)
                us.gdp -= damages
                decrease_happiness = round(random.uniform(0.76, 6.45), 2)
                decrease_stability = round(random.uniform(0.10, 4.25), 2)
                if (us.happiness - decrease_happiness) >= 3.5:
                    us.happiness -= decrease_happiness
                if (us.happiness - decrease_stability) >= 5:
                    us.stability -= decrease_stability

        if category == 3:
            print(f"A Category {category} hurricane is occurring now\n")
            death_chance = random.randrange(0, 2)
            damages = round(random.uniform(100000, 1000000), 2)
            if death_chance == 1:
                """If death is true"""
                deaths = random.randrange(2, 300)
                us.population -= deaths
                us.deaths += deaths
                print(f"{deaths} people died and there were ${damages} in damages\n")
                time.sleep(3)

            else:
                print(f"nobody was harmed, however there were ${damages} in damages\n")
                time.sleep(3)
                us.gdp -= damages
                decrease_happiness = round(random.uniform(0.76, 7.45), 2)
                decrease_stability = round(random.uniform(0.10, 5.25), 2)
                if (us.happiness - decrease_happiness) >= 3.5:
                    us.happiness -= decrease_happiness
                if (us.happiness - decrease_stability) >= 5:
                    us.stability -= decrease_stability

        if category == 4:
            print(f"A Category {category} hurricane is occurring now\n")
            death_chance = random.randrange(0, 2)
            damages = round(random.uniform(600000, 7000000), 2)
            if death_chance == 1:
                """If death is true"""
                deaths = random.randrange(2, 500)
                us.population -= deaths
                us.deaths += deaths
                print(f"{deaths} people died and there were ${damages} in damages\n")
                time.sleep(3)

            else:
                print(f"nobody was harmed, however there were ${damages} in damages\n")
                time.sleep(3)
                us.gdp -= damages
                decrease_happiness = round(random.uniform(0.76, 9.45), 2)
                decrease_stability = round(random.uniform(0.10, 6.25), 2)
                if (us.happiness - decrease_happiness) >= 3.5:
                    us.happiness -= decrease_happiness
                if (us.happiness - decrease_stability) >= 5:
                    us.stability -= decrease_stability

        if category == 5:
            print(f"A Category {category} hurricane is occurring now\n")
            death_chance = random.randrange(0, 2)
            damages = round(random.uniform(1000000, 50000000), 2)
            if death_chance == 1:
                """If death is true"""
                deaths = random.randrange(2, 1000)
                us.population -= deaths
                us.deaths += deaths
                print(f"{deaths} people died and there were ${damages} in damages\n")
                time.sleep(3)

            else:
                print(f"nobody was harmed, however there were ${damages} in damages\n")
                time.sleep(3)
                us.gdp -= damages
                decrease_happiness = round(random.uniform(0.76, 12.45), 2)
                decrease_stability = round(random.uniform(0.10, 8.25), 2)
                if (us.happiness - decrease_happiness) >= 3.5:
                    us.happiness -= decrease_happiness
                if (us.happiness - decrease_stability) >= 5:
                    us.stability -= decrease_stability
        pass

    elif chance % 30 == 7 and (us.date.month <= 10 and us.date.month >= 4):
        """Chance for a wildfire to occur
        - internal chance for loss of life
        - decrease in happiness and stability
        - decrease in GDP via consumer spending
            - increase via government spending (balances out)
            - increase in debt
        - soon to be decrease in natural and economic resources
        """
        regions = ["southwest", "northeast", "south", "midwest", "west", "east", "Alaska", "Hawaii"]
        print(f"Oh no...there is a wildfire spreading within (the) {regions[random.randrange(0, len(regions) - 1)]}.\n")
        chance = random.randrange(0, 2)
        economic_loss = round(random.uniform(10000, 900000), 2)
        if chance == 1:
            deaths = random.randrange(2, 40)
            print(f"{deaths} people have died and there has been ${economic_loss} in damage.\n")
            us.population -= deaths
            us.deaths += deaths
        us.national_debt += economic_loss * 0.75
        us.happiness -= round(random.uniform(0.01, 4.25), 2)
        us.stability -= round(random.uniform(0.01, 2.25), 2)

    elif chance % 50 == 3:
        """Chance that someone gets struck by lightning
        - decrease in happiness
        - decrease in population
        """
        print("Someone just got struck by lightning and died\n")
        time.sleep(3)
        decrease_happiness = round(random.uniform(0.76, 1.25), 2)
        decrease_stability = round(random.uniform(0.10, 0.75), 2)
        if (us.happiness - decrease_happiness) >= 3.5:
            us.happiness -= decrease_happiness
        if (us.happiness - decrease_stability) >= 5:
            us.stability -= decrease_stability
        us.population -= 1
        us.deaths += 1
def random_international(us):
    pass
def randomized_functions(us):
    random_economics(us)
    random_politics(us)
    random_social(us)
    random_weather(us)
    random_international(us)
"""Economic Functions"""

def economic_state(us):
    if us.date >= us.economic_change_date:
        """comparing current date with possible shift in business cycle, based upon 3 month cycle"""
        if us.past_gdp > us.current_gdp:
            """comparing past gdp to current gdp"""
            if us.economic_state == "expansion" or us.economic_state == "recovery":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recession":
                        print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=240)
                        economic_stimulus(us)
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif us.economic_state == "recession":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "depression":
                        print("Your economy has entered into a depression "
                              "after exceeding 6 months of decayed growth.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=210)
                        economic_stimulus(us)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """

        elif us.past_gdp < us.current_gdp:
            if us.economic_state == "depression" or us.economic_state == "recession":
                """current state is expansion or recovery"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recovery":
                        print("Your economy has finally entered its recovery period.\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=360)
                        """increasing amount of time to check up on GDP
                        Time is average amount(5 months cycle)
                        """

            elif us.economic_state == "recovery":
                """current state is recession and cycle is switching to depression"""
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("Your economy has finally entered its expansionary period. Woo!!!\n")
                        time.sleep(3)
                        us.economic_state = business_cycle[i]
                        us.economic_change_date = us.date + timedelta(days=120)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """
def slow_growth(us):
    us.consumer_spending = round(random.uniform(3000, 7500), 2)
    us.investment = round(random.uniform(2000, 5400), 2)

    us.government_spending = round(random.uniform(3000, 5000), 2)

    us.national_debt += (us.government_spending * round(random.uniform(0.05, 0.45), 2) +
                         us.consumer_spending * round(random.uniform(0.05, 0.30), 2))
    """
    National debt includes both portions of US government spending and consumer spending.
    The portions are comprised of the loans and bonds that are bought and sold
    """

    us.exports = round(random.uniform(4500, 75000), 2)
    us.imports = round(random.uniform(3200, 56000), 2)
    us.current_gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    us.happiness += 0.15

def fast_growth(us):
    us.consumer_spending = round(random.uniform(80000, 150000), 2)
    us.investment = round(random.uniform(60000, 150000), 2)
    us.government_spending = round(random.uniform(50000, 175000), 2)

    us.national_debt += (us.government_spending * round(random.uniform(0.05, 0.45), 2) +
                         us.consumer_spending * round(random.uniform(0.05, 0.30), 2))
    """
    National debt includes both portions of US government spending and consumer spending.
    The portions are comprised of the loans and bonds that are bought and sold
    """

    us.exports = round(random.uniform(15000, 170000), 2)
    us.imports = round(random.uniform(14000, 100000), 2)
    us.current_gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    us.happiness += 0.25

def slow_fall(us):
    us.consumer_spending = -(round(random.uniform(3500, 10250), 2))
    us.investment = -(round(random.uniform(3000, 40000), 2))
    if us.economic_stimulus:
        us.government_spending = round(random.uniform(75000, 3250000), 2)

    else:
        us.government_spending = round(random.uniform(50000, 7650000), 2)

    us.national_debt += (us.government_spending * round(random.uniform(0.05, 0.45), 2) +
                         -(us.consumer_spending) * round(random.uniform(0.05, 0.30), 2))
    """
    National debt includes both portions of US government spending and consumer spending.
    The portions are comprised of the loans and bonds that are bought and sold
    """

    us.exports = round(random.uniform(14000, 65000), 2)
    us.imports = round(random.uniform(14000, 140000), 2)
    us.current_gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    us.happiness -= 0.15
    us.stability -= round(random.uniform(0.15, 1.05), 2)

def fast_fall(us):
    us.consumer_spending = -(round(random.uniform(6000, 455000), 2))
    us.investment = -(round(random.uniform(6000, 560000), 2))
    if us.economic_stimulus:
        us.government_spending = round(random.uniform(500000, 12500000), 2)

    else:
        us.government_spending = round(random.uniform(50000, 1250000), 2)

    us.national_debt += (us.government_spending * round(random.uniform(0.05, 0.45), 2) +
                         -(us.consumer_spending) * round(random.uniform(0.05, 0.30), 2))
    """
    National debt includes both portions of US government spending and consumer spending.
    The portions are comprised of the loans and bonds that are bought and sold
    """

    us.exports = round(random.uniform(1200, 420000), 2)
    us.imports = round(random.uniform(140000, 1400000), 2)
    us.current_gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    us.happiness -= 0.25
    us.stability -= round(random.uniform(0.25, 1.25), 2)

def gdp_change(us):
    if us.economic_state == "recovery":
        slow_growth(us)

    elif us.economic_state == "expansion":
        fast_growth(us)

    elif us.economic_state == "recession":
        slow_fall(us)

    elif us.economic_state == "depression":
        fast_fall(us)

def economic_stimulus(us):
    us.stimulus = True

    if us.economic_state.lower() == "recession":
        choice = input("\nDo you want to increase the tax rate in order to support increased spending"
                       "(Remember this applies to the entire population)?:")
        """Prompting user to choose if they want to increase taxes"""

        if choice.lower() == "yes" or choice.lower() == "y":
            valid_choice = False

            while valid_choice:
                tax_hike = float(input("By how much do you want to increase taxes(max cap is 25)?: "))

                if tax_hike <= 25 and tax_hike >= 0.5:
                    """if statement covering if tax hike meets criteria"""
                    us.tax_rate += round(tax_hike, 2)
                    print(f"{us.tax_rate}% is your new tax rate")
                    us.happiness -= round(random.uniform(0.25, 3.45), 2)
                    us.stability -= round(random.uniform(0.25, 1.45), 2)
                    valid_choice = True

                elif tax_hike <= 0 or tax_hike > 25:
                    print(f"New tax hike of {tax_hike} is improper./n"
                          f"try again")
                    time.sleep(3)

                else:
                    print("Not a valid tax rate")
                    time.sleep(3)

    elif us.economic_state.lower() == "depression":

        tax_hike = round(random.uniform(10, 25), 2)
        if (us.tax_rate + tax_hike) <= 86.00:
            print(f"Congress has enacted a tax hike of {tax_hike} points")

def economic_decisions(us):
    if us.current_year < us.date.year:
        us.economic_growth = (us.current_gdp - us.past_gdp / ((us.past_gdp + us.current_gdp) / 2)) * 100

        if us.economic_growth <= 1.5:
            choice = input(f"Your GDP grew {us.economic_growth}% last year.\n"
                           f"Would you like to apply a stimulus?: ")

            if choice.lower() == "yes" or choice.lower() == "y":
                economic_stimulus(us)

    else:
        gdp_change(us)

"""Function designed to check stats"""
def check_stats(us):
    """Stats organized by...
    1. Politics
    2. Economics
    3. Social aspects
    4. Others
    """
    print(f"Your current President is {us.president}\n"
          f"Your current Vice President is {us.vice_president}\n"
          f"Democrats make up {round((us.democrats / us.population) * 100, 2)}% of the population\n"
          f"Republicans make up {round((us.republicans / us.population) * 100, 2)}% of the population\n"
          f"Your current political stability is {round(us.stability, 2)}%\n"
          f"Your current GDP is ${round(us.current_gdp, 2)}\n"
          f"Your economy is currently in a(n) {us.economic_state} period\n"
          f"Your current yearly gdp growth is {round(((us.current_gdp - us.past_gdp) / ((us.past_gdp + us.current_gdp) / 2)) * 100, 5 )}%\n"
          f"Your current national debt is ${round(us.national_debt, 2)}\n"
          f"Your current tax rate is {round(us.tax_rate, 2)}%\n"
          f"There have been {us.deaths} deaths that have occurred in {us.current_year}\n"
          f"There have been {us.births} births that have occurred in {us.current_year}\n"
          f"The current happiness rating of the United States is {round(us.happiness, 2)}%\n")

"""Main function of US_Version of game"""
def manual_game(us):
    # Establishment of date variable
    while us.population > 2000000:
        us.date = us.date + timedelta(days=1)
        print(f"Date: {us.date}")
        # function will incorporate daily changes in us population
        population_change(us)
        political_changes(us)
        economic_decisions(us)
        economic_state(us)
        randomized_functions(us)
        if us.blackout == True:
            blackout(us)

        if us.stability >= 50:
            choice = input("Important!!! view your stats: ")
            if choice == "y" or choice == "yes":
                check_stats(us)
class UnitedStates:
    def __init__(self, year):
        # population variables
        self.population = population[year]
        self.population_change = 0
        self.current_pop = self.population
        self.births = 0
        self.deaths = 0
        self.happiness = 96.56
        """Population controller if birth rate gets out of control"""
        self.condom_subsidy = False
        """Population controller if birth rate flops"""
        self.viagra_subsidy = False
        # political variables
        """Leaders of US"""
        self.president = presidents[year]
        self.vice_president = vice_presidents[year]
        """Political parties of US"""
        self.republicans = self.population * 0.5
        self.democrats = self.population - self.republicans
        """Other political variables"""
        self.stability = 95.00
        # economic variables
        self.economic_state = business_cycle[0]
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        """holds current year of gdp(used for comparing with future GDP
        to determine GDP growth)
        """
        self.national_debt = 0
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        """Taxes components"""
        self.tax_rate = tax_rate[year]
        # weather variables
        self.blackout = False
        self.blackout_date = None
        # military variables
        # international variables
        self.alliance = ""
        # time variables
        self.date = datetime(int(year), 1, 1)
        self.tax_change_date = self.date + timedelta(days=75)
        self.economic_change_date = self.date + timedelta(days=60)
        self.current_year = self.date.year

def main(time):
    united_states = UnitedStates(time)
    manual_game(united_states)