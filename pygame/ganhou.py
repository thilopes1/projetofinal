import pygame, sys
from termos import * 

pygame.init()

bg = pygame.image.load('pygame/imagens/tela_acerto.jpg')

def ganhou_function(tela1, resultado):
    score =(resultado[1]['acertos']*2 - resultado[1]['erros'])
    valor = '{0:.2f}'.format(score)
    valor = str(valor)
    

    click = False
    state = GANHOU
    clock = pygame.time.Clock()
    while state == GANHOU:
        clock.tick(fps)  
        tela1.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        tela1.blit(bg, (0,0))
        tela1.blit(valor,(506,314))            
              
        mx, my = pygame.mouse.get_pos()
        novamente = pygame.Rect(width/1.11,460,width/14,55)
        exit = pygame.Rect(width/1.11,530,width/14,55)
        if novamente.collidepoint((mx,my)):
            if click:
                state = MUSICA

        if exit.collidepoint((mx,my)):
            if click:
                pygame.quit()

        click = False
        pygame.display.flip()
        pygame.display.update()

    return state
