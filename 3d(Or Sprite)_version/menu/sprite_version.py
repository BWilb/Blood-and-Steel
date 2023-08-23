import random
import sys
import time
from datetime import datetime, timedelta
from database_management import upload_database

"""import arcade
import threading
from nation_state.north_america.mexico import mexico
from nation_state.north_america.canada import canada
import socket
from pygame.constants import VIDEORESIZE"""
# import opening_menu
import button
# from tkinter import *
# from tkinter.ttk import *
import pygame
import pyautogui

SCREEN_WIDTH = pyautogui.size().width
SCREEN_HEIGHT = pyautogui.size().height * 0.9
# initial width will be size of screen width and height will be 90% size of computer screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("War and Politics")

# define fonts
font = pygame.font.SysFont("arialblack", 40)
# define colour
text_col = (255, 255, 255)
# creation of button imgs
"""stats imgs"""
govt_img = pygame.image.load("buttons/game_buttons/government_button.jpg").convert_alpha()
econ_img = pygame.image.load("buttons/game_buttons/economy_buttion.jpg").convert_alpha()
foreign_img = pygame.image.load("buttons/game_buttons/foreign_button.jpg").convert_alpha()
social_img = pygame.image.load("buttons/game_buttons/social_button.jpg").convert_alpha()
"""paused imgs"""
quit_img = pygame.image.load("buttons/game_buttons/functionality_buttons/sprite_quit.jpg").convert_alpha()
cont_img = pygame.image.load("buttons/game_buttons/functionality_buttons/continue_button.jpg").convert_alpha()
back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/sprite_back.jpg").convert_alpha()
increment_img = pygame.image.load("buttons/game_buttons/functionality_buttons/increment_sing.jpg").convert_alpha()
decrement_img = pygame.image.load("buttons/game_buttons/functionality_buttons/decrement_sign.jpg").convert_alpha()
"""speed imgs"""
faster_img = pygame.image.load("buttons/game_buttons/functionality_buttons/faster.jpg").convert_alpha()
fast_img = pygame.image.load("buttons/game_buttons/functionality_buttons/fast.jpg").convert_alpha()
regular_img = pygame.image.load("buttons/game_buttons/functionality_buttons/regular_speed.jpg").convert_alpha()
slow_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slow.jpg").convert_alpha()
slower_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slower.jpg").convert_alpha()
# buttons
"""stats buttons"""
govt_button = button.Button(100, 0, govt_img, 0.16)
econ_button = button.Button(600, 0, econ_img, 0.16)
foreign_button = button.Button(1100, 0, foreign_img, 0.16)
social_button = button.Button(1600, 0, social_img, 0.16)
"""paused buttons"""
quit_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.15, quit_img, 0.25)
cont_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.45, cont_img, 0.25)
back_button = button.Button(SCREEN_WIDTH * 0.465, SCREEN_HEIGHT * 0.75, back_img, 0.25)
"""speed buttons"""
faster_button = button.Button(1720, 150, faster_img, 0.035)
fast_button = button.Button(1680, 150, fast_img, 0.035)
regular_button = button.Button(1640, 150, regular_img, 0.035)
slow_button = button.Button(1600, 150, slow_img, 0.035)
slower_button = button.Button(1560, 150, slower_img, 0.035)
"""tax buttons"""
cor_tax_inc_button = button.Button(SCREEN_WIDTH * 0.505, 450, increment_img, 0.05)
cor_tax_dec_button = button.Button(SCREEN_WIDTH * 0.555, 450, decrement_img, 0.05)
inc_tax_inc_button = button.Button(SCREEN_WIDTH * 0.505, 550, increment_img, 0.05)
inc_tax_dec_button = button.Button(SCREEN_WIDTH * 0.555, 550, decrement_img, 0.05)

# draw_text(f"Tax Rate: ${nation.tax_rate}%", font, text_col, SCREEN_WIDTH * 0.85, 200)

def draw_text(text, font, text_col, x, y):
    # draws the text on screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def check_flag(nation):
    # retrieving flag from nation flag variable and resizing flag
    return pygame.transform.scale(pygame.image.load(nation.flag).convert_alpha(), (200, 125))

def check_leader(nation):
    # retrieving leader from nation flag variable and resizing leader
    return pygame.transform.scale(pygame.image.load(nation.leader_image).convert_alpha(), (350, 500))
def economic_events(nation):
    pass

def social_events(nation):
    pass

def country_sprite(nation, globe):
    speed = 1.25
    """incrementing and decrementing buttons"""
    game_state = "game"
    run = True
    game_paused = False
    """three primary constraints on game"""
    upload_database.initial_upload_to_database(globe.nations)
    flag = check_flag(nation)
    leader = check_leader(nation)
    actual_day = nation.date

    while run:
        if not game_paused:
            if game_state == "game":
                screen.fill((52, 78, 91))

                pygame.draw.rect(screen, (211, 211, 211), (0, 0, SCREEN_WIDTH, 100))
                pygame.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH * 0.04, 140, flag.get_width() + 35, flag.get_height() + 25))

                if govt_button.draw(screen):
                    game_state = "view government"
                if econ_button.draw(screen):
                    game_state = "view economy"
                if foreign_button.draw(screen):
                    pass
                if social_button.draw(screen):
                    game_state = "view society"


                draw_text(f"{actual_day.date()}", font, text_col, SCREEN_WIDTH * 0.80, 100)
                if slower_button.draw(screen):
                    pass
                if slow_button.draw(screen):
                    pass
                if regular_button.draw(screen):
                    pass
                if fast_button.draw(screen):
                    pass
                if faster_button.draw(screen):
                    pass
                screen.blit(flag, (SCREEN_WIDTH * 0.05, 150))
                screen.blit(leader, (SCREEN_WIDTH * 0.015, 300))
                time.sleep(1.25)
                nation.check_economic_state()
                nation.population_change()
                nation.stability_happiness_change(globe)

                for i in range(len(globe.nations)):
                # will be re-introduced, once figure out how to deal with other nations than one currently playing as
                    if globe.nations[i].name == nation.name:
                        pass
                    else:
                        globe.nations[i].main(globe)

                actual_day += timedelta(days=1)
                upload_database.update_database_info(globe.nations)
                time.sleep(speed)

            elif game_state == "view government":
                """sub section of user nation that displays political information regarding nation"""
                screen.fill((52, 78, 91))
                draw_text(f"Political stats", font, text_col, SCREEN_WIDTH * 0.45, 100)
                draw_text(f"Current Leader: {nation.leader}", font, text_col,
                          (SCREEN_WIDTH * 0.355) - len(nation.leader), 200)
                draw_text(f"Stability: {round(nation.stability, 2)}%", font, text_col, SCREEN_WIDTH * 0.45, 300)
                if back_button.draw(screen):
                    game_state = "game"

            elif game_state == "view economy":
                """sub section of user nation that displays economic information regarding nation"""
                screen.fill((52, 78, 91))
                draw_text(f"Economic stats", font, text_col, SCREEN_WIDTH * 0.45, 100)
                draw_text(f"GDP: ${round(nation.current_gdp, 2)}", font, text_col, SCREEN_WIDTH * 0.405, 200)
                draw_text(f"National Debt: ${round(nation.national_debt, 2)}", font, text_col, SCREEN_WIDTH * 0.405,
                          300)
                draw_text(f"Current Corporate Tax Rate: {nation.corporate_tax_rate}%", font, text_col, SCREEN_WIDTH * 0.325, 400)
                draw_text(f"Current Income Tax Rate: {nation.income_tax_rate}%", font, text_col, SCREEN_WIDTH * 0.345, 500)
                if cor_tax_inc_button.draw(screen):
                    pass
                if cor_tax_dec_button.draw(screen):
                    pass
                if inc_tax_inc_button.draw(screen):
                    pass
                if inc_tax_dec_button.draw(screen):
                    pass
                if back_button.draw(screen):
                    game_state = "game"

            elif game_state == "view society":
                """sub section of user nation that displays social information regarding nation"""
                screen.fill((52, 78, 91))
                draw_text(f"Social stats", font, text_col, SCREEN_WIDTH * 0.45, 100)
                draw_text(f"Population: {nation.population}", font, text_col, SCREEN_WIDTH * 0.405, 200)
                draw_text(f"Happiness: {round(nation.happiness, 2)}%", font, text_col, SCREEN_WIDTH * 0.405,
                          300)
                if back_button.draw(screen):
                    game_state = "game"
            elif game_state == "paused":
                screen.fill((52, 78, 91))
                if cont_button.draw(screen):
                    pass
                if quit_button.draw(screen):
                    pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key == pygame.K_ESCAPE:
                    if game_paused == False:
                        game_paused = True
                    if game_paused == True:
                        game_paused = False
        """event handlers"""

        pygame.display.update()

    pygame.quit()
