import pygame
from קבועים import *
from game import screen


class Player(pygame.sprite.Sprite):

    def __init__(self, pos=(0, 0), size=(200, 200)):
        super(Player, self).__init__()
        self.original_image = step1
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = 0

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += 90   # Value will reapeat after 359. This prevents angle to overflow.
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.


def main2():
    player = Player(pos=(200, 200))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
        screen.fill((255, 255, 0))
        player.update()

        screen.blit(player.image, player.rect)
        pygame.display.update()
