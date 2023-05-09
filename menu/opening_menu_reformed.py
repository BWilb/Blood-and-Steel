import pygame
import button
import pyautogui

pygame.init()

width = pyautogui.size().width
height = pyautogui.size().height

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Welcome To War")
#game variables
game_paused = True
menu_state = "main"

#define font
font = pygame.font.SysFont("arialblack", 60)

#define colour
text_col = (255, 255, 255)

# load button images
start_img = pygame.image.load("buttons/start_bbutton.png").convert_alpha()
options_img = pygame.image.load("buttons/options_button.png").convert_alpha()
quit_img = pygame.image.load("buttons/quit_button.png").convert_alpha()
video_img = pygame.image.load('buttons/video_settings.png').convert_alpha()
audio_img = pygame.image.load('buttons/audio_settings.png').convert_alpha()
keys_img = pygame.image.load('buttons/key_bindings.png').convert_alpha()
back_img = pygame.image.load('buttons/back_button.png').convert_alpha()
resume_img = pygame.image.load('buttons/resume_button.png').convert_alpha()

# create instances
start_button = button.Button((width / 2) - 135, 225, start_img, 0.25)
quit_button = button.Button((width / 2) - 135, 525, quit_img, 0.25)
options_button = button.Button((width / 2) - 135, 825, options_img, 0.25)
video_button = button.Button((width / 2) - 125, 50, video_img, 0.25)
audio_button = button.Button((width / 2) - 125, 325, audio_img, 0.25)
keys_button = button.Button((width / 2) - 125, 600, keys_img, 0.25)
back_button = button.Button((width / 2) - 125, 875, back_img, 0.25)
resume_button = button.Button((width / 2) - 125, 125, resume_img, 0.25)

def draw_text(text, font,text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:
    screen.fill((52, 78, 81))
    # check if game is paused
    if game_paused == True:
        if menu_state == "main":
            welcome_text = font.render("Welcome to War", 1, text_col)
            screen.blit(welcome_text, ((width/2) - 260, height / 12))
            if start_button.draw(screen):
                pass
            if quit_button.draw(screen):
                run = False
            if options_button.draw(screen):
                menu_state = "options"
        elif menu_state == "options":
            if video_button.draw(screen):
                print("video settings")
            if audio_button.draw(screen):
                print("audio settings")
            if keys_button.draw(screen):
                print("Change key bindings")
            if back_button.draw(screen):
                menu_state = "main"
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