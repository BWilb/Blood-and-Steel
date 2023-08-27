import pygame
import pyautogui
import socket
from pygame.constants import VIDEORESIZE
from buttons import button
import accept_nation
import sys
import time
import threading

pygame.init()

# initialization of pygame screen done outside of class
class OpeningMenu:
    def __init__(self):
        self.HEIGHT = pyautogui.size().height * 0.9
        self.WIDTH = pyautogui.size().width
        # initial width and height will be 90% size of computer screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        #pygame.transform.scale(pygame.image.load(nation.flag).convert_alpha(), (200, 125))
        self.flare_background = \
            pygame.transform.scale(pygame.image.load("background_image_files/artillery_flares.jpg").convert_alpha(), (self.WIDTH, self.HEIGHT))
        # define fonts
        self.font = pygame.font.SysFont("arialblack", 40)
        # define colour
        self.text_col = (255, 255, 255)
        pygame.display.set_caption("Main Menu")
        self.is_running = True
        self.game_paused = False
        """constraint on while loop that will control primary function of class"""
        self.menu_state = "main"
        # menu state controls which piece of the menu you are looking at
        self.time_chosen = ""
        self.nation_chosen = ""
        """region chosen variable will aid in primary while loop function
        time and nation chosen variables will aid in kickstarting game
        """

    def draw_text(self, text, font, text_col, x, y):
        """function of opening menu class draws text"""
        # draws the text on screen
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def update_menu(self):
        """updates screen"""
        pygame.display.update()

    def primary_menu(self):
        """welcoming screen"""
        start_img = pygame.image.load("buttons/opening_menu_buttons/start_butt.jpg").convert_alpha()
        options_img = pygame.image.load("buttons/opening_menu_buttons/options_butt.jpg").convert_alpha()
        quit_img = pygame.image.load("buttons/opening_menu_buttons/quit_butt.jpg").convert_alpha()
        start_button = button.Button(self.WIDTH * 0.48, self.HEIGHT * 0.25, start_img, 0.25)
        options_button = button.Button(self.WIDTH * 0.48, self.HEIGHT * 0.5, options_img, 0.25)
        quit_button = button.Button(self.WIDTH * 0.48, self.HEIGHT * 0.75, quit_img, 0.25)
        """Primary images and buttons for main menu of game"""
        self.draw_text("Welcome to War and Politics", self.font, self.text_col, (self.WIDTH * 0.385), 100)
        if start_button.draw(self.screen):
            self.menu_state = "time"
        elif options_button.draw(self.screen):
            self.menu_state = "options"
        elif quit_button.draw(self.screen):
            pygame.quit()

    def time_menu(self):
        """user selects time from this panel of menu"""
        back_img = pygame.image.load("buttons/opening_menu_buttons/back_button.jpg").convert_alpha()
        secondary_quit = pygame.image.load("buttons/opening_menu_buttons/quit_button.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.38, 900, back_img, 0.10)
        secondary_quit_button = button.Button(self.WIDTH * 0.58, 900, secondary_quit, 0.10)
        """time button images"""
        img_1910 = pygame.image.load("buttons/time/1910_butt.jpg").convert_alpha()
        img_1914 = pygame.image.load("buttons/time/1914_butt.jpg").convert_alpha()
        img_1918 = pygame.image.load("buttons/time/1918_butt.jpg").convert_alpha()
        img_1932 = pygame.image.load("buttons/time/1932_butt.jpg").convert_alpha()
        img_1936 = pygame.image.load("buttons/time/1936_butt.jpg").convert_alpha()
        img_1939 = pygame.image.load("buttons/time/1939_butt.jpg").convert_alpha()
        """time buttons"""
        button_1910 = button.Button(self.WIDTH * 0.20, 300, img_1910, 0.25)
        button_1914 = button.Button(self.WIDTH * 0.20, 500, img_1914, 0.25)
        button_1918 = button.Button(self.WIDTH * 0.20, 700, img_1918, 0.25)
        button_1932 = button.Button(self.WIDTH * 0.65, 300, img_1932, 0.25)
        button_1936 = button.Button(self.WIDTH * 0.65, 500, img_1936, 0.25)
        button_1939 = button.Button(self.WIDTH * 0.65, 700, img_1939, 0.25)
        self.draw_text("Choose your timeframe!", self.font, self.text_col, self.WIDTH * 0.375, 100)
        if button_1910.draw(self.screen):
            self.time_chosen = "1910"
            self.menu_state = "region"
        if button_1914.draw(self.screen):
            self.time_chosen = "1914"
            self.menu_state = "region"
        if button_1918.draw(self.screen):
            self.time_chosen = "1918"
            self.menu_state = "region"
        if button_1932.draw(self.screen):
            self.time_chosen = "1932"
            self.menu_state = "region"
        if button_1936.draw(self.screen):
            self.time_chosen = "1936"
            self.menu_state = "region"
        if button_1939.draw(self.screen):
            self.time_chosen = "1939"
            self.menu_state = "region"
        if back_button.draw(self.screen):
            self.menu_state = "main"
        if secondary_quit_button.draw(self.screen):
            pygame.quit()

    def region_menu(self):
        """user selects region from menu panel"""
        back_img = pygame.image.load("buttons/opening_menu_buttons/back_button.jpg").convert_alpha()
        secondary_quit = pygame.image.load("buttons/opening_menu_buttons/quit_button.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.38, 900, back_img, 0.10)
        secondary_quit_button = button.Button(self.WIDTH * 0.58, 900, secondary_quit, 0.10)
        """region button images"""
        img_asia = pygame.image.load("buttons/region/asia/asia_button.jpg").convert_alpha()
        img_africa = pygame.image.load("buttons/region/africa/africa_button.jpg").convert_alpha()
        img_na = pygame.image.load("buttons/region/n_a/na_button.jpg").convert_alpha()
        img_sa = pygame.image.load("buttons/region/s_a/sa_button.jpg").convert_alpha()
        img_europe = pygame.image.load("buttons/region/europe/europe_button.jpg").convert_alpha()
        """region buttons"""
        europe_button = button.Button(self.WIDTH * 0.20, 250, img_europe, 0.25)
        asia_button = button.Button(self.WIDTH * 0.20, 450, img_asia, 0.25)
        na_button = button.Button(self.WIDTH * 0.65, 250, img_na, 0.25)
        sa_button = button.Button(self.WIDTH * 0.65, 450, img_sa, 0.25)
        africa_button = button.Button(self.WIDTH * 0.425, 650, img_africa, 0.25)
        self.draw_text("Choose your region!", self.font, self.text_col, self.WIDTH * 0.375, 100)
        if asia_button.draw(self.screen):
            self.menu_state = "asia"
        if na_button.draw(self.screen):
            self.menu_state = "na"
        if sa_button.draw(self.screen):
            self.menu_state = "sa"
        if europe_button.draw(self.screen):
            self.menu_state = "europe"
        if africa_button.draw(self.screen):
            self.menu_state = "africa"
        if back_button.draw(self.screen):
            self.menu_state = "time"
        if secondary_quit_button.draw(self.screen):
            pygame.quit()

    def asia_menu(self):
        back_img = pygame.image.load("buttons/opening_menu_buttons/back_button.jpg").convert_alpha()
        secondary_quit = pygame.image.load("buttons/opening_menu_buttons/quit_button.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.38, 900, back_img, 0.10)
        secondary_quit_button = button.Button(self.WIDTH * 0.58, 900, secondary_quit, 0.10)
        # asia button images
        img_japan = pygame.image.load("buttons/region/asia/japan_button.jpg").convert_alpha()
        img_china = pygame.image.load("buttons/region/asia/china_button.jpg").convert_alpha()
        img_afghanistan = pygame.image.load("buttons/region/asia/afghanistan_button.jpg").convert_alpha()
        img_turkey = pygame.image.load("buttons/region/asia/turkey_button.jpg").convert_alpha()
        img_iran = pygame.image.load("buttons/region/asia/iran_button.jpg").convert_alpha()
        img_iraq = pygame.image.load("buttons/region/asia/iraq_button.jpg").convert_alpha()
        # asia buttons
        afghan_button = button.Button(self.WIDTH * 0.205, self.HEIGHT * 0.20, img_afghanistan, 0.25)
        china_button = button.Button(self.WIDTH * 0.205, self.HEIGHT * 0.40, img_china, 0.25)
        iran_button = button.Button(self.WIDTH * 0.205, self.HEIGHT * 0.60, img_iran, 0.25)
        iraq_button = button.Button(self.WIDTH * 0.625, self.HEIGHT * 0.60, img_iraq, 0.25)
        japan_button = button.Button(self.WIDTH * 0.625, self.HEIGHT * 0.20, img_japan, 0.25)
        turkey_button = button.Button(self.WIDTH * 0.625, self.HEIGHT * 0.40, img_turkey, 0.25)

        self.draw_text("Choose your nation!", self.font, self.text_col, self.WIDTH * 0.375, 50)
        if afghan_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "afghanistan"
        if china_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "china"
        if iran_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "iran"
        if iraq_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "iraq"
        if japan_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "japan"
        if turkey_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "turkey"
        if back_button.draw(self.screen):
            self.menu_state = "region"
        if secondary_quit_button.draw(self.screen):
            pygame.quit()

    def na_menu(self):
        back_img = pygame.image.load("buttons/opening_menu_buttons/back_button.jpg").convert_alpha()
        secondary_quit = pygame.image.load("buttons/opening_menu_buttons/quit_button.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.38, 900, back_img, 0.10)
        secondary_quit_button = button.Button(self.WIDTH * 0.58, 900, secondary_quit, 0.10)
        # north america
        img_us = pygame.image.load("buttons/region/n_a/us_button.jpg").convert_alpha()
        img_canada = pygame.image.load("buttons/region/n_a/canada_button.jpg").convert_alpha()
        img_mexico = pygame.image.load("buttons/region/n_a/mexico_button.jpg").convert_alpha()
        img_cuba = pygame.image.load("buttons/region/n_a/cuba_button.jpg").convert_alpha()
        # north america
        us_button = button.Button(self.WIDTH * 0.225, 300, img_us, 0.25)
        canada_button = button.Button(self.WIDTH * 0.225, 550, img_canada, 0.25)
        mexico_button = button.Button(self.WIDTH * 0.625, 300, img_mexico, 0.25)
        cuba_button = button.Button(self.WIDTH * 0.625, 550, img_cuba, 0.25)

        self.draw_text("Choose your nation!", self.font, self.text_col, self.WIDTH * 0.375, 100)
        if us_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "united states"
        if canada_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "canada"
        if cuba_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "cuba"
        if mexico_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "mexico"
        if back_button.draw(self.screen):
            self.menu_state = "region"
        if secondary_quit_button.draw(self.screen):
            pygame.quit()

    def europe_menu(self):
        back_img = pygame.image.load("buttons/opening_menu_buttons/back_button.jpg").convert_alpha()
        secondary_quit = pygame.image.load("buttons/opening_menu_buttons/quit_button.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.38, 900, back_img, 0.10)
        secondary_quit_button = button.Button(self.WIDTH * 0.58, 900, secondary_quit, 0.10)
        # europe button images
        img_britain = pygame.image.load("buttons/region/europe/britain_button.jpg").convert_alpha()
        img_france = pygame.image.load("buttons/region/europe/france_button.jpg").convert_alpha()
        img_spain = pygame.image.load("buttons/region/europe/spain_button.jpg").convert_alpha()
        img_austria = pygame.image.load("buttons/region/europe/austria_button.jpg").convert_alpha()
        img_bulgaria = pygame.image.load("buttons/region/europe/bulgaria_button.jpg").convert_alpha()
        img_germany = pygame.image.load("buttons/region/europe/germany_button.jpg").convert_alpha()
        img_lux = pygame.image.load("buttons/region/europe/luxembourg_button.jpg").convert_alpha()
        img_belgian = pygame.image.load("buttons/region/europe/belgium_button.jpg").convert_alpha()
        img_albania = pygame.image.load("buttons/region/europe/albania_button.jpg").convert_alpha()
        img_denmark = pygame.image.load("buttons/region/europe/denmark_button.jpg").convert_alpha()
        img_greece = pygame.image.load("buttons/region/europe/greece_button.jpg").convert_alpha()
        img_montenegro = pygame.image.load("buttons/region/europe/montenegro_button.jpg").convert_alpha()
        img_netherlands = pygame.image.load("buttons/region/europe/netherlands_button.jpg").convert_alpha()
        img_norway = pygame.image.load("buttons/region/europe/norway_button.jpg").convert_alpha()
        img_romania = pygame.image.load("buttons/region/europe/romania_button.jpg").convert_alpha()
        img_russia = pygame.image.load("buttons/region/europe/russia_button.jpg").convert_alpha()
        img_sweden = pygame.image.load("buttons/region/europe/sweden_button.jpg").convert_alpha()
        img_swiss = pygame.image.load("buttons/region/europe/swiss_button.jpg").convert_alpha()
        img_italy = pygame.image.load("buttons/region/europe/italy_button.jpg").convert_alpha()
        # europe buttons
        britain_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.20, img_britain, 0.15)
        france_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.30, img_france, 0.15)
        spain_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.40, img_spain, 0.15)
        austria_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.50, img_austria, 0.15)
        bulgaria_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.60, img_bulgaria, 0.15)
        germany_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.70, img_germany, 0.15)
        luxembourg_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.80, img_lux, 0.15)
        belgium_button = button.Button(self.WIDTH * 0.35, self.HEIGHT * 0.20, img_belgian, 0.15)
        albania_button = button.Button(self.WIDTH * 0.35, self.HEIGHT * 0.30, img_albania, 0.15)
        denmark_button = button.Button(self.WIDTH * 0.35, self.HEIGHT * 0.40, img_denmark, 0.15)
        greece_button = button.Button(self.WIDTH * 0.35, self.HEIGHT * 0.50, img_greece, 0.15)
        montenegro_button = button.Button(self.WIDTH * 0.35, self.HEIGHT * 0.60, img_montenegro, 0.15)
        dutch_button = button.Button(self.WIDTH * 0.35, self.HEIGHT * 0.70, img_netherlands, 0.15)
        norway_button = button.Button(self.WIDTH * 0.35, self.HEIGHT * 0.80, img_norway, 0.15)
        romania_button = button.Button(self.WIDTH * 0.55, self.HEIGHT * 0.20, img_romania, 0.15)
        russia_button = button.Button(self.WIDTH * 0.55, self.HEIGHT * 0.30, img_russia, 0.15)
        sweden_button = button.Button(self.WIDTH * 0.55, self.HEIGHT * 0.40, img_sweden, 0.15)
        swiss_button = button.Button(self.WIDTH * 0.55, self.HEIGHT * 0.50, img_swiss, 0.15)
        italy_button = button.Button(self.WIDTH * 0.55, self.HEIGHT * 0.60, img_italy, 0.15)

        self.draw_text("Choose your nation!", self.font, self.text_col, self.WIDTH * 0.375, 50)
        if britain_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "great britain"
        if france_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "france"
        if spain_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "spain"
        if austria_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "austria"
        if bulgaria_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "bulgaria"
        if germany_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "germany"
        if luxembourg_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "luxembourg"
        if belgium_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "belgium"
        if albania_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "albania"
        if denmark_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "denmark"
        if greece_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "greece"
        if montenegro_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "montenegro"
        if dutch_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "netherlands"
        if norway_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "norway"
        if romania_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "romania"
        if russia_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "russia"
        if sweden_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "sweden"
        if swiss_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "switzerland"

        if italy_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "italy"

        if back_button.draw(self.screen):
            self.menu_state = "region"
        if secondary_quit_button.draw(self.screen):
            pygame.quit()

    def sa_menu(self):
        back_img = pygame.image.load("buttons/opening_menu_buttons/back_button.jpg").convert_alpha()
        secondary_quit = pygame.image.load("buttons/opening_menu_buttons/quit_button.jpg").convert_alpha()
        back_button = button.Button(self.WIDTH * 0.38, 900, back_img, 0.10)
        secondary_quit_button = button.Button(self.WIDTH * 0.58, 900, secondary_quit, 0.10)
        # south american button images
        img_brazil = pygame.image.load("buttons/region/s_a/brazil_button.jpg").convert_alpha()
        img_argentina = pygame.image.load("buttons/region/s_a/argentina_button.jpg").convert_alpha()

        # south american buttons
        brazil_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.20, img_brazil, 0.15)
        argentine_button = button.Button(self.WIDTH * 0.15, self.HEIGHT * 0.30, img_argentina, 0.15)


        self.draw_text("Choose your nation!", self.font, self.text_col, self.WIDTH * 0.375, 50)
        if brazil_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "brazil"

        if argentine_button.draw(self.screen):
            self.menu_state = "chosen"
            self.nation_chosen = "argentina"

        if back_button.draw(self.screen):
            self.menu_state = "region"
        if secondary_quit_button.draw(self.screen):
            pygame.quit()

    def chosen(self):
        yes_img = pygame.image.load("buttons/opening_menu_buttons/yes_button.jpg").convert_alpha()
        no_img = pygame.image.load("buttons/opening_menu_buttons/no_button.jpg").convert_alpha()
        yes_button = button.Button(self.WIDTH * 0.365, 800, yes_img, 0.15)
        no_button = button.Button(self.WIDTH * 0.57, 800, no_img, 0.15)
        self.draw_text(f"You have chosen {self.nation_chosen}", self.font, self.text_col,
                  self.WIDTH * 0.375 - len(self.nation_chosen), 50)
        self.draw_text(f"In the year {self.time_chosen}", self.font, self.text_col, self.WIDTH * 0.425 - len(self.time_chosen),
                  100)
        self.draw_text(f"Do you wish to proceed with your choice?", self.font, self.text_col, self.WIDTH * 0.275, 700)

        if yes_button.draw(self.screen):
            #self.yes_selection(self.nation_chosen, self.time_chosen)
            pygame.quit()
            accept_nation.accept_nation(self.nation_chosen, self.time_chosen)
        if no_button.draw(self.screen):
            self.menu_state = "region"

    def yes_selection(self, nation, time_chosen):
        from music_player import music_play
        music_play(nation, int(time_chosen))

    def background_music(self):
        if not pygame.mixer.init():
            pass
    def main_menu(self):
        """main menu that controls user process of navigating main menu"""
        pygame.mixer.init()
        pygame.mixer.music.load("background_music/[Hoi 4] The Great War Main theme.mp3")
        pygame.mixer.music.play(-1)
        print("hi")
        self.is_running = True
        while self.is_running:
            if not self.game_paused:
                opening = threading.Thread(target=self.primary_menu, args=())
                timing = threading.Thread(target=self.time_menu, args=())
                regional = threading.Thread(target=self.region_menu, args=())
                american = threading.Thread(target=self.na_menu, args=())
                asian = threading.Thread(target=self.asia_menu, args=())
                european = threading.Thread(target=self.europe_menu, args=())
                chose = threading.Thread(target=self.chosen, args=())

                self.screen.fill((0, 0, 0))
                self.screen.blit(self.flare_background, (0, 0))
                # sets background image
                self.background_music()

                if self.menu_state == "main":
                    self.primary_menu()

                elif self.menu_state == "time":
                    self.time_menu()

                elif self.menu_state == "region":
                    self.region_menu()

                elif self.menu_state == "na":
                    self.na_menu()

                elif self.menu_state == "europe":
                    self.europe_menu()

                elif self.menu_state == "asia":
                    self.asia_menu()

                elif self.menu_state == "sa":
                    self.sa_menu()

                elif self.menu_state == "chosen":
                    self.chosen()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # pushing of space key
                    if event.key == pygame.K_SPACE:
                        if self.game_paused:
                            self.game_paused = False

                        else:
                            self.game_paused = True

                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()

            self.update_menu()
        pygame.quit()

menu = OpeningMenu()
menu.main_menu()
