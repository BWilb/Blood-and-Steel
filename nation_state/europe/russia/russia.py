import random
import time
from datetime import datetime, timedelta

dictators = {
    "1910": "Nicolaus II",
    "1914": "Nicolaus II",
    "1918": "Vladimir Lenin",
    "1932": "Joseph Stalin",
    "1936": "Joseph Stalin",
    "1939": "Joseph Stalin"
}
alternate_monarchs = ["Olga I", "Peter of Oldenburg", "Nikolai III", "Alexandra I",
                      "Olga II", "Tatiana", "Maria", "Anastasia", "Alexei"]

lenin_successors = ["Leon Trotsky", "Joseph Stalin", "Vladimir Milyutin", "Nikolai Krylenko",
                    "Pavel Dybenko", "Alexei Rykov", "Anatoly Lunacharsky"]

stalin_successors = ["Vyacheslav Molotov", "Anastas Mikoyan", "Lavrentiy Beria", "Nikolai Bulganin", "Georgy Malenkov",]

population = {
    "1910": 126200000,
    "1914": 130000000,
    "1918": 136800000,
    "1932": 126000000,
    "1936": 104900000,
    "1939": 109397463
}

"""Economic Dictionaries and Variables"""
gdp = {
    "1910": 12003528421,
    "1914": 15085307368,
    "1918": 14723268421,
    "1932": 39024526316,
    "1936": 44568947368,
    "1939": 44428052632
}

business_cycle = ["recession", "recovery", "expansion", "depression"]

"""Randomized functions"""

def random_politics(russia):
    chance = random.randrange(10, 20000)

    if chance % 8 == 5:
        """chance that current ruler of Russia decides to eliminate some(random amount) of the anti-establishment party
            - if chance of killing off some of the ae's fails...
                -> increase in ae popularity
                -> decrease in stability
                -> potential for ruler to be assassinated
                    * further chance of assassination attempt failing and 
                    having more ae's killed
            - if chance of killing succeeds
                -> decrease in ae popularity
                -> decrease in population
                -> increase in stability
        """
        if russia.date < datetime(1917, 3, 1):
            if ((russia.ae / russia.current_pop) * 100) > 5.50:
                choice = input(f"{russia.ae} anti-tsarists live within your empire...an alarming number!!!\n"
                               f"Would you like to depopulate their ranks?(y or n): ")

                amount = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
                if choice.lower() == "y" or choice.lower() == "yes":
                    depopulate = input("Your choices are execution, internment in Siberia, or deportation,\n"
                                       f"for these {amount} individuals: ")

                    if depopulate.lower() == "execution":
                        """Choice for execution"""
                        print(f"You have chosen execution\n")
                        time.sleep(3)

                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the execution is successful"""
                            print("The execution was successful.\n")

                            russia.ae -= amount
                            russia.current_pop -= amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = alternate_monarchs[random.randrange(0, len(alternate_monarchs) - 1)]
                                print(f"{russia.leader} is your new monarch.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                    elif depopulate.lower() == "deportation":
                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the deportation is successful"""
                            nations = ["Switzerland", "France", "Great Britain", "Germany", "United States"]
                            print(
                                f"The anti-Tsarists have been deported to {nations[random.randrange(0, len(nations) - 1)]}")

                            russia.current_pop -= amount
                            russia.deportees += amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = alternate_monarchs[random.randrange(0, len(alternate_monarchs) - 1)]
                                print(f"{russia.leader} is your new monarch.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                                stability = round(random.uniform(0.25, 2.25), 2)
                                if (russia.stability - stability) > 5:
                                    russia.stability -= stability

                    elif depopulate.lower() == "internment" or depopulate.lower() == "siberia":
                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the internment is successful"""
                            print(f"The anti-Tsarists have been interned in Siberia")

                            russia.current_pop -= amount
                            russia.deportees += amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = alternate_monarchs[random.randrange(0, len(alternate_monarchs) - 1)]
                                print(f"{russia.leader} is your new monarch.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                                stability = round(random.uniform(0.25, 2.25), 2)
                                if (russia.stability - stability) > 5:
                                    russia.stability -= stability

            if russia.date < datetime(1924, 1, 21) and russia.date > datetime(1917, 3, 1):
                choice = input(f"{russia.ae} anti-Bolsheviks live within your Union...an alarming number!!!\n"
                               f"Would you like to depopulate their ranks?(y or n): ")

                amount = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
                if choice.lower() == "y" or choice.lower() == "yes":
                    depopulate = input("Your choices are execution, internment in Siberia, or deportation,\n"
                                       f"for these {amount} individuals: ")

                    if depopulate.lower() == "execution":
                        """Choice for execution"""
                        print(f"You have chosen execution\n")
                        time.sleep(3)

                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the execution is successful"""
                            print("The execution was successful.\n")

                            russia.ae -= amount
                            russia.current_pop -= amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = lenin_successors[random.randrange(0, len(lenin_successors) - 1)]
                                print(f"{russia.leader} is your new commissar.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                    elif depopulate.lower() == "deportation":
                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the deportation is successful"""
                            nations = ["Switzerland", "France", "Great Britain", "Germany", "United States"]
                            print(
                                f"The anti-Tsarists have been deported to {nations[random.randrange(0, len(nations) - 1)]}")

                            russia.current_pop -= amount
                            russia.deportees += amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = lenin_successors[random.randrange(0, len(lenin_successors) - 1)]
                                print(f"{russia.leader} is your new commissar.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                                stability = round(random.uniform(0.25, 2.25), 2)
                                if (russia.stability - stability) > 5:
                                    russia.stability -= stability

                    elif depopulate.lower() == "internment" or depopulate.lower() == "siberia":
                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the internment is successful"""
                            print(f"The anti-Tsarists have been interned in Siberia")

                            russia.current_pop -= amount
                            russia.deportees += amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = lenin_successors[random.randrange(0, len(lenin_successors) - 1)]
                                print(f"{russia.leader} is your new commissar.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                                stability = round(random.uniform(0.25, 2.25), 2)
                                if (russia.stability - stability) > 5:
                                    russia.stability -= stability

            if russia.date > datetime(1924, 1, 21):
                choice = input(f"{russia.ae} anti-Bolsheviks live within your Union...an alarming number!!!\n"
                               f"Would you like to depopulate their ranks?(y or n): ")

                amount = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
                if choice.lower() == "y" or choice.lower() == "yes":
                    depopulate = input("Your choices are execution, internment in Siberia, or deportation,\n"
                                       f"for these {amount} individuals: ")

                    if depopulate.lower() == "execution":
                        """Choice for execution"""
                        print(f"You have chosen execution\n")
                        time.sleep(3)

                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the execution is successful"""
                            print("The execution was successful.\n")

                            russia.ae -= amount
                            russia.current_pop -= amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = lenin_successors[random.randrange(0, len(lenin_successors) - 1)]
                                print(f"{russia.leader} is your new commissar.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                    elif depopulate.lower() == "deportation":
                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the deportation is successful"""
                            nations = ["Switzerland", "France", "Great Britain", "Germany", "United States"]
                            print(
                                f"The anti-Tsarists have been deported to {nations[random.randrange(0, len(nations) - 1)]}")

                            russia.current_pop -= amount
                            russia.deportees += amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = lenin_successors[random.randrange(0, len(lenin_successors) - 1)]
                                print(f"{russia.leader} is your new commissar.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                                stability = round(random.uniform(0.25, 2.25), 2)
                                if (russia.stability - stability) > 5:
                                    russia.stability -= stability

                    elif depopulate.lower() == "internment" or depopulate.lower() == "siberia":
                        chance = random.randrange(0, 6)
                        if chance % 2 == 1:
                            """Chance that the prisoners don't escape and that the internment is successful"""
                            print(f"The anti-Tsarists have been interned in Siberia")

                            russia.current_pop -= amount
                            russia.deportees += amount

                            stability = round(random.uniform(0.25, 2.25), 2)
                            if (russia.stability + stability) < 99:
                                russia.stability += stability

                        elif chance == 4:
                            """Chance that prisoners escape, and potentially assassinate the monarch"""
                            print("Oh crap, the guards were overpowered by the prisoners.\n")
                            time.sleep(3)
                            chance = random.randrange(0, 40)

                            if chance == 39:
                                """Chance that monarch is assassinated"""
                                print(
                                    f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
                                    f"before they could do anymore damage")
                                time.sleep(3)
                                russia.leader = lenin_successors[random.randrange(0, len(lenin_successors) - 1)]
                                print(f"{russia.leader} is your new commissar.\n")
                                time.sleep(3)
                                russia.ae -= amount
                                russia.current_pop -= amount

                                stability = round(random.uniform(0.25, 2.25), 2)
                                if (russia.stability - stability) > 5:
                                    russia.stability -= stability

    if chance % 29 == 16:
        """Chance that ae's stage an assassination on the Russian leader
        - internal chance of assassination plot failing or succeeding
            -> if success
                * death in some of conspirators
                    -> decrease in population
                    -> increase in ae popularity
                * stability declines
                * economy takes a hit(potential for economic downturn)
            -> if failure
                * death of all conspirators
                * 
        """
        chance = random.randrange(0, 5)
        if chance % 2 == 0:
            """Chance that an assassination attempt succeeds"""
            amount = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
            if russia.date < datetime(1917, 3, 1):
                print(f"SHIT!!! A group of {amount} anti-Tsarists just assassinated {russia.leader}.\n")
                russia.leader = alternate_monarchs[random.randrange(0, len(alternate_monarchs) - 1)]
                for i in range(0, len(alternate_monarchs) - 1):
                    if alternate_monarchs[i] == russia.leader:
                        """Removing selected alternate monarch from list"""
                        alternate_monarchs.pop(i)
                time.sleep(3)

                choice = input("How would you like to punish these captured assassins?\n"
                               "Through internment in Siberia, deportation, or death?: ")

                if choice.lower() == "internment" or choice.lower() == "gulag" or choice.lower() == "siberia":
                    """choice if user selects internment"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the royal family.\n")
                        time.sleep(3)
                    else:
                        print(f"The {amount} prisoners have joined the other {russia.siberians} internees.\n")
                        russia.siberians += amount
                        russia.ae -= amount

                elif choice.lower() == "death":
                    """choice if user selects death"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the royal family.\n")
                        time.sleep(3)
                    else:
                        print(f"The {amount} prisoners have been successfully wiped away from history\n")
                        russia.deaths += amount
                        russia.ae -= amount
                        russia.current_pop -= amount

                elif choice.lower() == "deportation":
                    """choice if user selects death"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the royal family.\n")
                        time.sleep(3)
                    else:
                        nations = ["Switzerland", "France", "Great Britain", "Germany", "United States"]
                        print(f"The {amount} prisoners have joined the other {russia.deportees} deported\n"
                              f"Which they were deported to {nations[random.randrange(0, len(nations) - 1)]}")
                        russia.deportees += amount
                        russia.ae -= amount
                        russia.current_pop -= amount

            elif russia.date > datetime(1917, 3, 1) and russia.date < datetime(1924, 1, 30):
                print(f"SHIT!!! A group of {amount} anti-Bolsheviks just assassinated {russia.leader}.\n")
                russia.leader = lenin_successors[random.randrange(0, len(lenin_successors) - 1)]
                for i in range(0, len(alternate_monarchs) - 1):
                    if lenin_successors[i] == russia.leader:
                        """Removing selected alternate monarch from list"""
                        lenin_successors.pop(i)
                time.sleep(3)

                choice = input("How would you like to punish these captured assassins?\n"
                               "Through internment in Siberia, deportation, or death?: ")

                if choice.lower() == "internment" or choice.lower() == "gulag" or choice.lower() == "siberia":
                    """choice if user selects internment"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the Committee.\n")
                        time.sleep(3)
                    else:
                        print(f"The {amount} prisoners have joined the other {russia.siberians} internees.\n")
                        russia.siberians += amount
                        russia.ae -= amount

                elif choice.lower() == "death":
                    """choice if user selects death"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the committee.\n")
                        time.sleep(3)
                    else:
                        print(f"The {amount} prisoners have been successfully wiped away from history\n")
                        russia.deaths += amount
                        russia.ae -= amount
                        russia.current_pop -= amount

                elif choice.lower() == "deportation":
                    """choice if user selects death"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the committee.\n")
                        time.sleep(3)
                    else:
                        nations = ["Switzerland", "France", "Great Britain", "Germany", "United States"]
                        print(f"The {amount} prisoners have joined the other {russia.deportees} deported\n"
                              f"Which they were deported to {nations[random.randrange(0, len(nations) - 1)]}")
                        russia.deportees += amount
                        russia.ae -= amount
                        russia.current_pop -= amount

            elif russia.date > datetime(1924, 1, 30):
                print(f"SHIT!!! A group of {amount} anti-Stalinists just assassinated {russia.leader}.\n")
                russia.leader = stalin_successors[random.randrange(0, len(stalin_successors) - 1)]
                for i in range(0, len(alternate_monarchs) - 1):
                    if stalin_successors[i] == russia.leader:
                        """Removing selected alternate monarch from list"""
                        stalin_successors.pop(i)
                time.sleep(3)

                choice = input("How would you like to punish these captured assassins?\n"
                               "Through internment in Siberia, deportation, or death?: ")

                if choice.lower() == "internment" or choice.lower() == "gulag" or choice.lower() == "siberia":
                    """choice if user selects internment"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the Committee.\n")
                        time.sleep(3)
                    else:
                        print(f"The {amount} prisoners have joined the other {russia.siberians} internees.\n")
                        russia.siberians += amount
                        russia.ae -= amount

                elif choice.lower() == "death":
                    """choice if user selects death"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the committee.\n")
                        time.sleep(3)
                    else:
                        print(f"The {amount} prisoners have been successfully wiped away from history\n")
                        russia.deaths += amount
                        russia.ae -= amount
                        russia.current_pop -= amount

                elif choice.lower() == "deportation":
                    """choice if user selects death"""
                    chance = random.randrange(0, 5)
                    if chance % 2 == 1:
                        print("The internees overpowered their guards and have escaped. Fortunately no further damage\n"
                              "has been done to the committee.\n")
                        time.sleep(3)
                    else:
                        nations = ["Switzerland", "France", "Great Britain", "Germany", "United States"]
                        print(f"The {amount} prisoners have joined the other {russia.deportees} deported\n"
                              f"Which they were deported to {nations[random.randrange(0, len(nations) - 1)]}")
                        russia.deportees += amount
                        russia.ae -= amount
                        russia.current_pop -= amount

def random_social(russia):
    chance = random.randrange(10, 20000)

    if chance % 5 == 4:
        """chance that someone has a surprise birthday for themselves
        - increase in happiness
        """
        print("Someone just had a surprise birthday thrown for them.\n")
        time.sleep(3)
        increase = round(random.uniform(0.10, 0.75), 2)
        if (russia.happiness + increase) < 98:
            russia.happiness += increase

    elif chance % 10 == 9:
        """Chance that homicide occurs
        however player not alerted, due to Russian secret police covering it up.
        - slight decrease in stability
        - decrease in population
        """
        people = random.randrange(10, 100)
        russia.current_pop -= people
        increase = round(random.uniform(0.10, 0.75), 2)
        if (russia.stability - increase) > 5:
            russia.stability -= increase

    elif chance % 15 == 11:
        """Chance a military parade occurs
        - increase in stability
        """
        print("Our grand military just hosted a parade. LONG LIVE THE MOTHERLAND.\n")
        time.sleep(3)
        increase = round(random.uniform(0.10, 0.75), 2)
        if (russia.stability + increase) < 98:
            russia.stability += increase

    elif chance % 20 == 15:
        """Chance that the Russian secret police arrest anti-establishment people
        - player will not be alerted, due to corruption of police
        - fate of people will be interned in Siberia, killed, or deported
            -> decrease in happiness
            -> increase in stability
            -> decrease in population
            -> increase in which punishment is chosen
        """
        choice = random.randrange(0, 3)
        people = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
        if choice == 0:
            """Chance that secret police kill people"""
            russia.ae -= people
            russia.current_pop -= people
            increase = round(random.uniform(0.10, 0.75), 2)
            if (russia.happiness - increase) > 5:
                russia.happiness -= increase

            if (russia.stability + increase) < 98:
                russia.stability += increase

        elif choice == 1:
            """Chance that secret police deport you"""
            nations = ["germany", "united states", "france", "great britain", "italy"]
            """Will later be incorporated with international relations"""
            russia.ae -= people
            russia.deportees += people
            russia.current_pop -= people

            increase = round(random.uniform(0.10, 0.75), 2)
            if (russia.stability + increase) < 98:
                russia.stability += increase

        elif choice == 2:
            """Chance that secret police intern you in Siberia"""
            russia.siberians += people
            russia.ae -= people
            increase = round(random.uniform(0.10, 0.75), 2)
            if (russia.stability + increase) < 98:
                russia.stability += increase

def random_crime(russia):
    pass
def random_economics(russia):
    pass
def random_international(russia):
    pass
def random_functions(russia):
    random_politics(russia)
    random_social(russia)
    random_crime(russia)
    random_economics(russia)
    random_international(russia)

"""Political Functions"""
def political_change(russia):
    """function for redrawing political lines"""
    if russia.date > russia.political_census:
        """If date exceeds census"""
        chance = random.randrange(0, 2)
        if chance == 0:
            loss = round(russia.pe * round(random.uniform(0.001, 0.009), 5), 0)
            russia.pe -= loss
            russia.ae += loss
        else:
            loss = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
            russia.ae -= loss
            russia.pe += loss

        russia.political_census = russia.date + timedelta(days=3)

    if round((russia.ae / russia.current_pop) * 100, 2) > 10.00:
        """Checking if anti-establishment parties have grown to powerful/influential"""
        if russia.date < datetime(1917, 3, 1):
            choice = input("Anti-Tsarist parties are flourishing, should we do something about it?(y or n): ")

            if choice.lower() == "yes" or choice.lower() == "y":
                options = random.randrange(0, 3)
                # choice of death, internment in Siberia, or deportation
                if options == 0:
                    """if options = 0, a small amount of people are sent to siberia"""
                    people = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
                    print(f"{people} anti-tsarists were sent to Siberia\n")
                    time.sleep(3)
                    russia.siberians += people

                elif options == 1:
                    """if options = 1, a small amount of people are killed"""
                    people = round(russia.ae * round(random.uniform(0.001, 0.009), 5), 0)
                    print(f"{people} anti-tsarists were killed for treason.\n")
                    time.sleep(3)
                    russia.deaths += people
                    russia.current_pop -= people
                    russia.ae -= people

                elif options == 2:
                    """if options = 2, a small amount of people are deported"""
                    people = round(russia.ae * round(random.uniform(0.001, 0.02), 5), 0)
                    print(f"{people} anti-tsarists were deported for treason.\n")
                    time.sleep(3)
                    russia.current_pop -= people
                    russia.deportees += people

"""population functions"""
def population_change(russia):
    if russia.past_year < russia.date.year:
        russia.pop_change = (russia.current_pop - russia.past_pop / (
                (russia.current_pop + russia.current_pop) / 2)) * 100

        russia.past_pop = russia.current_pop

        if russia.pop_change <= 5.50:
            """possible implementation of viagra with somewhat moderate growth, due to low population"""
            print(f"Your population growth for {russia.past_year} was {russia.population_change}%.\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                russia.viagra_subsidy = True

                if russia.condom_subsidy:
                    """Checking to see if condom subsidies exist"""
                    russia.condom_subsidy = False

        elif russia.pop_change >= 15.50:
            print(f"Your population growth for {russia.past_year} was {russia.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == 'y' or choice.lower() == "yes":
                russia.condom_subsidy = True

                if russia.viagra_subsidy:
                    russia.viagra_subsidy = False
    else:
        if russia.date < datetime(1914, 7, 28):
            births = random.randrange(100, 1000)
            deaths = random.randrange(100, 850)

            for i in range(0, births):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe += 1
                else:
                    russia.ae += 1

            russia.current_pop += births
            russia.births += births

            russia.current_pop -= deaths
            russia.deaths += deaths

            for i in range(0, deaths):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe -= 1
                else:
                    russia.ae -= 1

        elif russia.date > datetime(1914, 7, 28) and russia.date < datetime(1923, 6, 16):
            births = random.randrange(100, 800)
            deaths = random.randrange(100, 650)

            russia.current_pop += births
            russia.births += births

            for i in range(0, births):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe += 1
                else:
                    russia.ae += 1

            russia.current_pop -= deaths
            russia.deaths += deaths
            for i in range(0, deaths):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe -= 1
                else:
                    russia.ae -= 1

        elif russia.date > datetime(1923, 6, 16) and russia.date < datetime(1941, 6, 22):
            births = random.randrange(100, 500)
            deaths = random.randrange(100, 350)

            russia.current_pop += births
            russia.births += births

            for i in range(0, births):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe += 1
                else:
                    russia.ae += 1

            russia.current_pop -= deaths
            russia.deaths += deaths

            for i in range(0, deaths):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe -= 1
                else:
                    russia.ae -= 1

        elif russia.date > datetime(1941, 6, 22) and russia.date < datetime(1945, 5, 8):
            births = random.randrange(100, 1300)
            deaths = random.randrange(100, 1150)

            russia.current_pop += births
            russia.births += births

            for i in range(0, births):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe += 1
                else:
                    russia.ae += 1

            russia.current_pop -= deaths
            russia.deaths += deaths

            for i in range(0, deaths):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe -= 1
                else:
                    russia.ae -= 1

        elif russia.date > datetime(1945, 5, 8):
            births = random.randrange(100, 600)
            deaths = random.randrange(100, 450)

            russia.current_pop += births
            russia.births += births

            for i in range(0, births):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe += 1
                else:
                    russia.ae += 1

            russia.current_pop -= deaths
            russia.deaths += deaths

            for i in range(0, deaths):
                chance = random.randrange(0, 2)
                if chance == 0:
                    russia.pe -= 1
                else:
                    russia.ae -= 1
def recession(russia):
    """changes based upon whether an economic stimulus is in place and what year plan is in place
    extremity of losses or gains, based upon stimulus and year plans
    """
    if russia.economic_stimulus:
        if russia.year_plans == 0:

            russia.consumer_spending = -round(random.uniform(100, 90000), 2)
            russia.investment = -round(random.uniform(100, 500000), 2)
            russia.government_spending = round(random.uniform(1000, 500000), 2)

            russia.exports = round(random.uniform(10000, 400000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = -round(random.uniform(100, 80000), 2)
            russia.investment = -round(random.uniform(100, 350000), 2)
            russia.government_spending = round(random.uniform(1000, 600000), 2)

            russia.exports = round(random.uniform(10000, 500000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.009), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.009), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = -round(random.uniform(100, 70000), 2)
            russia.investment = -round(random.uniform(100, 300000), 2)
            russia.government_spending = round(random.uniform(1000, 700000), 2)

            russia.exports = round(random.uniform(10000, 550000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = -round(random.uniform(100, 50000), 2)
            russia.investment = -round(random.uniform(100, 200000), 2)
            russia.government_spending = round(random.uniform(1000, 750000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 4:

            russia.consumer_spending = -round(random.uniform(100, 30000), 2)
            russia.investment = -round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(1000, 850000), 2)

            russia.exports = round(random.uniform(10000, 900000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

    else:
        if russia.year_plans == 0:

            russia.consumer_spending = -round(random.uniform(100, 70000), 2)
            russia.investment = -round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(1000, 750000), 2)

            russia.exports = round(random.uniform(10000, 550000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = -round(random.uniform(100, 60000), 2)
            russia.investment = -round(random.uniform(100, 90000), 2)
            russia.government_spending = round(random.uniform(1000, 850000), 2)

            russia.exports = round(random.uniform(10000, 600000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = -round(random.uniform(100, 50000), 2)
            russia.investment = -round(random.uniform(100, 190000), 2)
            russia.government_spending = round(random.uniform(1000, 900000), 2)

            russia.exports = round(random.uniform(10000, 650000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = -round(random.uniform(100, 40000), 2)
            russia.investment = -round(random.uniform(100, 90000), 2)
            russia.government_spending = round(random.uniform(1000, 950000), 2)

            russia.exports = round(random.uniform(10000, 700000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 4:

            russia.consumer_spending = -round(random.uniform(100, 30000), 2)
            russia.investment = -round(random.uniform(100, 80000), 2)
            russia.government_spending = round(random.uniform(1000, 1000000), 2)

            russia.exports = round(random.uniform(10000, 800000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)


def depression(russia):
    if russia.economic_stimulus:
        if russia.year_plans == 0:

            russia.consumer_spending = -round(random.uniform(100, 500000), 2)
            russia.investment = -round(random.uniform(100, 500000), 2)
            russia.government_spending = round(random.uniform(1000, 650000), 2)

            russia.exports = round(random.uniform(10000, 550000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = -round(random.uniform(100, 400000), 2)
            russia.investment = -round(random.uniform(100, 400000), 2)
            russia.government_spending = round(random.uniform(1000, 750000), 2)

            russia.exports = round(random.uniform(10000, 650000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = -round(random.uniform(100, 300000), 2)
            russia.investment = -round(random.uniform(100, 300000), 2)
            russia.government_spending = round(random.uniform(1000, 850000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = -round(random.uniform(100, 200000), 2)
            russia.investment = -round(random.uniform(100, 200000), 2)
            russia.government_spending = round(random.uniform(1000, 950000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 4:

            russia.consumer_spending = -round(random.uniform(100, 100000), 2)
            russia.investment = -round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(1000, 1050000), 2)

            russia.exports = round(random.uniform(10000, 900000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

    else:
        if russia.year_plans == 0:

            russia.consumer_spending = -round(random.uniform(100, 700000), 2)
            russia.investment = -round(random.uniform(100, 700000), 2)
            russia.government_spending = round(random.uniform(1000, 650000), 2)

            russia.exports = round(random.uniform(10000, 550000), 2)
            russia.imports = round(random.uniform(10000, 1050000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = -round(random.uniform(100, 600000), 2)
            russia.investment = -round(random.uniform(100, 600000), 2)
            russia.government_spending = round(random.uniform(1000, 750000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = -round(random.uniform(100, 500000), 2)
            russia.investment = -round(random.uniform(100, 500000), 2)
            russia.government_spending = round(random.uniform(1000, 850000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 850000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = -round(random.uniform(100, 400000), 2)
            russia.investment = -round(random.uniform(100, 400000), 2)
            russia.government_spending = round(random.uniform(1000, 950000), 2)

            russia.exports = round(random.uniform(10000, 950000), 2)
            russia.imports = round(random.uniform(10000, 750000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 4:
            russia.consumer_spending = -round(random.uniform(100, 300000), 2)
            russia.investment = -round(random.uniform(100, 300000), 2)
            russia.government_spending = round(random.uniform(1000, 1050000), 2)

            russia.exports = round(random.uniform(10000, 1100000), 2)
            russia.imports = round(random.uniform(10000, 650000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (-russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

def recovery(russia):
    if russia.economic_stimulus:
        if russia.year_plans == 0:
            russia.consumer_spending = round(random.uniform(100, 10000), 2)
            russia.investment = round(random.uniform(100, 5000), 2)
            russia.government_spending = round(random.uniform(1000, 50000), 2)

            russia.exports = round(random.uniform(10000, 500000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)
        elif russia.year_plans == 1:
            russia.consumer_spending = round(random.uniform(100, 20000), 2)
            russia.investment = round(random.uniform(100, 10000), 2)
            russia.government_spending = round(random.uniform(1000, 60000), 2)

            russia.exports = round(random.uniform(10000, 650000), 2)
            russia.imports = round(random.uniform(10000, 750000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 2:
            russia.consumer_spending = round(random.uniform(100, 45000), 2)
            russia.investment = round(random.uniform(100, 20000), 2)
            russia.government_spending = round(random.uniform(1000, 55000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 450000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 3:
            russia.consumer_spending = round(random.uniform(100, 65000), 2)
            russia.investment = round(random.uniform(100, 30000), 2)
            russia.government_spending = round(random.uniform(1000, 225000), 2)

            russia.exports = round(random.uniform(10000, 1000000), 2)
            russia.imports = round(random.uniform(10000, 350000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 4:
            russia.consumer_spending = round(random.uniform(100, 80000), 2)
            russia.investment = round(random.uniform(100, 50000), 2)
            russia.government_spending = round(random.uniform(1000, 455000), 2)

            russia.exports = round(random.uniform(10000, 1200000), 2)
            russia.imports = round(random.uniform(10000, 325000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)
    else:
        if russia.year_plans == 0:
            russia.consumer_spending = round(random.uniform(100, 5000), 2)
            russia.investment = round(random.uniform(100, 2500), 2)
            russia.government_spending = round(random.uniform(1000, 350000), 2)

            russia.exports = round(random.uniform(10000, 450000), 2)
            russia.imports = round(random.uniform(10000, 1500000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)
        elif russia.year_plans == 1:
            russia.consumer_spending = round(random.uniform(100, 10000), 2)
            russia.investment = round(random.uniform(100, 5500), 2)
            russia.government_spending = round(random.uniform(1000, 500000), 2)

            russia.exports = round(random.uniform(10000, 650000), 2)
            russia.imports = round(random.uniform(10000, 1250000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 2:
            russia.consumer_spending = round(random.uniform(100, 35000), 2)
            russia.investment = round(random.uniform(100, 15000), 2)
            russia.government_spending = round(random.uniform(1000, 650000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 1000000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 3:
            russia.consumer_spending = round(random.uniform(100, 65000), 2)
            russia.investment = round(random.uniform(100, 30000), 2)
            russia.government_spending = round(random.uniform(1000, 755000), 2)

            russia.exports = round(random.uniform(10000, 1000000), 2)
            russia.imports = round(random.uniform(10000, 900000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 4:
            russia.consumer_spending = round(random.uniform(100, 80000), 2)
            russia.investment = round(random.uniform(100, 50000), 2)
            russia.government_spending = round(random.uniform(1000, 1000000), 2)

            russia.exports = round(random.uniform(10000, 1200000), 2)
            russia.imports = round(random.uniform(10000, 850000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

def expansion(russia):
    if russia.economic_stimulus:
        if russia.year_plans == 0:

            russia.consumer_spending = round(random.uniform(100, 100000), 2)
            russia.investment = round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(100, 300000), 2)

            russia.exports = round(random.uniform(10000, 700000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = round(random.uniform(100, 200000), 2)
            russia.investment = round(random.uniform(100, 200000), 2)
            russia.government_spending = round(random.uniform(100, 400000), 2)

            russia.exports = round(random.uniform(10000, 800000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = round(random.uniform(100, 200000), 2)
            russia.investment = round(random.uniform(100, 200000), 2)
            russia.government_spending = round(random.uniform(1000, 450000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 3:

            russia.consumer_spending = round(random.uniform(100, 300000), 2)
            russia.investment = round(random.uniform(100, 300000), 2)
            russia.government_spending = round(random.uniform(1000, 500000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 4:
            russia.consumer_spending = round(random.uniform(100, 400000), 2)
            russia.investment = round(random.uniform(100, 400000), 2)
            russia.government_spending = round(random.uniform(1000, 600000), 2)

            russia.exports = round(random.uniform(10000, 1500000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

    else:
        if russia.year_plans == 0:

            russia.consumer_spending = round(random.uniform(100, 100000), 2)
            russia.investment = round(random.uniform(100, 100000), 2)
            russia.government_spending = round(random.uniform(100, 300000), 2)

            russia.exports = round(random.uniform(10000, 700000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 1:

            russia.consumer_spending = round(random.uniform(100, 150000), 2)
            russia.investment = round(random.uniform(100, 150000), 2)
            russia.government_spending = round(random.uniform(100, 325000), 2)

            russia.exports = round(random.uniform(10000, 750000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 2:

            russia.consumer_spending = round(random.uniform(100, 250000), 2)
            russia.investment = round(random.uniform(100, 250000), 2)
            russia.government_spending = round(random.uniform(100, 425000), 2)

            russia.exports = round(random.uniform(10000, 770000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

        elif russia.year_plans == 3:
            russia.consumer_spending = round(random.uniform(100, 150000), 2)
            russia.investment = round(random.uniform(100, 150000), 2)
            russia.government_spending = round(random.uniform(100, 625000), 2)

            russia.exports = round(random.uniform(10000, 850000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)
        elif russia.year_plans == 4:
            russia.consumer_spending = round(random.uniform(100, 250000), 2)
            russia.investment = round(random.uniform(100, 250000), 2)
            russia.government_spending = round(random.uniform(100, 725000), 2)

            russia.exports = round(random.uniform(10000, 1050000), 2)
            russia.imports = round(random.uniform(10000, 950000), 2)

            russia.current_gdp += (russia.consumer_spending + russia.investment + russia.government_spending
                                   + (russia.exports - russia.imports))

            russia.national_debt += round((russia.government_spending * round(random.uniform(0.001, 0.005), 5)) +
                                          (russia.consumer_spending * round(random.uniform(0.001, 0.005), 5)), 2)

def economic_stimulus(russia):
    pass

def gdp_changes(russia):
    if russia.economic_state == "recovery":
        recovery(russia)
    elif russia.economic_state == "recession":
        recession(russia)
    elif russia.economic_state == "depression":
        depression(russia)
    elif russia.economic_state == "expansion":
        expansion(russia)

def economic_state(russia):
    if russia.date >= russia.economic_change_date:
        if russia.date >= russia.economic_change_date:
            """Comparing current date to when Italy's economic state could change"""
            chance = random.randrange(0, 2000)
            if chance % 37 == 10:
                """Making potential for economic disaster really low"""
                if russia.current_gdp < russia.past_gdp:
                    """Comparison of current gdp to past gdp"""
                    if russia.economic_state == "expansion" or russia.economic_state == "recovery":
                        for i in range(0, len(business_cycle) - 1):
                            if business_cycle[i] == "recession":
                                print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                                time.sleep(3)
                                russia.economic_state = business_cycle[i]
                                russia.economic_change_date = russia.date + timedelta(days=240)
                                economic_stimulus(russia)
                                """increasing amount of time to check up on GDP
                                Time is average amount(6 months cycle)
                                """
                    elif russia.economic_state == "recession":
                        for i in range(0, len(business_cycle) - 1):
                            if business_cycle[i] == "depression":
                                print("Your economy has entered into a depression "
                                      "after exceeding 6 months of decayed growth.\n")
                                time.sleep(3)
                                russia.economic_state = business_cycle[i]
                                russia.economic_change_date = russia.date + timedelta(days=270)
                                economic_stimulus(russia)
                                """
                                Since it takes awhile to escape a depression, amount of time on change date is increased
                                """

            if chance % 40 == 37:
                """making potential for economic expansion or recovery very low"""
                if russia.economic_state == "depression" or russia.economic_state == "recession":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "recovery":
                            print("Your economy hs finally entered its recovery period\n")
                            time.sleep(3)
                            russia.economic_state = business_cycle[i]
                            russia.economic_change_date = russia.date + timedelta(days=240)
                            """increasing amount of time to check up on GDP
                            Time is average amount(6 months cycle)
                            """

                elif russia.economic_state == "recovery":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "expansion":
                            print("Your economy has blasted into an expansionary period. Woo!\n")
                            time.sleep(3)
                            russia.economic_state = business_cycle[i]
                            russia.economic_change_date = russia.date + timedelta(days=270)
                            """
                            Since it takes awhile to escape a depression, amount of time on change date is increased
                            """
def economic_decisions(russia):
    if russia.past_year < russia.date.year:
        russia.economic_growth = (russia.current_gdp - russia.past_gdp /
                                  ((russia.past_gdp + russia.current_gdp) / 2)) * 100

        """Calculation of yearly economic growth"""
        if russia.economic_growth <= 3.35:
            if not russia.economic_stimulus:
                choice = input(f"Your GDP grew {russia.economic_growth}% last year.\n"
                               f"Would you like to apply a stimulus?: ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    economic_stimulus(russia)

        elif russia.economic_growth >= 9.56:
            if russia.economic_stimulus:
                russia.economic_stimulus = False
    else:
        gdp_changes(russia)
        economic_state(russia)
"""Stats functions"""
def stats(russia):
    print(f"Your current leader is {russia.leader}.\n"
          f"{round((russia.pe / russia.current_pop) * 100, 4)}% of your population support your regime.\n"
          f"{round((russia.ae / russia.current_pop) * 100, 4)}% of your population are against your regime.\n"
          f"Your national debt is ${round(russia.national_debt, 2)}.\n"
          f"Your current GDP is ${russia.current_gdp}.\n"
          f"Your current GDP growth rate is {round((russia.current_gdp - russia.past_gdp) / ((russia.current_gdp + russia.past_gdp) / 2) * 100, 5)}%\n"
          f"Your current debt to GDP ratio is {round((russia.national_debt / russia.current_gdp), 2)}%\n"
          f"Your current population is {russia.current_pop}.\n"
          f"There have been {russia.births} births in {russia.date.year}.\n"
          f"There have been {russia.deaths} deaths in {russia.date.year}.\n")
def manual_game(year):
    russia = Russia(year)
    while russia.current_pop > 3000000:
        political_change(russia)
        economic_decisions(russia)
        population_change(russia)
        random_functions(russia)
        answer = input("would you like to view your stats?: ")
        if answer.lower() == "y" or answer.lower() == "yes":
            stats(russia)
        time.sleep(3)

class Russia:
    def __init__(self, year):
        """Time variables"""
        self.date = datetime(int(year), 1, 1)
        self.past_year = self.date.year
        self.economic_change_date = self.date + timedelta(days=60)
        self.political_census = self.date + timedelta(days=3)
        self.year_plan_date = None
        """Population Variables"""
        self.current_pop = population[year]
        self.past_pop = self.current_pop
        self.deaths = 0
        self.births = 0
        self.happiness = 85.56
        self.pop_change = None
        self.condom_subsidy = None
        self.viagra_subsidy = None
        self.siberians = 0
        self.deportees = 0
        """Political Variables"""
        self.leader = dictators[year]
        self.pe = self.current_pop * 0.99
        self.ae = self.current_pop - self.pe
        self.stability = 85.00
        """Economic Variables"""
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.economic_state = "recovery"
        self.economic_growth = None
        # political economic variables
        self.national_debt = 0
        self.government_spending = 0
        self.economic_stimulus = None
        if self.date < datetime(1923, 6, 16):
            self.year_plans = 0
        else:
            self.year_plans = 1
        # GDP components
        self.consumer_spending = None
        self.investment = None
        self.exports = None
        self.imports = None