import random
import time
from datetime import datetime, timedelta
from game.ai import playable_nation

leaders = {
    "1910": "Ahmad Shah Qajar",
    "1914": "Ahmad Shah Qajar",
    "1918": "Ahmad Shah Qajar",
    "1932": "Reza shah",
    "1936": "Reza shah",
    "1939": "Reza shah"
}


population = {
    "1910": 10970000,
    "1914": 10320000,
    "1918": 9530000,
    "1932": 13270000,
    "1936": 14230000,
    "1939": 14970000
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

flags = {"1910": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1914": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1918": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1932": "../flags/iran/1920px-State_flag_of_Persia_(1907–1933).jpg",
         "1936": "../flags/iran/1920px-State_flag_of_Iran_(1933–1964).jpg",
         "1939": "../flags/iran/1920px-State_flag_of_Iran_(1933–1964).jpg"
         }

leader_images = {
    "1910": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1914": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1918": "../leaders/iran/330px-AhmadShahQajar2_1910-1918.jpg",
    "1932": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg",
    "1936": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg",
    "1939": "../leaders/iran/Reza_shah_uniform-1932-1939.jpg"
}

class Iran(playable_nation.PlayableNation):
    def __init__(self, year):
        super().__init__(year)
        self.name = "iran"
        # date variables
        self.date = datetime(int(year), 1, 1)
        self.improve_stability = self.date
        self.improve_happiness = self.date
        self.debt_repayment = self.date
        self.check_stats = self.date + timedelta(days=3)
        self.economic_change_date = self.date + timedelta(days=60)
        # amount of days that is given to the economy for it to either shrink or grow before being checked
        self.current_year = self.date.year
        # social variables
        """population"""
        self.population = population[year]
        self.births = 0
        self.deaths = 0
        self.birth_control = False
        self.birth_enhancer = False
        """happiness"""
        self.happiness = 98.56
        # political
        self.leader = leaders[year]
        self.leader_image = leader_images[year]
        """Stability"""
        self.stability = 95.56
        self.flag = flags[year]
        # economic
        self.national_debt = 0
        self.current_gdp = gdp[year]
        self.past_gdp = self.current_gdp
        self.e_s = "recovery"
        self.income_tax_rate = 25.00
        self.corporate_tax_rate = 35.00
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        # military
        # international
        """general"""
        self.alliance = ""
        # other
        self.chosen = False
    # population functions
    def population_change(self):
        """instead of having the headache of calling both national objects separately, why not combine them"""

        if self.current_year < self.date.year:
            pop_change = ((self.births - self.deaths) / ((self.births + self.deaths) / 2)) * 100

            if pop_change < 2.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = input(f"Your population growth rate for {self.current_year} was {pop_change}%.\n"
                               f"Would you like to promote population growth?: ")
                not_answered = False

                while not_answered:
                    if choice.lower() == "y" or choice.lower() == "yes":
                        self.birth_enhancer = True
                        not_answered = True

                    elif choice.lower() == "n" or choice.lower() == "no":
                        not_answered = True

                    else:
                        print("Please enter your answer more efficiently. (y, yes, n, or no)\n")
                        time.sleep(3)
            elif pop_change > 12.56:
                """incorporation of what happens when Mexican birth rate becomes too low"""
                choice = input(f"Your population growth rate for {self.current_year} was {pop_change}%.\n"
                               f"Would you like to slow your population growth?: ")
                not_answered = False

                while not_answered:
                    if choice.lower() == "y" or choice.lower() == "yes":
                        self.birth_control = True
                        not_answered = True

                    elif choice.lower() == "n" or choice.lower() == "no":
                        not_answered = True

                    else:
                        print("Please enter your answer more efficiently. (y, yes, n, or no)\n")
                        time.sleep(3)
        else:
            if self.birth_enhancer:
                births = random.randrange(20, 40)
                deaths = random.randrange(11, 30)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            if self.birth_control:
                births = random.randrange(10, 30)
                deaths = random.randrange(25, 35)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths

            else:
                births = random.randrange(7, 15)
                deaths = random.randrange(4, 10)
                self.population += (births - deaths)
                self.births += births
                self.deaths += deaths
    # economic functions