import pygame


#CONSTANTES
width, height = 800, 800
rows, cols = 8, 8
tam_casa = width//cols
vermelho = (255, 0, 0)
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0 , 255)

#CONSTANTES 2
FPS = 60

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo de Damas')

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()

main()