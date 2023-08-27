import pygame
import time
import threading
import keyboard

def play_music(mp3):
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()
    if keyboard.read_key() == "space":
        pygame.mixer.music.stop()


def music_play(nation, time):
    pygame.mixer.init()
    global music_thread
    if nation == "great britain":
        music_thread = threading.Thread(target=play_music, args=(
                "music/europe/British National Anthem -God Save The Queen (EN).mp3",))

    if nation == "germany":
        if time < 1918:
            music_thread = threading.Thread(target=play_music, args=(
                    "music/europe/Heil dir im Siegerkranz [Imperial German anthem][+English translation].mp3",))

        if time > 1918 and time < 1933:
            music_thread = threading.Thread(target=play_music, args=(
                    "music/europe/Weimar Republic 1919-1933 rare old vocal version.mp3",))

        if time >= 1933:
            music_thread = threading.Thread(target=play_music, args=(
                    "music/europe/Horst Wessel Lied - National Anthem of Nazi Germany _ Uncensor History montage edit.mp3",))

    if nation == "france":
        music_thread = threading.Thread(target=play_music, args=(
            "music/europe/_La Marseillaise_ - National Anthem of France.mp3",))

    if nation == "russia":
        if time <= 1918:
            music_thread = threading.Thread(target=play_music, args=(
                "music/europe/_Боже, Царя храни!_ - National Anthem of The Russian Empire [1833-1917].mp3",))

        if time >= 1932:
            music_thread = threading.Thread(target=play_music, args=(
                "music/europe/Russia National anthem Russian & English lyrics.mp3",))

    music_thread.start()


#music_play("germany", 1933)
