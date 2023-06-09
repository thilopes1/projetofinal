import pygame
import random
from sprites import *
from termos import *  
from selecao_musica import cardapio

def game(window):
    lista = cardapio(window)

    game = True
    inicio = True

    player_data = {
        'acertos' : 0,
        'erros' : 0,
        'notas' : 0
    }
    combo = 0
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Rhythm Raider')
    window.fill((0,0,0))


    dados_teclas = {
        'verde' : [verde, (terco+sexto , y_teclas), pygame.K_c],
        'vermelho' :[vermelho,(terco + 2 * sexto, y_teclas), pygame.K_v],
        'amarelo' : [amarelo,(terco + sexto*3, y_teclas), pygame.K_b],
        'azul' : [azul,(terco+4*sexto, y_teclas), pygame.K_n],
        'laranja' : [laranja,(terco+5*sexto, y_teclas), pygame.K_m]
    }

    assets = {
        'notas' : {
            'verde' : pygame.image.load('pygame/assets/notas/verde.png').convert_alpha(),
            'vermelho' : pygame.image.load('pygame/assets/notas/vermelho.png').convert_alpha(),
            'amarelo' : pygame.image.load('pygame/assets/notas/amarelo.png').convert_alpha(),
            'azul' : pygame.image.load('pygame/assets/notas/azul.png').convert_alpha(),
            'laranja' : pygame.image.load('pygame/assets/notas/laranja.png').convert_alpha()
        },
        'lifebar' : {
            '5' : pygame.image.load('pygame/assets/vidas/vida.png').convert_alpha(),
            '4' : pygame.image.load('pygame/assets/vidas/vida1.png').convert_alpha(),
            '3' : pygame.image.load('pygame/assets/vidas/vida2.png').convert_alpha(),
            '2' : pygame.image.load('pygame/assets/vidas/vida3.png').convert_alpha(),
            '1' : pygame.image.load('pygame/assets/vidas/vida4.png').convert_alpha(),
            '0' : pygame.image.load('pygame/assets/vidas/vida5.png').convert_alpha()
        }
    }

    todas_as_notas = pygame.sprite.Group()

    atual = 'verde'
    nota = Notes(atual, assets, dados_teclas)
    tecla = Teclas(atual, window, dados_teclas)
    acertos = 0
    vida = 5
    tempo = 0
    segundo = 0
    ta = 0

    pygame.mixer.init()

    pygame.mixer.music.load(lista[1])                   
    pygame.mixer.music.set_volume(1)                     

    font = pygame.font.SysFont(None, 48)
    state = GAME
    while state == GAME:
        
        cenario = pygame.image.load('pygame/imagens/fundo.jpg')
        lifebar = assets['lifebar'][str(vida)]

        if inicio == False: 
            clock.tick(fps)
            segundo = segundo % fps
            if segundo == 0:
                tempo += 1 
            segundo += 1
            
            if tempo != ta:
                ta += 1
                nota = Notes(random.choice(['verde', 'vermelho','amarelo','azul','laranja']),assets, dados_teclas)
                todas_as_notas.add(nota)
                player_data['notas'] +=1    

        else:
            tecla_start = font.render("Aperte uma tecla para começar", True,  (255,255,255)) 


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
                
            if tempo >= dicio[lista[1]]:
                state = GANHOU


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    dados_teclas['verde'][0] = branco
                    cpress = nota.nome == 'verde'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and cpress:
                        player_data['acertos']+=1
                        nota.remove()
                        vida+=1
                    else:
                        player_data['erros'] +=1

                        vida-=1
                
                if event.key == pygame.K_v:
                    dados_teclas['vermelho'][0] = branco
                    vpress = nota.nome == 'vermelho'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and vpress:
                        player_data['acertos']+=1
                        nota.remove()
                        vida+=1
                    else:
                        player_data['erros'] +=1
                        vida-=1
                        
                
                if event.key == pygame.K_b:
                    dados_teclas['amarelo'][0] = branco
                    bpress = nota.nome == 'amarelo'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and bpress:
                        player_data['acertos'] += 1
                        nota.remove()
                        vida+=1      
                    else:
                        player_data['erros'] +=1
                        vida-=1
                        

                if event.key == pygame.K_n:
                    dados_teclas['azul'][0] = branco
                    npress = nota.nome == 'azul'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and npress:
                        player_data['acertos'] +=1
                        nota.remove()
                        
                        vida+=1                    
                    else:
                        player_data['erros'] +=1
                        vida-=1
                        

                if event.key == pygame.K_m:
                    dados_teclas['laranja'][0] = branco
                    mpress = nota.nome  == 'laranja'
                    if nota.rect.y+2*nota.radius>tecla.posi[1]-tecla.radius and nota.rect.y<tecla.posi[1]+tecla.radius and mpress:
                        player_data['acertos']+=1
                        nota.remove()
                        
                        vida+=1
                    else:
                        player_data['erros'] +=1
                        vida-=1
                       
                


            if event.type == pygame.KEYUP:
                if inicio:
                    inicio = False
                    pygame.mixer.music.play()

                if event.key == pygame.K_ESCAPE:
                    exit()


                if event.key == pygame.K_c:
                    dados_teclas['verde'][0] = verde
                    cpress = False

                if event.key == pygame.K_v:
                    dados_teclas['vermelho'][0] = vermelho
                    vpress = False

                if event.key == pygame.K_b:
                    dados_teclas['amarelo'][0] = amarelo
                    bpress = False   

                if event.key == pygame.K_n:
                    dados_teclas['azul'][0] = azul
                    npress = False

                if event.key == pygame.K_m:

                    dados_teclas['laranja'][0] = laranja
                    mpress = False
        if nota.rect.y - 60 == y_teclas-2*tecla.radius+2:
            player_data['erros']+=1
            vida-=1

        if vida > 5:
            vida = 5
        if vida < 0:
            vida = 0
        
        window.blit(cenario,(0,0))
        window.blit(nota.image, nota.rect)
        window.blit(lifebar, (terco-2*sexto, y_teclas))
        todas_as_notas.update()
        if inicio:
            window.blit(tecla_start,(terco-101,height/3))  
        
        tecla.draw()
        for c in dados_teclas:
            tecla = Teclas(c, window, dados_teclas)
            tecla.draw()
            tecla.lines()
        
        if vida == 0:
            state = PERDEU
            pygame.mixer.music.stop()
        
        lista_para_return = [state, player_data]

        pygame.display.update()
        
    return lista_para_return