import pygame.sysfont
import time

class Menu:

    def __init__(self, pnw_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pnw_settings = pnw_settings

        self.font_color = (1, 1, 1)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_menu()

    def prep_menu(self):
        menu_str = "PONG"
        menu2_str = "AI - NO WALLS"

        self.menu_image = self.font.render(menu_str, True, self.font_color, self.pnw_settings.bg_color)
        self.menu2_image = self.font.render(menu2_str, True, self.font_color, self.pnw_settings.bg_color)

        self.menu_rect = self.menu_image.get_rect()
        self.menu2_rect = self.menu2_image.get_rect()

        self.menu_rect.centerx = self.screen_rect.centerx
        self.menu_rect.centery = self.screen_rect.bottom * 1/10
        self.menu2_rect.centerx = self.screen_rect.centerx
        self.menu2_rect.centery = self.screen_rect.bottom * 1/5

    def draw_menu(self):
        self.screen.blit(self.menu_image, self.menu_rect)
        self.screen.blit(self.menu2_image, self.menu2_rect)

    def draw_winner(self, msg):
        winner_str = msg
        winner2_str = "WINS"

        self.winner_image = self.font.render(winner_str, True, self.font_color, self.pnw_settings.bg_color)
        self.winner2_image = self.font.render(winner2_str, True, self.font_color, self.pnw_settings.bg_color)

        self.winner_rect = self.winner_image.get_rect()
        self.winner2_rect = self.winner2_image.get_rect()

        self.winner_rect.centerx = self.screen_rect.centerx
        self.winner_rect.centery = self.screen_rect.bottom * 1 / 10
        self.winner2_rect.centerx = self.screen_rect.centerx
        self.winner2_rect.centery = self.screen_rect.bottom * 1 / 5
        self.screen.blit(self.winner_image, self.winner_rect)
        self.screen.blit(self.winner2_image, self.winner2_rect)


