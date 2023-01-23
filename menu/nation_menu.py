import arcade
import time
from nation_state import britain

nations = ["Germany", "France", "Great Britain",
           "United States", "Japan", "Russia", "Italy"]
# nation_state array variable will be expanded upon as project continues

class Menu(arcade.Window):
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
        arcade.draw_text("Welcome to War", (self.width / 2) - 250, self.height - 100, color=arcade.color.BONE, font_size=25)

        arcade.draw_text("Choose your nation!", (self.width / 2) - 250, self.height - 150, color=arcade.color.BLUE, font_size=20)

        for i in range(0, len(nations)):
            # loop that goes through elements of time frame variable
            arcade.draw_text(f"{i + 1}. {nations[i]}", self.width / 2 - 215, self.menu_size, arcade.color.BLUE, font_size=20)
            self.menu_size -= 50
            print(f"{i + 1}. {nations[i]}")
    def on_draw(self):

        self.draw_background()

def main():
    menu = Menu(1800, 1200)

    arcade.start_render()

    menu.on_draw()
    menu.draw_content()
    arcade.finish_render()

    arcade.run()

if __name__ == '__main__':
    main()