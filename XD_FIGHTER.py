import pygame

pygame.init()
pygame.mixer.init()

#gerando tela inicial

comprimento = 800
altura = 600
window = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('XD fighter')

#gerando imagem(fd,cr7,jb)

Fd = pygame.image.load('Imagens_pygame/fd_pixel2.png').convert()
cr7 = pygame.image.load('Imagens_pygame/cr7_neutro_pixel.png').convert()
jb = pygame.image.load('Imagens_pygame/jb_n_e.png').convert()
cr7 = pygame.transform.scale(cr7, (50, 50))
Fd = pygame.transform.scale(Fd, (comprimento, altura))
jb = pygame.transform.scale(jb,(50, 50))
#classes
class CR7(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (0, 0)
        self.rect.y = (100, 100)
        
class JB(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (0, 0)
        self.rect.y = (100, 100)


#começo !!!

game = True
lutador1 = CR7(cr7)
lutador2 = JB(jb)

while game:
    #eventos
    for event in pygame.event.get():
        #consequências
         if event.type == pygame.QUIT:
            game = False
            #saída 

    window.blit(Fd,(0,0))
    window.blit(cr7,(400,300))
    window.blit(jb,(600,300))
    #atualiza
    pygame.display.update() 

#fim
pygame.quit() 

