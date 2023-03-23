import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))

image = pygame.image.load('Images//pleyer_2.png')
image = pygame.transform.rotate(image, 90)
img = pygame.transform.scale(image, (10, 10))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(img, (0, 100))
    pygame.display.update()