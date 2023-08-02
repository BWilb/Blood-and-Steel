"""within this file contains functions designed to make every day for each nation random.
even though this game runs along historical baselines as best it can,
random functions could throw the original timeline off"""
import random
import time
from datetime import timedelta


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
            print("The victim of the stabbing has survived.\n")
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

    elif chance % 11 == 5:
        """9.10% chance that a bank is robbed
        """
        loss = round(random.uniform(10000, 1000000), 2)
        print(f"A bank was just robbed in {nation.name} resulting in a loss of ${loss} in GDP.\n")
        time.sleep(1.5)
        nation.current_gdp -= loss

        happiness_decrease = round(random.uniform(0.05, 1.15), 2)
        stability_decrease = round(random.uniform(0.05, 0.75), 2)
        if (nation.happiness - happiness_decrease) > 5:
            nation.happiness -= happiness_decrease

        if (nation.stability - stability_decrease) > 5:
            nation.stability -= stability_decrease

    elif chance % 25 == 7:
        """3.98% chance that homicide occurs"""
        chance = random.randrange(1, 20)
        if chance % 2 == 0:
            kills = random.randrange(1, 10)
            print(f"A homicide occurred in {nation.name} resulting in {kills} people killed.\n")

            nation.population -= kills

            happiness_decrease = round(random.uniform(0.05, 1.15), 2)
            stability_decrease = round(random.uniform(0.05, 0.75), 2)
            if (nation.happiness - happiness_decrease) > 5:
                nation.happiness -= happiness_decrease

            if (nation.stability - stability_decrease) > 5:
                nation.stability -= stability_decrease

        if chance % 6 == 5:
            kills = random.randrange(10, 20)
            print(f"A homicide occurred in {nation.name} resulting in {kills} people killed.\n")

            nation.population -= kills

            happiness_decrease = round(random.uniform(1.15, 2.25), 2)
            stability_decrease = round(random.uniform(0.75, 1.75), 2)
            if (nation.happiness - happiness_decrease) > 5:
                nation.happiness -= happiness_decrease

            if (nation.stability - stability_decrease) > 5:
                nation.stability -= stability_decrease

        if chance % 12 == 7:
            kills = random.randrange(30, 60)
            print(f"A homicide occurred in {nation.name} resulting in {kills} people killed.\n")

            nation.population -= kills

            happiness_decrease = round(random.uniform(1.25, 2.55), 2)
            stability_decrease = round(random.uniform(1.12, 2.75), 2)
            if (nation.happiness - happiness_decrease) > 5:
                nation.happiness -= happiness_decrease

            if (nation.stability - stability_decrease) > 5:
                nation.stability -= stability_decrease

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

    elif chance % 16 == 6:
        """6.25% chance that government of any specific nation causes its debt to double in a single day due to overspending"""
        print(f"Due to lack of control in government spending, {nation.name}'s debt has doubled.\n")
        time.sleep(1.5)
        nation.national_debt *= 2

    elif chance % 20 == 5:
        """4.98% chance that random amount(1-20) of banks collapse"""
        banks = random.randrange(1, 20)
        if banks < 5:
            loss = round(random.uniform(1000, 100000), 2)
            print(f"{banks} banks have collapsed in {nation.name}.\n"
                  f"The collapse has resulted in a loss of ${loss} in GDP.\n")
            time.sleep(1.25)
            nation.current_gdp -= loss

            stability_loss = round(random.uniform(0.25, 0.75), 2)
            happiness_loss = round(random.uniform(1.01, 2.01), 2)
            if (nation.happiness - happiness_loss ) > 5:
                nation.happiness -= happiness_loss

            if (nation.stability - stability_loss) > 5:
                nation.stability -= stability_loss

        elif banks > 5 and banks < 15:
            loss = nation.current_gdp * round(random.uniform(0.001, 0.01), 2)
            print(f"{banks} banks have collapsed in {nation.name}.\n"
                  f"The collapse has resulted in a loss of ${loss} in GDP")
            time.sleep(1.25)

            nation.current_gdp -= loss

            stability_loss = round(random.uniform(0.75, 1.75), 2)
            happiness_loss = round(random.uniform(2.01, 4.01), 2)
            if (nation.happiness - happiness_loss) > 5:
                nation.happiness -= happiness_loss

            if (nation.stability - stability_loss) > 5:
                nation.stability -= stability_loss

        else:
            loss = nation.current_gdp * round(random.uniform(0.01, 0.05), 2)
            print(f"{banks} banks have collapsed in {nation.name}.\n"
                  f"The collapse has resulted in a loss of ${loss} in GDP")
            time.sleep(1.25)

            nation.current_gdp -= loss

            stability_loss = round(random.uniform(1.75, 3.25), 2)
            happiness_loss = round(random.uniform(3.01, 5.01), 2)
            if (nation.happiness - happiness_loss) > 5:
                nation.happiness -= happiness_loss

            if (nation.stability - stability_loss) > 5:
                nation.stability -= stability_loss
    elif chance % 300 == 50:
        """0.334% chance that specific nation's economy falls into a depression"""
        if nation.date > nation.economic_change_date:
            print(f"{nation.name}'s economy has fallen into a depression\n")
            time.sleep(1.5)
            nation.e_s = "depression"
            nation.economic_change_date += timedelta(days=120)
    elif chance % 400 == 50:
        """0.268% chance that specific nation's economy falls into an expansion"""
        if nation.date > nation.economic_change_date:
            print(f"{nation.name}'s economy has blasted into an expansion")
            time.sleep(1.5)
            nation.e_s = "expansion"
            nation.economic_change_date += timedelta(days=120)
def random_functions(nation, globe):
    random_social_events(nation)
    random_economics(nation)
    random_social_events(nation)
    random_international_events(nation, globe)
    random_crime(nation)