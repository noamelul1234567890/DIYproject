import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the timer interval (in milliseconds)
timer_interval = 5000

# Set the initial timer start time
timer_start_time = pygame.time.get_ticks()

# Set the timer event
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, timer_interval)



# Define a function to handle the button click event
def handle_button_click():
    global timer_start_time
    timer_start_time = pygame.time.get_ticks()
    pygame.time.set_timer(timer_event, timer_interval)


# Game loop
running = True
while running:
    print(timer_event)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                handle_button_click()
        elif event.type == timer_event:
            # Timer has expired, do something here
            print("Timer expired!")

    # Get the current time
    current_time = pygame.time.get_ticks()

    # Calculate the elapsed time since the timer started
    elapsed_time = current_time - timer_start_time # = 0

    # Draw the elapsed time on the screen
    font = pygame.font.Font(None, 36)
    text = font.render("Elapsed Time: " + str(elapsed_time), True,
                       (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
