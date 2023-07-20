import pygame
import time
import random
import winsound

pygame.init()

tamanho = (800, 600)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
running = True
posicao_x_bolinha = 0
posicao_y_bolinha = 300
velocidade_bolinha = 1
posicao_x_bolinha_red = 400
posicao_y_bolinha_red = 300
moving_red_ball_x = 0
moving_red_ball_y = 0
direita = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            moving_red_ball_x = -5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            moving_red_ball_x = 5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            moving_red_ball_x = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            moving_red_ball_x = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            moving_red_ball_y = -5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            moving_red_ball_y = 5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            moving_red_ball_y = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            moving_red_ball_y = 0

    tela.fill(branco)

    pygame.draw.circle(tela, preto, (posicao_x_bolinha, posicao_y_bolinha), 30)
    
    if posicao_x_bolinha >= 800:
        direita = False
        velocidade_bolinha = velocidade_bolinha + 1
        posicao_y_bolinha = random.randint(0, 600)
        winsound.Beep(500, 300)
    elif posicao_x_bolinha <= 0:
        direita = True
        velocidade_bolinha = velocidade_bolinha + 1
        winsound.Beep(500, 300)
    if direita:
        posicao_x_bolinha = posicao_x_bolinha + velocidade_bolinha
    else:
        posicao_x_bolinha = posicao_x_bolinha - velocidade_bolinha

    if posicao_x_bolinha_red < 0:
        posicao_x_bolinha_red = 0
    elif posicao_x_bolinha_red > 800:
        posicao_x_bolinha_red = 800
    else:
        posicao_x_bolinha_red = posicao_x_bolinha_red + moving_red_ball_x
    
    if posicao_y_bolinha_red < 0:
        posicao_y_bolinha_red = 0
    elif posicao_y_bolinha_red > 600:
        posicao_y_bolinha_red = 600
    else:
        posicao_y_bolinha_red = posicao_y_bolinha_red + moving_red_ball_y
        
    posicao_x_bolinha_red = posicao_x_bolinha_red + moving_red_ball_x
    posicao_y_bolinha_red = posicao_y_bolinha_red + moving_red_ball_y

    pygame.draw.circle(tela, vermelho, (posicao_x_bolinha_red, posicao_y_bolinha_red), 30)



    pygame.display.update()
    clock.tick(60)
pygame.quit()   




    #desenho1: pygame.draw.line(tela, preto, (0, 300), (800, 300), 2)
    #desenho2: pygame.draw.line(tela, preto, (0, 0), (800, 600), 2)
    #desenho3:pygame.draw.line(tela, preto, (200, 200), (400, 400), 2)
    #desenho3:pygame.draw.line(tela, preto, (600, 200), (400, 400), 2)
    #desenho3:pygame.draw.line(tela, preto, (200, 200), (600, 200), 2)
    #desenho4:pygame.draw.line(tela, preto, (0, 300), (800, 300), 2)
    #desenho4:pygame.draw.line(tela, preto, (30, 100), (30, 450), 2)
    #desenho4:pygame.draw.line(tela, preto, (30, 100), (80, 350), 2)