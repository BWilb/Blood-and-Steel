from datetime import timedelta
from game.menu.buttons import button

import pyautogui
import pygame

class Alert:
    # smaller pygame window that pops up to alert user of specific event
    def __init__(self, date, text):
        self.expiration_date = date + timedelta(days=10)
        self.text = text

    def draw_text(self, text, font, text_col, x, y):
        """function of Alert class draws text"""
        # draws the text on screen
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def check_expiration(self, date):
        if date > self.expiration_date:
            self.is_expired = True


    def main(self):
        back_img = pygame.image.load("buttons/opening_menu_buttons/back_button.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.38, 900, back_img, 0.10)

        while self.is_running:
            if back_button.draw(self.screen) or self.is_expired:
                pygame.quit()
