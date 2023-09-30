"""import pygame

import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse Click Example")
clock = pygame.time.Clock()
class PolygonButton:
    def __init__(self, vertices, color, nation_info):
        self.vertices = vertices
        self.color = color
        self.nation_info = nation_info

    def is_clicked(self, mouse_pos):
        return pygame.draw.polygon(screen, self.color, self.vertices).collidepoint(mouse_pos)
import pygame
pygame.init()

# Set up the display
#screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Polygon Buttons")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a list of lists where each sublist represents the vertices of a polygon
polygon_data = [
    [(100, 100), (200, 100), (200, 200), (100, 200)],  # Nation 1
    [(300, 100), (400, 100), (400, 200), (300, 200)]   # Nation 2
]

# Create a list of colors corresponding to each nation
colors = [(255, 4, 0), (0, 4, 255)]

# Create a list of nation information
nation_info = ["Nation 1 Info", "Nation 2 Info"]

running = True
screen.fill(WHITE)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                mouse_pos = pygame.mouse.get_pos()
                for i, vertices in enumerate(polygon_data):
                    if pygame.draw.polygon(screen, colors[i], vertices).collidepoint(mouse_pos):
                        print(f"Clicked on {nation_info[i]}")
                        # Perform further actions with the nation information
                        break

      # Clear the screen
    pygame.display.flip()

pygame.quit()
"""