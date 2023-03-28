import pygame
# Initialize Pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSPARENT_BLACK = (0, 0, 0, 128)

# Define a function to display the pause screen
def display_pause_screen():
    # Draw a translucent overlay on top of the game screen
    overlay = pygame.Surface((window_width, window_height), pygame.SRCALPHA)
    overlay.fill(TRANSPARENT_BLACK)
    game_window.blit(overlay, (0, 0))

    # Display some text indicating that the game is paused
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Paused", True, WHITE)
    text_rect = text.get_rect(center=(window_width/2, window_height/2 - 50))
    game_window.blit(text, text_rect)

    # Display a "resume" button
    resume_button = pygame.Rect(window_width/2 - 100, window_height/2 + 20, 200, 50)
    pygame.draw.rect(game_window, WHITE, resume_button)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Resume", True, BLACK)
    text_rect = text.get_rect(center=resume_button.center)
    game_window.blit(text, text_rect)

    # Display an "exit" button
    exit_button = pygame.Rect(window_width/2 - 100, window_height/2 + 80, 200, 50)
    pygame.draw.rect(game_window, WHITE, exit_button)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Exit Game", True, BLACK)
    text_rect = text.get_rect(center=exit_button.center)
    game_window.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Wait for the player to click a button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_x,pos_y = pygame.mouse.get_pos()
                if ((300 < pos_x < 500) and (380 < pos_y < 430)) :
                    return True
                if ((300 < pos_x < 500) and (320 < pos_y < 370)):
                    return "level 1"








