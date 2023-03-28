import pygame

pygame.init()

window_width = 500
window_height = 500
game_window = pygame.display.set_mode((window_width, window_height))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSPRET_BLACK = (0, 0, 0, 128)


def display_pause_screen():
    overlay = pygame.Surface((window_width, window_height), pygame.SRCALPHA)
    overlay.fill(TRANSPRET_BLACK)
    game_window.blit(overlay, (0, 0))

    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Paused", True, WHITE)
    text_react = text.get_rect(center=(window_width / 2, window_height / 2 - 50))
    game_window.blit(text, text_react)

    # Display a "resume" button
    resume_button = pygame.Rect(window_width / 2 - 100, window_height / 2 + 20, 200, 50)
    pygame.draw.rect(game_window, WHITE, resume_button)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Resume", True, BLACK)
    text_rect = text.get_rect(center=resume_button.center)
    game_window.blit(text, text_rect)

    # Display an "exit" button
    exit_button = pygame.Rect(window_width / 2 - 100, window_height / 2 + 80, 200, 50)
    pygame.draw.rect(game_window, WHITE, exit_button)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Exit Game", True, BLACK)
    text_rect = text.get_rect(center=exit_button.center)
    game_window.blit(text, text_rect)
    pygame.display.flip()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()
                if ((120 < posx < 350) and (330 < posy < 380)):
                    return True

                if ((120 < posx < 350) and (270 < posy < 320)):
                    return "level 1"

            if event.type == pygame.QUIT:
                finish = True
