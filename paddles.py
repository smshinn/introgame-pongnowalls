import pygame

from pygame.sprite import Sprite

class Paddles(Sprite):

    def __init__(self, pnw_settings, screen):
        super().__init__()
        self.screen = screen
        self.pnw_settings = pnw_settings
        self.screen_rect = screen.get_rect()

        # Human Paddles
        self.humanH1_image = pygame.image.load_basic('images/paddle1h.bmp')
        self.humanH1_rect = self.humanH1_image.get_rect()
        self.humanH1_rect.centerx = self.screen_rect.right * (1 / 4)
        self.humanH1_rect.y = 0

        self.humanH1_center = float(self.humanH1_rect.centerx)

        self.humanH2_image = pygame.image.load_basic('images/paddle1h.bmp')
        self.humanH2_rect = self.humanH2_image.get_rect()
        self.humanH2_rect.centerx = self.screen_rect.right * (1 / 4)
        self.humanH2_rect.y = self.screen_rect.bottom - self.humanH2_rect.height

        self.humanH2_center = float(self.humanH2_rect.centerx)

        self.humanV_image = pygame.image.load_basic('images/paddle1v.bmp')
        self.humanV_rect = self.humanV_image.get_rect()
        self.humanV_rect.x = 0
        self.humanV_rect.centery = self.screen_rect.centery

        self.humanV_center = float(self.humanV_rect.centery)

        # Human Paddles Move Values
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # CPU Paddles
        self.compH1_image = pygame.image.load_basic('images/paddle2h.bmp')
        self.compH1_rect = self.compH1_image.get_rect()
        self.compH1_rect.x = self.screen_rect.right * (3 / 4)
        self.compH1_rect.y = 0

        self.compH2_image = pygame.image.load_basic('images/paddle2h.bmp')
        self.compH2_rect = self.compH2_image.get_rect()
        self.compH2_rect.x = self.screen_rect.right * (3 / 4)
        self.compH2_rect.y = self.screen_rect.bottom - self.compH2_rect.height

        self.compV_image = pygame.image.load_basic('images/paddle2v.bmp')
        self.compV_rect = self.compV_image.get_rect()
        self.compV_rect.x = self.screen_rect.right - self.compV_rect.width
        self.compV_rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.humanH1_image, self.humanH1_rect)
        self.screen.blit(self.humanH2_image, self.humanH2_rect)
        self.screen.blit(self.humanV_image, self.humanV_rect)
        self.screen.blit(self.compH1_image, self.compH1_rect)
        self.screen.blit(self.compH2_image, self.compH2_rect)
        self.screen.blit(self.compV_image, self.compV_rect)

    def update(self):

        lefthalf = self.screen_rect.right/2

        if self.moving_right and self.humanH1_rect.right < lefthalf and self.humanH2_rect.right < lefthalf:
            self.humanH1_center += self.pnw_settings.human_paddle_speed
            self.humanH2_center += self.pnw_settings.human_paddle_speed
        if self.moving_left and self.humanH1_rect.left > 0 and self.humanH2_rect.left > 0:
            self.humanH1_center -= self.pnw_settings.human_paddle_speed
            self.humanH2_center -= self.pnw_settings.human_paddle_speed
        if self.moving_up and self.humanV_rect.top > 0:
            self.humanV_center -= self.pnw_settings.human_paddle_speed
        if self.moving_down and self.humanV_rect.bottom < self.screen_rect.bottom:
            self.humanV_center += self.pnw_settings.human_paddle_speed

        self.humanH1_rect.centerx = self.humanH1_center
        self.humanH2_rect.centerx = self.humanH2_center
        self.humanV_rect.centery = self.humanV_center

        """
        self.compH1_rect.centerx = self.compH1_center
        self.compH2_rect.centerx = self.compH2_center
        self.compV_rect.centery = self.compV_center
        """

    def collision_noise(self):
        pygame.mixer.init()
        pygame.mixer.music.load('sounds/boing.wav')
        pygame.mixer.music.play()