from קבועים import *
import pygame

class wall:

    def __init__(self,wall_x,wall_y,wall_w,wall_h):
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.wall_w = wall_w
        self.wall_h = wall_h
class Obstacle:
    def __init__(self, x, y, speed, width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0)) # Fill the obstacle with red color
        self.direction = 1 # Initial direction is right

    def update(self, dt):
        # Move the obstacle horizontally
        self.x += self.speed * self.direction * dt

        # Check if the obstacle has reached the edges of the screen
        if self.x <= 0:
            self.direction = 1 # Change direction to right
        elif self.x >= 60 :
            self.direction = -1 # Change direction to left

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))



