import arcade

options = ["Go back to Main Menu",
           "View Options",
           "View Stats"]

class OptionsMenu(arcade.Window):

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
        arcade.draw_text("War", (self.width / 2) - 150, self.height - 100, color=arcade.color.CYAN, font_size=25)
        arcade.draw_text("What would you like to do", (self.width / 2) - 300, self.height - 150, color=arcade.color.BLUE, font_size=25)

        for i in range(0, len(options)):
            # loop that goes through elements of time frame variable
            arcade.draw_text(f"{i + 1}. {options[i]}", self.width / 2 - 250, self.menu_size, arcade.color.BLUE, font_size=20)
            self.menu_size -= 50
        arcade.draw_text("hit x in right hand corner to exit menu",
                         self.width / 2 - 300, 500, arcade.color.BLUE, font_size=25)

    def on_draw(self):
        self.draw_background()

    def on_key_press(self, key: int, modifiers: int):
        """
        Key choices will act as user prompts.
        whichever time frame chosen will become value
        for time frame variable
        """
        """if key == arcade.key.SPACE:
            arcade.close_window()"""

def main():
    menu = OptionsMenu(1800, 1200)
    arcade.start_render()
    menu.on_draw()
    menu.draw_content()
    arcade.finish_render()
    arcade.run()
