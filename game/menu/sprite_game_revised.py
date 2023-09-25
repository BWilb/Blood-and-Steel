import random
import sys
import time
from datetime import timedelta
from buttons import button
# from globe_relations.message import Alert
from colors.color import Color
import pyautogui
import pygame
import os

from database_management import upload_database

pygame.init()
pygame.mixer.init()


class SpriteGame:
    def __init__(self, nation, globe):
        self.HEIGHT = pyautogui.size().height * 0.9
        self.WIDTH = pyautogui.size().width
        self.pop_alert = False
        # initial width and height will be 90% size of computer screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

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
        self.actual_day = self.globe.date
        self.speed = 1.5
        self.flag_button = button.Button(50, 50, pygame.image.load(self.nation.flag), 0.05)
        self.clock = pygame.time.Clock()

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
        if self.globe.date.year <= 1918:
            folder = "background_music/in_game/pre_1918"
            for song in os.listdir(folder):
                self.music_playlist.append(f"background_music/in_game/pre_1918/{song}")

        elif self.globe.date.year > 1918:
            folder = "background_music/in_game/after_1918"
            for song in os.listdir(folder):
                self.music_playlist.append(f"background_music/in_game/after_1918/{song}")
        self.background_music()

    def draw_text(self, text, font, text_col, x, y):
        """function of opening menu class draws text"""
        # draws the text on screen
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def update_screen(self):
        """updates screen"""
        pygame.display.update()

    def draw_nations(self):
        for i in range(0, len(self.globe.nations)):
            self.globe.nations[i].establish_map_coordinates()
            print(len(self.globe.nations[i].coordinates))
            for coordinates in range(0, len(self.globe.nations[i].coordinates)):
                if len((self.globe.nations[i].coordinates[coordinates])) == 1:
                    pygame.draw.polygon(self.screen, self.globe.nations[i].nation_color,
                                        self.globe.nations[i].coordinates[coordinates])
                else:
                    pygame.draw.polygon(self.screen, self.globe.nations[i].nation_color,
                                        self.globe.nations[i].coordinates[coordinates])

    def resize_leader(self):
        """function for resizing both leader that will be displayed"""
        return pygame.transform.scale(pygame.image.load(self.nation.leader_image).convert_alpha(), (250, 400))

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
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.15)
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
        cor_tax_inc_button = button.Button(self.WIDTH * 0.05, 435, increment_img, 0.025)
        cor_tax_dec_button = button.Button(self.WIDTH * 0.11, 435, decrement_img, 0.025)
        # income taxes
        inc_tax_inc_button = button.Button(self.WIDTH * 0.05, 535, increment_img, 0.025)
        inc_tax_dec_button = button.Button(self.WIDTH * 0.11, 535, decrement_img, 0.025)
        """sub section of user nation that displays economic information regarding nation"""

        # self.screen.blit(self.sprite_background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        self.draw_text(f"{self.actual_day.date()}", self.font, self.text_col, self.WIDTH * 0.80, 100)

        self.draw_text(f"Economic stats", pygame.font.SysFont("Arial-Black", 30), (255, 255, 255), self.WIDTH * 0.025,
                       50)
        #
        self.draw_text(f"GDP:", pygame.font.SysFont("Arial-Black", 20),
                       (255, 255, 255)
                       , self.WIDTH * 0.075, 150)
        self.draw_text(f"${round(self.nation.current_gdp, 2)}", pygame.font.SysFont("Arial-Black", 20),
                       (255, 255, 255)
                       , self.WIDTH * 0.035, 200)
        self.draw_text(f"National Debt: ", pygame.font.SysFont("Arial-Black", 20),
                       (255, 255, 255), self.WIDTH * 0.055, 250)
        self.draw_text(f"${round(self.nation.national_debt, 2)}", pygame.font.SysFont("Arial-Black", 20),
                       (255, 255, 255),
                       self.WIDTH * 0.045,
                       300)
        self.draw_text(f"Current Corporate Tax Rate",
                       pygame.font.SysFont("Arial-Black", 20), (255, 255, 255),
                       self.WIDTH * 0.015, 350)
        self.draw_text(f"{self.nation.corporate_tax_rate}%",
                       pygame.font.SysFont("Arial-Black", 20), (255, 255, 255),
                       self.WIDTH * 0.07, 400)
        self.draw_text(f"Current Income Tax Rate:",
                       pygame.font.SysFont("Arial-Black", 20), (255, 255, 255),
                       self.WIDTH * 0.015, 450)
        self.draw_text(f"{self.nation.income_tax_rate}%",
                       pygame.font.SysFont("Arial-Black", 20), (255, 255, 255),
                       self.WIDTH * 0.07, 500)
        if cor_tax_inc_button.draw(self.screen):
            self.nation.corporate_tax_rate += 0.5
            time.sleep(0.5)
            """
            these effects will be brought in once the economic structure of every nation has been changed
            self.nation.investment -= 20
            self.nation.government_spending += 35"""

        if cor_tax_dec_button.draw(self.screen):
            self.nation.corporate_tax_rate -= 0.5
            time.sleep(0.5)
            """
            these effects will be brought in once the economic structure of every nation has been changed
            self.nation.investment += 10
            self.nation.government_spending -= 10"""

        if inc_tax_inc_button.draw(self.screen):
            self.nation.income_tax_rate += 0.5
            time.sleep(0.5)

            """self.nation.consumer_spending -= 10
            self.nation.government_spending += 10"""

        if inc_tax_dec_button.draw(self.screen):
            self.nation.income_tax_rate -= 0.5
            time.sleep(0.5)

            """self.nation.consumer_spending += 10
                self.nation.government_spending -= 10"""
        if back_button.draw(self.screen):
            self.game_state = "main game"

    def view_society(self):
        """sub section of user nation that displays social information regarding nation"""
        # self.screen.blit(self.sprite_background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        self.draw_text(f"{self.actual_day.date()}", self.font, self.text_col, self.WIDTH * 0.80, 100)

        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/sprite_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.05)
        self.draw_text(f"Social stats", pygame.font.SysFont("Arial-Black", 30),
                       self.text_col, self.WIDTH * 0.1, 100)
        self.draw_text(f"Population:", pygame.font.SysFont("Arial-Black", 20),
                       self.text_col, self.WIDTH * 0.1, 200)

        self.draw_text(f"{self.nation.population}", pygame.font.SysFont("Arial-Black", 20),
                       self.text_col, self.WIDTH * 0.1, 250)

        self.draw_text(f"Happiness: {round(self.nation.happiness, 2)}%", pygame.font.SysFont("Arial-Black", 20),
                       self.text_col, self.WIDTH * 0.1,
                       300)

        self.draw_text(f"{round(self.nation.happiness, 2)}%", pygame.font.SysFont("Arial-Black", 20),
                       self.text_col, self.WIDTH * 0.1,
                       350)
        if back_button.draw(self.screen):
            self.game_state = "main game"

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
        """primary screen user sees after opening menu"""
        upload_database.initial_upload_to_database(self.globe.nations, self.globe)

        self.screen.fill((65, 105, 225))
        """"""
        self.draw_nations()
        """"""
        # later on background will be an actual SVG image of world and not part of the screen
        self.draw_text(f"{self.globe.date}", self.font, self.text_col, self.WIDTH * 0.80, 100)
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
        # self.screen.blit(flag, (self.WIDTH * 0.05, 150))
        # self.screen.blit(leader, (self.WIDTH * 0.015, 300))
        if self.flag_button.draw(self.screen):
            self.game_state = "view infographics"

        self.nation_changes()
        self.globe_changes()
        self.globe.date += timedelta(days=1)


    def infographics(self):
        govt_img = pygame.image.load("buttons/game_buttons/government_button.jpg").convert_alpha()
        econ_img = pygame.image.load("buttons/game_buttons/economy_buttion.jpg").convert_alpha()
        foreign_img = pygame.image.load("buttons/game_buttons/foreign_button.jpg").convert_alpha()
        social_img = pygame.image.load("buttons/game_buttons/social_button.jpg").convert_alpha()
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(125, 850, back_img, 0.05)

        """stats buttons"""
        govt_button = button.Button(100, 450, govt_img, 0.125)
        econ_button = button.Button(100, 550, econ_img, 0.125)
        foreign_button = button.Button(100, 650, foreign_img, 0.125)
        social_button = button.Button(100, 750, social_img, 0.125)
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
        """back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/sprite_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.25)"""
        self.screen.fill((0, 0, 0))
        # self.screen.blit(self.sprite_background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
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

        leader = self.resize_leader()
        self.screen.blit(leader, (50, 0))

        if govt_button.draw(self.screen):
            self.game_state = "view government"
        if econ_button.draw(self.screen):
            self.game_state = "view economy"
        if foreign_button.draw(self.screen):
            pass
        if social_button.draw(self.screen):
            self.game_state = "view society"

        if back_button.draw(self.screen):
            self.game_state = "main game"

    def main_game(self):
        self.load_music()
        self.nation.sprite = True
        while self.is_running:
            if not self.game_paused:
                if self.game_state == "main game":
                    self.primary_game()
                elif self.game_state == "view infographics":
                    self.infographics()

                elif self.game_state == "view society":
                    self.view_society()

                elif self.game_state == "view government":
                    self.view_government()

                elif self.game_state == "view economy":
                    self.view_economy()
            self.clock.tick(220)
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
