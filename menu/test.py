import datetime
import random
import time


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
