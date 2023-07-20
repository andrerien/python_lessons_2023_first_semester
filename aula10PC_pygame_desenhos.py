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

    #desenho1: pygame.draw.line(tela, preto, (0, 300), (800, 300), 2)
    #desenho2: pygame.draw.line(tela, preto, (0, 0), (800, 600), 2)
    #desenho3:pygame.draw.line(tela, preto, (200, 200), (400, 400), 2)
    #desenho3:pygame.draw.line(tela, preto, (600, 200), (400, 400), 2)
    #desenho3:pygame.draw.line(tela, preto, (200, 200), (600, 200), 2)
    #desenho4:pygame.draw.line(tela, preto, (0, 300), (800, 300), 2)
    #desenho4:pygame.draw.line(tela, preto, (30, 100), (30, 450), 2)
    #desenho4:pygame.draw.line(tela, preto, (30, 100), (80, 350), 2)
    #desenho4:pygame.draw.line(tela, preto, (80, 350), (120, 140), 2)
    #desenho4:pygame.draw.line(tela, preto, (120, 140), (145, 430), 2)
    #desenho4:pygame.draw.line(tela, preto, (145, 430), (280, 90), 2)
    #desenho4:pygame.draw.line(tela, preto, (280, 90), (500, 400), 2)
    #desenho5:pygame.draw.line(tela, preto, (0, 600), (800, 0), 2)
    #desenho5:pygame.draw.circle(tela, preto, (400, 300), 100)
    #desenho5:pygame.draw.circle(tela, branco, (400, 300), 98)
    #desenho6:pygame.draw.line(tela, preto, (120, 120), (250, 500), 2)
    #desenho6:pygame.draw.line(tela, preto, (250, 500), (450, 350), 2)
    #desenho6:pygame.draw.line(tela, preto, (450, 300), (650, 300), 2)
    #desenho6:pygame.draw.circle(tela, preto, (120, 120), 50)
    #desenho6:pygame.draw.circle(tela, branco, (120, 120), 49)
    #desenho6:pygame.draw.circle(tela, preto, (250, 500), 50)
    #desenho6:pygame.draw.circle(tela, branco, (250, 500), 49)
    #desenho6:pygame.draw.circle(tela, preto, (450, 300), 50)
    #desenho6:pygame.draw.circle(tela, branco, (450, 300), 49)
    #desenho6:pygame.draw.circle(tela, preto, (650, 300), 50)
    #desenho6:pygame.draw.circle(tela, branco, (650, 300), 49)
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()   