import random
import time
from datetime import datetime, timedelta
import arcade

class StatisticsMenu(arcade.Window):

    def __init__(self, width, height, nation):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.nation = nation
        self.is_active = True

    def draw_background(self):
        # creation of background
        arcade.draw_rectangle_filled(0, 0, self.width, self.height, color=arcade.color.BLACK)

    def draw_content(self):
        """method creates title and primary choices for the specific time frame you want"""
        self.menu_size = self.height / 1.15

        arcade.draw_lrtb_rectangle_filled(0, self.width, self.height, self.height / 1.1, color=arcade.color.DARK_GREEN)
        arcade.draw_text("Current Stats", (self.width / 2) - 300, self.height - 45, color=arcade.color.DARK_RED, font_size=35)
        # header and welcoming of user

        """for i in range(0, int(len(time_frame)/2)):
            # loop that goes through elements of time frame variable
            arcade.draw_text(f"{i + 1}. {time_frame[i]}", self.width / 2 - 350, self.menu_size, arcade.color.NEON_FUCHSIA, font_size=20)
            self.menu_size -= 75

        self.menu_size = self.height / 1.15
        # menu_size is reset for next set of text to be printed out
        for i in range(int(len(time_frame)/2), len(time_frame)):
            arcade.draw_text(f"{i + 1}. {time_frame[i]}", self.width / 2 - 50, self.menu_size, arcade.color.NEON_FUCHSIA,
                             font_size=20)
            self.menu_size -= 75"""

    def on_draw(self):
        self.draw_background()
        #self.is_active = True

    def on_key_press(self, key: int, modifiers: int):
        """
        Key choices will act as user prompts.
        whichever time frame chosen will become value
        for time frame variable
        """
        if key == arcade.key.SPACE:
            arcade.close_window()
            self.is_active = False

"""Population Dictionaries"""
population = {
    # population will be set up to increase or decrease randomly throughout every year
    "1910": 92410000,
    "1914": 99110000,
    "1918": 103210000,
    "1932": 124840000,
    "1936": 128050000,
    "1939": 130880000
}
"""Political Dictionaries"""
presidents = {
    "1910": "William Howard Taft",
    "1914": "Woodrow Wilson",
    "1918": "Woodrow Wilson",
    "1932": "Herbert Hoover",
    "1936": "Franklin D. Roosevelt",
    "1939": "Franklin D. Roosevelt"
}

vice_presidents = {
    # dictionary of vice presidents incase president gets assassinated
    "1910": "James S. Sherman",
    "1914": "Thomas R. Marshall",
    "1918": "Thomas R. Marshall",
    "1932": "Charles Curtis",
    "1936": "John Garner",
    "1939": "Henry Wallace"
}
"""Economic dictionaries & Variables"""
business_cycle = ["expansion", "recession"]
gdp = {
    "1910": 520000000000,
    "1914": 500000000000,
    "1918": 550000000000,
    "1932": 550000000000,
    "1936": 575000000000,
    "1939": 1100000000000
}

tax_rate = {
    "1910": 0,
    "1914": 1.00,
    "1918": 6.00,
    "1932": 4.00,
    "1936": 4.00,
    "1939": 4.00
}

"""Subsidiary functions of game"""

"""population functions"""
def population_change(us):
    """Function is exaggerated in numbers
    incorporates population growth
    """
    if us.current_year < us.date.year:
        us.population_change = (us.population - us.current_pop / ((us.population + us.current_pop)/2)) * 100
        """Calculation of population change over year"""
        us.current_pop = us.population
        # reset of current population
        us.current_year = us.date.year
        # reset of current year

        if us.viagra_subsidize:
            us.population += random.randrange(25000, 50000)
            # Incorporation of deaths
            us.population -= random.randrange(4000, 15000)
            # Incorporation of births
            if us.population_change >= 10:
                """choice if population growth is out of control"""
                choice = input(f"your yearly population growth rate of {us.population_change}% is unsustainable"
                               f"Do you want to increase subsidies for population control?: ")
                if choice.lower() == "yes" or choice.lower() == "y":
                    us.viagra_subsidize = False
                    us.condom_subsidize = True

        elif us.condom_subsidize:
            """Choice if us population growth is too low"""
            us.population += random.randrange(5000, 20000)
            # Incorporation of deaths
            us.population -= random.randrange(8000, 25000)
            # Incorporation of births
            if us.population_change <= 1.5:
                """Choice if population growth is too low"""
                choice = input(f"your yearly population growth rate of {us.population_change}% is unsustainable"
                               f"Do you want to increase subsidies for population growth?: ")
                us.viagra_subsidize = True
                us.condom_subsidize = False
    else:
        us.population += random.randrange(6700, 45000)
        us.population -= random.randrange(4500, 27000)

"""political functions"""

"""Random functions"""
def random_politics(us):
    """Function based upon random political events"""
    chance = random.randrange(10, 20000)
    if chance % 12 == 5:
        issues = ["Abortion", "Immigration", "Guns", "Women's Rights"]
        print(f"A {issues[random.randrange(0, len(issues) - 1)]} protest occurred in DC.")

def random_economics(us):
    """Function based upon random economic events"""
    chance = random.randrange(10, 20000)
    if chance % 5 == 3:
        """Chance that Congress spends a bit of money"""
        money = round(random.uniform(145000, 150000000), 2)
        print(f"Congress decided to spend ${money} today")
        us.gdp += money
        us.government_debt += round((money * random.uniform(0.25, 0.75)), 2)

    elif chance % 8 == 3:
        """Chance that congress raises tax rate"""
        if us.tax_rate < 10.00:
            increase = round(random.uniform(0.25, 2.25), 2)
            print(f"Congress decided to raise taxes by {increase}%")
            us.investment -= round(random.uniform(120000, 1020000), 2)
            us.consumer_spending -= round(random.uniform(20000, 400000), 2)
            us.happiness -= round(random.uniform(0.25, 1.25), 2)
            time.sleep(3)
            us.tax_rate += increase

    elif chance % 10 == 6:
        """chance that congress lowers tax rate"""
        decrease = round(random.uniform(0.25, 2.25), 2)
        print(f"Congress decided to lower taxes by {decrease}%")
        us.investment += round(random.uniform(140000, 1200000), 2)
        us.consumer_spending += round(random.uniform(20000, 600000), 2)
        us.happiness += round(random.uniform(0.25, 1.25), 2)
        time.sleep(3)
        us.tax_rate -= decrease

    elif chance % 35 == 3:
        """Chance the economy goes for a run"""
        growth = round(random.uniform(3.56, 8.56), 2)
        print(f"The economy has whipped itself into a frenzy of extreme growth has taken place!!\n"
              f"Numbers indicate that it is beginning to grow at {growth}%.")
        time.sleep(3)
        us.gdp *= growth
        us.stability += round(random.uniform(0.95, 4.56), 2)
        us.happiness += round(random.uniform(0.56, 20.45), 2)

    elif chance % 45 == 4:
        """Chance that the economy goes into a tailspin"""
        retraction = round(random.uniform(5.56, 10.00), 2)
        print("OH FUCK, the economy has fallen into a tailspin.\n"
              f"It is being reported that it is beginning to shrink at {retraction}%")
        time.sleep(3)
        us.gdp /= retraction
        us.happiness -= round(random.uniform(10.45, 34.56), 2)
        us.stability -= round(random.uniform(12.56, 50.55), 2)
        if us.economic_state != "recession":
            us.economic_state = "depression"


def random_social(us):
    """Random events based upon a social aspect"""
    chance = random.randrange(10, 20000)
    if chance % 4 == 0:
        print("Someone threw a surprise birthday for their child!")
        time.sleep(3)
        us.happiness += round(random.uniform(0.5, 2), 2)

    elif chance % 8 == 3:
        print("A parade occurred")
        time.sleep(3)
        us.happiness += round(random.uniform(0.5, 2), 2)

    elif chance % 10 == 4:
        print("Someone just got married!!")
        time.sleep(3)
        us.happiness += round(random.uniform(0.5, 2), 2)

    elif chance % 12 == 5:
        money = random.randrange(1000, 10000000)
        print(f"Someone just won ${money} at their local lottery")


    elif chance % 15 == 2:
        people = random.randrange(3, 25)
        print(f"Someone lost control of their car and ran into a group of people.\n"
              f"{people} people died.")
        time.sleep(3)
        us.happiness -= round(random.uniform(0.5, 2), 2)

    elif chance % 24 == 5:
        locations = ["School", "Bank", "Store", "Parade"]
        people = random.randrange(0, 50)
        print(f"Someone decided to shoot up a {locations[random.randrange(0, len(locations) - 1)]}.\n"
              f"{people} people died")
        time.sleep(3)
        us.population -= people
        us.stability -= round(random.uniform(0.5, 5), 2)
        us.happiness -= round(random.uniform(0.5, 14), 2)

def random_weather(us):
    """Function covers random weather events"""
    print()

def random_international(us):
    """
    Function deals with un-anticipated international events.
    These events will include terrorism, pre-emptive strikes,
    trade(possibly), international aid, and many more
    """
    print()
def randomized_functions(us):
    """Function that deviates to other subsidiary functions"""
    random_politics(us)
    random_social(us)
    random_economics(us)
    random_weather(us)
    random_international(us)

"""Economic Functions"""
def low_growth(us):
    if us.economic_state == "expansion":
        """Very slight growth within economy"""
        us.consumer_spending = round(random.uniform(30000, 75000), 2)
        us.investment = round(random.uniform(20000, 54000), 2)
        us.government_spending = round(random.uniform(300000, 500000), 2)
        us.government_debt += us.government_spending * round(random.uniform(0.25, 0.75), 2)
        us.exports = round(random.uniform(20000, 560000), 2)
        us.imports = round(random.uniform(32000, 560000), 2)
        us.gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    else:
        """Entry into a recession"""
        us.consumer_spending = -(round(random.uniform(15000, 65500), 2))
        us.investment = -(round(random.uniform(3000, 5000), 2))
        us.government_spending = round(random.uniform(200000, 450000), 2)
        us.government_debt += us.government_spending * round(random.uniform(0.25, 0.75), 2)
        us.exports = round(random.uniform(6200, 120000), 2)
        us.imports = round(random.uniform(140000, 1400000), 2)
        us.gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
def moderate_growth(us):
    if us.economic_state == "expansion":
        """State of moderate wealth for nation"""
        us.consumer_spending = round(random.uniform(60000, 105000), 2)
        us.investment = round(random.uniform(60000, 100000), 2)
        us.government_spending += round(random.uniform(100000, 350000), 2)
        us.government_debt += us.government_spending * round(random.uniform(0.25, 0.75), 2)
        us.exports = round(random.uniform(60000, 860000), 2)
        us.imports = round(random.uniform(62000, 880000), 2)
        us.gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    else:
        """Economy turning towards depression"""
        us.consumer_spending = -(round(random.uniform(35000, 102500), 2))
        us.investment = -(round(random.uniform(30000, 40000), 2))
        us.government_spending = round(random.uniform(500000, 1050000), 2)
        us.government_debt += us.government_spending * round(random.uniform(0.25, 0.75), 2)
        us.exports = round(random.uniform(140000, 1200000), 2)
        us.imports = round(random.uniform(140000, 1400000), 2)
        us.gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))

def high_growth(us):
    if us.economic_state == "expansion":
        """State of glorious wealth for nation"""
        us.consumer_spending = round(random.uniform(60000, 105000), 2)
        us.investment = round(random.uniform(60000, 100000), 2)
        us.government_spending = round(random.uniform(50000, 75000), 2)
        us.government_debt += us.government_spending * round(random.uniform(0.25, 0.75), 2)
        us.exports = round(random.uniform(120000, 1200000), 2)
        us.imports = round(random.uniform(140000, 1400000), 2)
        us.gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))
    else:
        """Very severe economic depression"""
        us.consumer_spending = -(round(random.uniform(6000, 10500), 2))
        us.investment = -(round(random.uniform(6000, 10000), 2))
        us.government_spending = round(random.uniform(500000, 1250000), 2)
        us.government_debt += us.government_spending * round(random.uniform(0.25, 0.75), 2)
        us.exports = round(random.uniform(1200, 120000), 2)
        us.imports = round(random.uniform(140000, 1400000), 2)
        us.gdp += (us.consumer_spending + us.investment + us.government_spending + (us.exports - us.imports))

def stimulus(us):
    """Fucntion deals with increased government spending"""
    """Function covering government spending and taxes
    in times of economic crisis
    """
    us.economic_stimulus = True
    """us.government_spending += random.randrange(24000, 100000)"""
    if us.recess_years < 3 and us.economic_growth >= 0.5:

        choice = input("Do you want to increase tax rate(Remember this applies to the entire population).\n"
                       "Yes or No?: ")
        """Prompting user to choose if they want to increase taxes"""

        if choice.lower() == 'yes' or choice.lower() == 'y':
            """if statement covering if answer is yes"""
            valid_choice = False
            while valid_choice:
                tax_hike = float(input("what will your new tax rate(between 0.5 & 10.0 be?: "))
                if tax_hike <= 10.00 and tax_hike >= 0.5:
                    """if statement if tax rate meets criteria"""
                    print(f"{tax_hike}% is new tax rate.")

                    valid_choice = True
                elif tax_hike <= 0:
                    """if statement if tax rate is below 0"""
                    print("new tax rate will be impossible to carry out. choose another tax rate")

                elif tax_hike >= 10:
                    """if statement if tax rate is too high"""
                    print("New tax rate will piss a lot of people off. Choose another tax rate.")
                else:
                    print("not a valid tax rate")

    elif us.recess_years >= 3:
        """if statement if economy has been growing slowly for past 3 years"""
        us.tax_rate = round(random.uniform(us.tax_rate, 10.0), 2)
        print("Congress has voted to raise the tax rate, without your involvement!")
        print(f"New tax rate {us.tax_rate}%")

def gdp_change(us):
    """Function covers direction of gdp change
    over daily count
    """
    if us.tax_rate <= 3 and us.tax_rate >= 0.5:
        """Economic growth under low tax rate"""
        high_growth(us)

    elif us.tax_rate <= 7.5 and us.tax_rate >= 3.1:
        """Economic growth under moderate tax rate"""
        moderate_growth(us)

    else:
        """Economic growth under high tax rate"""
        low_growth(us)

def economic_decisions(us):
    if us.current_year < us.date.year:

        us.economic_growth = (us.gdp - us.current_gdp / ((us.gdp + us.current_gdp) / 2)) * 100
        """Simplified calculation for economic growth"""

        if us.economic_growth <= 1.5:
            choice = input(f"Your GDP grew {us.economic_growth}% last year.\n"
                           f"Do you want to stimulate your economy?: ")
            if choice.lower() == "yes" or choice.lower() == 'y':
                stimulus(us)

            elif choice.lower() == "no" or choice.lower() == 'n':
                """Incorporation of user choice no"""
                if us.recess_years > 3 and us.economic_growth <= 0.5:
                    """Implementation of Economic Stimulus if economy hasn't been growing 
                    for past 3 years
                    """
                    print("Your economy has been declining for three years.\n"
                          "An economic stimulus has been implemented!")
                    time.sleep(3)
                    stimulus(us)
    else:
        gdp_change(us)

"""Main function of US_Version of game"""
def manual_game(us):
    # Establishment of date variable
    while us.population > 2000000:
        us.date = us.date + timedelta(days=1)
        print(f"Date: {us.date}")
        # function will incorporate daily changes in us population
        population_change(us)
        economic_decisions(us)
        randomized_functions(us)
        if us.stability < 100:
            choice = input("view your stats: ")
            if choice.lower() == "y" or choice.lower() == "yes":
                menu = StatisticsMenu(1800, 1200, us)
                arcade.start_render()
                menu.on_draw()
                menu.draw_content()
                arcade.run()
                while not menu.is_active:
                    print('hi')
        """if us.current_year%4 == 0:
            us_elections(us)"""
class UnitedStates:
    def __init__(self, year):
        # population variables
        self.population = population[year]
        self.population_change = 0
        self.current_pop = self.population
        self.happiness = 96.56
        """Population controller if birth rate gets out of control"""
        self.condom_subsidize = False
        """Population controller if birth rate flops"""
        self.viagra_subsidize = False
        # political variables
        """Leaders of US"""
        self.president = presidents[year]
        self.vice_president = vice_presidents[year]
        """Political parties of US"""
        self.republicans = self.population * 0.5
        self.democrats = self.population - self.republicans
        """Other political variables"""
        self.stability = 95.00
        # economic variables
        self.economic_state = business_cycle[random.randrange(len(business_cycle) - 1)]
        self.gdp = gdp[year]
        self.current_gdp = self.gdp
        """holds current year of gdp(used for comparing with future GDP
        to determine GDP growth)
        """
        self.government_debt = 0
        """Components of GDP"""
        self.consumer_spending = 0
        self.investment = 0
        self.government_spending = 0
        self.exports = 0
        self.imports = 0
        """Economic Stimulus components"""
        self.economic_stimulus = False
        self.tax_rate = tax_rate[year]
        # military variables
        # international variables
        self.alliance = ""
        # time variables
        self.date = datetime(int(year), 1, 1)
        self.current_year = self.date.year

def main(time):
    united_states = UnitedStates(time)
    manual_game(united_states)