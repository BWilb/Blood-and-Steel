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

"""class PolygonButton:
    def __init__(self, vertices, color, nation_info, screen):
        self.vertices = vertices
        self.color = color
        self.nation_info = nation_info
        self.screen = screen

    def is_clicked(self, mouse_pos):
        return pygame.draw.polygon(self.screen, self.color, self.vertices).collidepoint(mouse_pos)"""
class PolygonButton:
    def __init__(self, vertices, color, nation_info):
        self.vertices = vertices
        self.color = color
        self.nation_info = nation_info

    def draw(self, screen):
        for coord_sets in range(0, len(self.vertices)):
            pygame.draw.polygon(screen, self.color, self.vertices[coord_sets])

    def is_clicked(self, mouse_pos):
        x, y = mouse_pos

        for vertices in self.vertices:
            n = len(vertices)
            inside = False

            p1x, p1y = vertices[0]

            for i in range(1, n + 1):
                p2x, p2y = vertices[i % n]
                #print(p2x, p2y)

                if y > min(p1y, p2y):
                    if y <= max(p1y, p2y):
                        if x <= max(p1x, p2x):
                            if p1y != p2y:
                                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                                if p1x == p2x or x <= xinters:
                                    inside = not inside

                p1x, p1y = p2x, p2y

            if inside:
                return True

        return False
        """Aided by ChatGPT in finding algorithm that could calculate whether or not a mouseclick was within
        a polygon's borders
        
        Prompt: rewrite for polygons with multiple sets of vertices        
        """
