import pygame
pygame.mixer.init()

def play_music(nation):

    pygame.mixer.music.load(
        "german/Kaiser Wilhelm II.'s speech about WWI. - Address to the German people [TRANSLATED].mp3")

    pygame.mixer.music.play(-1)

    stop = input("please enter something to stop")
    print(stop)

play_music("nation")