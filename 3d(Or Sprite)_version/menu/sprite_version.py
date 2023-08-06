import threading
import time

from nation_state.north_america.mexico import mexico
from nation_state.north_america.canada import canada
import pygame
import pyautogui
import socket
from pygame.constants import VIDEORESIZE
import button

pygame.init()

def draw_text(text, font, text_col, x, y):
    # draws the text on screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
paused = True

SCREEN_WIDTH = pyautogui.size().width
SCREEN_HEIGHT = pyautogui.size().height * 0.9
# initial width and height will be 90% size of computer screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("War and Politics")

# define fonts
font = pygame.font.SysFont("arialblack", 40)
# define colour
text_col = (255, 255, 255)

"""start_img = pygame.image.load("buttons/start_butt.jpg").convert_alpha()
options_img = pygame.image.load("buttons/options_butt.jpg").convert_alpha()
quit_img = pygame.image.load("buttons/quit_butt.jpg").convert_alpha()

start_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.25, start_img, 0.25)
options_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.5, options_img, 0.25)
quit_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.75, quit_img, 0.25)"""

"""while paused:
    draw_text("Welcome to War and Politics", font, text_col, (SCREEN_WIDTH * 0.385), 100)
    if start_button.draw(screen):
        menu_state = "time"
    elif options_button.draw(screen):
        print("options")
    elif quit_button.draw(screen):
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # pushing of space key
            if event.key == pygame.K_SPACE:
                if paused:
                    paused = False
                    time_section = False
                else:
                    paused = True
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.QUIT:
            run = False
    event handlers

    pygame.display.update()

pygame.quit()"""
def country_sprite(nation, globe):
    while nation.is_intact:
        print("hi")
        time.sleep(1.25)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # pushing of space key
                if event.key == pygame.K_SPACE:
                    pygame.quit()

            if event.type == pygame.QUIT:
                run = False
        """event handlers"""

        pygame.display.update()

    pygame.quit()
