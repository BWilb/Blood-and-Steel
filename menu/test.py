import datetime
import random
import time

alternate_monarchs = ["Olga I", "Peter of Oldenburg", "Nikolai III", "Alexandra I",
                      "Olga II", "Tatiana", "Maria", "Anastasia", "Alexei"]

lenin_successors = ["Leon Trotsky", "Joseph Stalin", "Vladimir Milyutin", "Nikolai Krylenko",
                    "Pavel Dybenko", "Alexei Rykov", "Anatoly Lunacharsky"]

stalin_successors = ["Vyacheslav Molotov", "Anastas Mikoyan", "Lavrentiy Beria", "Nikolai Bulganin", "Georgy Malenkov",]

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
        if russia.date < datetime.datetime(1917, 3, 1):
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
                            print(f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
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
                        print(f"The anti-Tsarists have been deported to {nations[random.randrange(0, len(nations) - 1)]}")

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

        if russia.date < datetime.datetime(1924, 1, 21):
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
                            print(f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
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
                        print(f"The anti-Tsarists have been deported to {nations[random.randrange(0, len(nations) - 1)]}")

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

        if russia.date > datetime.datetime(1924, 1, 21):
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
                            print(f"SHIT!!! {russia.leader} was just assassinated...the assassins were successfully killed,\n"
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
                        print(f"The anti-Tsarists have been deported to {nations[random.randrange(0, len(nations) - 1)]}")

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