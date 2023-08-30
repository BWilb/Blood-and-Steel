import random
import sys
import time
from datetime import datetime, timedelta
from buttons import button

import pyautogui
import pygame
from nation_state.asia.se_asia.japan import japan
import globe
import os

from database_management import upload_database

pygame.init()
pygame.mixer.init()


class SpriteGame:
    def __init__(self, nation, globe):
        self.HEIGHT = pyautogui.size().height * 0.9
        self.WIDTH = pyautogui.size().width
        # initial width and height will be 90% size of computer screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.flare_background = \
            pygame.transform.scale(pygame.image.load("background_image_files/artillery_flares.jpg").convert_alpha(),
                                   (self.WIDTH, self.HEIGHT))

        # music playlist
        self.music_playlist = []

        # define fonts
        self.font = pygame.font.SysFont("Arial-Black", 40)
        # define colour
        self.text_col = (0, 0, 0)
        pygame.display.set_caption("Main Menu")
        self.is_running = True
        self.game_paused = False
        self.game_state = "main game"
        # while loop constraint; controls entire game
        self.nation = nation
        self.globe = globe
        self.actual_day = self.nation.date
        self.speed = 1.5

    def background_music(self):
        """within function while loop will be established that """
        pygame.mixer.music.load(self.music_playlist[0])
        pygame.mixer.music.play()

    def check_stream(self):
        """checks to see if the current music stream is busy or not
        if the music stream is currently in use pass
        if music stream isn't in use, pop off the first music file and send the next one
        to background_music function
        """
        if pygame.mixer.music.get_busy():
            pass
        else:
            self.music_playlist.pop(0)
            self.background_music()

    def load_music(self):
        # loads background music into game's playlist
        if self.nation.date.year < 1918:
            folder = "background_music/in_game/pre_1918"
            for song in os.listdir(folder):
                self.music_playlist.append(f"background_music/in_game/pre_1918/{song}")

        elif self.nation.date.year > 1918:
            folder = "background_music/in_game/after_1918"
            for song in os.listdir(folder):
                self.music_playlist.append(f"background_music/in_game/after_1918/{song}")
                print(song)
        self.background_music()

    def draw_text(self, text, font, text_col, x, y):
        """function of opening menu class draws text"""
        # draws the text on screen
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def update_screen(self):
        """updates screen"""
        pygame.display.update()

    def resize_leader(self):
        """function for resizing both leader that will be displayed"""
        return pygame.transform.scale(pygame.image.load(self.nation.leader_image).convert_alpha(), (350, 500))

    def resize_flag(self):
        """function for resizing both flag that will be displayed"""
        return pygame.transform.scale(pygame.image.load(self.nation.flag).convert_alpha(), (200, 125))

    def view_government(self):
        """sub section of user nation that displays political information regarding nation"""
        self.screen.fill((52, 78, 91))
        self.draw_text(f"Political stats", self.font, self.text_col, self.WIDTH * 0.45, 100)
        self.draw_text(f"Current Leader: {self.nation.leader}", self.font, self.text_col,
                       (self.WIDTH * 0.355) - len(self.nation.leader), 200)
        self.draw_text(f"Stability: {round(self.nation.stability, 2)}%", self.font, self.text_col, self.WIDTH * 0.45,
                       300)
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/sprite_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.25)
        if back_button.draw(self.screen):
            self.game_state = "main game"

    def view_economy(self):
        increment_img = pygame.image.load(
            "buttons/game_buttons/functionality_buttons/increment_sing.jpg").convert_alpha()
        decrement_img = pygame.image.load(
            "buttons/game_buttons/functionality_buttons/decrement_sign.jpg").convert_alpha()
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/sprite_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.25)
        """tax buttons"""
        # corporate taxes
        cor_tax_inc_button = button.Button(self.WIDTH * 0.505, 450, increment_img, 0.05)
        cor_tax_dec_button = button.Button(self.WIDTH * 0.555, 450, decrement_img, 0.05)
        # income taxes
        inc_tax_inc_button = button.Button(self.WIDTH * 0.505, 550, increment_img, 0.05)
        inc_tax_dec_button = button.Button(self.WIDTH * 0.555, 550, decrement_img, 0.05)
        """sub section of user nation that displays economic information regarding nation"""
        self.screen.fill((52, 78, 91))
        self.draw_text(f"Economic stats", self.font, self.text_col, self.WIDTH * 0.45, 100)
        self.draw_text(f"GDP: ${round(self.nation.current_gdp, 2)}", self.font, self.text_col, self.WIDTH * 0.405, 200)
        self.draw_text(f"National Debt: ${round(self.nation.national_debt, 2)}", self.font, self.text_col,
                       self.WIDTH * 0.405,
                       300)
        self.draw_text(f"Current Corporate Tax Rate: {self.nation.corporate_tax_rate}%", self.font, self.text_col,
                       self.WIDTH * 0.325,
                       400)
        self.draw_text(f"Current Income Tax Rate: {self.nation.income_tax_rate}%", self.font, self.text_col,
                       self.WIDTH * 0.345, 500)
        if cor_tax_inc_button.draw(self.screen):
            pass
        if cor_tax_dec_button.draw(self.screen):
            pass
        if inc_tax_inc_button.draw(self.screen):
            pass
        if inc_tax_dec_button.draw(self.screen):
            pass
        if back_button.draw(self.screen):
            self.game_state = "main game"

    def view_society(self):
        """sub section of user nation that displays social information regarding nation"""
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/sprite_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.25)
        self.screen.fill((52, 78, 91))
        self.draw_text(f"Social stats", self.font, self.text_col, self.WIDTH * 0.45, 100)
        self.draw_text(f"Population: {self.nation.population}", self.font, self.text_col, self.WIDTH * 0.405, 200)
        self.draw_text(f"Happiness: {round(self.nation.happiness, 2)}%", self.font, self.text_col, self.WIDTH * 0.405,
                       300)
        if back_button.draw(self.screen):
            self.game_state = "game"

    def nation_changes(self):
        self.nation.check_economic_state()
        self.nation.population_change()
        self.nation.stability_happiness_change(self.globe)

    def globe_changes(self):
        for i in range(len(self.globe.nations)):
            # will be re-introduced, once figure out how to deal with other nations than one currently playing as
            if self.globe.nations[i].name == self.nation.name:
                pass
            else:
                self.globe.nations[i].main(self.globe)

        upload_database.update_database_info(self.globe.nations)

    def primary_game(self):
        """speed imgs"""
        faster_img = pygame.image.load("buttons/game_buttons/functionality_buttons/faster.jpg").convert_alpha()
        fast_img = pygame.image.load("buttons/game_buttons/functionality_buttons/fast.jpg").convert_alpha()
        regular_img = pygame.image.load("buttons/game_buttons/functionality_buttons/regular_speed.jpg").convert_alpha()
        slow_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slow.jpg").convert_alpha()
        slower_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slower.jpg").convert_alpha()
        """speed buttons"""
        faster_button = button.Button(1720, 150, faster_img, 0.035)
        fast_button = button.Button(1680, 150, fast_img, 0.035)
        regular_button = button.Button(1640, 150, regular_img, 0.035)
        slow_button = button.Button(1600, 150, slow_img, 0.035)
        slower_button = button.Button(1560, 150, slower_img, 0.035)
        #
        govt_img = pygame.image.load("buttons/game_buttons/government_button.jpg").convert_alpha()
        econ_img = pygame.image.load("buttons/game_buttons/economy_buttion.jpg").convert_alpha()
        foreign_img = pygame.image.load("buttons/game_buttons/foreign_button.jpg").convert_alpha()
        social_img = pygame.image.load("buttons/game_buttons/social_button.jpg").convert_alpha()
        """stats buttons"""
        govt_button = button.Button(100, 0, govt_img, 0.16)
        econ_button = button.Button(600, 0, econ_img, 0.16)
        foreign_button = button.Button(1100, 0, foreign_img, 0.16)
        social_button = button.Button(1600, 0, social_img, 0.16)
        """primary screen user sees after opening menu"""
        upload_database.initial_upload_to_database(self.globe.nations)
        flag = self.resize_flag()
        leader = self.resize_leader()

        self.screen.fill((0, 0, 0))
        sprite_background = \
            pygame.transform.scale(
                pygame.image.load("background_image_files/Untitled.jpg").convert_alpha(),
                (self.WIDTH, self.HEIGHT))
        self.screen.blit(sprite_background, (0, 0))
        pygame.draw.rect(self.screen, (211, 211, 211), (0, 0, self.WIDTH, 100))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.WIDTH * 0.04, 140, flag.get_width() + 35, flag.get_height() + 25))
        if govt_button.draw(self.screen):
            self.game_state = "view government"
        if econ_button.draw(self.screen):
            self.game_state = "view economy"
        if foreign_button.draw(self.screen):
            pass
        if social_button.draw(self.screen):
            self.game_state = "view society"

        self.draw_text(f"{self.actual_day.date()}", self.font, self.text_col, self.WIDTH * 0.80, 100)
        if slower_button.draw(self.screen):
            self.speed = 2.75
        if slow_button.draw(self.screen):
            self.speed = 2.25
        if regular_button.draw(self.screen):
            self.speed = 1.75
        if fast_button.draw(self.screen):
            self.speed = 1.25
        if faster_button.draw(self.screen):
            self.speed = 0.75
        self.screen.blit(flag, (self.WIDTH * 0.05, 150))
        self.screen.blit(leader, (self.WIDTH * 0.015, 300))

        self.nation_changes()
        self.globe_changes()
        self.actual_day += timedelta(days=1)
        time.sleep(1.25)

    def main_game(self):
        self.load_music()
        while self.is_running:
            if not self.game_paused:
                if self.game_state == "main game":
                    self.primary_game()

                elif self.game_state == "view society":
                    self.view_society()

                elif self.game_state == "view government":
                    self.view_government()

                elif self.game_state == "view economy":
                    self.view_economy()
            self.check_stream()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # pushing of space key
                    if event.key == pygame.K_SPACE:
                        if self.game_paused:
                            self.game_paused = False

                        else:
                            self.game_paused = True

                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()

            self.update_screen()
        pygame.quit()