import pygame
from termos import *
from perdeu import perdeu
from menu import main_menu
from jogo import game
from selecao_musica import cardapio

pygame.init()
pygame.font.init()
pygame.mixer.init()

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rhythm Raider')

state = INIT
while state != QUIT:
    if state == INIT:
        state = main_menu(window) 
    if state == MUSICA:
        state = cardapio(window)
    if state[0] == 2:
        state = game(window)
        dados = state
    if dados[0] == 5:
        state = perdeu(window)

pygame.quit() 