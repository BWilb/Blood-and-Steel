import pygame
import threading
import time
import sys
import pyautogui
import socket
import button


def draw_text(text, font, text_col, x, y):
    # draws the text on screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def opening_menu():
    answered = False
    while not answered:
        user_choice = input(f"{socket.gethostname()} would you like to play a text adventure game or sprite game?: ")
        # prompting user to choose between text and sprite
        if user_choice.lower() == "sprite" or user_choice.lower() == "sprite game":
            sprite_menu()

        elif user_choice.lower() == "text adventure game" or user_choice.lower() == "text adventure" \
                or user_choice.lower() == "text":
            text_menu()

        else:
            print(f"\nUser {socket.gethostname()}, enter either text or sprite!!!!\n")
            time.sleep(1.5)

def sprite_menu():
    """function handles most basic functionality of sprite menu"""
    pygame.init()

    SCREEN_WIDTH = pyautogui.size().width
    SCREEN_HEIGHT = pyautogui.size().height * 0.9
    # initial width and height will be 90% size of computer screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    fullscreen = False
    pygame.display.set_caption("Main Menu")
    # game variables
    game_paused = True
    menu_state = "main"

    # define fonts
    font = pygame.font.SysFont("arialblack", 40)
    # define colour
    text_col = (255, 255, 255)

    """basic button images"""
    start_img = pygame.image.load("buttons/opening_menu_buttons/start_butt.jpg").convert_alpha()
    options_img = pygame.image.load("buttons/opening_menu_buttons/options_butt.jpg").convert_alpha()
    quit_img = pygame.image.load("buttons/opening_menu_buttons/quit_butt.jpg").convert_alpha()

    """basic buttons"""
    start_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.25, start_img, 0.25)
    options_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.5, options_img, 0.25)
    quit_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.75, quit_img, 0.25)

    run = True
    while run:
        screen.fill((52, 78, 91))
        # check if game is paused
        if game_paused == True:
            if menu_state == "main":
                draw_text("Welcome to War and Politics", font, text_col, (SCREEN_WIDTH * 0.385), 100)
                if start_button.draw(screen):
                    time_menu(screen)
                elif options_button.draw(screen):
                    print("options")
                elif quit_button.draw(screen):
                    pygame.quit()

def time_menu(screen):
    """structure similar to opening menu"""
    run = True
    menu_state = "time menu"
    if menu_state == "time menu":
        pass

def text_menu():
    """function handles most basic functionality of text menu"""
    pass