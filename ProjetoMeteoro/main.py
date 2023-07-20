import pygame
import random
pygame.init()
tamanho = (600,600)
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Meteoro Bumm!")
meteoroSound = pygame.mixer.Sound("meteoro.mp3")
branco = (255,255,255)
preto = (0,0,0)
clock = pygame.time.Clock()
nave = pygame.image.load("nave.png")
meteoro = pygame.image.load("meteoro.png")
pygame.display.set_icon(meteoro)
fundo = pygame.image.load("back.jpg")
running  = True
posicaoX = 300
movimentoX = 0
posicaoXMeteoro = 300
posicaoYMeteoro = -100
velocidadeMeteoro = 1
pygame.mixer.music.load("trilha.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.Sound.play(meteoroSound)
dificuldade = 70
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            movimentoX = -5
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            movimentoX = 5
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            movimentoX = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            movimentoX = 0
    
    if posicaoX < 0 :
        posicaoX = 0
    elif posicaoX>500:
        posicaoX = 500
    else:
        posicaoX = posicaoX + movimentoX

    #tela.fill(branco)
    tela.blit(fundo,(0,0))
    tela.blit(nave, (posicaoX,450))

    if posicaoYMeteoro > 600:
        posicaoYMeteoro = -100
        posicaoXMeteoro = random.randint(0,600)
        velocidadeMeteoro = velocidadeMeteoro + 1
        pygame.mixer.Sound.play(meteoroSound)


    posicaoYMeteoro =posicaoYMeteoro + velocidadeMeteoro

    tela.blit(meteoro, (posicaoXMeteoro,posicaoYMeteoro))
    
    #pygame.draw.circle(tela,preto, (posicaoX,550),30  )
    pixelsYNave = list(range(450, 550))
    pixelsXNave = list(range(posicaoX, posicaoX + 100))
    
    pixelsYMeteoro = list(range(posicaoYMeteoro, posicaoYMeteoro+100)) #101 é o tamanho da imagem
    pixelsXMeteoro = list(range(posicaoXMeteoro, posicaoXMeteoro+100))
    
    if len(list(set(pixelsXNave) & set(pixelsXMeteoro))) > dificuldade:
        if len(list(set(pixelsYNave) & set(pixelsYMeteoro))) > dificuldade:
            running = False
            print("Morreu!")



    pygame.display.update()
    clock.tick(60)

pygame.quit()