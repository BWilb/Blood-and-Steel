import sys
import time
from datetime import timedelta
from buttons import button
import pyautogui
import pygame
import os
import networkx as nx

import matplotlib.pyplot as plt
from database_management import upload_database

pygame.init()
pygame.mixer.init()


class SpriteGame:
    def __init__(self, nation, globe):
        self.HEIGHT = pyautogui.size().height * 0.9
        self.WIDTH = pyautogui.size().width
        self.pop_alert = False
        # initial width and height will be 90% size of computer screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # music playlist
        self.music_playlist = []

        # define fonts
        self.font = pygame.font.SysFont("Arial-Black", 40)
        # define colour
        self.text_col = (0, 0, 0)
        pygame.display.set_caption("Main Menu")
        self.is_running = True
        self.game_paused = False
        self.game_state = "main game"
        # while loop constraint; controls entire game
        self.nation = nation
        self.globe = globe
        self.actual_day = self.globe.date
        self.speed = 1.5
        self.flag_button = button.Button(50, 50, pygame.image.load(self.nation.flag), 0.05)
        self.clock = pygame.time.Clock()
        self.nation_map = []
        self.nation_button = None
        self.network = nx.Graph()

    def background_music(self):
        """within function while loop will be established that """
        pygame.mixer.music.load(self.music_playlist[0])
        pygame.mixer.music.play()

    def check_stream(self):
        """checks to see if the current music stream is busy or not
        if the music stream is currently in use pass
        if music stream isn't in use, pop off the first music file and send the next one
        to background_music function
        """
        if pygame.mixer.music.get_busy():
            pass
        else:
            self.music_playlist.pop(0)
            self.background_music()

    def load_music(self):
        # loads background music into game's playlist
        if self.globe.date.year <= 1918:
            folder = "background_music/in_game/pre_1918"
            for song in os.listdir(folder):
                self.music_playlist.append(f"background_music/in_game/pre_1918/{song}")

        elif self.globe.date.year > 1918:
            folder = "background_music/in_game/after_1918"
            for song in os.listdir(folder):
                self.music_playlist.append(f"background_music/in_game/after_1918/{song}")
        self.background_music()

    def draw_text(self, text, font, text_col, x, y):
        """function of opening menu class draws text"""
        # draws the text on screen
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def update_screen(self):
        """updates screen"""
        pygame.display.update()

    def establish_relations(self, nation1, nation2):

        if not self.network.has_node(nation1.name):
            self.network.add_node(nation1.name)
        if not self.network.has_node(nation2.name):
            self.network.add_node(nation2.name)
        if not self.network.has_edge(nation1.name, nation2.name):
            print('hi')
            self.network.add_edge(nation1.name, nation2.name)
            self.nation.improving_relations.append(nation2.name)
            print(self.network)
        if not self.network.has_edge(nation1.name, nation2.name):
            print("no edge")

    def remove_relations(self, nation1, nation2):
        if self.network.has_edge(nation1.name, nation2.name):
            self.network.remove_edge(nation1.name, nation2.name)
            #print(self.network)

        for i in range(0, len(self.nation.improving_relations)):
            if nation2.name == self.nation.improving_relations[i]:
                self.nation.improving_relations.pop(i)

    def establish_nodes(self):
        for i in range(0, len(self.globe.nations)):
            self.network.add_node(self.globe.nations[i].name)


    def loading_buttons(self):
        """loading buttons establishes buttons that will be drawn to screen(enabling user interaction)
        through user interaction of pressing buttons, if nation selected is not nation that user is playing as,
        user will have option of potentially repairing or destroying relations. Network variable will come into play once selected.
        If improving relations involves establishing alliance, edge will be drawn between user nation and AI nation, removed
        once alliance is broken. Network nodes will be nation names, to keep things simple
        """
        for i in range(0, len(self.globe.nations)):
            self.nation_button = button.PolygonButton(self.globe.nations[i].coordinates,
                                                      self.globe.nations[i].nation_color,
                                                      self.globe.nations[i])
            self.nation_map.append(self.nation_button)

    def draw_nations(self):
        """for i in range(0, len(self.globe.nations)):
            #print(self.globe.nations[i].name, self.globe.nations[i].coordinates)
            for coordinates in range(0, len(self.globe.nations[i].coordinates)):

                if len((self.globe.nations[i].coordinates[coordinates])) == 1:

                    pygame.draw.polygon(self.screen, self.globe.nations[i].nation_color,
                                        self.globe.nations[i].coordinates[coordinates])
                else:
                    pygame.draw.polygon(self.screen, self.globe.nations[i].nation_color,
                                        self.globe.nations[i].coordinates[coordinates])"""
        """for i in range(0, len(self.nation_map)):
            for vertice_sets in range(0, len(self.nation_map[i].vertices)):
                pygame.draw.polygon(self.screen,
                                    self.nation_map[i].color,
                                    self.nation_map[i].vertices[vertice_sets])"""
        for i in range(0, len(self.nation_map)):
            self.nation_map[i].draw(self.screen)

            """nx.draw(self.network, pos=self.nation_map[i].nation_info, with_labels=False)"""
            nx.draw(self.network, with_labels=True)
            #plt.show()

    def resize_leader(self, leader_image):
        """function for resizing both leader that will be displayed"""
        return pygame.transform.scale(pygame.image.load(leader_image).convert_alpha(), (250, 350))

    def resize_flag(self):
        """function for resizing both flag that will be displayed"""
        return pygame.transform.scale(pygame.image.load(self.nation.flag).convert_alpha(), (200, 125))

    def view_government(self):
        """sub section of user nation that displays political information regarding nation"""
        self.screen.fill((52, 78, 91))
        self.draw_text(f"Political stats", self.font, self.text_col, self.WIDTH * 0.45, 100)
        self.draw_text(f"Current Leader: {self.nation_selected.leader}", self.font, self.text_col,
                       (self.WIDTH * 0.355) - len(self.nation_selected.leader), 200)
        self.draw_text(f"Stability: {round(self.nation_selected.stability, 2)}%", self.font, self.text_col,
                       self.WIDTH * 0.45,
                       300)
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.15)

        if back_button.draw(self.screen):
            self.game_state = "main game"

    def view_economy(self):
        increment_img = pygame.image.load(
            "buttons/game_buttons/functionality_buttons/increment_sing.jpg").convert_alpha()
        decrement_img = pygame.image.load(
            "buttons/game_buttons/functionality_buttons/decrement_sign.jpg").convert_alpha()
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/sprite_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.25)
        """tax buttons"""
        # corporate taxes
        cor_tax_inc_button = button.Button(self.WIDTH * 0.05, 435, increment_img, 0.025)
        cor_tax_dec_button = button.Button(self.WIDTH * 0.11, 435, decrement_img, 0.025)
        # income taxes
        inc_tax_inc_button = button.Button(self.WIDTH * 0.05, 535, increment_img, 0.025)
        inc_tax_dec_button = button.Button(self.WIDTH * 0.11, 535, decrement_img, 0.025)
        """sub section of user nation that displays economic information regarding nation"""

        # self.screen.blit(self.sprite_background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        # self.draw_text(f"{self.anation_selectedday.date()}", self.font, self.text_col, self.WIDTH * 0.80, 100)

        self.draw_text(f"Economic stats", pygame.font.SysFont("Arial-Black", 30), (255, 255, 255), self.WIDTH * 0.025,
                       50)
        #
        self.draw_text(f"GDP:", pygame.font.SysFont("Arial-Black", 20),
                       (255, 255, 255)
                       , self.WIDTH * 0.075, 150)
        self.draw_text(f"${round(self.nation_selected.current_gdp, 2)}", pygame.font.SysFont("Arial-Black", 20),
                       (255, 255, 255)
                       , self.WIDTH * 0.035, 200)
        self.draw_text(f"National Debt: ", pygame.font.SysFont("Arial-Black", 20),
                       (255, 255, 255), self.WIDTH * 0.055, 250)
        self.draw_text(f"${round(self.nation_selected.national_debt, 2)}", pygame.font.SysFont("Arial-Black", 20),
                       (255, 255, 255),
                       self.WIDTH * 0.045,
                       300)
        self.draw_text(f"Current Corporate Tax Rate",
                       pygame.font.SysFont("Arial-Black", 20), (255, 255, 255),
                       self.WIDTH * 0.015, 350)
        self.draw_text(f"{self.nation_selected.corporate_tax_rate}%",
                       pygame.font.SysFont("Arial-Black", 20), (255, 255, 255),
                       self.WIDTH * 0.07, 400)
        self.draw_text(f"Current Income Tax Rate:",
                       pygame.font.SysFont("Arial-Black", 20), (255, 255, 255),
                       self.WIDTH * 0.015, 450)
        self.draw_text(f"{self.nation_selected.income_tax_rate}%",
                       pygame.font.SysFont("Arial-Black", 20), (255, 255, 255),
                       self.WIDTH * 0.07, 500)
        if cor_tax_inc_button.draw(self.screen):
            self.nation_selected.corporate_tax_rate += 0.5
            time.sleep(0.5)
            """
            these effects will be brought in once the economic structure of every nation has been changed
            self.nation.investment -= 20
            self.nation.government_spending += 35"""

        if cor_tax_dec_button.draw(self.screen):
            self.nation_selected.corporate_tax_rate -= 0.5
            time.sleep(0.5)
            """
            these effects will be brought in once the economic structure of every nation has been changed
            self.nation.investment += 10
            self.nation.government_spending -= 10"""

        if inc_tax_inc_button.draw(self.screen):
            self.nation_selected.income_tax_rate += 0.5
            time.sleep(0.5)

            """self.nation.consumer_spending -= 10
            self.nation.government_spending += 10"""

        if inc_tax_dec_button.draw(self.screen):
            self.nation_selected.income_tax_rate -= 0.5
            time.sleep(0.5)

            """self.nation.consumer_spending += 10
                self.nation.government_spending -= 10"""
        if back_button.draw(self.screen):
            self.game_state = "main game"

    def view_society(self):
        """sub section of user nation that displays social information regarding nation"""
        # self.screen.blit(self.sprite_background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        self.draw_text(f"{self.actual_day.date()}", self.font, self.text_col, self.WIDTH * 0.80, 100)

        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.465, self.HEIGHT * 0.75, back_img, 0.05)
        self.draw_text(f"Social stats", pygame.font.SysFont("Arial-Black", 30),
                       self.text_col, self.WIDTH * 0.1, 100)
        self.draw_text(f"Population:", pygame.font.SysFont("Arial-Black", 20),
                       self.text_col, self.WIDTH * 0.1, 200)

        self.draw_text(f"{self.nation_selected.population}", pygame.font.SysFont("Arial-Black", 20),
                       self.text_col, self.WIDTH * 0.1, 250)

        self.draw_text(f"Happiness: {round(self.nation_selected.happiness, 2)}%",
                       pygame.font.SysFont("Arial-Black", 20),
                       self.text_col, self.WIDTH * 0.1,
                       300)

        self.draw_text(f"{round(self.nation_selected.happiness, 2)}%", pygame.font.SysFont("Arial-Black", 20),
                       self.text_col, self.WIDTH * 0.1,
                       350)
        if back_button.draw(self.screen):
            self.game_state = "main game"

    def nation_changes(self):
        self.nation.check_economic_state()
        self.nation.population_change()
        self.nation.stability_happiness_change(self.globe)
        self.nation.improve_relations()


    def globe_changes(self):
        for i in range(len(self.globe.nations)):
            # will be re-introduced, once figure out how to deal with other nations than one currently playing as
            if self.globe.nations[i].name == self.nation.name:
                pass
            else:
                self.globe.nations[i].main(self.globe)

        upload_database.update_database_info(self.globe.nations)

    def primary_game(self):
        """speed imgs"""
        faster_img = pygame.image.load("buttons/game_buttons/functionality_buttons/faster.jpg").convert_alpha()
        fast_img = pygame.image.load("buttons/game_buttons/functionality_buttons/fast.jpg").convert_alpha()
        regular_img = pygame.image.load("buttons/game_buttons/functionality_buttons/regular_speed.jpg").convert_alpha()
        slow_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slow.jpg").convert_alpha()
        slower_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slower.jpg").convert_alpha()
        """speed buttons"""
        faster_button = button.Button(1720, 150, faster_img, 0.035)
        fast_button = button.Button(1680, 150, fast_img, 0.035)
        regular_button = button.Button(1640, 150, regular_img, 0.035)
        slow_button = button.Button(1600, 150, slow_img, 0.035)
        slower_button = button.Button(1560, 150, slower_img, 0.035)
        """primary screen user sees after opening menu"""

        # later on background will be an actual SVG image of world and not part of the screen
        self.draw_text(f"{self.globe.date}", self.font, self.text_col, self.WIDTH * 0.80, 100)
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

        """if self.flag_button.draw(self.screen):
            self.game_state = "view infographics"
            self.nation_selected = self.nation"""

    def infographics(self):
        govt_img = pygame.image.load("buttons/game_buttons/government_button.jpg").convert_alpha()
        econ_img = pygame.image.load("buttons/game_buttons/economy_buttion.jpg").convert_alpha()
        foreign_img = pygame.image.load("buttons/game_buttons/foreign_button.jpg").convert_alpha()
        social_img = pygame.image.load("buttons/game_buttons/social_button.jpg").convert_alpha()
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(125, 850, back_img, 0.05)

        """stats buttons"""
        govt_button = button.Button(100, 450, govt_img, 0.125)
        econ_button = button.Button(100, 550, econ_img, 0.125)
        foreign_button = button.Button(100, 650, foreign_img, 0.125)
        social_button = button.Button(100, 750, social_img, 0.125)
        """speed imgs"""
        faster_img = pygame.image.load("buttons/game_buttons/functionality_buttons/faster.jpg").convert_alpha()
        fast_img = pygame.image.load("buttons/game_buttons/functionality_buttons/fast.jpg").convert_alpha()
        regular_img = pygame.image.load("buttons/game_buttons/functionality_buttons/regular_speed.jpg").convert_alpha()
        slow_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slow.jpg").convert_alpha()
        slower_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slower.jpg").convert_alpha()
        """speed buttons"""
        faster_button = button.Button(1720, 150, faster_img, 0.035)
        fast_button = button.Button(1680, 150, fast_img, 0.035)
        regular_button = button.Button(1640, 150, regular_img, 0.035)
        slow_button = button.Button(1600, 150, slow_img, 0.035)
        slower_button = button.Button(1560, 150, slower_img, 0.035)
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        # self.draw_text(f"{self.actual_day.date()}", self.font, self.text_col, self.WIDTH * 0.80, 100)
        self.draw_text(f"{self.globe.date}", self.font, self.text_col, self.WIDTH * 0.80, 100)
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

        leader = self.resize_leader(self.nation_selected.leader_image)
        # leader variable set to resizing function that resizes leader image
        self.screen.blit(leader, (50, 0))

        if govt_button.draw(self.screen):
            self.game_state = "view government"
        if econ_button.draw(self.screen):
            self.game_state = "view economy"
        if foreign_button.draw(self.screen):
            pass
        if social_button.draw(self.screen):
            self.game_state = "view society"

        if back_button.draw(self.screen):
            self.game_state = "main game"

    def view_foreign_nation(self):

        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(125, 850, back_img, 0.05)
        """back button established to escape function"""
        improve_relation_img = pygame.image.load("buttons/relations_buttons/improve_relations.jpg").convert_alpha()
        relation_button = button.Button(25, 400, improve_relation_img, 0.20)
        stop_relation_img = pygame.image.load("buttons/relations_buttons/stop.jpg").convert_alpha()
        stop_relations_button = button.Button(25, 400, stop_relation_img, 0.20)
        establish_pact = pygame.image.load("buttons/relations_buttons/establish_pact.jpg").convert_alpha()
        pact_button = button.Button(25, 475, establish_pact, 0.20)
        embargo = pygame.image.load("buttons/relations_buttons/embargo.jpg").convert_alpha()
        embargo_button = button.Button(25, 550, embargo, 0.20)
        worsen = pygame.image.load("buttons/relations_buttons/worsen_relations.jpg").convert_alpha()
        worsen_button = button.Button(25, 625, worsen, 0.20)
        justify = pygame.image.load("buttons/relations_buttons/justify_war.jpg").convert_alpha()
        justify_button = button.Button(25, 700, justify, 0.20)
        """Diplomacy buttons"""
        diplomacy_img = pygame.image.load("buttons/relations_buttons/diplomacy.jpg").convert_alpha()
        diplomacy_button = button.Button(10, 350, diplomacy_img, 0.1)
        details_img = pygame.image.load("buttons/relations_buttons/national_details.jpg").convert_alpha()
        details_button = button.Button(200, 350, details_img, 0.1)

        self.draw_text(f"{self.globe.date}", self.font, self.text_col, self.WIDTH * 0.80, 100)

        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        """Two primary pieces of information on nation; leader and national flag"""
        leader = self.resize_leader(self.nation_selected.leader_image)
        self.screen.blit(leader, (50, 0))

        if diplomacy_button.draw(self.screen):
            pass

        if details_button.draw(self.screen):
            pass

        if not self.nation_selected.name in self.nation.improving_relations:
            if relation_button.draw(self.screen):
                self.establish_relations(self.nation, self.nation_selected)

        else:
            if stop_relations_button.draw(self.screen):
                self.remove_relations(self.nation, self.nation_selected)

        if pact_button.draw(self.screen):
            pass
        if embargo_button.draw(self.screen):
            pass
        if worsen_button.draw(self.screen):
            pass
        if justify_button.draw(self.screen):
            pass

        if back_button.draw(self.screen):
            self.game_state = "main game"

    def main_game(self):
        self.load_music()
        self.nation.sprite = True
        self.loading_buttons()
        self.establish_nodes()
        print(self.network)
        upload_database.initial_upload_to_database(self.globe.nations, self.globe)
        while self.is_running:
            if not self.game_paused:
                self.screen.fill((65, 105, 225))
                """"""
                self.draw_nations()
                """"""
                if self.game_state == "main game":
                    self.primary_game()

                elif self.game_state == "view foreign nation":
                    self.view_foreign_nation()

                elif self.game_state == "view infographics":
                    self.infographics()

                elif self.game_state == "view society":
                    self.view_society()

                elif self.game_state == "view government":
                    self.view_government()

                elif self.game_state == "view economy":
                    self.view_economy()
                self.globe.date += timedelta(days=1)
                self.nation_changes()
                self.globe_changes()
                self.clock.tick(60)
                time.sleep(1.25)
            self.check_stream()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # pushing of space key
                    if event.key == pygame.K_SPACE:
                        if self.game_paused:
                            self.game_paused = False

                        else:
                            self.game_paused = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button clicked
                        mouse_pos = pygame.mouse.get_pos()

                        # Check if the mouse click is inside any of the buttons
                        for button in self.nation_map:
                            if button.is_clicked(mouse_pos):
                                self.nation_selected = button.nation_info
                                if not self.nation_selected.chosen:
                                    self.game_state = "view foreign nation"
                                else:
                                    self.game_state = "view infographics"
                                # Perform further actions with the nation information if needed
                                # Exit the loop after the first button is clicked
                        """received code from ChatGPT
                        IMPROVE FOLLOWING CODE

                        if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button clicked
                        mouse_pos = pygame.mouse.get_pos()
                        for i in range(0, len(self.nation_map)):
                            for vertex in range(0, len(self.nation_map[i].vertices)):
                                if pygame.draw.polygon(self.screen, 
                                self.nation_map[i].color, 
                                self.nation_map[i].vertices[vertex]).collidepoint(mouse_pos):
                                    print(f"Clicked on {self.globe.nations[i]}")
                                    self.nation_selected = self.globe.nations[i]
                                    self.game_state = "view infographics"
                                    # Perform further actions with the nation information
                                    break
                        for buttons in self.nation_map:
                            print(self.mouse_position)
                            if buttons.is_clicked(self.mouse_position):
                                print(buttons)
                                self.nation_selected = buttons.nation_info
                                self.game_state = "view infographics"
                                print(self.nation_selected)
                        """

                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()

            self.update_screen()
        pygame.quit()
