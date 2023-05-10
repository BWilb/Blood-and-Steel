import pygame
import button
import pyautogui

pygame.init()

width = pyautogui.size().width
height = pyautogui.size().height

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome To War")
#game variables
game_paused = False
game_state = "main"
inner_game_menu = "time"

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
img_us = pygame.image.load("region_buttons/north_america/nation_buttons/united_states_button.png")
img_canada = pygame.image.load("region_buttons/north_america/nation_buttons/canada_button.png")
img_mexico = pygame.image.load("region_buttons/north_america/nation_buttons/mexico_button.png")

"""europe"""
img_europe = pygame.image.load("region_buttons/europe/europe_button.png").convert_alpha()
uk = pygame.image.load("region_buttons/europe/nation_buttons/britain_button.png")
germany = pygame.image.load("region_buttons/europe/nation_buttons/germany_button.png")
italy = pygame.image.load("region_buttons/europe/nation_buttons/Italy_button.png")
france = pygame.image.load("region_buttons/europe/nation_buttons/france_button.png")
russia = pygame.image.load("region_buttons/europe/nation_buttons/russia_button.png")

"""africa"""
img_africa = pygame.image.load("region_buttons/africa/africa_button.png").convert_alpha()

"""asia"""
img_asia = pygame.image.load("region_buttons/asia/asia_button.png").convert_alpha()

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
# nation buttons
"""europe"""
europe_button = button.Button(width * 0.20, 400, img_europe, 0.25)
"""africa"""
africa_button = button.Button(width * 0.65, 200, img_africa, 0.25)
"""asia"""
asia_button = button.Button(width * 0.65, 400, img_asia, 0.25)
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
                menu_state = "options"

        elif game_state == "options":
            if video_button.draw(screen):
                print("video settings")
            if audio_button.draw(screen):
                print("audio settings")
            if keys_button.draw(screen):
                # change key bindings
                print("Change key bindings")
            if back_button.draw(screen):
                game_state = "main"

        elif game_state == "start":
            """If statement dealing with """
            start_text = font.render("Choose your time", 1, text_col)
            screen.blit(start_text, ((width / 2) - 260, 60))

            if inner_game_menu == "time":
                if button_1910.draw(screen):
                    inner_game_menu = "region"

                if button_1914.draw(screen):
                    pass

                if button_1918.draw(screen):
                    pass

                if button_1932.draw(screen):
                    pass

                if button_1936.draw(screen):
                    pass

                if button_1939.draw(screen):
                    pass

            if inner_game_menu == "region":
                if na_button.draw(screen):
                    pass

                if europe_button.draw(screen):
                    pass

                if africa_button.draw(screen):
                    pass

                if asia_button.draw(screen):
                    pass

                if sa_button.draw(screen):
                    pass

            if back_button.draw(screen):
                game_state = "main"
    else:
        if resume_button.draw(screen):
            game_paused = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()