import random
import time
from datetime import timedelta


def diplomats_kicked_out(self):
    print("your diplomats have been kicked out of Spain.\n")
    time.sleep(1.5)
    self.europe_limit = self.date + timedelta(days=5)

def french_relations(self, france, globe):
    # self represents the US
    # self represents the US
    positive = ["\n1. improve relations for 60 days(15 political power, decrease pp exponent by 0.2 points)",
                "2. guarantee France independence(10 initial political power, decrease pp exponent by 0.5 points",
                "3. increase exports to France for 60 days(25 political power, improves US economy)",
                f"4. establish a {self.name} embassy within Madrid(13 political power cost, decrease 0.1 pp exponent while its installed",
                "5. establish an economic treaty with France(15 political power, improves both economies)",
                "6. establish a military alliance with France(10 political power)",
                "7. Establish student transfer student program(improve economy for 120 days)"]

    negative = ["1. Expel French nationals(15 political power; loss in US population, worsen relations by 25%)",
                "2. Jail French nationals\n(25 political power; worsen relations by 1.25% every day nationals are in jail)",
                "4. Embargo French economy\n(worsen relations by 35%, hurts both economies by 5%)",
                "5. Leave alliance\n(if not in alliance will not affect relationship)",
                "6. Hurt French relations for 30 days\n(15 political power initially, decrease by 0.75% every day)",
                "7. Declare war on France(potential for other nations to get involved if Spain is in alliance)."]
    done = True
    while done:
        type_choice = input("\nWould you like to improve or hinder relations with France?(enter quit to escape)\n"
                            f"Remember you have {self.political_power} political power left: ")
        if type_choice.lower() == "improve":
            for i in range(0, len(positive)):
                print(f"{positive[i]}.\n")
                time.sleep(1.25)

            relation_choice = int(input("would you like to choose 1 - 7?(enter quit to escape): "))
            chance = random.randrange(0, 75)

            if globe.tension < 50 and self.france_relations > 50:
                """high chance that British parliament will accept proposals"""

                if relation_choice == 1:
                    if self.political_power >= 15:
                        self.political_power -= 15
                        if chance % 2 == 0:
                            """50.67% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to improve relations with {self.name}.\n")
                            self.political_exponent -= 0.2
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.3% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 2:
                            """24% chance that US diplomats get killed """
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 2 and not self.guarantee_france:
                    if self.political_power >= 10:
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has accepted our guarantee for their independence.\n")
                            self.political_exponent -= 0.5
                            self.guarantee_france = True
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)


                        elif chance % 4 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 3:
                    if self.political_power >= 25:
                        self.political_power -= 25
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to buy more {self.name} goods.\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)


                        elif chance % 4 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)
                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 4:
                    if self.political_power >= 13:
                        self.political_power -= 13
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to install a(n) {self.name} embassy within Paris.\n")
                            self.political_exponent -= 0.1
                            time.sleep(1.5)


                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)


                        elif chance % 4 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 5:
                    if self.political_power >= 15:
                        self.political_power -= 15
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(
                                f"{france.leader} has agreed to establish an economic treaty with {self.name}\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 6:
                    if self.political_power >= 10:
                        self.political_power -= 10
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            if france.alliance:
                                print(f"{france.leader} has allowed us to enter the {france.alliance}\n")
                                time.sleep(1.5)
                            else:
                                print(f"{france.leader} has agreed to forming a military alliance")
                                time.sleep(1.5)
                                alliance = input("what would you like to name your alliance?: ")
                                self.alliance = alliance
                                france.alliance = alliance

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)

                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                        time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 7:
                    if chance % 2 == 0:
                        """49.1% chance that British parliament accepts proposal"""
                        print(f"{france.leader} has agreed to establish a student transfer program\n")
                        time.sleep(1.5)

                    elif chance % 3 == 1:
                        """33.8% chance that US diplomats get kicked out of Britain"""
                        print("Your diplomats have been kicked out of the the French Parliament.\n")
                        time.sleep(1.5)
                        globe.tension += round(random.uniform(0.5, 2), 2)
                        self.france_relations -= round(random.uniform(1, 2), 2)

                    elif chance % 4 == 2:
                        """24% chance that US diplomats get kicked out of Britain"""
                        print("Your diplomats have been called out for espionage and have been killed\n")
                        time.sleep(1.5)
                        globe.tension += round(random.uniform(0.5, 5), 2)
                        self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print("Your offer died in the sea of geopolitics.\n")
                        time.sleep(3)

            if globe.tension < 50 and self.france_relations < 50:
                """moderate chance that British Parliament will accept proposals"""

                if relation_choice == 1:
                    if self.political_power >= 15:
                        self.political_power -= 15
                        chance = random.randrange(1, 60)
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to improve relations with {self.name}.\n")
                            self.political_exponent -= 0.2
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 3:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 2 and not self.guarantee_france:
                    if self.political_power >= 10:
                        self.political_power -= 10
                        chance = random.randrange(1, 60)
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has accepted our guarantee for their independence.\n")
                            self.political_exponent -= 0.5
                            self.guarantee_britain = True
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 3:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 3:
                    if self.political_power >= 25:
                        self.political_power -= 25
                        chance = random.randrange(1, 60)
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to buy more {self.name} goods.\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 3:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 4:
                    if self.political_power >= 13:
                        self.political_power -= 13
                        chance = random.randrange(1, 60)
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to install a(n) {self.name} embassy within Paris.\n")
                            self.political_exponent -= 0.1
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 3:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 5:
                    if self.political_power >= 15:
                        self.political_power -= 15
                        chance = random.randrange(1, 60)
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(
                                f"{france.leader} has agreed to establish an economic treaty with {self.name}\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 3:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 6:
                    if self.political_power >= 10:
                        self.political_power -= 10
                        chance = random.randrange(1, 60)
                        if chance % 2 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            if france.alliance:
                                print(f"{france.leader} has allowed us to enter the {france.alliance}\n")
                                time.sleep(1.5)
                            else:
                                print(f"{france.leader} has agreed to forming a military alliance")
                                time.sleep(1.5)
                                alliance = input("what would you like to name your alliance?: ")
                                self.alliance = alliance
                                france.alliance = alliance

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 4 == 3:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 7:
                    chance = random.randrange(1, 60)
                    if chance % 2 == 0:
                        """49.1% chance that British parliament accepts proposal"""
                        print(f"{france.leader} has agreed to establish a student transfer program\n")
                        time.sleep(1.5)

                    elif chance % 3 == 1:
                        """33.8% chance that US diplomats get kicked out of Britain"""
                        print("Your diplomats have been kicked out of the the French Parliament.\n")
                        time.sleep(1.5)
                        globe.tension += round(random.uniform(0.5, 2), 2)
                        self.france_relations -= round(random.uniform(1, 2), 2)

                    elif chance % 4 == 3:
                        """25.4% chance that US diplomats get kicked out of Britain"""
                        print("Your diplomats have been called out for espionage and have been killed\n")
                        time.sleep(1.5)
                        globe.tension += round(random.uniform(0.5, 5), 2)
                        self.france_relations -= round(random.uniform(1, 6), 2)

            elif globe.tension > 50 and self.france_relations > 50:
                """low to moderate chance that British parliament will accept proposals"""
                chance = random.randrange(0, 45)

                if relation_choice == 1:
                    if self.political_power >= 15:
                        self.political_power -= 15
                        if chance % 3 == 0:
                            """33.3% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to improve relations with the United States.\n")
                            self.political_exponent -= 0.2
                            time.sleep(1.5)

                        elif chance % 2 == 0:
                            """51.1% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 5 == 2:
                            """20% chance that US diplomats get killed """
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)
                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 2 and not self.guarantee_france:
                    if self.political_power >= 10:
                        if chance % 3 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has accepted our guarantee for their independence.\n")
                            self.political_exponent -= 0.5
                            self.guarantee_france = True
                            time.sleep(1.5)

                        elif chance % 2 == 0:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)


                        elif chance % 5 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 3:
                    if self.political_power >= 25:
                        self.political_power -= 25
                        if chance % 3 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to buy more {self.name} goods.\n")
                            time.sleep(1.5)


                        elif chance % 2 == 0:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)


                        elif chance % 5 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)
                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 4:
                    if self.political_power >= 13:
                        """If player has enough political capital to follow through with choice"""
                        self.political_power -= 13
                        if chance % 3 == 0:
                            """49.1% cuba that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to install a(n) {self.name} embassy within Paris.\n")
                            self.political_exponent -= 0.1
                            time.sleep(1.5)


                        elif chance % 2 == 0:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)


                        elif chance % 5 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)
                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 5:
                    if self.political_power >= 15:
                        self.political_power -= 15
                        if chance % 3 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(
                                f"{france.leader} has agreed to establish an economic treaty with {self.name}\n")
                            time.sleep(1.5)

                        elif chance % 2 == 0:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 5 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)
                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 6:
                    if self.political_power >= 10:
                        self.political_power -= 10
                        if chance % 3 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            if france.alliance:
                                print(f"{france.leader} has allowed us to enter the {france.alliance}\n")
                                time.sleep(1.5)
                            else:
                                print(f"{france.leader} has agreed to forming a military alliance")
                                time.sleep(1.5)
                                alliance = input("what would you like to name your alliance?: ")
                                self.alliance = alliance
                                france.alliance = alliance

                        elif chance % 2 == 0:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)

                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 5 == 2:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)

                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 7:
                    if chance % 3 == 0:
                        """49.1% chance that British parliament accepts proposal"""
                        print(f"{france.leader} has agreed to establish a student transfer program\n")
                        time.sleep(1.5)

                    elif chance % 2 == 0:
                        """33.8% chance that US diplomats get kicked out of Britain"""
                        print("Your diplomats have been kicked out of the the French Parliament.\n")
                        time.sleep(1.5)
                        globe.tension += round(random.uniform(0.5, 2), 2)
                        self.france_relations -= round(random.uniform(1, 2), 2)

                    elif chance % 5 == 2:
                        """25.4% chance that US diplomats get kicked out of Britain"""
                        print("Your diplomats have been called out for espionage and have been killed\n")
                        time.sleep(1.5)
                        globe.tension += round(random.uniform(0.5, 5), 2)
                        self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print("Your offer died in the sea of geopolitics.\n")
                        time.sleep(3)

            elif globe.tension > 50 and self.france_relations > 50:
                """very low chance that British parliament will accept proposals"""

                chance = random.randrange(0, 75)

                if relation_choice == 1:
                    if self.political_power >= 15:
                        self.political_power -= 15
                        if chance % 5 == 0:
                            """20% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to improve relations with {self.name}.\n")
                            self.political_exponent -= 0.2
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.3% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 2 == 0:
                            """50.67% chance that US diplomats get killed """
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 2 and not self.guarantee_france:
                    if self.political_power >= 10:
                        if chance % 5 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has accepted our guarantee for their independence.\n")
                            self.political_exponent -= 0.5
                            self.guarantee_france = True
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 2 == 0:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)
                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 3:
                    if self.political_power >= 25:
                        self.political_power -= 25
                        if chance % 5 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to buy more {self.name} goods.\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 2 == 0:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 4:
                    if self.political_power >= 13:
                        self.political_power -= 13
                        if chance % 5 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(f"{france.leader} has agreed to install a(n) {self.name} embassy within Paris.\n")
                            self.political_exponent -= 0.1
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)
                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 2 == 0:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)
                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 5:
                    if self.political_power >= 15:
                        self.political_power -= 15
                        if chance % 5 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            print(
                                f"{france.leader} has agreed to establish an economic treaty with {self.name}\n")
                            time.sleep(1.5)

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)

                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 2 == 0:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)

                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 6:
                    if self.political_power >= 10:
                        self.political_power -= 10
                        if chance % 5 == 0:
                            """49.1% chance that British parliament accepts proposal"""
                            if france.alliance:
                                print(f"{france.leader} has allowed us to enter the {france.alliance}\n")
                                time.sleep(1.5)
                            else:
                                print(f"{france.leader} has agreed to forming a military alliance")
                                time.sleep(1.5)
                                alliance = input("what would you like to name your alliance?: ")
                                self.alliance = alliance
                                france.alliance = alliance

                        elif chance % 3 == 1:
                            """33.8% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been kicked out of the the French Parliament.\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 2), 2)

                            self.france_relations -= round(random.uniform(1, 2), 2)

                        elif chance % 2 == 0:
                            """25.4% chance that US diplomats get kicked out of Britain"""
                            print("Your diplomats have been called out for espionage and have been killed\n")
                            time.sleep(1.5)
                            globe.tension += round(random.uniform(0.5, 5), 2)

                            self.france_relations -= round(random.uniform(1, 6), 2)

                        else:
                            print("Your offer died in the sea of geopolitics.\n")
                            time.sleep(3)

                    else:
                        print(f"You do not have enough political capital to carry through with this task!!.\n")
                        time.sleep(1.25)

                elif relation_choice == 7:
                    if chance % 5 == 0:
                        """49.1% chance that British parliament accepts proposal"""
                        print(f"{france.leader} has agreed to establish a student transfer program\n")
                        time.sleep(1.5)

                    elif chance % 3 == 1:
                        """33.8% chance that US diplomats get kicked out of Britain"""
                        print("Your diplomats have been kicked out of the the French Parliament.\n")
                        time.sleep(1.5)
                        globe.tension += round(random.uniform(0.5, 2), 2)
                        self.france_relations -= round(random.uniform(1, 2), 2)

                    elif chance % 2 == 0:
                        """25.4% chance that US diplomats get kicked out of Britain"""
                        print("Your diplomats have been called out for espionage and have been killed\n")
                        time.sleep(1.5)
                        globe.tension += round(random.uniform(0.5, 5), 2)
                        self.france_relations -= round(random.uniform(1, 6), 2)

                    else:
                        print("Your offer died in the sea of geopolitics.\n")
                        time.sleep(3)

                    if type_choice.lower() == "quit":
                        done = False

        elif type_choice.lower() == "hinder":
            for i in range(0, len(negative)):
                if i == 0:
                    print(f"\n{negative[i]}\n")
                    time.sleep(1.25)
                else:
                    print(f"{negative[i]}\n")
                    time.sleep(1.25)

            relations_choice = int(input("Choose an option(1-7; enter 0 to escape): "))
            if relations_choice == 1:
                if not self.spain_nationals_dealt:
                    """checking if Canadian nationals haven't had a misfortune happen to them yet"""
                    if self.political_power >= 15:
                        """checking if player has enough political power"""
                        self.political_power -= 15
                        """expelling british nationals"""
                        nationals = random.randrange(3000, 10000)
                        print(f"We have expelled {nationals} French nationals from our lands.\n")
                        time.sleep(1.25)
                        self.population -= nationals
                        france.population += nationals
                        self.france_relations -= self.france_relations * 0.25
                        globe.tension += round(random.uniform(3.45, 5.56), 2)

                        chance = random.randrange(0, 60)
                        if chance % 4 == 0:
                            """25% chance that American diplomats are kicked out of Canada"""
                            diplomats_kicked_out(self)
                            done = False

                    else:
                        print("You do not have enough political power to commence this action.\n")
                        time.sleep(1.25)
                else:
                    print(f"You have already dealt with the French Nationals within {self.name} territory.\n")
                    time.sleep(1.25)

            elif relations_choice == 2:
                if not self.france_nationals_dealt:
                    if self.political_power >= 25:
                        self.political_power -= 25
                        nationals = random.randrange(3000, 10000)
                        print(f"We have jailed {nationals} French nationals.\n")
                        time.sleep(1.25)
                        self.france_relations -= self.france_relations * 0.0125
                        globe.tension += round(random.uniform(1.45, 3.56), 2)

                        chance = random.randrange(0, 45)
                        if chance % 3 == 0:
                            """33.3% chance that American diplomats are kicked out of Canada"""
                            diplomats_kicked_out(self)
                            done = False
                    else:
                        print("You do not have enough political power to commence this action.\n")
                        time.sleep(1.25)
                else:
                    print(f"You have already dealt with the French Nationals within {self.name} territory.\n")
                    time.sleep(1.25)

            elif relations_choice == 3:

                if not self.france_nationals_dealt:
                    """checking if Canadian nationals haven't had a misfortune happen to them yet"""
                    if self.political_power >= 15:
                        """checking if player has enough political power"""
                        self.political_power -= 15
                        """expelling british nationals"""
                        nationals = random.randrange(3000, 10000)
                        print(f"We have killed {nationals} French on claims of espionage.\n")
                        time.sleep(1.25)
                        self.population -= nationals
                        self.spfrance_relations -= self.france_relations * 0.5
                        globe.tension += round(random.uniform(6.45, 12.56), 2)

                        chance = random.randrange(0, 45)
                        if chance % 2 == 0:
                            """51.1% chance that American diplomats are kicked out of Canada"""
                            diplomats_kicked_out(self)
                            done = False

                    else:
                        print("You do not have enough political power to commence this action.\n")
                        time.sleep(1.25)
                else:
                    print(f"You have already dealt with the French Nationals within {self.name} territory.\n")
                    time.sleep(1.25)

            elif relations_choice == 4:
                if not self.britain_embargo:
                    """setting up a check upon whether US has britain embargoed or not"""
                    us_loss = (self.current_gdp * 0.03)
                    spain_loss = (france.current_gdp * 0.10)
                    print(f"We have embargoed France's economy.\n"
                          f"This however, has created a loss of ${us_loss} in GDP for the {self.name}.\n")
                    time.sleep(1.25)
                    self.current_gdp -= us_loss
                    france.current_gdp -= spain_loss
                    self.france_relations -= self.france_relations * 0.25
                    globe.tension += round(random.uniform(3.45, 5.56), 2)
                else:
                    print("You currently have France under an embargo!!.")
                    time.sleep(1.25)

            elif relations_choice == 5:
                if self.alliance.lower() == france.alliance.lower():
                    print(f"You have decided to leave the {self.alliance}.\n")
                    time.sleep(1.25)

            elif relations_choice == 6:
                if self.political_power >= 15:
                    print("you have decided to insult your relations with France for 30 days.\n")
                    time.sleep(1.25)

            elif relations_choice == 7:
                choice = input("Are you sure you want to declare war on France?: ")
                if choice.lower() == "yes" or choice.lower() == "y":
                    print("you have now officially declared war on France.\n")
                    time.sleep(1.25)

        elif type_choice.lower() == "quit":
            done = False