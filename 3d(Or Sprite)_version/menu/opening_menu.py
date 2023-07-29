import pygame
import pyautogui
import socket
from pygame.constants import VIDEORESIZE
import button

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

# img files
"""basic button images"""
start_img = pygame.image.load("buttons/start_butt.jpg").convert_alpha()
options_img = pygame.image.load("buttons/options_butt.jpg").convert_alpha()
quit_img = pygame.image.load("buttons/quit_butt.jpg").convert_alpha()
"""time button images"""
img_1910 = pygame.image.load("buttons/time/1910_butt.jpg").convert_alpha()
img_1914 = pygame.image.load("buttons/time/1914_butt.jpg").convert_alpha()
img_1918 = pygame.image.load("buttons/time/1918_butt.jpg").convert_alpha()
img_1932 = pygame.image.load("buttons/time/1932_butt.jpg").convert_alpha()
img_1936 = pygame.image.load("buttons/time/1936_butt.jpg").convert_alpha()
img_1939 = pygame.image.load("buttons/time/1939_butt.jpg").convert_alpha()
"""region button images"""
img_asia = pygame.image.load("buttons/region/asia/asia_button.jpg").convert_alpha()
img_africa = pygame.image.load("buttons/region/africa/africa_button.jpg").convert_alpha()
img_na = pygame.image.load("buttons/region/n_a/na_button.jpg").convert_alpha()
img_sa = pygame.image.load("buttons/region/s_a/sa_button.jpg").convert_alpha()
img_europe = pygame.image.load("buttons/region/europe/europe_button.jpg").convert_alpha()

# buttons
"""basic buttons"""
start_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.25, start_img, 0.25)
options_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.5, options_img, 0.25)
quit_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.75, quit_img, 0.25)
"""time buttons"""
button_1910 = button.Button(SCREEN_WIDTH * 0.48, 150, img_1910, 0.20)
button_1914 = button.Button(SCREEN_WIDTH * 0.48, 300, img_1914, 0.20)
button_1918 = button.Button(SCREEN_WIDTH * 0.48, 450, img_1918, 0.20)
button_1932 = button.Button(SCREEN_WIDTH * 0.48, 600, img_1932, 0.20)
button_1936 = button.Button(SCREEN_WIDTH * 0.48, 750, img_1936, 0.20)
button_1939 = button.Button(SCREEN_WIDTH * 0.48, 900, img_1939, 0.20)


def draw_text(text, font, text_col, x, y):
    # draws the text on screen
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


"""host = socket.gethostname()
print(host)"""

run = True
while run:

    screen.fill((52, 78, 91))
    # check if game is paused
    if game_paused == True:
        if menu_state == "main":
            if start_button.draw(screen):
                menu_state = "time"
            elif options_button.draw(screen):
                print("options")
            elif quit_button.draw(screen):
                pygame.quit()

        elif menu_state == "time":
            if button_1910.draw(screen):
                print("1910")
            if button_1914.draw(screen):
                print("1914")
            if button_1918.draw(screen):
                print("1918")

    else:
        draw_text("Press Space to pause", font, text_col, SCREEN_WIDTH * 0.40, SCREEN_HEIGHT * 0.5)

    for event in pygame.event.get():
        if event.type == VIDEORESIZE:
            if not fullscreen:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            # pushing of space key
            if event.key == pygame.K_SPACE:
                if game_paused:
                    game_paused = False
                    time_section = False
                else:
                    game_paused = True
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.QUIT:
            run = False
    """event handlers"""

    pygame.display.update()

pygame.quit()
