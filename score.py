import pygame.sysfont

class Score:

    def __init__(self, pnw_settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pnw_settings = pnw_settings
        self.stats = stats

        self.text_color = (0, 98, 196)
        self.text_color2 = (237, 28, 36)
        self.text_color3 = (1, 1, 1)
        self.font = pygame.sysfont.SysFont(None, 48)
        self.font2 = pygame.sysfont.SysFont(None, 35)

        self.prep_images()

    def prep_images(self):
        self.prep_humanscore()
        self.prep_compscore()
        self.prep_points()

    def prep_humanscore(self):
        rounded_humanscore = self.stats.humanscore
        humanscore_str = "{:,}".format(rounded_humanscore)

        self.humanscore_image = self.font.render(humanscore_str, True, self.text_color, self.pnw_settings.bg_color)

        self.humanscore_rect = self.humanscore_image.get_rect()
        self.humanscore_rect.centerx = self.screen_rect.centerx - self.screen_rect.centerx * (1/10)
        self.humanscore_rect.bottom = self.screen_rect.bottom * (1/10)

    def prep_compscore(self):
        rounded_compscore = self.stats.compscore
        compscore_str = "{:,}".format(rounded_compscore)

        self.compscore_image = self.font.render(compscore_str, True, self.text_color2, self.pnw_settings.bg_color)

        self.compscore_rect = self.compscore_image.get_rect()
        self.compscore_rect.centerx = self.screen_rect.centerx + self.screen_rect.centerx * (1 / 10)
        self.compscore_rect.bottom = self.screen_rect.bottom * (1 / 10)

    def prep_points(self):
        points = int(self.pnw_settings.points)
        points_str = "{:,}".format(points)

        self.points_image = self.font2.render(points_str, True, self.text_color3, self.pnw_settings.bg_color)

        self.points_rect = self.points_image.get_rect()
        self.points_rect.centerx = self.screen_rect.centerx
        self.points_rect.bottom = self.screen_rect.bottom * (1/8)


    def show_score(self):
        self.screen.blit(self.humanscore_image, self.humanscore_rect)
        self.screen.blit(self.compscore_image, self.compscore_rect)
        self.screen.blit(self.points_image, self.points_rect)