import pygame

pygame.init()
pygame.mixer.init()

#gerando tela inicial

comprimento = 800
altura = 600
window = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('XD fighter')

#gerando imagem(fd)

image = pygame.image.load('Imagens_pygame/fd_pixel2.png').convert()
image = pygame.transform.scale(image, (comprimento, altura))

#começo !!!

game = True


while game:
    #eventos
    for event in pygame.event.get():
        #consequências
         if event.type == pygame.QUIT:
            game = False
            #saída 

    window.blit(image,(0,0))
    #atualiza
    pygame.display.update() 

#fim
pygame.quit() 

