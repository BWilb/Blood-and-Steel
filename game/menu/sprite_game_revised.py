import sys
import time
from datetime import timedelta
from buttons import button
import pyautogui
import pygame
import os
import networkx as nx
from military.soldier import Soldier
import matplotlib.pyplot as plt
from database_management import upload_database
"""import matplotlib.pyplot as plt
from database_management import upload_database"""

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
        self.flag_img = pygame.image.load(self.nation.flag).convert_alpha()
        self.flag_button = button.Button((self.WIDTH / 2) + 15,
                                         self.HEIGHT * 0.85, pygame.transform.scale(self.flag_img, (350, 250)), 0.35)
        self.clock = pygame.time.Clock()
        self.nation_map = []
        self.nation_button = None
        self.network = nx.Graph()
        self.coordinates = []

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
            self.network.add_edge(nation1.name, nation2.name)
            self.nation.improving_relations.append(nation2.name)
            #print(self.network)

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
        for i in range(0, len(self.nation_map)):
            self.nation_map[i].draw(self.screen)

    def resize_leader(self, leader_image):
        """function for resizing both leader that will be displayed"""
        return pygame.transform.scale(pygame.image.load(leader_image).convert_alpha(), (250, 350))

    def resize_flag(self):
        """function for resizing both flag that will be displayed"""
        return pygame.transform.scale(pygame.image.load(self.nation.flag).convert_alpha(), (200, 125))

    def view_government(self):
        """sub section of user nation that displays political information regarding nation"""
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(125, 850, back_img, 0.05)
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        leader = self.resize_leader(self.nation.leader_image)
        # leader variable set to resizing function that resizes leader image
        self.screen.blit(leader, (50, 0))
        self.draw_text("Political Stats", pygame.font.SysFont("Arial-Black", 20), (255, 255, 255), self.WIDTH * 0.05, 400)

        if back_button.draw(self.screen):
            self.game_state = "view infographics"

    def view_economy(self):
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(125, 850, back_img, 0.05)
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        leader = self.resize_leader(self.nation.leader_image)
        # leader variable set to resizing function that resizes leader image
        self.screen.blit(leader, (50, 0))
        self.draw_text("Economic Stats", pygame.font.SysFont("Arial-Black", 20), (255, 255, 255), self.WIDTH * 0.05, 375)
        self.draw_text(f"National GDP: ${self.nation.current_gdp}", pygame.font.SysFont("Arial-Black", 20), (255, 255, 255), self.WIDTH * 0.01, 425)
        self.draw_text(f"National Debt: ${round(self.nation.national_debt, 2)}", pygame.font.SysFont("Arial-Black", 20), (255, 255, 255), self.WIDTH * 0.01, 475)

        if back_button.draw(self.screen):
            self.game_state = "view infographics"

    def view_society(self):
        #self.draw_text(f"{self.globe.date.date()}", self.font, self.text_col, self.WIDTH * 0.805, 25)
        """sub section of user nation that displays social information regarding nation"""
        # self.screen.blit(self.sprite_background, (0, 0))
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(125, 850, back_img, 0.05)
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        leader = self.resize_leader(self.nation.leader_image)
        # leader variable set to resizing function that resizes leader image
        self.screen.blit(leader, (50, 0))
        self.draw_text("Social Stats", pygame.font.SysFont("Arial-Black", 20), (255, 255, 255), self.WIDTH * 0.05, 400)

        if back_button.draw(self.screen):
            self.game_state = "view infographics"

    def nation_changes(self):
        self.nation.check_economic_state(self.globe)
        self.nation.check_population_growth(self.globe)
        self.nation.stability_happiness_change(self.globe)
        #self.nation.improve_relations()

    def globe_changes(self):
        for i in range(len(self.globe.nations)):
            # will be re-introduced, once figure out how to deal with other nations than one currently playing as
            if self.globe.nations[i].name == self.nation.name:
                pass
            else:
                self.globe.nations[i].main(self.globe, self.network, self.nation)
                """print(self.network)

                print(self.globe.nations[i].name, (self.globe.nations[i].military['military']['Army']['Figures']['Cost']))"""

        upload_database.update_database_info(self.globe.nations)

    def foreign_interactions(self):
        for nation_agent in self.globe.nations:
            nation_agent.determine_diplomatic_approach(self.globe.nations, self.globe, self.network)

    def primary_game(self):
        """global event img & button"""
        glob_event_img = pygame.image.load("buttons/events/check.jpg").convert_alpha()
        globe_event_button = button.Button((self.WIDTH / 2) - 50, 50, glob_event_img, 0.50)
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
        # self.draw_text(f"{self.actual_day.date()}", self.font, self.text_col, self.WIDTH * 0.80, 100)
        """Date Functionality"""
        self.draw_text(f"{self.globe.date.date()}", self.font, self.text_col, self.WIDTH * 0.805, 25)
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

        if globe_event_button.draw(self.screen):
            self.game_state = "view events"
        if self.flag_button.draw(self.screen):
            self.game_state = "view infographics"
        print(self.network)
        nx.draw_circular(self.network, with_labels= True)
        plt.show()

    def view_foreign_events(self):
        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(125, 850, back_img, 0.05)
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

        """Date functionality"""
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((self.WIDTH / 3) - 200, (self.HEIGHT / 3) - 200, (self.WIDTH / 2) + 200, (self.HEIGHT / 2) + 250))
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
            self.draw_text(f"{self.globe.events['Foreign events'][message]['event']}: {self.globe.events['Foreign events'][message]['date']}",
                           pygame.font.SysFont("Arial-Black", 10), (255, 255, 255), x, y)
            y += 35

        if back_button.draw(self.screen):
            self.game_state = 'main game'

    """following functions deal with viewing nation info, both with
        user controlled nation and AI controlled nations
    """

    def infographics(self):
        """Infographic buttons"""
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
        faster_button = button.Button(1720, 75, faster_img, 0.035)
        fast_button = button.Button(1680, 75, fast_img, 0.035)
        regular_button = button.Button(1640, 75, regular_img, 0.035)
        slow_button = button.Button(1600, 75, slow_img, 0.035)
        slower_button = button.Button(1560, 75, slower_img, 0.035)
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))

        """Date functionality"""
        self.draw_text(f"{self.globe.date.date()}", self.font, self.text_col, self.WIDTH * 0.805, 25)
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

        leader = self.resize_leader(self.nation.leader_image)
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

        if self.flag_button.draw(self.screen):
            if self.game_state == "view infographics":
                self.game_state = "main game"

        if back_button.draw(self.screen):
            self.game_state = "main game"

    def finding_pos_foreign_nations(self):
        nations = []
        for nation in self.nation_selected.improving_relations:
            for foreign_nation in self.nation_selected.foreign_relations['foreign relations']:
                if nation['nation name'] == foreign_nation['nation'].name:
                    nations.append(foreign_nation['nation'].flag)
        return nations

    def finding_neg_foreign_relations(self):
        nations = []
        for nation in self.nation_selected.worsening_relations:
            for foreign_nation in self.nation_selected.foreign_relations['foreign relations']:
                if nation['nation name'] == foreign_nation['nation'].name:
                    nations.append(foreign_nation['nation'].flag)

        return nations

    def finding_guarantees(self):
        nations = []
        for nation in self.nation_selected.foreign_relations['foreign relations']:
            if nation['guaranteeing independence']:
                nations.append(nation['nation'].flag)

        return nations

    def finding_embargoes(self):
        nations = []
        for nation in self.nation_selected.foreign_relations['foreign relations']:
            if nation['embargoed']:
                nations.append(nation['nation'].flag)
        #print(nations)

        return nations

    def view_foreign_nation_info(self):
        font = pygame.font.SysFont("Arial-Black", 15)
        diplomacy_img = pygame.image.load("buttons/relations_buttons/diplomacy.jpg").convert_alpha()
        diplomacy_button = button.Button(10, 350, diplomacy_img, 0.1)
        details_img = pygame.image.load("buttons/relations_buttons/national_details.jpg").convert_alpha()
        details_button = button.Button(200, 350, details_img, 0.1)
        """Time images and buttons"""
        faster_img = pygame.image.load("buttons/game_buttons/functionality_buttons/faster.jpg").convert_alpha()
        fast_img = pygame.image.load("buttons/game_buttons/functionality_buttons/fast.jpg").convert_alpha()
        regular_img = pygame.image.load("buttons/game_buttons/functionality_buttons/regular_speed.jpg").convert_alpha()
        slow_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slow.jpg").convert_alpha()
        slower_img = pygame.image.load("buttons/game_buttons/functionality_buttons/slower.jpg").convert_alpha()
        faster_button = button.Button(1720, 75, faster_img, 0.035)
        fast_button = button.Button(1680, 75, fast_img, 0.035)
        regular_button = button.Button(1640, 75, regular_img, 0.035)
        slow_button = button.Button(1600, 75, slow_img, 0.035)
        slower_button = button.Button(1560, 75, slower_img, 0.035)
        """Date functionality"""
        self.draw_text(f"{self.globe.date.date()}", self.font, self.text_col, self.WIDTH * 0.805, 25)
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

        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 350, self.HEIGHT))
        leader = self.resize_leader(self.nation_selected.leader_image)
        self.screen.blit(leader, (50, 0))
        self.draw_text(f"Government Stats", font, (255, 255, 255), 100, 400)
        self.draw_text(f"Ideology: {self.nation_selected.political_typology}", font, (255, 255, 255), 100, 450)
        self.draw_text(f"Army size: {len(self.nation_selected.military['military']['Army']['Figures']['Army size'])}", font,
                       (255, 255, 255), 75, 475)

        self.draw_text('Economic stats', font, (255, 255, 255), 115, 525)
        self.draw_text(f'Gross Domestic Product: ${self.nation_selected.current_gdp}', font, (255, 255, 255), 20, 550)
        self.draw_text(f'National Debt: ${self.nation_selected.national_debt}', font, (255, 255, 255), 75, 575)

        self.draw_text('Social stats', font, (255, 255, 255), 125, 625)
        self.draw_text(f'Population: {self.nation_selected.population}', font, (255, 255, 255), 75, 650)

        if diplomacy_button.draw(self.screen):
            self.game_state = "view foreign nation"

        if details_button.draw(self.screen):
            pass

        if self.flag_button.draw(self.screen):
            pass

    def view_foreign_nation_diplomacy(self):
        #print(self.nation_selected.flag)
        improving_relations = self.finding_pos_foreign_nations()
        worsening_relations = self.finding_neg_foreign_relations()
        guaranteeing = self.finding_guarantees()
        embargoing = self.finding_embargoes()

        back_img = pygame.image.load("buttons/game_buttons/functionality_buttons/info_back.jpg").convert_alpha()
        back_button = button.Button(125, 900, back_img, 0.05)
        """back button established to escape function"""
        """relation images and buttons for foreign nations"""
        improve_relation_img = pygame.image.load("buttons/relations_buttons/improve_relations.jpg").convert_alpha()
        relation_button = button.Button(25, 400, improve_relation_img, 0.20)
        worsen = pygame.image.load("buttons/relations_buttons/worsen_relations.jpg").convert_alpha()
        worsen_button = button.Button(25, 500, worsen, 0.20)
        stop_worsening_relation = pygame.image.load("buttons/relations_buttons/stop_worsening.png").convert_alpha()
        stop_worsening_relation = pygame.transform.scale(stop_worsening_relation, (230, 50))
        stop_worsen_button = button.Button(25, 500, stop_worsening_relation, 1.25)
        stop_relation_img = pygame.image.load("buttons/relations_buttons/stop.jpg").convert_alpha()
        stop_relations_button = button.Button(25, 400, stop_relation_img, 0.20)
        establish_pact = pygame.image.load("buttons/relations_buttons/establish_pact.jpg").convert_alpha()
        pact_button = button.Button(25, 600, establish_pact, 0.20)
        embargo_img = pygame.image.load("buttons/relations_buttons/embargo.jpg").convert_alpha()
        embargo_button = button.Button(25, 700, embargo_img, 0.20)
        stop_embargo_img = pygame.image.load("buttons/relations_buttons/remove_embargo.png").convert_alpha()
        stop_embargo_img = pygame.transform.scale(stop_embargo_img, (230, 50))
        stop_em_button = button.Button(25, 700, stop_embargo_img, 1.25)
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
            self.game_state = "view foreign nation stats"

        if not self.nation_selected.name in self.nation.improving_relations:
            if relation_button.draw(self.screen):
                self.nation.add_improve_relations(self.network, self.nation_selected)

        else:
            if stop_relations_button.draw(self.screen):
                self.nation.remove_improving_relations(self.network, self.nation_selected)

        x = 15
        for flag in improving_relations:
            flag_img = pygame.image.load(flag).convert_alpha()
            flag_img = pygame.transform.scale(flag_img, (50, 50))
            flag_button = button.Button(x, 465, flag_img, 0.40)
            flag_button.draw(self.screen)
            x += 40

        if not self.nation_selected.name in self.nation.worsening_relations:
            if worsen_button.draw(self.screen):
                self.nation.add_worsening_relations(self.network, self.nation_selected)

        else:
            if stop_worsen_button.draw(self.screen):
                self.nation.remove_worsening_relations(self.network, self.nation_selected)
        x = 15
        for flag in worsening_relations:
            flag_img = pygame.image.load(flag).convert_alpha()
            flag_img = pygame.transform.scale(flag_img, (50, 50))
            flag_button = button.Button(x, 575, flag_img, 0.40)
            flag_button.draw(self.screen)
            x += 40

        if pact_button.draw(self.screen):
            pass

        x = 15
        for flag in guaranteeing:
            flag_img = pygame.image.load(flag).convert_alpha()
            flag_img = pygame.transform.scale(flag_img, (50, 50))
            flag_button = button.Button(x, 675, flag_img, 0.40)
            flag_button.draw(self.screen)
            x += 40

        for foreign_nation in self.nation.foreign_relations['foreign relations']:
            if foreign_nation['nation'].name == self.nation_selected.name:
                if not foreign_nation['embargoed']:
                    if embargo_button.draw(self.screen):
                        self.nation.add_embargo(self.network, self.nation_selected)
                else:
                    if stop_em_button.draw(self.screen):
                        self.nation.remove_embargo(self.network, self.nation_selected)
        x = 15
        #print(embargoing)
        for flag in embargoing:
            flag_img = pygame.image.load(flag).convert_alpha()
            flag_img = pygame.transform.scale(flag_img, (50, 50))
            flag_button = button.Button(x, 775, flag_img, 0.40)
            flag_button.draw(self.screen)
            x += 40
        """
        if justify_button.draw(self.screen):
            pass"""
        if self.flag_button.draw(self.screen):
            pass

        if back_button.draw(self.screen):
            self.game_state = "main game"

    def main_game(self):
        self.load_music()
        self.nation.sprite = True
        self.loading_buttons()
        self.establish_nodes()
        upload_database.initial_upload_to_database(self.globe.nations, self.globe)
        while self.is_running:
            if not self.game_paused:
                self.screen.fill((65, 105, 225))
                """"""
                self.draw_nations()
                """"""
                if self.game_state == "main game":
                    self.primary_game()

                elif self.game_state == "view events":
                    self.view_foreign_events()

                elif self.game_state == "view foreign nation":
                    self.view_foreign_nation_diplomacy()

                elif self.game_state == "view foreign nation stats":
                    self.view_foreign_nation_info()

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
                time.sleep(self.speed)
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
                                if not self.nation_selected.is_chosen:
                                    self.game_state = "view foreign nation"
                                else:
                                    self.game_state = "view infographics"
                                # Perform further actions with the nation information if needed
                                # Exit the loop after the first button is clicked
                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()

            self.update_screen()
        pygame.quit()