import random
import time
from datetime import timedelta

def rebellion(germany):
    if (germany.date <= germany.riot_over) or germany.rebellers != 0:
        loss = round(random.uniform(0.01, 0.09), 2) * germany.rebellers
        print(f"Today, we were able to defeat(kill) {round(loss, 2)} rebels today")
        time.sleep(3)
        civilian_loss = random.randrange(30, 1000)
        germany.rebel_deaths += (loss + civilian_loss)
        germany.deaths += loss
        germany.rebellers -= loss
        germany.population -= loss

        germany.stability -= round(random.uniform(0.75, 3.75), 2)
        germany.happiness -= round(random.uniform(1.75, 5.75), 2)

        germany.current_gdp -= round(random.uniform(1000, 40000), 2)
        germany.national_debt += round(random.uniform(100000, 400000), 2)

    else:
        print("The rebellion in our Vaterland is finally over.\n"
              f"Around {germany.rebel_deaths} deaths(both civilian and rebels) occurred in our scuffle.\n")
        time.sleep(3)
        germany.stability += round(random.uniform(0.75, 3.75), 2)
        germany.happiness += round(random.uniform(1.75, 5.75), 2)
def random_crime(germany):
    chance = random.randrange(10, 20000)
    if chance % 4 == 5:
        """Chance that somebody gets mugged
        - chance for death
        - decrease in happiness
        """
        death_chance = random.randrange(0, 2)
        print("A mugging has just occurred.\n")
        if death_chance == 1:
            print("The mugging has resulted in the victims death")
            germany.deaths += 1
            germany.population -= 1
            decrease = round(random.uniform(0.1, 0.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease
        else:
            decrease = round(random.uniform(0.1, 0.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease

    elif chance % 6 == 7:
        """Chance that someone burglarizes a house
        - internal chance for death
        - decrease in happiness
        """
        death_chance = random.randrange(0, 2)
        print("A burglary has just occurred.\n")
        if death_chance == 1:
            deaths = random.randrange(1, 7)
            print(f"The burglary has resulted in the {deaths} death(s)")
            germany.deaths += deaths
            germany.population -= deaths
            decrease = round(random.uniform(0.1, 0.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease
        else:
            decrease = round(random.uniform(0.1, 0.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease

    elif chance % 12 == 9:
        """Chance that a homicide occurs
        - decrease in stability and happiness
        - decrease in population
        """
        deaths = random.randrange(3, 56)
        print(f"A homicide has just occurred.\n"
              f"{deaths} deaths occurred during this homicide.\n")
        time.sleep(3)
        germany.population -= deaths
        germany.deaths += deaths

        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability

    elif chance % 13 == 7:
        """Chance that somebody decides to rob a bank
        - internal chance of it being successful or not
            -> further internal chance if death occurs
                * Decrease happiness and stability
                * Decrease in population if people are killed
            * Decrease in happiness and stability
            * Decrease in GDP
                - will be a drop by 3/4 of what was lost
            * increase in national debt to replace losses
                - both government and consumer spending
        """
        chance = random.randrange(0, 2)
        if chance == 0:
            """Chance if bank robbery is successful"""
            chance_two = random.randrange(0, 2)
            if chance_two == 0:
                """Chance that the failed robbery is non-lethal"""
                print("A bank robbery was just attempted.\n"
                      "The robber was unsuccessful and nobody got hurt.\n")
                time.sleep(3)

            elif chance_two == 1:
                """Chance that failed robbery is lethal"""
                deaths = random.randrange(3, 20)
                print("A bank robbery was just attempted.\n"
                      f"The robber was unsuccessful, but killed {deaths} people in the process\n")
                time.sleep(3)
                germany.deaths += deaths
                germany.population -= deaths
                stability_increase = round(random.uniform(0.1, 1.00), 2)
                happiness_increase = round(random.uniform(1.25, 3.00), 2)

                if (germany.happiness - happiness_increase) > 5:
                    germany.happiness -= happiness_increase

                if (germany.stability - stability_increase) > 5:
                    germany.stability -= stability_increase

        elif chance == 1:
            """Chance that bank robbery is successful"""
            chance_two = random.randrange(0, 2)
            if chance_two == 0:
                """Chance that bank robbery was successful yet non lethal"""
                loss = round(random.uniform(10000, 900000), 2)
                print(f"A bank robbery just occurred. The specific bank lost ${loss}.\n"
                      f"Fortunately nobody was hurt")
                time.sleep(3)

                germany.current_gdp -= loss
                germany.national_debt += round(loss * round(random.uniform(0.25, 0.75), 2), 2)

                stability_increase = round(random.uniform(0.5, 1.25), 2)
                happiness_increase = round(random.uniform(1.00, 2.25), 2)

                if (germany.happiness - happiness_increase) < 5:
                    germany.happiness -= happiness_increase

                if (germany.stability - stability_increase) < 5:
                    germany.stability -= stability_increase

            elif chance == 1:
                """Chance that bank robbery is successful and lethal"""
                loss = round(random.uniform(10000, 900000), 2)
                deaths = random.randrange(3, 20)
                print(f"A bank robbery just occurred. The specific bank lost ${loss}.\n"
                      f"{deaths} deaths occurred during this bank robbery\n")
                time.sleep(3)

                germany.current_gdp -= loss
                germany.national_debt += round(loss * round(random.uniform(0.25, 0.75), 2), 2)

                stability_increase = round(random.uniform(1.00, 2.00), 2)
                happiness_increase = round(random.uniform(1.00, 3.25), 2)

                if (germany.happiness - happiness_increase) > 5:
                    germany.happiness -= happiness_increase

                if (germany.stability - stability_increase) > 5:
                    germany.stability -= stability_increase

    elif chance % 14 == 10:
        """Chance that a certain public space gets shot up
        - Decrease in population
        - Decrease in stability and happiness
        """
        locations = ["School", "Library", "Restaurant", "Bakery", "Courthouse", "Bank"]
        deaths = random.randrange(6, 100)
        print(f"Oh no there was a shooting at a local {locations[random.randrange(0, len(locations) - 1)]}.\n"
              f"This shooting resulted in the deaths of {deaths} people.\n")
        germany.stability += round(random.uniform(0.25, 1.75), 2)
        germany.happiness += round(random.uniform(0.25, 4.75), 2)
        germany.population -= deaths
        germany.deaths += deaths

        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability

        time.sleep(3)

    elif chance % 17 == 13:
        """Chance that a human trafficking ring gets exposed(suppose all victims died)
        - decrease in population
        - decrease in happiness and stability
        - increase in national debt and GDP
            -> govt spending to clean mess up
        """
        if germany.date.year > 1918:
            people = random.randrange(700, 15000)
            print(f"A human trafficking ring with {people} victims was just uncovered")
            time.sleep(3)
            germany.population -= people
            decrease = round(random.uniform(1.10, 5.56), 2)
            if (germany.happiness - decrease) > 5:
                germany.happiness -= decrease
            if (germany.stability - decrease) > 5:
                germany.stability -= decrease
            increase = round(random.uniform(10000, 2000000), 2)
            germany.current_gdp += increase
            germany.national_debt += round(increase * round(random.uniform(0.25, 0.75), 2), 2)

    elif chance % 25 == 30:
        """Chance that a major political scandal is uncovered
        - potential rebellion occurs
        - major decrease in stability and GDP(slash by 1.5)
        """
        loss = round(random.uniform(100000, 3000000), 2)
        print(f"A major political scandal has just been uncovered.\n"
              f"It is being reported that ${loss} was siphoned from Germany's GDP")
        time.sleep(3)
        germany.current_gdp -= loss

    elif chance % 60 == 50 and germany.rebllion != True:
        """Chance that a riot begins(could lead to rebellion)
        - major decrease in stability and happiness
        - can arise in any of the states of Germany
        - major decrease in GDP(slashed by factor of 2.5 or 5, depends)
            -> causes economy to go into depression or recession
                * based on chance
        - increase in national debt
        - later on, initiates a buildup of troops
        """
        days = random.randrange(30, 120)
        rebels = germany.population * round(random.uniform(0.01, 0.15), 2)
        print(f"A riot has begun in the region of {germany.regions[random.randrange(0, len(germany.regions) - 1)]}\n"
              f"It is being said that it will take {days} to quell this riot before it gets out of hand.\n'"
              f"So far, only {rebels} rebels have joined the cause/riot.\n")
        time.sleep(3)
        economic_chance = random.randrange(0, 2)
        if economic_chance == 0:
            print("Due to infighting the Germany economy has fallen into a Recession.\n")
            time.sleep(3)
            germany.economic_state = "recession"
            germany.economic_change_date = germany.date + timedelta(days=days)
            # economic_stimulus(germany)

        elif chance == 1:
            print("Due to infighting the Germany economy has fallen into a Depression.\n")
            time.sleep(3)
            germany.economic_state = "depression"
            germany.economic_change_date = germany.date + timedelta(days=days)
            # economic_stimulus(germany)
        germany.riot_over = germany.date + timedelta(days=days)