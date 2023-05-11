import pygame

def play_music():
    pygame.mixer.init()

    pygame.mixer.music.load("germany.mp3")

    pygame.mixer.music.play(-1)

    stop = input("please enter something to stop")
    print(stop)

play_music()