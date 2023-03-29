# import pygame
# from קבועים import *
# from game import screen
#
#
# class Player(pygame.sprite.Sprite):
#
#     def __init__(self, pos=(0, 0), size=(200, 200)):
#         super(Player, self).__init__()
#         self.original_image = step1
#         self.image = self.original_image
#         self.rect = self.image.get_rect()
#         self.rect.center = pos
#         self.angle = 0
#
#     def update(self):
#         self.image = pygame.transform.rotate(self.original_image, self.angle)
#         self.angle += 90   # Value will reapeat after 359. This prevents angle to overflow.
#         x, y = self.rect.center  # Save its current center.
#         self.rect = self.image.get_rect()  # Replace old rect with new rect.
#         self.rect.center = (x, y)  # Put the new rect's center at old center.
#
#
# def main2():
#     player = Player(pos=(200, 200))
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 raise SystemExit
#         screen.fill((255, 255, 0))
#         player.update()
#
#         screen.blit(player.image, player.rect)
#         pygame.display.update()

# import time
#
# # initialize the t0 variable, "starting the stopwatch"
# t0 = time.time()
#
# while True:
#   # calculate the time since some reference point (here the Unix Epoch)
#   t1 = time.time()
#
#   # calculate the difference, i.e. the time elapsed
#   dt = t1 - t0
#
#   if dt >= 3:
#     print ("Three seconds reached, resetting timer")
#     t0 = t1
#   else:
#     print ("Time elapsed is", dt, "seconds")
import pygame

pygame.init()

reference_timer = 0
game_ended = True
while True:

    if game_ended:
        reference_timeR = pygame.time.get_ticks()
        # reset game session
        current_time = pygame.time.get_ticks() - reference_timer
      # 60 frames per second)

    print(current_time // 1000)

    if (current_time) > 5:
        game_ended = False
        clock = pygame.time.get_ticks()
        print(clock//1000)