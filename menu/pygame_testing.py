import pygame
pygame.mixer.init()

def play_music(nation):

    pygame.mixer.music.load(
        "music/europe/＂Preußens Gloria＂ march with prussian flag[⏎1892–1918] @NationalPrideFlags.mp3")

    pygame.mixer.music.play(-1)

    stop = input("please enter something to stop")
    print(stop)

play_music("nation")