import threading
from nation_state.north_america.mexico import mexico
from nation_state.north_america.canada import canada
import globe
import pygame
import pyautogui
import socket
from pygame.constants import VIDEORESIZE
import button
"""def accept_nation(nation, time):
    if nation == "mexico":
        mexico.main(time)
    elif nation == "canada":
        mexico.main(time)"""
def accept_nation(nation, time):
    from sprite_version import country_sprite
    globe1 = globe.Globe()
    if nation == "mexico":
        mexican = mexico.Mexico(time)
        country_sprite(mexican, globe)
def play_music(mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
music_thread = threading.Thread(target=play_music, args=())
def wait():
    input()
    pygame.mixer.music.stop()

region = ""
region_chosen = ""
time_chosen = ""
nation_chosen = ""

user_choice = input(f"{socket.gethostname()} would you like to play a text adventure game or sprite game?: ")
if user_choice.lower() == "sprite" or user_choice.lower() == "sprite game":

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
    yes_img = pygame.image.load("buttons/yes_button.jpg").convert_alpha()
    no_img = pygame.image.load("buttons/no_button.jpg").convert_alpha()
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
    img_germany = pygame.image.load("buttons/region/europe/germany_button.jpg").convert_alpha()
    img_lux = pygame.image.load("buttons/region/europe/luxembourg_button.jpg").convert_alpha()
    img_belgian = pygame.image.load("buttons/region/europe/belgium_button.jpg").convert_alpha()
    img_albania = pygame.image.load("buttons/region/europe/albania_button.jpg").convert_alpha()
    img_denmark = pygame.image.load("buttons/region/europe/denmark_button.jpg").convert_alpha()
    img_greece = pygame.image.load("buttons/region/europe/greece_button.jpg").convert_alpha()
    img_montenegro = pygame.image.load("buttons/region/europe/montenegro_button.jpg").convert_alpha()
    img_netherlands = pygame.image.load("buttons/region/europe/netherlands_button.jpg").convert_alpha()
    img_norway = pygame.image.load("buttons/region/europe/norway_button.jpg").convert_alpha()
    img_romania = pygame.image.load("buttons/region/europe/romania_button.jpg").convert_alpha()
    img_russia = pygame.image.load("buttons/region/europe/russia_button.jpg").convert_alpha()
    img_sweden = pygame.image.load("buttons/region/europe/sweden_button.jpg").convert_alpha()
    img_swiss = pygame.image.load("buttons/region/europe/swiss_button.jpg").convert_alpha()
    # asia
    img_japan = pygame.image.load("buttons/region/asia/japan_button.jpg").convert_alpha()
    img_china = pygame.image.load("buttons/region/asia/china_button.jpg").convert_alpha()
    img_afghanistan = pygame.image.load("buttons/region/asia/afghanistan_button.jpg").convert_alpha()
    img_turkey = pygame.image.load("buttons/region/asia/turkey_button.jpg").convert_alpha()
    img_iran = pygame.image.load("buttons/region/asia/iran_button.jpg").convert_alpha()
    img_iraq = pygame.image.load("buttons/region/asia/iraq_button.jpg").convert_alpha()
    # buttons
    """basic buttons"""
    start_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.25, start_img, 0.25)
    options_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.5, options_img, 0.25)
    quit_button = button.Button(SCREEN_WIDTH * 0.48, SCREEN_HEIGHT * 0.75, quit_img, 0.25)
    back_button = button.Button(SCREEN_WIDTH * 0.38, 900, back_img, 0.10)
    secondary_quit_button = button.Button(SCREEN_WIDTH * 0.58, 900, secondary_quit, 0.10)
    yes_button = button.Button(SCREEN_WIDTH * 0.365, 800, yes_img, 0.15)
    no_button = button.Button(SCREEN_WIDTH * 0.57, 800, no_img, 0.15)
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
    britain_button = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.20, img_britain, 0.15)
    france_button = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.30, img_france, 0.15)
    spain_button = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.40, img_spain, 0.15)
    austria_button = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.50, img_austria, 0.15)
    bulgaria_button = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.60, img_bulgaria, 0.15)
    germany_button = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.70, img_germany, 0.15)
    luxembourg_button = button.Button(SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.80, img_lux, 0.15)
    belgium_button = button.Button(SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.20, img_belgian, 0.15)
    albania_button = button.Button(SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.30, img_albania, 0.15)
    denmark_button = button.Button(SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.40, img_denmark, 0.15)
    greece_button = button.Button(SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.50, img_greece, 0.15)
    montenegro_button = button.Button(SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.60, img_montenegro, 0.15)
    dutch_button = button.Button(SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.70, img_netherlands, 0.15)
    norway_button = button.Button(SCREEN_WIDTH * 0.35, SCREEN_HEIGHT * 0.80, img_norway, 0.15)
    romania_button = button.Button(SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.20, img_romania, 0.15)
    russia_button = button.Button(SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.30, img_russia, 0.15)
    sweden_button = button.Button(SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.40, img_sweden, 0.15)
    swiss_button = button.Button(SCREEN_WIDTH * 0.55, SCREEN_HEIGHT * 0.50, img_swiss, 0.15)
    # asia
    afghan_button = button.Button(SCREEN_WIDTH * 0.205, SCREEN_HEIGHT * 0.20, img_afghanistan, 0.25)
    china_button = button.Button(SCREEN_WIDTH * 0.205, SCREEN_HEIGHT * 0.40, img_china, 0.25)
    iran_button = button.Button(SCREEN_WIDTH * 0.205, SCREEN_HEIGHT * 0.60, img_iran, 0.25)
    iraq_button = button.Button(SCREEN_WIDTH * 0.625, SCREEN_HEIGHT * 0.60, img_iraq, 0.25)
    japan_button = button.Button(SCREEN_WIDTH * 0.625, SCREEN_HEIGHT * 0.20, img_japan, 0.25)
    turkey_button = button.Button(SCREEN_WIDTH * 0.625, SCREEN_HEIGHT * 0.40, img_turkey, 0.25)
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
                draw_text("Welcome to War and Politics", font, text_col, (SCREEN_WIDTH * 0.385), 100)
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
                    time_chosen = "1910"
                    menu_state = "region"
                if button_1914.draw(screen):
                    time_chosen = "1914"
                    menu_state = "region"
                if button_1918.draw(screen):
                    time_chosen = "1918"
                    menu_state = "region"
                if button_1932.draw(screen):
                    time_chosen = "1932"
                    menu_state = "region"
                if button_1936.draw(screen):
                    time_chosen = "1936"
                    menu_state = "region"
                if button_1939.draw(screen):
                    time_chosen = "1939"
                    menu_state = "region"
                if back_button.draw(screen):
                    menu_state = "main"
                if secondary_quit_button.draw(screen):
                    pygame.quit()

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
                if secondary_quit_button.draw(screen):
                    pygame.quit()

            if menu_state == "nation":
                if region == "na":
                    draw_text("Choose your nation!", font, text_col, SCREEN_WIDTH * 0.375, 100)
                    if us_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "united states"
                    if canada_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "canada"
                    if cuba_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "cuba"
                    if mexico_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "mexico"
                    if back_button.draw(screen):
                        menu_state = "region"
                    if secondary_quit_button.draw(screen):
                        pygame.quit()

                elif region == "africa":
                    if ethiopia_button.draw(screen):
                        pass
                    if back_button.draw(screen):
                        menu_state = "region"
                    if secondary_quit_button.draw(screen):
                        pygame.quit()

                elif region == "europe":
                    draw_text("Choose your nation!", font, text_col, SCREEN_WIDTH * 0.375, 50)
                    if britain_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "great britain"
                    if france_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "france"
                    if spain_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "spain"
                    if austria_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "austria"
                    if bulgaria_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "bulgaria"
                    if germany_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "germany"
                    if luxembourg_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "luxembourg"
                    if belgium_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "belgium"
                    if albania_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "albania"
                    if denmark_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "denmark"
                    if greece_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "greece"
                    if montenegro_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "montenegro"
                    if dutch_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "netherlands"
                    if norway_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "norway"
                    if romania_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "romania"
                    if russia_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "russia"
                    if sweden_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "sweden"
                    if swiss_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "switzerland"

                    if back_button.draw(screen):
                        menu_state = "region"
                    if secondary_quit_button.draw(screen):
                        pygame.quit()

                elif region == "asia":
                    draw_text("Choose your nation!", font, text_col, SCREEN_WIDTH * 0.375, 50)
                    if afghan_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "afghanistan"
                    if china_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "china"
                    if iran_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "iran"
                    if iraq_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "iraq"
                    if japan_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "japan"
                    if turkey_button.draw(screen):
                        menu_state = "chosen"
                        nation_chosen = "turkey"
                    if back_button.draw(screen):
                        menu_state = "region"
                    if secondary_quit_button.draw(screen):
                        pygame.quit()
            if menu_state == "chosen":
                draw_text(f"You have chosen {nation_chosen}", font, text_col, SCREEN_WIDTH * 0.375 - len(nation_chosen), 50)
                draw_text(f"In the year {time_chosen}", font, text_col, SCREEN_WIDTH * 0.425 - len(time_chosen), 100)
                draw_text(f"Do you wish to proceed with your choice?", font, text_col, SCREEN_WIDTH * 0.275, 700)
                if yes_button.draw(screen):
                    pygame.quit()
                    accept_nation(nation_chosen, time_chosen)
                if no_button.draw(screen):
                    menu_state = "region"


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

elif user_choice.lower() == "text adventure game" or user_choice.lower() == "text adventure":
    pass