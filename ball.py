import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):

    def __init__(self, pnw_settings, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.settings = pnw_settings

        self.image = pygame.image.load_basic('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.pnw_settings = pnw_settings

        self.rect.center = self.screen_rect.center
        self.rect.centerx = self.screen_rect.centerx
        self.xVect = pnw_settings.ballVect[randint(0, 1)]
        self.yVect = pnw_settings.ballVect[randint(0, 1)]

        self.right = True
        self.above = True
        self.below = False
        self.left = False

    def update(self):

        if self.above:
            self.rect.centery -= (self.pnw_settings.ball_speed_factor * self.yVect)
        elif self.below:
            self.rect.centery += (self.pnw_settings.ball_speed_factor * self.yVect)

        if self.right:
            self.rect.centerx += (self.pnw_settings.ball_speed_factor * self.xVect)
        elif self.left:
            self.rect.centerx -= (self.pnw_settings.ball_speed_factor * self.xVect)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ball(self):
        self.rect.center = self.screen_rect.center