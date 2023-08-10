import sys
import time
from datetime import datetime, timedelta

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
quit_img = pygame.image.load("buttons/quit_butt.jpg").convert_alpha()
cont_img = pygame.image.load("buttons/continue_button.jpg").convert_alpha()
main_menu_img = pygame.image.load("buttons/continue_button.jpg").convert_alpha()
# buttons
"""stats buttons"""
govt_button = button.Button(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.25, govt_img, 0.15)
econ_button = button.Button(SCREEN_WIDTH * 0.45, SCREEN_HEIGHT * 0.25, econ_img, 0.15)
foreign_button = button.Button(SCREEN_WIDTH * 0.65, SCREEN_HEIGHT * 0.25, foreign_img, 0.15)
social_button = button.Button(SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.25, social_img, 0.15)
"""paused buttons"""
quit_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.15, quit_img, 0.25)
cont_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.30, cont_img, 0.25)
main_menu_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.45, main_menu_img, 0.25)


def draw_text(text, font, text_col, x, y):
    # draws the text on screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def country_sprite(nation, globe):
    game_state = "game"
    run = True
    actual_day = nation.date
    """two primary constraints on game"""
    print("hi")
    while run:
        print("hi")
        screen.fill((52, 78, 91))

        draw_text(f"{actual_day}", font, text_col, SCREEN_WIDTH * 0.685, 100)
        actual_day += timedelta(days=1)
        draw_text(f"{nation.name}", font, text_col, SCREEN_WIDTH * 0.15, 100)
        """draw_text(f"Internal stats", font, text_col, SCREEN_WIDTH * 0.10, 100)
        draw_text(f"Population: {nation.population}", font, text_col, SCREEN_WIDTH * 0.05, 200)
        draw_text(f"Happiness: {round(nation.happiness, 2)}", font, text_col, SCREEN_WIDTH * 0.05,
                  300)
        draw_text(f"GDP: {round(nation.current_gdp, 2)}", font, text_col, SCREEN_WIDTH * 0.05, 400)
        draw_text(f"Stability: {round(nation.stability, 2)}", font, text_col, SCREEN_WIDTH * 0.05, 500)
        # drawing of global tension
        draw_text(f"Global tension", font, text_col, SCREEN_WIDTH * 0.715, 200)
        draw_text(f"{globe.tension}%", font, text_col, SCREEN_WIDTH * 0.785, 300)"""
        time.sleep(1.25)
        nation.check_economic_state()
        nation.population_change()
        nation.stability_happiness_change(globe)

        pop_change = ((nation.births - nation.deaths) / ((nation.births + nation.deaths) / 2)) * 100
        if pop_change < 3.45:
            not_answered = False
            while not_answered:
                pass

    if game_state == "paused":
        if quit_button.draw(screen):
            pygame.quit()
            sys.exit()

        if cont_button.draw(screen):
            game_state = "game"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.K_SPACE:
                    if game_state == "game":
                        game_state = "paused"
                    elif game_state == "paused":
                        game_state = "game"

        pygame.display.update()

    pygame.quit()
