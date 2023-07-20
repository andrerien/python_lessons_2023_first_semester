import pygame
import time
import random
import winsound

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Exemplo de pontos")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

running = True
x = 0

def desenharLinha():
    for x in range(0,800):
        pygame.draw.circle(screen, RED, (x,300),1)

def desenharEletro(linhas):
    anterior  = (0,300)
    for i in linhas:
        pygame.draw.line(screen,RED,anterior,i,1)    
        anterior= i

anterior = (0,300)
linhas  = []
linhas.append(anterior)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
    screen.fill(WHITE)
    desenharLinha()
   
    y = random.randint(200,400)
    pygame.draw.circle(screen, RED, (x, y), 10)
    if x < 800:
        x = x + 5
    else:
        x = 0
        linhas = []

    linhas.append((x,y))
    desenharEletro(linhas)
    winsound.Beep(4000, 30) 

    pygame.display.update()
    time.sleep(0.5)

# Sair do Pygame
pygame.quit()