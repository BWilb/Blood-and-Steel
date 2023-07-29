"""within this file contains functions designed to make every day for each nation random.
even though this game runs along historical baselines as best it can,
random functions could throw the original timeline off"""
import random
import time


def random_international_events(nation, globe):
    pass
def random_social_events(nation):
    pass
def random_politics(nation):
    pass
def random_crime(nation):
    chance = random.randrange(10, 3000)
    if chance % 3 == 0:
        """33.31% chance that someone gets stabbed"""
        print(f"A citizen from {nation.name} has been stabbed.")
        chance = random.randrange(0, 2)
        if chance == 1:
            print("The victim of the stabbing has survived.")
            time.sleep(1.25)
            happiness_decrease = round(random.uniform(0.05, 1.00), 2)
            stability_decrease = round(random.uniform(0.05, 0.56), 2)
            if (nation.happiness - happiness_decrease) > 5:
                nation.happiness -= happiness_decrease

            if (nation.stability - stability_decrease) > 5:
                nation.stability -= stability_decrease

        else:
            print("The victim of the stabbing has survived.\n")
            time.sleep(1.25)
            happiness_decrease = round(random.uniform(0.05, 1.15), 2)
            stability_decrease = round(random.uniform(0.05, 0.75), 2)
            if (nation.happiness - happiness_decrease) > 5:
                nation.happiness -= happiness_decrease

            if (nation.stability - stability_decrease) > 5:
                nation.stability -= stability_decrease

    elif chance % 4 == 3:
        """24.98% chance that someone gets robbed"""
        loss = round(random.uniform(10, 250), 2)
        print(f"A citizen from {nation.name} was robbed of ${loss}.\n")
        time.sleep(1.25)
        nation.current_gdp -= loss

        happiness_decrease = round(random.uniform(0.05, 1.15), 2)
        stability_decrease = round(random.uniform(0.05, 0.75), 2)
        if (nation.happiness - happiness_decrease) > 5:
            nation.happiness -= happiness_decrease

        if (nation.stability - stability_decrease) > 5:
            nation.stability -= stability_decrease

    elif chance % 6 == 5:
        """16.69% chance that government forcefully liquidates a bank
        
        """
def random_economics(nation):
    chance = random.randrange(10, 3000)
    if chance % 3 == 2:
        """33.4% chance that someone from any nation takes out a loan for any specific thing(home, car, etc)"""
        objects = ["Home", "Car", "Business", "Investment", "Estate"]
        loan = round(random.uniform(10000, 250000), 2)
        print(f"A citizen from {nation.name} has pulled out a loan for a new {objects[random.randrange(0, len(objects) - 1)]}.\n"
              f"The loan was worth ${loan}.\n")
        time.sleep(1.5)

        nation.current_gdp += round(loan * round(random.uniform(0.15, 0.25), 5), 2)
        nation.national_debt += round(loan * round(random.uniform(0.05, 0.10), 5), 2)

    elif chance % 4 == 3:
        """25.02% chance that some from any nation begins to invest"""
        initial = round(random.uniform(100, 10000), 2)
        print(f"A smart lad from {nation.name} has decided to begin investing with an initial ${initial}.\n")
        time.sleep(1.5)

        nation.current_gdp += initial

    elif chance % 5 == 0:
        """20% chance that someone from any nation loses something valuable
        affects both gdp and national debt(consumer debt)
        """
        objects = ["home", "business", "estate", "car"]
        loss = round(random.uniform(1000, 100000), 2)
        debt = round(random.uniform(100, 10000), 2)

        print(f"Someone from {nation.name} lost their {objects[random.randrange(0, len(objects) - 1)]} resulting in a ${loss} loss\n"
              f"They have taken out a ${debt} loan.\n")

        happiness_decrease = round(random.uniform(1.05, 2.96), 2)
        if (nation.happiness - happiness_decrease) > 5:
            nation.happiness -= happiness_decrease
        time.sleep(1.5)
def random_functions(nation, globe):
    random_social_events(nation)
    random_economics(nation)
    random_social_events(nation)
    random_international_events(nation, globe)
    random_crime(nation)