import arcade
time_frame = ["1910", "1914", "1918", "1932", "1936",
              "1939"]
# time frame array will be expanded as project continues on

nations = ["Japan", "United States", "Russia", "Germany",
                    "Britain", "France", "Serbia", "Italy"]
# nation_state array variable will be expanded upon as project continues

time_chosen = ""
nation_chosen = ""
"""global variables created and initialized
    values will be stored to an external database, to remember users choices
"""

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
        self.menu_size = self.height / 1.25

        arcade.draw_lrtb_rectangle_filled(0, self.width, self.height, self.height / 1.1, color=arcade.color.BLUE)
        arcade.draw_text("Welcome to War", (self.width / 2) - 250, self.height - 100, color=arcade.color.CYAN, font_size=25)

        arcade.draw_text("Choose your nation!", (self.width / 2) - 250, self.height - 150, color=arcade.color.BLUE, font_size=20)

        for i in range(0, len(nations)):
            # loop that goes through elements of time frame variable
            arcade.draw_text(f"{i + 1}. {nations[i]}", self.width / 2 - 215, self.menu_size, arcade.color.BLUE, font_size=20)
            self.menu_size -= 50
            print(f"{i + 1}. {nations[i]}")
    def on_draw(self):

        self.draw_background()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.SPACE:
            # when user hits space bar, window closes
            arcade.close_window()
# break

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
        self.menu_size = self.height / 1.25

        arcade.draw_lrtb_rectangle_filled(0, self.width, self.height, self.height / 1.1, color=arcade.color.BLUE)
        arcade.draw_text("Welcome to War", (self.width / 2) - 250, self.height - 100, color=arcade.color.CYAN, font_size=25)
        arcade.draw_text("Choose your time frame!", (self.width / 2) - 275, self.height - 150, color=arcade.color.BLUE, font_size=20)
        # header and welcoming of user

        for i in range(0, len(time_frame)):
            # loop that goes through elements of time frame variable
            arcade.draw_text(f"{i + 1}. {time_frame[i]}", self.width / 2 - 175, self.menu_size, arcade.color.BLUE, font_size=20)
            self.menu_size -= 50
            print(f"{i + 1}. {time_frame[i]}")
        arcade.draw_text("Hit space bar to close window",
                         self.width / 2 - 325, 500, arcade.color.BLUE, font_size=25)

    def on_draw(self):
        self.draw_background()

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.SPACE:
            # when user hits space bar, window closes
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

    time_chosen = input("Which time period do you choose?: ")
    # user is prompted to choose time period

    """Beginning of nation menu"""
    nationmenu = NationalMenu(1800, 1200)
    arcade.start_render()
    nationmenu.on_draw()
    nationmenu.draw_content()
    arcade.finish_render()
    arcade.run()
    """Ending of nation menu"""

    nation_chosen = input("Which nation do you choose?: ")
    # user is prompted to choose nation

if __name__ == '__main__':
    time_main()