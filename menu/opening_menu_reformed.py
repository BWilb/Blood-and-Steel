import pygame
from pygame import mixer
import pygame
import button
import time
import pyautogui
from nation_state.north_america.united_states import us_reformed
import nation_state.europe.britain.britain
from nation_state.europe.italy import italy
import nation_state.europe.france.france
import nation_state.europe.russia.russia
from nation_state.europe.germany import germany_reformed
import nation_state.asia.japan.japan

def begin_game(nation, time):
    if nation == "United States":
        national = us_reformed.UnitedStates(time)
        us_reformed.manual_game(national)
        pygame.quit()

pygame.init()
# game is initialized
width = pyautogui.size().width
height = pyautogui.size().height

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome To War")
#game variables
game_paused = False
game_state = "main"
inner_game_state = "time"

# choice variables
time_chosen = ""
nation_chosen = ""

#define font
font = pygame.font.SysFont("arialblack", 60)

#define colour
text_col = (255, 255, 255)

# menu button images
start_img = pygame.image.load("buttons/start_bbutton.png").convert_alpha()
options_img = pygame.image.load("buttons/options_button.png").convert_alpha()
quit_img = pygame.image.load("buttons/quit_button.png").convert_alpha()
video_img = pygame.image.load('buttons/video_settings.png').convert_alpha()
audio_img = pygame.image.load('buttons/audio_settings.png').convert_alpha()
keys_img = pygame.image.load('buttons/key_bindings.png').convert_alpha()
back_img = pygame.image.load('buttons/back_button.png').convert_alpha()
resume_img = pygame.image.load('buttons/resume_button.png').convert_alpha()
yes_img = pygame.image.load('buttons/yes_button.png').convert_alpha()
no_img = pygame.image.load('buttons/no_button.png').convert_alpha()

# time button images
img_1910 = pygame.image.load("time_buttons/1910_button.png").convert_alpha()
img_1914 = pygame.image.load("time_buttons/1914_button.png").convert_alpha()
img_1918 = pygame.image.load("time_buttons/1918_button.png").convert_alpha()
img_1932 = pygame.image.load("time_buttons/1932_button.png").convert_alpha()
img_1936 = pygame.image.load("time_buttons/1936_button.png").convert_alpha()
img_1939 = pygame.image.load("time_buttons/1940_button.png").convert_alpha()

# region images
"""north america"""
img_north_america = pygame.image.load("region_buttons/north_america/north_america_button.png").convert_alpha()
# nation images
img_us = pygame.image.load("region_buttons/north_america/nation_buttons/united_states_button.png").convert_alpha()
img_canada = pygame.image.load("region_buttons/north_america/nation_buttons/canada_button.png").convert_alpha()
img_mexico = pygame.image.load("region_buttons/north_america/nation_buttons/mexico_button.png").convert_alpha()

"""europe"""
img_europe = pygame.image.load("region_buttons/europe/europe_button.png").convert_alpha()
uk = pygame.image.load("region_buttons/europe/nation_buttons/britain_button.png").convert_alpha()
germany = pygame.image.load("region_buttons/europe/nation_buttons/germany_button.png").convert_alpha()
italian = pygame.image.load("region_buttons/europe/nation_buttons/Italy_button.png").convert_alpha()
france = pygame.image.load("region_buttons/europe/nation_buttons/france_button.png").convert_alpha()
russia = pygame.image.load("region_buttons/europe/nation_buttons/russia_button.png").convert_alpha()

"""africa"""
img_africa = pygame.image.load("region_buttons/africa/africa_button.png").convert_alpha()

"""asia"""
img_asia = pygame.image.load("region_buttons/asia/asia_button.png").convert_alpha()
img_japan = pygame.image.load("region_buttons/asia/nation_buttons/japan_button.png").convert_alpha()
img_china = pygame.image.load("region_buttons/asia/nation_buttons/china_button.png").convert_alpha()

"""south america"""
img_south_america = pygame.image.load("region_buttons/south_america/south_america_button.png").convert_alpha()

# menu buttons
start_button = button.Button((width / 2) - 135, 225, start_img, 0.25)
quit_button = button.Button((width / 2) - 135, 525, quit_img, 0.25)
options_button = button.Button((width / 2) - 135, 825, options_img, 0.25)
video_button = button.Button((width / 2) - 125, 50, video_img, 0.25)
audio_button = button.Button((width / 2) - 125, 325, audio_img, 0.25)
keys_button = button.Button((width / 2) - 125, 600, keys_img, 0.25)
back_button = button.Button((width / 2) - 125, 875, back_img, 0.25)
resume_button = button.Button((width / 2) - 125, 125, resume_img, 0.25)
yes_button = button.Button((width / 2) - 600, 875, yes_img, 0.25)
no_button = button.Button((width / 2) + 400, 875, no_img, 0.25)

# time buttons
button_1910 = button.Button(width * 0.20, 200, img_1910, 0.25)
button_1914 = button.Button(width * 0.65, 200, img_1914, 0.25)
button_1918 = button.Button(width * 0.20, 400, img_1918, 0.25)
button_1932 = button.Button(width * 0.65, 400, img_1932, 0.25)
button_1936 = button.Button(width * 0.20, 600, img_1936, 0.25)
button_1939 = button.Button(width * 0.65, 600, img_1939, 0.25)

# region buttons
"""north america"""
na_button = button.Button(width * 0.20, 200, img_north_america, 0.25)
canada_button = button.Button(width * 0.43, 200, img_canada, 0.25)
mexico_button = button.Button(width * 0.43, 400, img_mexico, 0.25)
us_button = button.Button(width * 0.43, 600, img_us, 0.25)

# nation buttons
"""europe"""
europe_button = button.Button(width * 0.65, 200, img_europe, 0.25)
britain_button = button.Button(width * 0.20, 200, uk, 0.25)
german_button = button.Button(width * 0.65, 200, germany, 0.25)
russian_button = button.Button(width * 0.20, 400, russia, 0.25)
italian_button = button.Button(width * 0.65, 400, italian, 0.25)
france_button = button.Button(width * 0.425, 600, france, 0.25)

"""africa"""
africa_button = button.Button(width * 0.65, 400, img_africa, 0.25)

"""asia"""
asia_button = button.Button(width * 0.20, 400, img_asia, 0.25)
japan = button.Button(width * 0.425, 200, img_japan, 0.25)
china = button.Button(width * 0.425, 400, img_china, 0.25)

"""south america"""
sa_button = button.Button(width * 0.425, 600, img_south_america, 0.25)

def draw_text(text, font,text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:

    screen.fill((52, 78, 81))
    # check if game is paused
    if game_paused == False:
        if game_state == "main":

            welcome_text = font.render("Welcome to War", 1, text_col)
            screen.blit(welcome_text, ((width/2) - 260, height / 12))

            if start_button.draw(screen):
                game_state = "start"
            if quit_button.draw(screen):
                run = False
            if options_button.draw(screen):
                game_state = "options"

        if game_state == "options":
            if video_button.draw(screen):
                print("video settings")
            if audio_button.draw(screen):
                print("audio settings")
            if keys_button.draw(screen):
                # change key bindings
                print("Change key bindings")
            if back_button.draw(screen):
                game_state = "main"

        if game_state == "start":
            """If statement dealing with beginning of game"""
            start_text = font.render("Choose your time", 1, text_col)
            screen.blit(start_text, ((width / 2) - 260, 60))

            if inner_game_state == "time" and game_state == "start":
                if button_1910.draw(screen):
                    time_chosen = "1910"
                    game_state = "region"

                if button_1914.draw(screen):
                    time_chosen = "1914"
                    game_state = "region"

                if button_1918.draw(screen):
                    time_chosen = "1918"
                    game_state = "region"

                if button_1932.draw(screen):
                    time_chosen = "1932"
                    game_state = "region"

                if button_1936.draw(screen):
                    time_chosen = "1936"
                    game_state = "region"

                if button_1939.draw(screen):
                    time_chosen = "1939"
                    game_state = "region"

                if back_button.draw(screen):
                    game_state = "main"

        if game_state == "region":
            """Menu switches to regions"""
            region = font.render("Choose your region", 1, text_col)
            screen.blit(region, ((width / 2) - 300, 60))

            if na_button.draw(screen):
                game_state = "na"
            if europe_button.draw(screen):
                game_state = "euro"
            if asia_button.draw(screen):
                game_state = "asia"
            if africa_button.draw(screen):
                game_state = "africa"
            if sa_button.draw(screen):
                game_state = "sa"
            if back_button.draw(screen):
                game_state = "main"

        if game_state == "na":
            """Menu switches to North America"""
            nation = font.render("Choose your nation", 1, text_col)
            screen.blit(nation, ((width / 2) - 300, 60))

            if us_button.draw(screen):
                nation_chosen = "United States"
                game_state = "chosen"
            if canada_button.draw(screen):
                nation_chosen = "Canada"
                game_state = "unavailable"
            if mexico_button.draw(screen):
                nation_chosen = "Mexico"
                game_state = "unavailable"
            if back_button.draw(screen):
                game_state = "main"

        if game_state == "euro":
            """Menu switches to Europe"""
            nation = font.render("Choose your nation", 1, text_col)
            screen.blit(nation, ((width / 2) - 300, 60))
            if britain_button.draw(screen):
                nation_chosen = "Great Britain"
                game_state = "unavailable"

            if russian_button.draw(screen):
                nation_chosen = "Russia"
                game_state = "unavailable"

            if german_button.draw(screen):
                nation_chosen = "Germany"
                game_state = "chosen"

            if italian_button.draw(screen):
                nation_chosen = "Italy"
                game_state = "chosen"

            if france_button.draw(screen):
                nation_chosen = "France"
                game_state = "unavailable"

            if back_button.draw(screen):
                game_state = "region"

        if game_state == "asia":
            nation = font.render("Choose your nation", 1, text_col)
            screen.blit(nation, ((width / 2) - 300, 60))
            if japan.draw(screen):
                nation_chosen = "Japan"
                game_state = "unavailable"
            if china.draw(screen):
                nation_chosen = "China"
                game_state = "unavailable"
            if back_button.draw(screen):
                game_state = "main"

        if game_state == "africa":
            nation = font.render("Nations aren't available yet", 1, text_col)
            screen.blit(nation, ((width / 2) - 425, (height/2) - 100))

            if back_button.draw(screen):
                game_state = "main"

        if game_state == "sa":
            nation = font.render("Nations aren't available yet", 1, text_col)
            screen.blit(nation, ((width / 2) - 425, (height/2) - 100))

            if back_button.draw(screen):
                game_state = "main"

        if game_state == "unavailable":
            nation = font.render(f"{nation_chosen} isn't available yet", 1, text_col)
            screen.blit(nation, ((width / 2) - 425, (height / 2) - 100))

            if back_button.draw(screen):
                game_state = "na"

        if game_state == "chosen":
            chosen = font.render(f"You chose {nation_chosen} in {time_chosen}", 1, text_col)
            screen.blit(chosen, (450, (height / 2) - 300))

            question = font.render(f"Is this correct?", 1, text_col)
            screen.blit(question, ((width / 2) - 235, (height / 2) - 100))

            if yes_button.draw(screen):
                game_state = "yes"
            if no_button.draw(screen):
                game_state = "start"

        if game_state == "yes":

            music = font.render(f"Congrats for choosing {nation_chosen}.", 1, text_col)
            screen.blit(music, ((width / 2) - 600, 60))
            space = font.render(f"Press space bar to continue.", 1, text_col)
            screen.blit(space, ((width / 2) - 460, 160))

    else:
        """pausing the game"""
        if resume_button.draw(screen):
            game_paused = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            """registering key event of pressing space bar"""
            if event.key == pygame.K_SPACE:
                run = False
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
print(nation_chosen)
if nation_chosen == "United States":
    national = us_reformed.UnitedStates(time_chosen)
    us_reformed.manual_game(national)

elif nation_chosen == "Germany":
    national = germany_reformed.Germany(time_chosen)
    germany_reformed.manual_game(national)

elif nation_chosen == "Italy":
    national = italy.Italy(time_chosen)
    italy.manual_game(national)