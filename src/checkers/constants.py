import pygame

width, height = 800, 800

rows, cols = 8, 8

square_size = width//cols

# rgb
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0 , 255)
green = (0, 245, 0)
grey = (128, 128, 128)
grey31 = (79, 79, 79)
navy = (0, 0, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))