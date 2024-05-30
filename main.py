import pygame
import random
pygame.init()
tamanho = (800, 600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Iron Man do Arthur")
branco = (255,255,255)
preto = (0,0,0)
posicaoxpersona = 400
posicaoypersona = 300
movimentoxpersona = 0
movimentoypersona = 0
posicaoxmissel = random.randint(0,800)
posicaoymissel = -240
velocidademissel = 1
iron = pygame.image.load("assets/iron.png")
fundo= pygame.image.load("assets/fundo.png")
missel = pygame.image.load("assets/missile.png")
fonte = pygame.font.SysFont("comicsans", 14)
#misselsound = pygame.mixer.
pygame.mixer.music.play("assets/ironsound.mp3")
pygame.mixer.music.play(-1)


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoxpersona = 5 
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoxpersona = -5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoxpersona = 0 
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoxpersona = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoypersona = -5 
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoypersona = 5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoypersona = 0 
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoypersona = 0
    posicaoypersona = posicaoypersona + movimentoypersona


    posicaoxpersona = posicaoxpersona + movimentoxpersona
    if posicaoxpersona < 0:
        posicaoxpersona = 10
    elif posicaoxpersona >550:
        posicaoxpersona = 540


    if posicaoypersona < 0:
        posicaoypersona = 10
    elif posicaoypersona >473:
        posicaoypersona = 472

    

    

    

    tela.fill(branco)
    tela.blit(fundo, (0,0))
    #pygame.draw.circle(tela, preto, (posicaoxpersona , posicaoypersona), 40, 0)
    tela.blit(iron, (posicaoxpersona, posicaoypersona))
    posicaoymissel = posicaoymissel + velocidademissel
    if posicaoymissel > 600:
        posicaoymissel = -240
        velocidademissel = velocidademissel + 1
        posicaoxmissel = random.randint
    tela.blit(missel, (posicaoxmissel, posicaoymissel))
    texto = fonte.render(str(posicaoxpersona)+"-"+str(posicaoypersona), True, branco)
    tela.blit(texto, (posicaoxpersona -30,posicaoypersona -10))

    
    pygame.display.update()
    

    relogio.tick(60)

                                   