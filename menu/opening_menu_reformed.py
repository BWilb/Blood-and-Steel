import pygame

height = 500
width = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Main Menu")

# load button images
start_img = pygame.image.load("start_btn.png").convert_alpha()
exit_img = pygame.image.load("exit_btn.png").convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        pygame.font.init()
        text_font = pygame.font.SysFont("monospace", 40)
        text = text_font.render("Welcome to War", 1, (0, 0, 0))
        action = False
        # get mouse positions
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(text, (225, 50))
        return action


start_button = Button(100, 200, start_img, .5)
exit_button = Button(450, 200, exit_img, .5)

run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw() == True:
        print("hi")
    if exit_button.draw():
        print("exit")
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()