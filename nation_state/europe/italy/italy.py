"""Political variables and dictionaries"""
import random
from datetime import datetime, timedelta
import time

prime_ministers = {
    "1910": "Luigi Luzzatti",
    "1914": "Antonio Salandra",
    "1918": "Vittorio Emanuele Orlando",
    "1932": "Benito Mussolini",
    "1936": "Benito Mussolini",
    "1939": "Benito Mussolini"
}

monarchs = {
    "1910": "Victor Emmanuel III",
    "1914": "Victor Emmanuel III",
    "1918": "Victor Emmanuel III",
    "1932": "Victor Emmanuel III",
    "1936": "Victor Emmanuel III",
    "1939": "Victor Emmanuel III"
}
"""Economic variables and dictionaries"""
gdp = {
    "1910": 7243560000,
    "1914": 7294052632,
    "1918": 7318292632,
    "1932": 12072684211,
    "1936": 15920315789,
    "1939": 19837894737
}
tax_rate = {
    "1910": 18.00,
    "1914": 18.00,
    "1918": 36.00,
    "1932": 10.00,
    "1936": 8.00,
    "1939": 12.00
}

business_cycle = ["recovery", "expansion", "recession", "depression"]

"""Population variables and dictionaries"""
population = {
    "1910": 36100000,
    "1914": 36500000,
    "1918": 36800000,
    "1932": 41000000,
    "1936": 42400000,
    "1939": 43500000
}
"""Military variables and dictionaries"""

army_size = {
    "1910": 252169,
    "1914": 497219,
    "1918": 2700000,
    "1932": 354169,
    "1936": 381336,
    "1939": 645000
}
"""Stability and happiness functions"""
def stability_happiness(italy):
    chance = random.randrange(0, 2)

    if chance == 0:
        increase_happiness = round(random.uniform(0.001, 0.09), 3)
        increase_stability = round(random.uniform(0.001, 0.009), 3)

        if (italy.happiness + increase_happiness) < 98:
            italy.happiness += increase_happiness
        if (italy.stability + increase_stability) < 98:
            italy.stability += increase_stability

    elif chance == 1:
        decrease_happiness = round(random.uniform(0.001, 0.09), 3)
        decrease_stability = round(random.uniform(0.001, 0.009), 3)

        if (italy.happiness - decrease_happiness) > 5:
            italy.happiness -= decrease_happiness
        if (italy.stability - decrease_stability) > 5:
            italy.stability -= decrease_stability
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

def retire_soldiers(italy):
    """function for retiring old, wounded, or stupid soldiers"""
    italy.army -= random.randrange(2, 100)
def increase_army(italy):
    increase = round(italy.conscripts * round(random.uniform(0.0001, 0.0005), 6), 0)
    italy.army += increase
    italy.conscripts -= increase
def increase_conscripts(italy):
    if italy.conscription_status == "volunteer":
        if italy.date == italy.conscript_census:
            """Amount of population that is eligible under volunteering draft"""
            italy.conscripts = round(italy.current_pop * round(random.uniform(0.0001, 0.0009), 5), 0)
            italy.conscript_census = italy.date + timedelta(days=15)

    elif italy.conscription_status == "limited":
        if italy.date == italy.conscript_census:
            """Amount of population that is eligible under limited draft"""
            italy.conscripts = round(italy.current_pop * round(random.uniform(0.0001, 0.002), 5), 0)
            italy.conscript_census = italy.date + timedelta(days=20)

    elif italy.conscript_status == "extensive":
        if italy.date == italy.conscript_census:
            """Amount of population that is eligible under extensive draft"""
            italy.conscripts = round(italy.current_pop * round(random.uniform(0.0001, 0.005), 5), 0)
            italy.conscript_census = italy.date + timedelta(days=25)

    elif italy.conscript_status == "required":
        if italy.date == italy.conscript_census:
            """Amount of population that is eligible under required drafting"""
            italy.conscripts = round(italy.current_pop * round(random.uniform(0.0001, 0.02), 5), 0)
            italy.conscript_census = italy.date + timedelta(days=30)
def military_functions(italy):
    increase_conscripts(italy)
    increase_army(italy)
    retire_soldiers(italy)

"""population functions"""
def population_change(italy):
    if italy.past_year < italy.date.year:
        italy.population_change = (italy.current_pop - italy.past_pop / (
                    (italy.current_pop + italy.current_pop) / 2)) * 100
        italy.past_pop = italy.current_pop

        if italy.population_change <= 2.1:
            """possible implementation of viagra with somewhat moderate growth, due to low population"""
            print(f"Your population growth for {italy.past_year} was {italy.population_change}%.\n")

            choice = input("Would you like to subsidize viagra for your population?: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                italy.viagra_subsidy = True

                if italy.condom_subsidy:
                    """Checking to see if condom subsidies exist"""
                    italy.condom_subsidy = False

        elif italy.population_change >= 12.5:
            print(f"Your population growth for {italy.past_year} was {italy.population_change}%.\n")
            choice = input("Would you like to subsidize condoms?: ")
            if choice.lower() == 'y' or choice.lower() == "yes":
                italy.condom_subsidy = True

                if italy.viagra_subsidy:
                    italy.viagra_subsidy = False
    else:
        if italy.viagra_subsidy:
            births = random.randrange(50, 600)
            italy.births += births
            italy.current_pop += births

            for i in range(0, births):
                """Looping through births to assign to political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party += 1

                elif chance == 1:
                    italy.italian_liberal_party += 1

                elif chance == 2:
                    italy.italian_peoples_party += 1

                elif chance == 3:
                    italy.italian_republican_party += 1

            deaths = random.randrange(25, 150)
            italy.deaths += deaths
            italy.current_pop -= deaths

            for i in range(0, births):
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

        elif italy.condom_subsidy:
            births = random.randrange(50, 200)
            italy.births += births
            italy.current_pop += births

            for i in range(0, births):
                """Looping through births to assign to political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party += 1

                elif chance == 1:
                    italy.italian_liberal_party += 1

                elif chance == 2:
                    italy.italian_peoples_party += 1

                elif chance == 3:
                    italy.italian_republican_party += 1

            deaths = random.randrange(25, 150)
            italy.deaths += deaths
            italy.current_pop -= deaths

            for i in range(0, deaths):
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

        else:
            births = random.randrange(50, 300)
            italy.births += births
            italy.current_pop += births
            for i in range(0, births):
                """Looping through births to assign to political parties"""
                chance = random.randrange(0, 4)
                # chance of chance variable being 0 - 3
                if chance == 0:
                    italy.italian_socialist_party += 1

                elif chance == 1:
                    italy.italian_liberal_party += 1

                elif chance == 2:
                    italy.italian_peoples_party += 1

                elif chance == 3:
                    italy.italian_republican_party += 1

            deaths = random.randrange(25, 150)
            italy.deaths += deaths
            italy.current_pop -= deaths

            for i in range(0, deaths):
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

"""Economic Functions"""
def economic_state(italy):
    if italy.date >= italy.economic_change_date:
        """Comparing current date to when Italy's economic state could change"""
        chance = random.randrange(0, 2000)
        if chance % 37 == 10:
            """Making potential for economic disaster really low"""
            if italy.current_gdp < italy.past_gdp:
                """Comparison of current gdp to past gdp"""
                if italy.economic_state == "expansion" or italy.economic_state == "recovery":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "recession":
                            print("Your economy has entered into a recession after 6 months of decayed growth.\n")
                            time.sleep(3)
                            italy.economic_state = business_cycle[i]
                            italy.economic_change_date = italy.date + timedelta(days=240)
                            economic_stimulus(italy)
                            """increasing amount of time to check up on GDP
                            Time is average amount(6 months cycle)
                            """
                elif italy.economic_state == "recession":
                    for i in range(0, len(business_cycle) - 1):
                        if business_cycle[i] == "depression":
                            print("Your economy has entered into a depression "
                                  "after exceeding 6 months of decayed growth.\n")
                            time.sleep(3)
                            italy.economic_state = business_cycle[i]
                            italy.economic_change_date = italy.date + timedelta(days=270)
                            economic_stimulus(italy)
                            """
                            Since it takes awhile to escape a depression, amount of time on change date is increased
                            """

        if chance % 40 == 37:
            """making potential for economic expansion or recovery very low"""
            if italy.economic_state == "depression" or italy.economic_state == "recession":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "recovery":
                        print("Your economy hs finally entered its recovery period\n")
                        time.sleep(3)
                        italy.economic_state = business_cycle[i]
                        italy.economic_change_date = italy.date + timedelta(days=240)
                        """increasing amount of time to check up on GDP
                        Time is average amount(6 months cycle)
                        """

            elif italy.economic_state == "recovery":
                for i in range(0, len(business_cycle) - 1):
                    if business_cycle[i] == "expansion":
                        print("Your economy has blasted into an expansionary period. Woo!\n")
                        time.sleep(3)
                        italy.economic_state = business_cycle[i]
                        italy.economic_change_date = italy.date + timedelta(days=270)
                        """
                        Since it takes awhile to escape a depression, amount of time on change date is increased
                        """
def economic_stimulus(italy):
    italy.economic_stimulus = True

    if italy.economic_state == "recession":
        choice = input("Do you want to increase the tax rate in order to support increased spending?\n"
                       "(Remember this will apply to the entire population): ")

        if choice.lower() == "yes" or choice.lower() == "y":
            valid_choice = False

            while valid_choice:

                tax_hike = float(input("By how much do you to increase taxes(max cap is 10)?: "))
                if tax_hike <= 10 and tax_hike >= 1.0:
                    italy.tax_rate += tax_hike
                    print(f"{italy.tax_rate}% is your new tax rate.\n")
                    time.sleep(3)
                    decrease = round(random.uniform(0.25, 1.45), 2)

                    if (italy.happiness - decrease) < 5:
                        italy.happiness -= decrease

                    valid_choice = True

                elif tax_hike <= 0 or tax_hike > 10:
                    print(f"New tax hike of {tax_hike}% is improper.\n"
                          f"Try again.")
                    time.sleep(3)

                else:
                    print("Not a valid tax rate")
                    time.sleep(3)

    elif italy.economic_state == "depression":
        tax_hike = round(random.uniform(0.5, 10), 2)
        if (italy.tax_rate + tax_hike) <= 68.00:
            if italy.date.year <= 1922 or italy.date.year >= 1946:
                print(f"Parliament has enacted a tax hike of {tax_hike}%\n")

            if italy.date.year > 1922 and italy.date.year < 1946:
                print(f"Il Duce has enacted a tax hike of {tax_hike}%\n")
            time.sleep(3)
def recession(italy):
    """Recession simulation based upon stimulus and tax rate"""
    if italy.economic_stimulus:
        """Recession with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:

            italy.consumer_spending = -round(random.uniform(100, 1000), 2)
            italy.investment = -round(random.uniform(100, 2000), 2)
            italy.government_spending = round(random.uniform(1000, 3000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.01, 0.09), 2), 2))

            italy.exports = round(random.uniform(120000, 750000), 2)
            italy.imports = round(random.uniform(120000, 1100000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 4000), 2)
            italy.investment = -round(random.uniform(1000, 3000), 2)
            italy.government_spending = round(random.uniform(1000, 9000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.01, 0.09), 2), 2))

            italy.exports = round(random.uniform(120000, 560000), 2)
            italy.imports = round(random.uniform(120000, 1100000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
    else:
        """Recession without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 2500), 2)
            italy.investment = -round(random.uniform(1000, 4000), 2)
            italy.government_spending = round(random.uniform(1000, 5000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.01, 0.09), 2), 2))

            italy.exports = round(random.uniform(120000, 560000), 2)
            italy.imports = round(random.uniform(120000, 1100000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 6000), 2)
            italy.investment = -round(random.uniform(1000, 6000), 2)
            italy.government_spending = round(random.uniform(1000, 12000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.01, 0.09), 2), 2))

            italy.exports = round(random.uniform(120000, 460000), 2)
            italy.imports = round(random.uniform(120000, 1100000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))

def depression(italy):
    """Recession simulation based upon stimulus and tax rate"""
    if italy.economic_stimulus:
        """Depression with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:

            italy.consumer_spending = -round(random.uniform(1000, 3000), 2)
            italy.investment = -round(random.uniform(1000, 4000), 2)
            italy.government_spending = round(random.uniform(1000, 16000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.15), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))
            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment)

            italy.exports = round(random.uniform(120000, 690000), 2)
            italy.imports = round(random.uniform(120000, 1400000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 6000), 2)
            italy.investment = -round(random.uniform(1000, 8000), 2)
            italy.government_spending = round(random.uniform(1000, 19000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.11), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))
            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment)


            italy.exports = round(random.uniform(120000, 590000), 2)
            italy.imports = round(random.uniform(120000, 1400000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
    else:
        """Depression without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 2500), 2)
            italy.investment = -round(random.uniform(1000, 4000), 2)
            italy.government_spending = round(random.uniform(1000, 25000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.11), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))
            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment)

            italy.exports = round(random.uniform(120000, 750000), 2)
            italy.imports = round(random.uniform(120000, 1400000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = -round(random.uniform(1000, 10000), 2)
            italy.investment = -round(random.uniform(1000, 16000), 2)
            italy.government_spending = round(random.uniform(1000, 35000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.21), 2), 2) +
                                    round(-italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))

            italy.exports = round(random.uniform(120000, 590000), 2)
            italy.imports = round(random.uniform(120000, 1400000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
def recovery(italy):
    """Recession simulation based upon stimulus and tax rate"""
    if italy.economic_stimulus:
        """Depression with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:

            italy.consumer_spending = round(random.uniform(100, 2000), 2)
            italy.investment = round(random.uniform(100, 2500), 2)
            italy.government_spending = round(random.uniform(1000, 16000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.001, 0.05), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.055), 2), 2))

            italy.exports = round(random.uniform(120000, 690000), 2)
            italy.imports = round(random.uniform(120000, 660000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))

        elif italy.tax_rate > 25.00:
            italy.consumer_spending = round(random.uniform(100, 1000), 2)
            italy.investment = round(random.uniform(1000, 2000), 2)
            italy.government_spending = round(random.uniform(1000, 19000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.001, 0.05), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.05), 2), 2))

            italy.exports = round(random.uniform(120000, 590000), 2)
            italy.imports = round(random.uniform(120000, 560000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
    else:
        """Recovery without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:
            italy.consumer_spending = round(random.uniform(100, 1500), 2)
            italy.investment = round(random.uniform(100, 2000), 2)
            italy.government_spending = round(random.uniform(1000, 25000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.0011, 0.05), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.05), 2), 2))

            italy.exports = round(random.uniform(120000, 590000), 2)
            italy.imports = round(random.uniform(120000, 560000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = round(random.uniform(100, 1000), 2)
            italy.investment = round(random.uniform(100, 1500), 2)
            italy.government_spending = round(random.uniform(1000, 35000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.001, 0.05), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.05), 2), 2))

            italy.exports = round(random.uniform(120000, 450000), 2)
            italy.imports = round(random.uniform(120000, 420000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
def expansion(italy):
    """Recession simulation based upon stimulus and tax rate"""
    if italy.economic_stimulus:
        """Expansion with economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:

            italy.consumer_spending = round(random.uniform(100, 4000), 2)
            italy.investment = round(random.uniform(100, 6500), 2)
            italy.government_spending = round(random.uniform(1000, 20000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.01, 0.095), 2), 2))

            italy.exports = round(random.uniform(120000, 1000000), 2)
            italy.imports = round(random.uniform(120000, 750000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))

        elif italy.tax_rate > 25.00:
            italy.consumer_spending = round(random.uniform(100, 2500), 2)
            italy.investment = round(random.uniform(100, 4500), 2)
            italy.government_spending = round(random.uniform(1000, 30000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.09), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.01, 0.095), 2), 2))

            italy.exports = round(random.uniform(120000, 750000), 2)
            italy.imports = round(random.uniform(120000, 650000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
    else:
        """Expansion without economic stimulus in place alongside tax rate
        * severity of losses depend upon tax rate
        """
        if italy.tax_rate < 25.00:
            italy.consumer_spending = round(random.uniform(100, 6000), 2)
            italy.investment = round(random.uniform(100, 8000), 2)
            italy.government_spending = round(random.uniform(1000, 30000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.11), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.01, 0.095), 2), 2))

            italy.exports = round(random.uniform(120000, 750000), 2)
            italy.imports = round(random.uniform(120000, 650000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
        elif italy.tax_rate > 25.00:
            italy.consumer_spending = round(random.uniform(100, 4500), 2)
            italy.investment = round(random.uniform(100, 3500), 2)
            italy.government_spending = round(random.uniform(1000, 55000), 2)
            italy.national_debt += (round(italy.government_spending * round(random.uniform(0.01, 0.21), 2), 2) +
                                    round(italy.consumer_spending * round(random.uniform(0.001, 0.009), 2), 2))

            italy.exports = round(random.uniform(120000, 560000), 2)
            italy.imports = round(random.uniform(120000, 340000), 2)

            italy.current_gdp += (italy.consumer_spending + italy.government_spending + italy.investment +
                                  (italy.exports - italy.imports))
def gdp_changes(italy):
    if italy.economic_state == "recovery":
        recovery(italy)
    elif italy.economic_state == "expansion":
        expansion(italy)
    elif italy.economic_state == "recession":
        recession(italy)
    elif italy.economic_state == "depression":
        depression(italy)
def economic_decisions(italy):
    if italy.past_year < italy.date.year:

        italy.economic_growth = (italy.current_gdp - italy.past_gdp / ((italy.past_gdp + italy.current_gdp) / 2)) * 100
        """Calculation of yearly economic growth"""
        if italy.economic_growth <= 1.5:
            if not italy.economic_stimulus:
                choice = input(f"Your GDP grew {italy.economic_growth} last year.\n"
                               f"Would you like to apply a stimulus?: ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    economic_stimulus(italy)

        elif italy.economic_growth >= 10.5:
            if italy.economic_stimulus:
                italy.economic_stimulus = False
    else:
        gdp_changes(italy)
        economic_state(italy)

"""stats functions"""
def stats(italy):
    """Stats go from...
    1. Political
    2. Population
    3. Economic
    4. Social???
    5. Other
    """
    print(f"Your current monarch is {italy.monarch}\n"
          f"Your current prime minister is {italy.pm}\n"
          f"Your current stability is {round(italy.stability, 3)}\n"
          f"Your current population is {italy.current_pop}\n"
          f"Socialists make up {round((italy.italian_socialist_party / italy.current_pop) * 100, 4)}% of population.\n"
          f"Republicans make up {round((italy.italian_republican_party / italy.current_pop) * 100, 4)}% of the population.\n"
          f"The peoples party make up {round((italy.italian_peoples_party / italy.current_pop) * 100, 4)}% of the population.\n"
          f"Liberals make up {round((italy.italian_liberal_party / italy.current_pop) * 100, 4)}% of the population.\n"
          f"Your current happiness level is {round(italy.happiness, 3)}\n"
          f"There have been {italy.births} births in {italy.past_year}\n"
          f"There have been {italy.deaths} deaths in {italy.past_year}\n"
          f"Your current GDP is ${round(italy.current_gdp, 2)}\n"
          f"Your current GDP growth rate is {round((italy.current_gdp - italy.past_gdp) / ((italy.current_gdp + italy.past_gdp)/2) * 100, 5)}%\n"
          f"Your current debt to GDP ratio is {round((italy.national_debt / italy.current_gdp), 2)}%\n"
          f"Your current tax rate is {italy.tax_rate}\n"
          f"Your economy is currently in a(n) {italy.economic_state}\n"
          f"Your current national debt it ${round(italy.national_debt, 2)}.\n"
          f"Your current tax rate is {italy.tax_rate}%\n"
          f"Your current army size is {italy.army}\n")
def social_events(italy):
    if italy.date.year > 1945 and italy.date == datetime(italy.year, 4, 25):
        print("Today is the day that we wrestled our futures from Mussolini's tyranny.\n")
        italy.happiness += round(random.uniform(0.25, 1.25), 2)
        time.sleep(3)
def economic_events(italy):
    if italy.date > datetime(1922, 10, 24) and italy.date < datetime(1929, 10, 24):
        increment = round(random.uniform(1000, 10000), 2)
        italy.curent_gdp += increment
        italy.national_debt += round(increment * round(random.uniform(0.001, 0.009), 2), 2)

    if italy.date == datetime(1929, 10, 24):
        print("The Italian economy has fallen into a Depression.\n"
              "It is being reported that our economy has been slashed by a factor of 5\n"
              "Other nations across the globe are experiencing similar issues.\n")
        time.sleep(3)
        italy.current_gdp /= 5
        italy.government_spending = round(random.uniform(100000, 5000000), 2)
        italy.national_debt = round(italy.government_spending * round(random.uniform(0.001, 0.05), 2), 2)
def political_events(italy):
    if italy.date == datetime(1922, 10, 27):
        print(f"Benito Mussolini has stormed Rome, forcing {italy.monarch} to elect as PM.\n")
        time.sleep(3)
        italy.pm = "Benito Mussolini"

    elif italy.date == datetime(1940, 10, 28):
        print("Italy has entered world war 2 alongside Hitler, bonding them together.\n")
        italy.alliance = "Axis"
        time.sleep(3)
def events(italy):
    political_events(italy)
    economic_events(italy)
    social_events(italy)

def manual_game(italy):
    while italy.current_pop > 150000:
        print(f"Date: {italy.date}")
        italy.date += timedelta(days=1)
        # incrementing of time
        stability_happiness(italy)
        events(italy)
        population_change(italy)
        economic_decisions(italy)
        military_functions(italy)
        randomized_functions(italy)
        if italy.stability > 50:
            choice = input("view stats: ")
            if choice.lower() == "yes" or choice.lower() == "y":
                stats(italy)
        time.sleep(3)
class Italy:
    def __init__(self, year):
        """Time variables"""
        self.date = datetime(int(year), 1, 1)

        self.past_year = self.date.year

        """Population variables"""
        self.current_pop = population[year]
        self.population_change = 0
        self.past_pop = self.current_pop
        self.births = 0
        self.deaths = 0
        self.happiness = 95.56
        # population controller if birth rate gets out of hand
        self.condom_subsidy = False
        # population controller if birth rate flops

        self.viagra_subsidy = False
        """Political variables"""
        self.pm = prime_ministers[year]
        self.monarch = monarchs[year]
        self.stability = 90.00
        self.anti_establishment = 0
        # political parties based upon time frame
        if self.date < datetime(1922, 10, 27):
            self.italian_socialist_party = round(self.current_pop * round(random.uniform(0.1, 0.25), 2), 0)

            self.italian_republican_party = round((self.current_pop - self.italian_socialist_party) *
                                                  round(random.uniform(0.1, 0.25), 2), 0)


            self.italian_peoples_party = round((self.current_pop - self.italian_socialist_party -
                                                self.italian_republican_party) *
                                                round(random.uniform(0.1, 0.25), 2), 0)

            self.italian_liberal_party = round((self.current_pop - self.italian_socialist_party -
                                                self.italian_republican_party - self.italian_peoples_party))

        """Economic_variables"""
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.economic_state = "recovery"
        self.tax_rate = tax_rate[year]
        self.economic_stimulus = False
        self.economic_growth = 0
        self.economic_change_date = self.date + timedelta(days=60)
        # gdp components
        self.consumer_spending = 0
        self.investment = 0
        self.exports = 0
        self.imports = 0
        # political economic variables
        self.government_spending = 0
        self.national_debt = 10000000
        """international variables"""
        self.alliance = None
        """military variables"""
        self.army = army_size[year]
        self.conscripts = round(self.current_pop * round(random.uniform(0.001, 0.009), 5), 0)
        self.conscription_status = "limited"
        self.conscript_census = self.date + timedelta(days=15)
        self.war_deaths = 0