import datetime

times = 0

"""Display of data within menus will be re-written later on"""

import arcade
from nation_state.asia.japan import japan
from nation_state.north_america.united_states import united_states
from nation_state.europe.germany import germany
from nation_state.europe.russia import russia
from nation_state.europe.italy import italy
from nation_state.europe.france import france
from nation_state.europe.britain import britain

time_frame = ["1910", "1914", "1918", "1932", "1936",
              "1939", "1945(defunct)", "1950(defunct)",
              "1962(defunct", "1960(defunct)", "1981(defunct)",
              "2001(defunct)", "2020(defunct)", "2022(defunct)"]
# time frame array will be expanded as project continues on

asia = ["Japan", "China(Defunct)", "Turkey(Defunct)", "India(Defunct)", "Vietnam(Defunct)",
        "North Korea(Defunct)", "South Korea(defunct)", "Pakistan(Defunct)", "Saudi Arabia(D)",
        "Iran(Defunct)", "Afghanistan(Defunct)"]
# array containing major nations in Asia

north_america = ["United States", "Canada(Defunct)", "Mexico(Defunct)", "Cuba(Defunct"]
# array containing major nations in North America

europe = ["Britain", "Russia", "Germany", "France", "Italy", "Serbia(Defunct)",
          "Netherlands(Defunct)", "Spain(Defunct)", "Belgium(Defunct)",
          "Poland(Defunct)"]
# array containing major nations in Europe

africa = ["Egypt", "Algeria", "Morocco", "South Africa",
          "Ethiopia", "Angola", "Congo", "Nigeria",
          "Tunisia"]
# array containing major players in Africa

south_america = ["Brazil", "Chile", "Argentina",
                 "Venezuela", "Columbia"]
# array containing major players in South America

australiasia = ["Australia", "New Zealand"]

"""global variables created and initialized
    values will be stored to an external database, to remember users choices
"""

class TimeFrameMenu(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height

    def draw_background(self):
        # creation of background
        arcade.draw_rectangle_filled(0, 0, self.width, self.height, color=arcade.color.BLACK)

    def draw_content(self):
        """method creates title and primary choices for the specific time frame you want"""
        self.menu_size = self.height / 1.15

        arcade.draw_lrtb_rectangle_filled(0, self.width, self.height, self.height / 1.1, color=arcade.color.DARK_GREEN)
        arcade.draw_text("Welcome to War", (self.width / 2) - 300, self.height - 45, color=arcade.color.DARK_RED, font_size=35)
        arcade.draw_text("Choose your time frame!", (self.width / 2) - 275, self.height - 75, color=arcade.color.DARK_RED, font_size=20)
        arcade.draw_text("hit spacebar to continue",
                         self.width / 2 - 275, self.height - 105, arcade.color.DARK_RED, font_size=20)
        # header and welcoming of user

        for i in range(0, int(len(time_frame)/2)):
            # loop that goes through elements of time frame variable
            arcade.draw_text(f"{i + 1}. {time_frame[i]}", self.width / 2 - 350, self.menu_size, arcade.color.NEON_FUCHSIA, font_size=20)
            self.menu_size -= 75

        self.menu_size = self.height / 1.15
        # menu_size is reset for next set of text to be printed out
        for i in range(int(len(time_frame)/2), len(time_frame)):
            arcade.draw_text(f"{i + 1}. {time_frame[i]}", self.width / 2 - 50, self.menu_size, arcade.color.NEON_FUCHSIA,
                             font_size=20)
            self.menu_size -= 75

    def on_draw(self):
        self.draw_background()

    def on_key_press(self, key: int, modifiers: int):
        """
        Key choices will act as user prompts.
        whichever time frame chosen will become value
        for time frame variable
        """
        if key == arcade.key.SPACE:
            arcade.close_window()

# break between both files
class NationalMenu(arcade.Window):
    """Class will eventually be migrated to time_frame file"""

    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height

    def draw_background(self):
        # creation of background
        arcade.draw_rectangle_filled(0, 0, self.width, self.height, color=arcade.color.BLACK)

    def draw_content(self):
        """method creates title and primary choices for the specific time frame you want"""
        self.menu_size = self.height - 200

        arcade.draw_lrtb_rectangle_filled(0, self.width, self.height + 50, self.height / 1.1, color=arcade.color.DARK_GREEN)
        #arcade.draw_text("Welcome to War", (self.width / 2) - 300, self.height - 50, color=arcade.color.DARK_RED,
        #                 font_size=35)
        arcade.draw_text("Choose your Nation!", (self.width / 2) - 325, self.height - 50,
                         color=arcade.color.DARK_RED, font_size=30)
        arcade.draw_text("press space bar to exit",(self.width / 2) - 275, self.height - 100, color=arcade.color.DARK_RED, font_size=20)

        arcade.draw_text("Asia", 100, self.height - 150,
                         color=arcade.color.CAMOUFLAGE_GREEN, font_size=20, bold=True)
        for i in range(0, len(asia)):
            arcade.draw_text(f"{i + 1}. {asia[i]}", 100, self.menu_size, color=arcade.color.NEON_FUCHSIA, font_size=15)
            self.menu_size -= 50
            # end of asian loop

        self.menu_size = self.height - 200
        # beginning of European loop
        arcade.draw_text("Europe", 400, self.height - 150,
                     color=arcade.color.CAMOUFLAGE_GREEN, font_size=20, bold=True)

        for i in range(0, len(europe)):
            arcade.draw_text(f"{i + 1}. {europe[i]}", 400, self.menu_size, color=arcade.color.NEON_FUCHSIA, font_size=15)
            self.menu_size -= 50
        # ending of european loop

        # beginning of american loop
        self.menu_size = self.height - 200
        # beginning of European loop
        arcade.draw_text("North America", 650, self.height - 150,
                         color=arcade.color.CAMOUFLAGE_GREEN, font_size=20, bold=True)

        for i in range(0, len(north_america)):
            arcade.draw_text(f"{i + 1}. {north_america[i]}", 650, self.menu_size, color=arcade.color.NEON_FUCHSIA,
                             font_size=15)
            self.menu_size -= 50

        self.menu_size = self.height - 200
        arcade.draw_text("Africa(Defunct)", 925, self.height - 150,
                         arcade.color.CAMOUFLAGE_GREEN, font_size=20, bold=True)
        for i in range(0, len(africa)):
            arcade.draw_text(f"{i + 1}. {africa[i]}", 925, self.menu_size, color=arcade.color.NEON_FUCHSIA,
                             font_size=15)
            self.menu_size -= 50

        self.menu_size = self.height - 200
        arcade.draw_text("South America(Defunct)", 1200, self.height - 150,
                         arcade.color.CAMOUFLAGE_GREEN, font_size=20, bold=True, italic=True)
        for i in range(0, len(south_america)):
            arcade.draw_text(f"{i + 1}. {south_america[i]}", 1200, self.menu_size, color=arcade.color.NEON_FUCHSIA,
                             font_size=15)
            self.menu_size -= 50

    def on_draw(self):

        self.draw_background()

    def on_key_press(self, key: int, modifiers: int):
        """
        Key choices will act as user prompts.
        whichever nation chosen will become value
        for nation variable. The other choice will be calling
        the main function for whichever nation file chosen.
        """
        if key == arcade.key.SPACE:
            arcade.close_window()

def time_main():
    """Beginning of time frame menu"""
    menu = TimeFrameMenu(1800, 1200)
    arcade.start_render()
    menu.on_draw()
    menu.draw_content()
    arcade.finish_render()
    arcade.run()
    """ending of time frame menu"""

    """Beginning of nation menu"""
    nationmenu = NationalMenu(1800, 1200)
    arcade.start_render()
    nationmenu.on_draw()
    nationmenu.draw_content()
    arcade.finish_render()
    arcade.run()
    """Ending of nation menu"""
    time_chosen = input("which time_frame do you choose?: ")
    nation_chosen = input("which nation do you choose?: ")

    if nation_chosen.lower() == "japan":
        japan.main(time_chosen)
    elif nation_chosen.strip().lower() == "united states" or nation_chosen.strip().lower() == "us":
        united_states.main(time_chosen)
    elif nation_chosen.strip().lower() == "germany":
        germany.main(time_chosen)
    elif nation_chosen.strip().lower() == "russia":
        russia.main(time_chosen)
    elif nation_chosen.strip().lower() == "italy":
        italy.main(time_chosen)
    elif nation_chosen.strip().lower() == "france":
        france.main(time_chosen)
    elif nation_chosen.strip().lower() == "britain":
        britain.main(time_chosen)

if __name__ == '__main__':
    time_main()