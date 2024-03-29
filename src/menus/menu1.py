import pygame
import sys
from checkers.constants import *
from checkers.startgame import run_startgame, run_startgame_minimax
from menus.button import Button

def run_menu1(): 
    pygame.init()

    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")

    BG = pygame.image.load("src/assets/Background.png")

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("src/assets/font.ttf", size)

    def play():
        while True:
            run_startgame_minimax()
            pygame.display.update()
        
    def options():
        while True:
            run_startgame()
            pygame.display.update()

    def main_menu():
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("src/assets/Play Rect.png"), pos=(640, 250), 
                                text_input="1 JOGADOR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("src/assets/Options Rect.png"), pos=(640, 400), 
                                text_input="2 JOGADORES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("src/assets/Quit Rect.png"), pos=(640, 550), 
                                text_input="SAIR", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    main_menu()