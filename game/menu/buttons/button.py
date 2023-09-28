import pygame


class Button():
    def __init__(self, x, y, image, scale):
        width = int(image.get_width())
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

class PolygonButton:
    def __init__(self, vertices, color, screen):
        self.vertices = vertices
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, self.vertices)

    def is_hovered(self, mouse_pos):
        return pygame.draw.polygon(self.screen, self.color, self.vertices).collidepoint(mouse_pos)

    """
    Code taken from ChatGPT and worked into what I want it to do
    
    turning multiple pygame polygon into button and storing in list
    import pygame
    import sys
    
    pygame.init()
    
    # Colors
    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)
    
    # Initialize the screen
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Polygon Buttons")
    
    # Define a polygon shape for the buttons
    button1_vertices = [(100, 200), (200, 150), (300, 200), (200, 250)]
    button2_vertices = [(400, 200), (500, 150), (600, 200), (500, 250)]
    button_color = GRAY
    
    class PolygonButton:
        def __init__(self, vertices, color):
            self.vertices = vertices
            self.color = color
    
        def draw(self):
            pygame.draw.polygon(screen, self.color, self.vertices)
    
        def is_hovered(self, mouse_pos):
            return pygame.draw.polygon(screen, self.color, self.vertices).collidepoint(mouse_pos)
    
        # Create a list to store the buttons
        buttons = []
        buttons.append(PolygonButton(button1_vertices, button_color))
        buttons.append(PolygonButton(button2_vertices, button_color))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            screen.fill(WHITE)
            
            mouse_pos = pygame.mouse.get_pos()
        
            for button in buttons:
                if button.is_hovered(mouse_pos):
                    button.color = WHITE
                else:
                    button.color = GRAY
        
                button.draw()
        
            pygame.display.flip()

    """