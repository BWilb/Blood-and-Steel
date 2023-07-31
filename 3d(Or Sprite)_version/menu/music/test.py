import pygame
import time
import threading

def play_music(mp3):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()

def wait():
    input()
    pygame.mixer.music.stop()

#music_thread = threading.Thread(target=play_music, args=("Battotai - Imperial Japanese Army March.mp3"))
input_thread = threading.Thread(target=wait())

play_music("British National Anthem - ＂God Save The Queen＂ (EN).mp3")
input_thread.start()