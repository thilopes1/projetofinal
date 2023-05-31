INIT = 0
MUSICA = 1
GAME = 2
GANHOU = 3
QUIT = 4
PERDEU = 5

width = 800
height = 600

fps = 60

branco = (255,255,255)
verde = (0,255,0)
vermelho = (255,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
laranja = (255,122,0)
transparente = (0,0,0,0)

terco = int(width/3)
sexto = int(terco/6)

linha_e_i = (terco, 0)
linha_e_f = (terco, height)

linha_d_i = (2*terco, 0)
linha_d_f = (2*terco, height)

y_teclas = int(height * 15/17)


dicio = {'assets/musicas/anotherlove.mp3':198, 'assets/musicas/innerbloom.mp3':190, 'assets/musicas/eyeofthetiger.mp3':181}

