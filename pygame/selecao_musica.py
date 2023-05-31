from tkinter import RIGHT
import pygame, sys
from termos import *

bgmusica = pygame.image.load('imagens/musicas.jpeg')


def cardapio(janela):
    click = False
    clock = pygame.time.Clock()
    state = MUSICA
    musica_escolhida = ''

    while state == MUSICA:
        clock.tick(fps)  
        janela.fill((0,0,0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                state = QUIT
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button:
                if evento.button == 1:
                    click = True
        janela.blit(bgmusica, (0,0))

        mx, my = pygame.mouse.get_pos()
        m1 = pygame.Rect(width/12,130,width/2,50)
        m2 = pygame.Rect(width/12,200,width/2.2,50)
        m3 = pygame.Rect(width/12,290,width/1.7,50)

        if m1.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/anotherlove.mp3'
                state = GAME
        if m2.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/innerbloom.mp3'
                state = GAME
        if m3.collidepoint((mx,my)):
            if click:
                musica_escolhida = 'assets/musicas/eyeofthetiger.mp3'
                state = GAME

        pygame.display.flip()
        pygame.display.update()
        click = False
        lista_return = [state,musica_escolhida]

    return lista_return
