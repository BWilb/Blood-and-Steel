if event.type == pygame.MOUSEBUTTONDOWN:
    if event.button == 1:  # Left mouse button clicked
        mouse_pos = pygame.mouse.get_pos()
        """for i in range(0, len(self.nation_map)):
            for vertex in range(0, len(self.nation_map[i].vertices)):
                if pygame.draw.polygon(self.screen, self.nation_map[i].color, self.nation_map[i].vertices[vertex]).collidepoint(mouse_pos):
                    print(f"Clicked on {self.globe.nations[i]}")
                    self.nation_selected = self.globe.nations[i]
                    self.game_state = "view infographics"
                    # Perform further actions with the nation information
                    break"""
        for buttons in self.nation_map:
            print(self.mouse_position)
            if buttons.is_clicked(self.mouse_position):
                print(buttons)
                self.nation_selected = buttons.nation_info
                self.game_state = "view infographics"
        print(self.nation_selected)