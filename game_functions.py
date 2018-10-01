import sys
import time

import pygame
from paddles import Paddles

def check_play_button(pnw_settings, screen, menu, button, stats, sb, ball, paddles, mouse_x, mouse_y):
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        start_game(stats)

def check_events(pnw_settings, screen, menu, button, stats, sb, ball, paddles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pnw_settings, screen, menu, button, stats, sb, ball, paddles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pnw_settings, screen, menu, button, stats, sb, ball, paddles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(pnw_settings, screen, menu, button, stats, sb, ball, paddles, mouse_x, mouse_y)

def check_keydown_events(event, pnw_settings, screen, menu, button, stats, sb, ball, paddles):
    if event.key == pygame.K_RIGHT:
        paddles.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddles.moving_left = True
    elif event.key == pygame.K_UP:
        paddles.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddles.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, pnw_settings, screen, menu, button, stats, sb, ball, paddles):
    if event.key == pygame.K_RIGHT:
        paddles.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddles.moving_left = False
    elif event.key == pygame.K_UP:
        paddles.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddles.moving_down = False

def update_screen(pnw_settings, screen, menu, button, stats, sb, ball, paddles):
    screen.fill(pnw_settings.bg_color)
    drawline(screen)

    ball.blitme()
    paddles.blitme()

    sb.show_score()
    if not stats.game_active:
        screen.fill(pnw_settings.bg_color)
        menu.draw_menu()
        button.draw_button()
    if stats.comp_win():
        screen.fill(pnw_settings.bg_color)
        menu.draw_winner("COMPUTER")
        stats.game_active = False

        pygame.mouse.set_visible(True)
    if stats.human_win():
        screen.fill(pnw_settings.bg_color)
        menu.draw_winner("PLAYER")
        stats.game_active = False
        pygame.mouse.set_visible(True)

    pygame.display.flip()

def check_ball_collision(pnw_settings, ball, paddles):
    if ball.rect.colliderect(paddles.humanH1_rect):
        paddles.collision_noise()
        if ball.yVect == 1:
            ball.yVect = -1
        elif ball.yVect == -1:
            ball.yVect = 1
    elif ball.rect.colliderect(paddles.humanH2_rect):
        paddles.collision_noise()
        if ball.yVect == 1:
            ball.yVect = -1
        elif ball.yVect == -1:
            ball.yVect = 1
    elif ball.rect.colliderect(paddles.compH1_rect):
        paddles.collision_noise()
        if ball.yVect == 1:
            ball.yVect = -1
        elif ball.yVect == -1:
            ball.yVect = 1
    elif ball.rect.colliderect(paddles.compH2_rect):
        paddles.collision_noise()
        if ball.yVect == 1:
            ball.yVect = -1
        elif ball.yVect == -1:
            ball.yVect = 1
    elif ball.rect.colliderect(paddles.humanV_rect):
        paddles.collision_noise()
        if ball.xVect == 1:
            ball.xVect == -1
        elif ball.xVect == -1:
            ball.xVect = 1
    elif ball.rect.colliderect(paddles.compV_rect):
        paddles.collision_noise()
        if ball.xVect == 1:
            ball.xVect == -1
        elif ball.xVect == -1:
            ball.xVect = 1

def check_oob(pnw_settings, screen, stats, sb, ball):
    screenRect = screen.get_rect()
    if ball.rect.centerx < screenRect.centerx:
        if ball.rect.centerx < 0:
            stats.human_scores()
            sb.prep_humanscore()
            ball.center_ball()
        elif ball.rect.centery < 0:
            stats.human_scores()
            sb.prep_humanscore()
            ball.center_ball()
        elif ball.rect.centery > screenRect.bottom:
            stats.human_scores()
            sb.prep_humanscore()
            ball.center_ball()
    elif ball.rect.centerx > screenRect.centerx:
        if ball.rect.centerx > screenRect.right:
            stats.comp_scores()
            sb.prep_compscore()
            ball.center_ball()
        elif ball.rect.centery < 0:
            stats.comp_scores()
            sb.prep_compscore()
            ball.center_ball()
        elif ball.rect.centery > screenRect.bottom:
            stats.comp_scores()
            sb.prep_compscore()
            ball.center_ball()


def drawline(screen):
    screen_rect = screen.get_rect()
    pygame.draw.line(screen, (0, 0, 0), (screen_rect.centerx, 0), (screen_rect.centerx, screen_rect.bottom))

def start_game(stats):
    pygame.mouse.set_visible(False)

    stats.reset_stats()
    stats.game_active = True