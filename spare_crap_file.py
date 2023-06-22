"""random functions"""
"""Russia's"""
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
                russia.leader = lenin_successors[random.randrange(0, len(lenin_successors))]
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


def random_economics(russia):
    chance = random.randrange(10, 20000)

    if chance % 7 == 6:
        """Chance that a factory opens...
        - if military factory
            -> later on increases amount of soldiers in army
            -> increase in stability
        - if civilian factory 
            -> gdp multiplied by 1.15
            -> increase in happiness
        """

    elif chance % 9 == 5:
        """Chance that leader of Russia siphons off some of Russia's GDP for himself
        - player will not be alerted of siphoning
            -> GDP loss based off random amount
        """
        loss = round(random.uniform(1000, 1000000), 2)
        russia.current_gdp -= loss

    elif chance % 11 == 10:
        """Chance that raw material exports rise in a given day
        - GDP multiplied by 1.25
        - increase in happiness and stability
        """
        print("Your current raw material exports have doubled.\n")
        time.sleep(3)
        russia.current_gdp *= 1.25
        increase = round(random.uniform(0.25, 1.5), 2)

        if (russia.happiness + increase) < 98:
            russia.happiness += increase

        if (russia.stability + increase) < 98:
            russia.stability += increase

    elif chance % 15 == 13:
        """Chance that grain exports increase by 2-4 usual amount for any given day
        - GDP multiplied by 1.5
        - decrease in happiness
        - increase in stability
        - potential for famine to start
            -> influences population growth
        """
        increase = round(random.uniform(1, 5), 2)
        decrease = round(random.uniform(1, 5), 2)
        print(f"Your nation's grain exports have multiplied by {increase} times.\n")
        time.sleep(3)
        russia.current_gdp *= 1.5

        if (russia.happiness - decrease) > 5:
            russia.happiness -= decrease

        if (russia.stability + increase) < 98:
            russia.stability += increase

        chance = random.randrange(0, 20)
        if chance == 15 and russia.date > russia.famine_time:
            print("due to focusing on exporting your grain and not feeding your population, famines have begun.\n")
            time.sleep(3)
            russia.famine_time = russia.date + timedelta(days=90)
            russia.famine = True

    elif chance % 25 == 16:
        """Chance that secret police raid a random amount of private banks
        - will not alert player, due to police covering it up
            -> decrease in stability and happiness
            -> GDP loss based upon amount of banks raided
        """
        raided_banks = random.randrange(2, 30)
        decrease = round(random.uniform(1, 5), 2)

        if raided_banks < 10:
            russia.current_gdp -= round(random.uniform(1000, 100000), 2)

        elif raided_banks < 20 and raided_banks > 10:
            russia.current_gdp -= round(random.uniform(100000, 900000), 2)

        elif raided_banks > 20:
            russia.current_gdp /= 1.5

        if (russia.happiness - decrease) > 5:
            russia.happiness -= decrease

        if (russia.stability - decrease) > 5:
            russia.stability -= decrease

    elif chance % 35 == 25:
        """Chance that a random amount of banks collapse
        - decrease in stability and happiness
        - GDP loss based upon amount of banks collapsed
        """

        collapse = random.randrange(2, 30)
        if collapse < 10:
            loss = round(random.uniform(1000, 100000), 2)
            russia.current_gdp -= loss
            print(f"{collapse} banks have collapsed, resulting in a loss of ${loss}")

        elif collapse < 20 and collapse > 10:
            loss = round(random.uniform(100000, 900000), 2)
            russia.current_gdp -= loss
            print(f"{collapse} banks have collapsed, resulting in a loss of ${loss}")

        elif collapse > 20:
            russia.current_gdp /= 1.5
            print(f"{collapse} banks have collapsed, resulting in a slashing of gdp by 1.5")

        decrease = round(random.uniform(1, 5), 2)

        if (russia.happiness - decrease) > 5:
            russia.happiness -= decrease

        if (russia.stability - decrease) > 5:
            russia.stability -= decrease

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

def random_international(russia):
    pass
def random_functions(russia):
    random_politics(russia)
    random_social(russia)
    random_crime(russia)
    random_economics(russia)
    random_international(russia)

"""Italy's"""
def random_economic(italy):
    chance = random.randrange(10, 5000)
    if chance % 5 == 7:
        """Chance that somebody loses at their casino
        - decrease in gdp and happiness
        - increase in national debt
        """
        loss = round(random.uniform(55000, 350000), 2)
        print(f"Someone just lost ${loss} at their local casino\n")
        italy.current_gdp -= loss
        italy.national_debt += round(loss * round(random.uniform(0.001, 0.09), 5), 2)
        decrease = round(random.uniform(0.25, 1.25), 2)
        if (italy.happiness - decrease) > 5:
            italy.happiness -= decrease

    elif chance % 10 == 6:
        """chance that somebody wins at their casino
        - increase in GDP and national debt(consumer debt)
        - increase in happiness
        """
        win = round(random.uniform(10000, 400000), 2)
        print(f"Someone won ${win} at their local casino.\n")
        time.sleep(3)
        italy.current_gdp += win
        italy.national_debt += round(win * round(random.uniform(0.001, 0.009), 5), 2)
        increase = round(random.uniform(0.25, 1.25), 2)
        if (italy.happiness + increase) < 98:
            italy.happiness += increase

    elif chance % 20 == 18:
        """Chance that somebody wins the Enalotto(italian lottery)
        - increase in GDP and national debt(consumer spending)
        - increase in happiness
        """
        lottery = round(random.uniform(10000, 6000000), 2)
        print(f"Somebody just won ${lottery} in their local Enalotto.\n")
        time.sleep(3)
        italy.current_gdp += lottery
        italy.national_debt += round(lottery * round(random.uniform(0.001, 0.009), 5), 2)
        increase = round(random.uniform(0.25, 1.56), 2)
        if (italy.happiness + increase) < 98:
            italy.happiness += increase

    elif chance % 70 == 56:
        """Chance that a random amount of banks collapse
        - decrease in GDP(depending upon severity), could be slashed by 2 or 4
        - potential for recession or depression
        - increase in national debt(govt spending to recover)
        - decrease in happiness and stability
        """
        amount = random.randrange(2, 25)
        print(f"{amount} banks collapsed today.\n")
        time.sleep(3)
        if amount < 5:
            """Less severe outlook/probability"""
            loss = round(random.uniform(10000, 400000), 2)
            print(f"The collapse resulted in a loss of ${loss}\n")
            time.sleep(3)
            italy.current_gdp -= loss
            italy.national_debt += round(loss * round(random.uniform(0.001, 0.09), 5), 2)
            increase = round(random.uniform(0.25, 1.56), 2)
            if (italy.happiness - increase) > 5:
                italy.happiness -= increase

        elif amount > 5 and amount < 20:
            """more moderately severe outlook/probability"""
            loss = round(random.uniform(90000, 900000), 2)
            print(f"The collapse resulted in a loss of ${loss}\n")
            time.sleep(3)
            italy.current_gdp /= 2
            italy.national_debt += round(loss * round(random.uniform(0.001, 0.09), 5), 2)
            print("The Italian economy faced a severe backlash from the bank failures.\n"
                  "It experienced a slash factor of 2. However, thanks to 'quick' government action,\n"
                  "a major economic downturn was avoided\n")
            time.sleep(3)
            increase = round(random.uniform(0.25, 3.56), 2)
            if (italy.happiness - increase) > 5:
                italy.happiness -= increase

        elif amount > 20:
            """most severe outlook/probability"""
            loss = round(random.uniform(300000, 900000), 2)
            print(f"The collapse resulted in a loss of ${loss}\n")
            time.sleep(3)
            italy.current_gdp /= 5
            italy.national_debt += round(loss * round(random.uniform(0.001, 0.09), 5), 2)
            chance = random.randrange(0, 2)
            """Internal chance of moderate or severe economic backlash"""
            if chance == 0:
                italy.economic_state = "recession"
            elif chance == 1:
                italy.economic_state = "depression"
            print("The Italian economy faced a severe backlash from the bank failures.\n"
                  "It experienced a slash factor of 5. Unfortunately 'quick' government responses weren't enough.\n"
                  f"The Italian economy is now in a(n) {italy.economic_state}!!!!\n")
            italy.economic_change_date = italy.date + timedelta(days=60)

            time.sleep(3)
            increase = round(random.uniform(0.25, 10.56), 2)
            if (italy.happiness - increase) > 5:
                italy.happiness -= increase

    elif chance % 100 == 77 and italy.date > italy.economic_change_date:
        """chance that italian economy falls into a depression
        - decrease in gdp 
        - increase in national debt
        - decrease in happiness and stability
        - later on, potential for Italy to break apart
        """
        print("Welp, the Italian economy has fallen into a Depression.\n")
        italy.current_gdp /= 10
        spending = round(random.uniform(100000, 10000000), 2)
        italy.national_debt += round(spending * round(random.uniform(0.01, 0.10), 5), 2)
        italy.economic_state = "depression"
        # economic_stimulus(italy)
        decrease_happiness = round(random.uniform(0.25, 15.5), 3)
        decrease_stability = round(random.uniform(0.25, 10.5), 3)

        if (italy.happiness - decrease_happiness) > 5:
            italy.happiness -= decrease_happiness
        if (italy.stability - decrease_stability) > 5:
            italy.stability -= decrease_stability
        italy.economic_change_date = italy.date + timedelta(days=60)

    elif chance % 160 == 57:
        """chance that italian economy falls into an expansion
        - decrease in gdp 
        - increase in national debt(govt and consumer)
        - decrease in happiness and stability
        """
        print("Welp, the Italian economy has risen into an expansion.\n")
        italy.current_gdp *= 10
        spending = round(random.uniform(100000, 5000000), 2)
        italy.national_debt += round(spending * round(random.uniform(0.01, 0.10), 5), 2)
        italy.economic_state = "expansion"
        # economic_stimulus(italy)
        increase_happiness = round(random.uniform(0.25, 15.5), 3)
        increase_stability = round(random.uniform(0.25, 10.5), 3)

        if (italy.happiness + increase_happiness) < 98:
            italy.happiness += increase_happiness
        if (italy.stability + increase_stability) < 98:
            italy.stability += increase_stability
        italy.economic_change_date = italy.date + timedelta(days=60)

def random_social(italy):
    chance = random.randrange(10, 5000)
    print(chance)
    if chance % 5 == 0:
        """Chance that someone throws a surprise birthday for their kid
        - increase in happiness and stability
        """
        print("Someone just threw their child a surprise party.\n")
        time.sleep(3)
        increase = round(random.uniform(0.25, 1.5), 2)
        if (italy.happiness + increase) < 98:
            italy.happiness += increase

        if(italy.stability + increase) < 98:
            italy.stability += increase

    elif chance % 7 == 8:
        """Chance that someone gets married
        - increase in happiness and stability
        """
        print("Somebody just got married.\n")
        time.sleep(3)
        increase = round(random.uniform(0.25, 1.5), 2)
        if (italy.happiness + increase) < 98:
            italy.happiness += increase

        if (italy.stability + increase) < 98:
            italy.stability += increase

    elif chance % 15 == 6:
        """Chance that the mafia recruits a random amount of people
        - decrease in stability
        - increase in gdp(due to spending of mafia)
        """
        people = random.randrange(2, 25)
        print(f"The mafia just recruited {people} people to their ranks.\n")
        time.sleep(3)
        italy.current_gdp += round(random.uniform(1000, 50000), 2)
        decrease = round(random.uniform(0.25, 1.5), 2)

        if (italy.stability - decrease) > 5:
            italy.stability -= decrease

    elif chance % 20 == 15:
        """Chance that a random parade occurs
        - increase in happiness
        """
        print("A parade just occurred.\n")
        time.sleep(3)

        increase = round(random.uniform(0.25, 1.5), 2)
        if (italy.happiness + increase) < 98:
            italy.happiness += increase
def random_crime(italy):
    chance = random.randrange(10, 5000)
    if chance % 6 == 6:
        """Chance that the mafia attacks someone/group of people
        - internal chance that attack kills the person/people
        * decrease in stability and happiness
        * decrease in population
        """
        chance = random.randrange(1, 5)
        if chance % 2 == 0:
            kills = random.randrange(10, 50)
            print(f"The Mafia just killed {kills} people.\n")
            time.sleep(3)
            italy.current_pop -= kills
            italy.deaths += kills

            for i in range(0, kills):
                """Looping through deaths to un-assign political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party -= 1

                elif chance == 1:
                    italy.italian_liberal_party -= 1

                elif chance == 2:
                    italy.italian_peoples_party -= 1

                elif chance == 3:
                    italy.italian_republican_party -= 1

        elif chance % 7 == 5:
            """Chance that the Mafia robs a bank(s)
            - no alert given(Mafia pays government to cover up)
            - decrease in GDP
            - Increase in national debt
            """
            stolen = round(random.uniform(100000, 1000000), 2)
            italy.current_gdp -= stolen
            italy.national_debt += round(stolen * round(random.uniform(0.001, 0.09), 5), 2)

        elif chance % 10 == 9:
            """Chance that a rape occurs
            - internal chance of rapist or victim being killed
            - decrease in happiness
            """
            chance = random.randrange(0, 2)

            if chance == 0:
                """chance that rape is attempted, but unsuccessful"""
                print("A rape was just attempted, however the attempt failed.")
                time.sleep(3)
                chance = random.randrange(0, 2)
                if chance == 0:
                    """Chance that rapist is killed"""
                    print("After pursuing their attempted rapist, the victim slit the throat of the rapist.\n")
                    time.sleep(3)
                    italy.current_pop -= 1
                    italy.deaths += 1
                    for i in range(0, 1):
                        """Looping through deaths to un-assign political parties"""
                        chance = random.randrange(0, 4)
                        # chance of chance variable being 0 - 3
                        if chance == 0:
                            italy.italian_socialist_party -= 1

                        elif chance == 1:
                            italy.italian_liberal_party -= 1

                        elif chance == 2:
                            italy.italian_peoples_party -= 1

                        elif chance == 3:
                            italy.italian_republican_party -= 1
                elif chance == 1:
                    print("after alerting bystanders with the unsuccessful rape, the rapist is forced to kill the victim.\n")
                    time.sleep(3)

                    italy.current_pop -= 1
                    italy.deaths += 1
                    for i in range(0, 1):
                        """Looping through deaths to un-assign political parties"""
                        chance = random.randrange(0, 4)
                        # chance of chance variable being 0 - 3
                        if chance == 0:
                            italy.italian_socialist_party -= 1

                        elif chance == 1:
                            italy.italian_liberal_party -= 1

                        elif chance == 2:
                            italy.italian_peoples_party -= 1

                        elif chance == 3:
                            italy.italian_republican_party -= 1

            if chance == 1:
                """Chance that rape is successful"""
                print("A rape was just attempted, which the attempt was successful")
                time.sleep(3)
                chance = random.randrange(0, 2)
                if chance == 0:
                    """Chance that rapist is killed"""
                    print("After being raped, the victim was filled with anger and decided to kill the rapist via flaying\n")
                    time.sleep(3)
                    italy.current_pop -= 1
                    italy.deaths += 1
                    for i in range(0, 1):
                        """Looping through deaths to un-assign political parties"""
                        chance = random.randrange(0, 4)
                        # chance of chance variable being 0 - 3
                        if chance == 0:
                            italy.italian_socialist_party -= 1

                        elif chance == 1:
                            italy.italian_liberal_party -= 1

                        elif chance == 2:
                            italy.italian_peoples_party -= 1

                        elif chance == 3:
                            italy.italian_republican_party -= 1
                elif chance == 1:
                    print(
                        "after alerting bystanders with the successful rape, the rapist is forced to kill the victim.\n")
                    time.sleep(3)

                    italy.current_pop -= 1
                    italy.deaths += 1
                    for i in range(0, 1):
                        """Looping through deaths to un-assign political parties"""
                        chance = random.randrange(0, 4)
                        # chance of chance variable being 0 - 3
                        if chance == 0:
                            italy.italian_socialist_party -= 1

                        elif chance == 1:
                            italy.italian_liberal_party -= 1

                        elif chance == 2:
                            italy.italian_peoples_party -= 1

                        elif chance == 3:
                            italy.italian_republican_party -= 1

        elif chance % 12 == 8:
            """Chance that street performers rob tourists
            - internal chance of success and death(of either street performer or tourist)
            """
            chance = random.randrange(0, 2)
            if chance == 0:
                """Chance that robbing is unsuccessful"""
                chance = random.randrange(0, 2)
                print("A street performer attempted to rob a tourist but was unsuccessful.")
                time.sleep(3)
                if chance == 0:
                    """chance that street performer dies"""
                    print("The street performer was also killed by the tourist.\n")
                    time.sleep(3)
                    italy.current_pop -= 1
                    italy.deaths += 1

                    for i in range(0, 1):
                        """Looping through deaths to un-assign political parties"""
                        chance = random.randrange(0, 4)
                        # chance of chance variable being 0 - 3
                        if chance == 0:
                            italy.italian_socialist_party -= 1

                        elif chance == 1:
                            italy.italian_liberal_party -= 1

                        elif chance == 2:
                            italy.italian_peoples_party -= 1

                        elif chance == 3:
                            italy.italian_republican_party -= 1

                elif chance == 1:
                    """Chance that tourist dies"""
                    print("Due to the unsuccessful robbery, the street performer decided to kill the tourist.\n")
                    time.sleep(3)

            elif chance == 1:
                """Chance that the robbing is successful"""
                chance = random.randrange(0, 2)
                print("A street performer just robbed a tourist.")
                time.sleep(3)
                if chance == 0:
                    """chance that street performer dies"""
                    print("The street performer, however, was tracked down and killed by the tourist.\n")
                    time.sleep(3)
                    italy.current_pop -= 1
                    italy.deaths += 1
                    for i in range(0, 1):
                        """Looping through deaths to un-assign political parties"""
                        chance = random.randrange(0, 4)
                        # chance of chance variable being 0 - 3
                        if chance == 0:
                            italy.italian_socialist_party -= 1

                        elif chance == 1:
                            italy.italian_liberal_party -= 1

                        elif chance == 2:
                            italy.italian_peoples_party -= 1

                        elif chance == 3:
                            italy.italian_republican_party -= 1

                elif chance == 1:
                    """Chance that tourist dies"""
                    print("Due to the tourist fighting back, the street performer decide to kill the tourist\n")
                    time.sleep(3)

        elif chance % 20 == 17:
            """Chance that a homicide occurs
            - decrease in population
            - decrease in happiness and stability
            """
            homicides = random.randrange(1, 12)
            print(f"{homicides} homicide(s) just occurred.\n")
            time.sleep(3)
            italy.current_pop -= homicides
            italy.deaths += homicides
            decrease = round(random.uniform(0.25, 1.25), 2)
            if (italy.happiness - decrease) > 5:
                italy.happiness -= decrease

            for i in range(0, homicides):
                """Looping through deaths to un-assign political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party -= 1

                elif chance == 1:
                    italy.italian_liberal_party -= 1

                elif chance == 2:
                    italy.italian_peoples_party -= 1

                elif chance == 3:
                    italy.italian_republican_party -= 1
def random_politics(italy):
    pass
def random_international(italy):
    pass
def randomized_functions(italy):
    random_social(italy)
    random_economic(italy)
    random_crime(italy)
    random_politics(italy)
    random_international(italy)

"""Germany's"""
def random_politics(germany):
    chance = random.randrange(10, 20000)
    if chance % 5 == 10:
        """Chance that politician of any political party makes a speech
        - if politician is making speech from 1932 to 1945
            * Potential for politicians death and portion of rebels death
            * increase in stability and decrease in happiness
        """
        if germany.date < datetime(1932, 1, 30):
            chance = random.randrange(0, 3)

            if chance == 0:
                """Chance that the free conservative party holds a speech"""
                print("The free conservative party just held a speech in Berlin.\n")
                time.sleep(3)
                for i in range(0, random.randrange(100, 2000)):
                    chance = random.randrange(0, 2)
                    """Chance that influence either takes supporters away from progressive
                    or center party
                    """
                    if chance == 0:
                        germany.center_party -= 1
                        germany.free_conservatives += 1
                    elif chance == 1:
                        germany.progressives -= 1
                        germany.free_conservatives += 1

            elif chance == 1:
                """Chance that the progressive party holds a speech"""
                print("The progressive party just held a speech in Berlin.\n")
                time.sleep(3)

                for i in range(0, random.randrange(100, 2000)):
                    chance = random.randrange(0, 2)
                    """Chance that influence either takes supporters away from progressive
                    or center party
                    """
                    if chance == 0:
                        germany.center_party -= 1
                        germany.progressives += 1
                    elif chance == 1:
                        germany.free_conservatives -= 1
                        germany.progressives += 1

            elif chance == 2:
                """Chance that the center party holds a speech"""
                print("The center party just held a speech in Berlin.\n")
                time.sleep(3)

                for i in range(0, random.randrange(100, 2000)):
                    chance = random.randrange(0, 2)
                    """Chance that influence either takes supporters away from progressive
                    or center party
                    """
                    if chance == 0:
                        germany.progressives -= 1
                        germany.center_party += 1
                    elif chance == 1:
                        germany.free_conservatives -= 1
                        germany.center_party += 1

    elif chance % 19 == 15:
        """Chance that politician secretly influences GDP
        - increase in GDP and national debt
        """
        increase = round(random.uniform(12000, 300000), 2)
        germany.current_gdp += increase
        germany.national_debt += round(round(random.uniform(0.09, 0.30), 2), 2)

    elif chance % 25 == 21:
        """Chance that politician secretly influences population
        - increases in population
        """
        births = random.randrange(13, 2000)
        germany.births += births
        germany.population += births
        for i in range(0, births):
            chance = random.randrange(0, 3)
            if chance == 0:
                germany.free_conservatives += 1

            elif chance == 1:
                germany.progressives += 1

            elif chance == 2:
                germany.center_party += 1

    elif chance % 48 == 38:
        """Chance that an assassination attempt is made on the German Chancellor
        - internal chance if successful or not
            -> other people will die as well
        - economy goes into recession
            -> GDP slashed by 1.25
        - decrease in stability
        """

    elif chance % 60 == 59:
        """Chance that the Kaiser or Heir to the throne is assassinated
        - internal chance if successful or not
            -> other people will die as well
        - if Kaiser is in power...GDP will be slashed by 1.5
        - decrease in stability
        """
        chance = random.randrange(0, 9)
        if germany.date < datetime(1918, 11, 11):
            if chance % 8 == 0:
                print(f"Kaiser {germany.kaiser} has been assassinated!!!\n")
                germany.kaiser = kaisers[0]
                kaisers.pop(0)
                print(f"{germany.kaiser} has replace him")
                germany.current_gdp /= 1.5
                economic_stimulus(germany)
                germany.stability -= round(random.uniform(1.25, 10.25), 2)
def random_economics(germany):
    chance = random.randrange(10, 20000)
    if chance % 3 == 7:
        """Chance that someone starts a new business
        - slight increase in GDP
            -> investment
        - increase in happiness and stability
        - increase in national debt
            -> loans required for starting business
        """
        print("Someone has begun a new business.\n")
        time.sleep(3)

        gdp_increase = round(random.uniform(1200, 3000), 2)
        germany.current_gdp += gdp_increase
        germany.national_debt += round(gdp_increase * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(0.1, 1.00), 2)
        happiness_increase = round(random.uniform(0.1, 1.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase

    elif chance % 6 == 5:
        """Chance that someone gets sued
        - decrease in happiness
        - slight decrease in GDP
            -> Consumer spending
        """
        print("Someone just got sued.\n")
        time.sleep(3)

        germany.current_gdp -= round(random.uniform(1000, 30000), 2)
        # representing loss in CPP

        happiness_decrease = round(random.uniform(0.1, 1.00), 2)
        if (germany.happiness - happiness_decrease) > 5:
            germany.happiness -= happiness_decrease

    if chance % 8 == 3:
        """Chance that somebod loses their savings @ a casino
        - decrease in happiness
        - slight decrease in GDP(Consumer spending)
        """
        loss = round(random.uniform(10000, 600000), 2)
        print(f"Someone just lost ${loss} at their local casino")

        decrease = round(random.uniform(0.25, 2.56), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        germany.current_gdp -= round(loss * round(random.uniform(0.25, 0.55), 2), 2)

    elif chance % 9 == 5:
        """Chance that somebody begins to invest in economy
        - increase in happiness and stability
        - slight increase in GDP
            -> Investment
        """
        print("Someone has begun to invest. "
              "What a smart lad\n")

        germany.current_gdp += round(random.uniform(1200, 6000), 2)

        stability_increase = round(random.uniform(0.1, 1.00), 2)
        happiness_increase = round(random.uniform(0.1, 1.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase

    elif chance % 17 == 9:
        """Chance that somebody wins the lottery
        - increase in GDP by 3/4 of winnings
        - increase in national debt by randomized selection of 1/4 to 3/4
            -> consumer debt
        - increase in happiness and stability
        """
        winnings = round(random.uniform(100000, 2000000), 2)
        print(f"somebody won {winnings} in the Eurojackpot.\n")
        time.sleep(3)

        germany.current_gdp += winnings * 0.75
        germany.national_debt += round(winnings * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(0.1, 0.5), 2)
        happiness_increase = round(random.uniform(1.25, 3.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase

    elif chance % 20 == 11:
        """Chance of the Bundestag/Reichstag spending an extra amount of money
        - increase in GDP by randomized selection of 1/4 to 3/4 of money
            -> increase in national debt by same amount
        - increase in stability and happiness
        """
        spending = round(random.uniform(10000, 500000), 2)
        print(f"The Bundestag decided to spend an extra ${spending} today\n")
        time.sleep(3)

        germany.current_gdp += round(spending * round(random.uniform(0.25, 0.75), 2), 2)
        germany.national_debt += round(spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(1.00, 1.5), 2)
        happiness_increase = round(random.uniform(0.25, 1.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase

    elif chance % 27 == 17:
        """Chance of a certain amount of banks(1-15) collapse
        - Decrease in GDP
            -> loss based upon severity
        - increase in national debt
            -> government and consumer spending
        - decrease in stability and happiness
        """
        banks = random.randrange(1, 16)
        loss = 0
        if banks < 10:
            loss = round(random.uniform(10000, 200000), 2)
        if banks > 10:
            loss = round(random.uniform(200000, 1000000), 2)

        print(f"{banks} bank(s) collapsed today resulting in a loss of ${loss}.\n")
        time.sleep(3)
        germany.current_gdp -= loss
        germany.national_debt += round(loss * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(1.00, 5.5), 2)
        happiness_increase = round(random.uniform(2.25, 8.00), 2)

        if (germany.happiness - happiness_increase) > 5:
            germany.happiness -= happiness_increase

        if (germany.stability - stability_increase) > 5:
            germany.stability -= stability_increase

    elif chance % 32 == 11 and germany.date >= germany.tax_change_date:
        """Chance that the Bundestag/Reichstag raises taxes
        - decrease in stability and happiness
        **Internal checks will be put in place to prevent 
        rates over 100%**
        """
        tax_hike = round(random.uniform(0.25, 5.56), 2)
        if (germany.tax_rate + tax_hike) < 100:
            print(f"the Bundestag raised taxes by {tax_hike}% today.\n")
            time.sleep(3)
            stability_increase = round(random.uniform(0.20, 1.00), 2)
            happiness_increase = round(random.uniform(0.25, 2.00), 2)

            if (germany.happiness - happiness_increase) > 5:
                germany.happiness -= happiness_increase

            if (germany.stability - stability_increase) > 5:
                germany.stability -= stability_increase
            germany.tax_change_date = germany.date + timedelta(days=60)

        else:
            print(f"the Bundestag attempted to raise taxes by {tax_hike}%.\n"
                  f"However the hike would've made the tax rate exceed 100%.\n")

    elif chance % 39 == 13 and germany.date >= germany.tax_change_date:
        """Chance that the Bundestag/Reichstag lowers taxes
        - increase in stability and happiness
        - increase in GDP
            -> Consumer and government spending and investment
        - increase in National debt
            -> government and consumer spending
        **Internal checks will be put in place to prevent 
        rates below 10% **
        """
        tax_hike = round(random.uniform(0.25, 5.56), 2)
        if (germany.tax_rate - tax_hike) >= 10:
            print(f"the Bundestag lowered taxes by {tax_hike}% today.\n")
            time.sleep(3)
            stability_increase = round(random.uniform(0.20, 1.00), 2)
            happiness_increase = round(random.uniform(0.25, 2.00), 2)

            if (germany.happiness + happiness_increase) < 98:
                germany.happiness += happiness_increase

            if (germany.stability + stability_increase) < 98:
                germany.stability += stability_increase
            germany.tax_change_date = germany.date + timedelta(days=60)

        else:
            print(f"the Bundestag attempted to lower taxes by {tax_hike}%.\n"
                  f"However the hike would've made the tax rate dip below 10%.\n")

    elif chance % 49 == 20 and (germany.date >= germany.economic_change_date) and \
            germany.economic_state != "recession":
        """Chance that German economy shifts into a Recession
        - stimulus function gets called
        - GDP gets slashed by 1.5
        - stability and happiness decrease
        - Government spending increases alongside national debt by 1/4 to 3/4 of that spending
        - later on, potential for Brandenburg-Prussia to lose control of other states
            -> especially Bavaria
        """
        print("The German economy has randomly fallen into a Recession.\n")
        time.sleep(3)
        germany.economic_state = "recession"
        germany.current_gdp /= 1.5
        spending = round(random.uniform(120000, 1000000), 2)
        germany.current_gdp += spending
        germany.national_debt += round(spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(2.20, 5.00), 2)
        happiness_increase = round(random.uniform(3.25, 8.00), 2)

        if (germany.happiness - happiness_increase) > 5:
            germany.happiness -= happiness_increase

        if (germany.stability - stability_increase) > 5:
            germany.stability -= stability_increase

        germany.economic_change_date = germany.date + timedelta(days=120)
        economic_stimulus(germany)

    elif chance % 49 == 15 and (germany.date >= germany.economic_change_date) and \
            germany.economic_state != "recovery":
        """Chance that German economy shifts into a Recovery stage
                - GDP gets multiplied by 1.5
                - stability and happiness increase
                - Government spending increases alongside national debt by 1/4 to 3/4 of that spending
        """

        print("The German economy has randomly fallen into a Recession.\n")
        time.sleep(3)
        germany.economic_state = "recovery"
        germany.current_gdp *= 1.5
        consumer_spending = round(random.uniform(120000, 1000000), 2)
        germany.current_gdp += consumer_spending
        germany.national_debt += round(consumer_spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(2.20, 5.00), 2)
        happiness_increase = round(random.uniform(3.25, 8.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability - stability_increase) < 98:
            germany.stability -= stability_increase

        germany.economic_change_date = germany.date + timedelta(days=120)

    elif chance % 60 == 29 and (germany.date >= germany.economic_change_date) and \
            germany.economic_state != "depression":
        """Chance that German economy collapses in a depression
        - stimulus function gets called
        - GDP gets slashed by 3
        - stability and happiness decrease
        - Government spending increases alongside national debt by 1/4 to 3/4 of that spending
        - later on, potential for Brandenburg-Prussia to lose control of other states
            -> especially Bavaria
        """
        print("The German economy has randomly fallen into a Depression.\n")
        time.sleep(3)
        germany.economic_state = "depression"
        germany.current_gdp /= 3
        spending = round(random.uniform(1000000, 9000000), 2)
        germany.current_gdp += spending
        germany.national_debt += round(spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(10.20, 15.00), 2)
        happiness_increase = round(random.uniform(13.25, 20.00), 2)

        if (germany.happiness - happiness_increase) > 5:
            germany.happiness -= happiness_increase

        if (germany.stability - stability_increase) > 5:
            germany.stability -= stability_increase
        economic_stimulus(germany)

    elif chance % 60 == 15 and (germany.date >= germany.economic_change_date) and \
            germany.economic_state != "expansion":
        """Chance that German economy shifts into an expansion stage
                - GDP gets multiplied by 3
                - stability and happiness increase
                - Government spending increases alongside national debt by 1/4 to 3/4 of that spending
        """
        print("The German economy has randomly fallen into an expansion.\n")
        time.sleep(3)
        germany.economic_state = "expansion"
        germany.current_gdp *= 3
        consumer_spending = round(random.uniform(1000000, 9000000), 2)
        germany.current_gdp += consumer_spending
        germany.national_debt += round(consumer_spending * round(random.uniform(0.05, 0.25), 2), 2)

        stability_increase = round(random.uniform(10.20, 15.00), 2)
        happiness_increase = round(random.uniform(13.25, 20.00), 2)

        if (germany.happiness + happiness_increase) < 98:
            germany.happiness += happiness_increase

        if (germany.stability + stability_increase) < 98:
            germany.stability += stability_increase
def random_social(germany):
    chance = random.randrange(10, 20000)

    if chance % 10 == 3:
        """Chance that a parade occurs
        - increase in happiness and stability
        """
        print("A parade just occurred.\n")
        time.sleep(3)

    elif chance % 16 == 5:
        """Chance that someone gets married
        - increase in happiness and stability
        """
        print("someone just got married\n")
        time.sleep(3)
        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability

    elif chance % 18 == 7:
        """Chance that a college dorm throws a party
        - increase in happiness
        - internal chance of death
            -> if death 
                - decrease in happiness
        """
        print("A college dorm is throwing a wild party\n")
        time.sleep(3)
        chance = random.randrange(0, 2)
        if chance == 1:
            people = random.randrange(1, 30)
            print(f"Well bad news...{people} people died from partying a little to hard.\n")
            time.sleep(3)
            germany.population -= people
            germany.deaths += people
            time.sleep(3)
            germany.happiness -= random.randrange(1, 4)
        else:
            germany.happiness += random.randrange(2, 7)

    elif chance % 21 == 10:
        """Chance that a high schooler throws a party
        - increase in happiness
        - internal chance of death
            -> if death 
                - decrease in happiness
        """
        print("A popular high schooler is throwing a wild party\n")
        time.sleep(3)
        chance = random.randrange(0, 2)
        if chance == 1:
            people = random.randrange(1, 30)
            print(f"Well bad news...{people} people died from partying a little to hard.\n")
            germany.population -= people
            germany.deaths += people
            time.sleep(3)
            germany.happiness -= random.randrange(1, 4)
        else:
            germany.happiness += random.randrange(2, 7)

    elif chance % 26 == 8:
        """Chance that car rolls into group of people
        - decrease in population
        - decrease in happiness and stability
        """
        deaths = random.randrange(3, 25)
        print(f"Someone just rolled their car into a group of people. {deaths} people died.\n")
        germany.population -= deaths
        time.sleep(3)

        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness - decrease) > 5:
            germany.happiness -= decrease

        if (germany.stability - decrease_stability) > 10:
            germany.stability -= decrease_stability

    elif chance % 36 == 7:
        """Chance that somebody converts and begins to believe in God
        -> Christian, Islamic, Jewish, or other
        - increase in happiness and stability
        """
        religions = ["Jewish", "Christian", "Islamic"]
        print(
            f"An Atheist just converted to believing in the {religions[random.randrange(0, len(religions) - 1)]} God\n")
        decrease = round(random.uniform(0.25, 0.75), 2)
        decrease_stability = round(random.uniform(0.25, 1.75), 2)
        if (germany.happiness + decrease) < 98:
            germany.happiness += decrease

        if (germany.stability + decrease_stability) < 98:
            germany.stability += decrease_stability
        time.sleep(3)

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
                germany.national_debt += round(loss * round(random.uniform(0.05, 0.25), 2), 2)

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
                germany.national_debt += round(loss * round(random.uniform(0.05, 0.25), 2), 2)

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
            germany.national_debt += round(increase * round(random.uniform(0.05, 0.25), 2), 2)

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

    elif chance % 60 == 50 and germany.rebellion != True:
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

def random_international(germany):
    chance = random.randrange(10, 20000)
    if chance % 6 == 9:
        """Chance that Germany's relations with another nation improves
        - later on...
            * improved relations with other nation
            * more potential for trade relations
        """
    elif chance % 10 == 11:
        """Chance that Germany's relations with another nation deteriorate
        - later on...
            * worsened relations with specific nation
            * less potential for trade
        """

    elif chance % 15 == 14:
        """Chance that Germany randomly embargoes another nation
        - nation will not be in alliance
        """

    elif chance % 34 == 19:
        """Chance that a terrorist attack occurs on German soil
        - nation that commences terrorism will not be in alliance
        """

    elif chance % 50 == 46:
        """Random chance that Germany decides to go to war with another nation
        - nation will not be in alliance
        """
    pass

"""Primary Random Function"""
def random_functions(germany):
    random_social(germany)
    random_politics(germany)
    random_economics(germany)
    random_crime(germany)

"""Britain's"""
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