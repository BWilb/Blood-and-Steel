import random
import time


def random_economics(us):
    chance = random.randrange(10, 20000)

    if chance % 3 == 2:
        """Chance that someone wins the lottery
        - increase in happiness
        - increase in consumer debt
        """
        lottery = round(random.uniform(125000, 956000), 2)
        us.national_debt += round(lottery * 0.45, 2)
        us.happiness -= round(random.uniform(0.25, 1.00))
        print(f"Someone just won ${lottery} in their local lottery")
        time.sleep(3)
        
    elif chance % 8 == 5:
        """chance that someone loses their savings @ a casino
        - decrease in happiness
        """
        print(f"Someone just lost ${round(random.uniform(10000, 900000))} at their local Casino")
        us.happiness -= round(random.uniform(0.55, 2.00))
        time.sleep(3)

    elif chance % 12 == 7:
        """chance that somebody gets robbed
        - potential for death
        - decrease in happiness
        """
        death = random.randrange(0, 2)
        if death == 0:
            print("Someone just got mugged. They were left unharmed though!")
            us.happiness -= round(random.uniform(0.55, 1.55))
            time.sleep(3)
            
        elif death == 1:
            print("Someone just got mugged. The mugging resulted in the victims death")
            us.population -= 1
            us.happiness -= round(random.uniform(0.55, 1.25))
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
            print(f"A bank robbery just occurred. The bank lost ${robbery} in assets")
        if death_chance == 0:
            print(f"A bank robbery just occurred. The bank lost ${robbery} in assets.\n"
                  f"The robber was also armed, killing {deaths} people.")
            us.deaths += deaths
        us.stability -= round(random.uniform(0.25, 1.24), 2)
        us.happiness -= round(random.uniform(2.34, 5.56), 2)
        us.gdp -= robbery
        us.national_debt += round(robbery * 0.75)
        time.sleep(3)

    elif chance % 17 == 2:
        """Chance that Congress decides to spend extra money
        - increase in government debt
        - increase in GDP
        - increase in stability
        """
        pass

    elif chance % 20 == 3:
        """Chance that a bank or multiple banks collapse
        - decrease in GDP
            -> loss in investment
            -> increase in government spending
                -> increase in national debt
        - decrease in stability and happiness
        """

    elif chance % 28 == 6:
        """Chance that congress decides to raise taxes
        - decrease in happiness
        - decrease in stability
        - increase of government spending and national debt
        - increase in democratic support
        - decrease in republican support
        """

    elif chance % 35 == 12:
        """chance that congress decides to lower taxes
        - increase in happiness
        - increase in stability 
        - increase of consumer spending
        - decrease of government spending and increase of national debt(consumer spending)
        - increase in republican support
        - decrease of democratic support
        """

    elif chance % 42 == 9 and us.economic_state != "depression":
        """chance that economy collapses into depression
        - stimulus function gets called
        - gdp gets slashed by a factor of 10
            -> time for potential cycle change is reset
        - stability and happiness decrease
        - government spending increases and national debt increases
        - later on, potential for entire Union to break apart
        """

    elif chance % 48 == 5:
        """chance that economy experiences boom
        - tax rate decreases
        - gdp gets multiplied by 4
        - investment increases
        - national debt increases
            -> consumer spending increases
        - stability and happiness increase
        """
def random_social(us):
    pass

def random_politics(us):
    pass

def random_weather(us):
    pass

def random_international(us):
    pass

def randomized_functions(us):
    random_economics(us)
    random_politics(us)
    random_social(us)
    random_weather(us)
    random_international(us)