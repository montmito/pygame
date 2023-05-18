import pygame

pygame.init()
pygame.mixer.init()

#gerando tela inicial

comprimento = 800
altura = 600
window = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('XD fighter')

#gerando imagem(fd)

Fd = pygame.image.load('Imagens_pygame/fd_pixel2.png').convert()
cr7 = pygame.image.load('Imagens_pygame/cr7_neutro_pixel.png').convert()
cr7 = pygame.transform.scale(cr7, (50, 50))
Fd = pygame.transform.scale(Fd, (comprimento, altura))

#começo !!!

game = True


while game:
    #eventos
    for event in pygame.event.get():
        #consequências
         if event.type == pygame.QUIT:
            game = False
            #saída 

    window.blit(Fd,(0,0))
    window.blit(cr7,(400,300))
    #atualiza
    pygame.display.update() 

#fim
pygame.quit() 

