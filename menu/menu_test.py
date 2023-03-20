"""import pygame
import os
import sys
pygame.init()

width = 1500
height = 800
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("War")
fps = 60
timer = pygame.time.Clock()

main_menu = False

def draw_game():
    menu_button = pygame.draw.rect(screen, "silver", [230, 450, 260, 40], 0, 5)


def draw_menu():
    pass

run = True
while run:
    screen.fill("black")
    timer.tick(fps)
    if main_menu:
        draw_menu()
    else:
        draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()"""

from twilio.rest import Client


account_sid = 'AC8cfab00e5f45213672ef125916330613'

auth_token = '3eab7703c24e94b098fbb22b28491068'

client = Client(account_sid, auth_token)

for i in range(0, 14):

    message = client.messages\
        .create(body="Hello Brooke",
                                     from_="+18775226703",
                                     to='+15158083673'
                                     )
print(message.sid)