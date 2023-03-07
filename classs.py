from קבועים import *

class wall:

    def __init__(self,wall_x,wall_y,wall_w,wall_h):
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.wall_w = wall_w
        self.wall_h = wall_h

class line_wall:
    def __init__(self,x_start,y_start,x_end,y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end














# import pyga
# import random
#
# class Obstacle:
#     def _init_(self, x, y, speed, width, height):
#         self.x = x
#         self.y = y
#         self.speed = speed
#         self.width = width
#         self.height = height
#         self.image = pygame.Surface((self.width, self.height))
#         self.image.fill((255, 0, 0)) # Fill the obstacle with red color
#         self.direction = 1 # Initial direction is right
#
#     def update(self, dt):
#         # Move the obstacle horizontally
#         self.x += self.speed * self.direction * dt
#
#         # Check if the obstacle has reached the edges of the screen
#         if self.x <= 0:
#             self.direction = 1 # Change direction to right
#         elif self.x >= screen_width - self.width:
#             self.direction = -1 # Change direction to left
#
#     def draw(self, surface):
#         surface.blit(self.image, (self.x, self.y))
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the screen
# screen_width = 640
# screen_height = 480
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Obstacle Example")
#
# # Create an obstacle
# obstacle_width = 50
# obstacle_height = 50
# obstacle_x = 0
# obstacle_y = random.randint(0, screen_height - obstacle_height)
# obstacle_speed = 100 # pixels per second
# obstacle = Obstacle(obstacle_x, obstacle_y, obstacle_speed, obstacle_width, obstacle_height)
#
# # Set up the clock
# clock = pygame.time.Clock()
#
# # Game loop
# while True:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#
#     # Clear the screen
#     screen.fill((255, 255, 255))
#
#     # Update and draw the obstacle
#     dt = clock.tick(60) / 1000.0 # Elapsed time since last update in seconds
#     obstacle.update(dt)
#     obstacle.draw(screen)
#
#     # Update the screen
#     pygame.display.update()



