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
# buttons
"""stats buttons"""
govt_button = button.Button(SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.15, govt_img, 0.16)
econ_button = button.Button(SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.35, econ_img, 0.16)
foreign_button = button.Button(SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.55, foreign_img, 0.16)
social_button = button.Button(SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.75, social_img, 0.16)
"""paused buttons"""
quit_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.15, quit_img, 0.25)
cont_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.45, cont_img, 0.25)
back_button = button.Button(SCREEN_WIDTH * 0.465, SCREEN_HEIGHT * 0.75, back_img, 0.25)
"""tax buttons"""
tax_inc_button = button.Button(SCREEN_WIDTH * 0.60, 400, increment_img, 0.05)
tax_dec_button = button.Button(SCREEN_WIDTH * 0.60, 450, decrement_img, 0.05)


# draw_text(f"Tax Rate: ${nation.tax_rate}%", font, text_col, SCREEN_WIDTH * 0.85, 200)

def draw_text(text, font, text_col, x, y):
    # draws the text on screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def check_flag(nation):
    return pygame.transform.scale(pygame.image.load(nation.flag).convert_alpha(), (200, 150))

def check_leader(nation):
    return pygame.transform.scale(pygame.image.load(nation.leader_image).convert_alpha(), (350, 400))


def country_sprite(nation, globe):
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
                if govt_button.draw(screen):
                    game_state = "view government"
                if econ_button.draw(screen):
                    game_state = "view economy"
                if foreign_button.draw(screen):
                    pass
                if social_button.draw(screen):
                    game_state = "view society"

                draw_text(f"{actual_day.date()}", font, text_col, SCREEN_WIDTH * 0.785, 50)
                draw_text(f"{nation.name}", font, text_col, (SCREEN_WIDTH * 0.45) - len(nation.name), 50)
                screen.blit(flag, (SCREEN_WIDTH * 0.485, 150))
                screen.blit(leader, (SCREEN_WIDTH * 0.445, 300))
                time.sleep(1.25)
                nation.check_economic_state()
                nation.population_change()
                nation.stability_happiness_change(globe)

                for i in range(len(globe.nations)):
                # will be re-introduced, once figure out how to deal with other nations than one currently playing as
                    if globe.nations[i].name != nation.name:
                        globe.nations[i].main(globe)

                actual_day += timedelta(days=1)
                upload_database.update_database_info(globe.nations)
                time.sleep(1)

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
                draw_text(f"Tax Rate: {nation.tax_rate}%", font, text_col, SCREEN_WIDTH * 0.405, 400)
                if tax_inc_button.draw(screen):
                    """if taxes are increased overall national happiness decreases"""
                    nation.tax_rate += 0.5
                    decrement = round(random.uniform(1.0, 3.0), 2)
                    if nation.happiness - decrement > 5:
                        nation.happiness -= decrement
                if tax_dec_button.draw(screen):
                    """if taxes are increased overall national happiness increases"""
                    nation.tax_rate -= 0.5
                    increment = round(random.uniform(1.0, 3.0), 2)
                    if nation.happiness + increment < 100:
                        nation.happiness += increment
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
