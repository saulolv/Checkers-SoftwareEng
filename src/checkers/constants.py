import pygame

WIDTH, HEIGHT = 800, 800

ROWS, COLS = 8, 8

SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0 , 255)
GREEN = (0, 245, 0)
GREY = (128, 128, 128)
GREY31 = (79, 79, 79)
NAVY = (0, 0, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
MENU1_PIC = pygame.transform.scale(pygame.image.load('assets/menu1pic.png'), (WIDTH, HEIGHT))