def view_foreign_events(self):
    """speed imgs"""
    faster_img = pygame.image.load("buttons/game_buttons/functionality_buttons/faster.jpg").convert_alpha()
    fast_img = pygame.image.load("buttons/game_buttons/functionality_buttons/fast.jpg").convert_alpha()
    regular_img = pygame.image.load("buttons/game_buttons/functionality_buttons/regular_speed.jpg").convert_alpha()
    slow_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slow.jpg").convert_alpha()
    slower_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slower.jpg").convert_alpha()
    """speed buttons"""
    faster_button = button.Button(1720, 75, faster_img, 0.035)
    fast_button = button.Button(1680, 75, fast_img, 0.035)
    regular_button = button.Button(1640, 75, regular_img, 0.035)
    slow_button = button.Button(1600, 75, slow_img, 0.035)
    slower_button = button.Button(1560, 75, slower_img, 0.035)
    self.draw_text(f"{self.globe.date.date()}", self.font, self.text_col, self.WIDTH * 0.805, 25)
    pygame.draw.rect(self.screen, (0, 0, 0), ((self.WIDTH / 2) - 200, (self.HEIGHT / 3) - 200, (self.WIDTH / 2) + 200, (self.HEIGHT / 2) + 250))
    if slower_button.draw(self.screen):
        self.speed = 2.75
    if slow_button.draw(self.screen):
        self.speed = 2.25
    if regular_button.draw(self.screen):
        self.speed = 1.75
    if fast_button.draw(self.screen):
        self.speed = 1.25
    if faster_button.draw(self.screen):
        self.speed = 0.75
    y = (self.HEIGHT / 3) - 150
    x = (self.WIDTH / 2) - 175
    for message in range(0, len(self.globe.events['Foreign events'])):
        self.draw_text(f"{self.globe.events['Foreign events'][message]['event']}: {self.globe.events['Foreign events'][message]['date']}", self.font, self.text_col, x, y)
        y += 35
