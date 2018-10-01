import pygame

from settings import Settings
from game_stats import GameStats
import game_functions as gf
from paddles import Paddles
from ball import Ball
from score import Score
from menu import Menu
from button import Button
import time

def run_game():
    pygame.init()

    pnw_settings = Settings()

    screen = pygame.display.set_mode((pnw_settings.screen_width, pnw_settings.screen_height))
    pygame.display.set_caption("Pong No Walls")

    menu = Menu(pnw_settings, screen)
    stats = GameStats(pnw_settings)

    button = Button(pnw_settings, screen, "Start")

    paddles = Paddles(pnw_settings, screen)
    ball = Ball(pnw_settings, screen)

    # Score
    stats = GameStats(pnw_settings)
    sb = Score(pnw_settings, screen, stats)

    while True:
        gf.check_events(pnw_settings, screen, menu, button, stats, sb, ball, paddles)

        if stats.game_active:
            paddles.update()
            ball.update()
            gf.check_ball_collision(pnw_settings, ball, paddles)
            gf.check_oob(pnw_settings, screen, stats, sb, ball)
            gf.update_screen(pnw_settings, screen, menu, button, stats, sb, ball, paddles)
            if not stats.game_active:
                time.sleep(2)
                stats.reset_stats()
        else:
            gf.start_game(stats)



run_game()