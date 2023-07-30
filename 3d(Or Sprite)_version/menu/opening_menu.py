import pygame
import pyautogui
import socket
from pygame.constants import VIDEORESIZE
import button

region = ""

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
back_img = pygame.image.load("buttons/back_button.jpg").convert_alpha()
secondary_quit = pygame.image.load("buttons/quit_button.jpg").convert_alpha()
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
"""nation button images"""
# north america
img_us = pygame.image.load("buttons/region/n_a/us_button.jpg").convert_alpha()
img_canada = pygame.image.load("buttons/region/n_a/canada_button.jpg").convert_alpha()
img_mexico = pygame.image.load("buttons/region/n_a/mexico_button.jpg").convert_alpha()
img_cuba = pygame.image.load("buttons/region/n_a/cuba_button.jpg").convert_alpha()
# africa
img_ethiopia = pygame.image.load("buttons/region/africa/ethiopia_button.jpg").convert_alpha()
# europe
img_britain = pygame.image.load("buttons/region/europe/britain_button.jpg").convert_alpha()
img_france = pygame.image.load("buttons/region/europe/france_button.jpg").convert_alpha()
img_spain = pygame.image.load("buttons/region/europe/spain_button.jpg").convert_alpha()
img_austria = pygame.image.load("buttons/region/europe/austria_button.jpg").convert_alpha()
img_bulgaria = pygame.image.load("buttons/region/europe/bulgaria_button.jpg").convert_alpha()

# buttons
"""basic buttons"""
start_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.25, start_img, 0.25)
options_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.5, options_img, 0.25)
quit_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.75, quit_img, 0.25)
back_button = button.Button(SCREEN_WIDTH * 0.38, 900, back_img, 0.10)
secondary_quit_button = button.Button(SCREEN_WIDTH * 0.58, 900, secondary_quit, 0.10)
"""time buttons"""
button_1910 = button.Button(SCREEN_WIDTH * 0.20, 300, img_1910, 0.25)
button_1914 = button.Button(SCREEN_WIDTH * 0.20, 500, img_1914, 0.25)
button_1918 = button.Button(SCREEN_WIDTH * 0.20, 700, img_1918, 0.25)
button_1932 = button.Button(SCREEN_WIDTH * 0.65, 300, img_1932, 0.25)
button_1936 = button.Button(SCREEN_WIDTH * 0.65, 500, img_1936, 0.25)
button_1939 = button.Button(SCREEN_WIDTH * 0.65, 700, img_1939, 0.25)
"""region buttons"""
europe_button = button.Button(SCREEN_WIDTH * 0.20, 250, img_europe, 0.25)
asia_button = button.Button(SCREEN_WIDTH * 0.20, 450, img_asia, 0.25)
na_button = button.Button(SCREEN_WIDTH * 0.65, 250, img_na, 0.25)
sa_button = button.Button(SCREEN_WIDTH * 0.65, 450, img_sa, 0.25)
africa_button = button.Button(SCREEN_WIDTH * 0.425, 650, img_africa, 0.25)
"""nation buttons"""
# north america
us_button = button.Button(SCREEN_WIDTH * 0.225, 300, img_us, 0.25)
canada_button = button.Button(SCREEN_WIDTH * 0.225, 550, img_canada, 0.25)
mexico_button = button.Button(SCREEN_WIDTH * 0.625, 300, img_mexico, 0.25)
cuba_button = button.Button(SCREEN_WIDTH * 0.625, 550, img_cuba, 0.25)
# africa
ethiopia_button = button.Button(SCREEN_WIDTH * 0.45, SCREEN_HEIGHT * 0.45, img_ethiopia, 0.25)
# europe
britain_button = button.Button(SCREEN_WIDTH * 0.20, SCREEN_WIDTH * 0.20, img_britain, 0.15)
france_button = button.Button(SCREEN_WIDTH * 0.20, SCREEN_WIDTH * 0.25, img_france, 0.15)
spain_button = button.Button(SCREEN_WIDTH * 0.20, SCREEN_WIDTH * 0.30, img_spain, 0.15)
austria_button = button.Button(SCREEN_WIDTH * 0.20, SCREEN_WIDTH * 0.35, img_austria, 0.15)
bulgaria_button = button.Button(SCREEN_WIDTH * 0.20, SCREEN_WIDTH * 0.40, img_bulgaria, 0.15)
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

        if menu_state == "time":
            """changing menu to allow user to select time placement they want"""
            draw_text("Choose your timeframe!", font, text_col, SCREEN_WIDTH * 0.375, 100)
            if button_1910.draw(screen):
                menu_state = "region"
            if button_1914.draw(screen):
                menu_state = "region"
            if button_1918.draw(screen):
                menu_state = "region"
            if button_1932.draw(screen):
                menu_state = "region"
            if button_1936.draw(screen):
                menu_state = "region"
            if button_1939.draw(screen):
                menu_state = "region"
            if back_button.draw(screen):
                menu_state = "main"

        if menu_state == "region":
            """changing menu to allow user to select region they want
            region variable will store selected region to display nations of that region
            """
            draw_text("Choose your region!", font, text_col, SCREEN_WIDTH * 0.375, 100)
            if asia_button.draw(screen):
                print("asia")
                region = "asia"
                menu_state = "nation"
            if na_button.draw(screen):
                print("na")
                region = "na"
                menu_state = "nation"
            if sa_button.draw(screen):
                print("sa")
                region = "sa"
                menu_state = "nation"
            if europe_button.draw(screen):
                print("europe")
                region = "europe"
                menu_state = "nation"
            if africa_button.draw(screen):
                print("africa")
                region = "africa"
                menu_state = "nation"
            if back_button.draw(screen):
                menu_state = "time"

        if menu_state == "nation":
            if region == "na":
                draw_text("Choose your nation!", font, text_col, SCREEN_WIDTH * 0.375, 100)
                if us_button.draw(screen):
                    pass
                if canada_button.draw(screen):
                    pass
                if cuba_button.draw(screen):
                    pass
                if mexico_button.draw(screen):
                    pass
                if back_button.draw(screen):
                    menu_state = "region"
                if secondary_quit_button.draw(screen):
                    pygame.quit()

            elif region == "africa":
                if ethiopia_button.draw(screen):
                    pass

            elif region == "europe":
                if britain_button.draw(screen):
                    pass
                if france_button.draw(screen):
                    pass
                if spain_button.draw(screen):
                    pass
                if austria_button.draw(screen):
                    pass
                if bulgaria_button.draw(screen):
                    pass

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
