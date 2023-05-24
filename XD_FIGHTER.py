import pygame

pygame.init()
pygame.mixer.init()

#gerando tela inicial
chao = 350
comprimento = 800
altura = 600
window = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('XD fighter')
g = 5
#gerando imagem(fd,cr7,jb)

Fd = pygame.image.load('Imagens pygame/fd_pixel2.png').convert_alpha()
cr7 = pygame.image.load('Imagens pygame/cr7_neutro_pixel.png').convert_alpha()
jb = pygame.image.load('Imagens pygame/jb_n_e.png').convert_alpha()
cr7 = pygame.transform.scale(cr7, (75, 75))
Fd = pygame.transform.scale(Fd, (comprimento, altura))
jb = pygame.transform.scale(jb,(75, 75))

#classes
class CR7(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 350
        self.speedx = 0
        self.speedy = 0
        self.movey = 0
    def update(self):
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.speedy += g
        #self.speedy = 0
        if self.rect.bottom >= chao:
            self.rect.y = chao
        if self.rect.x > 600:
            self.rect.x = 600
        if self.rect.x < 150:
            self.rect.x = 150
class JB(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 350
        self.speedx = 0
        self.speedy = 0
        self.movey = 0

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.speedy += g
        #self.speedy = 0

        if self.rect.bottom >= chao:
            self.rect.y = chao
        if self.rect.x > 600:
            self.rect.x = 600
        if self.rect.x < 150:
            self.rect.x = 150
            

#começo !!!

game = True
#ajustes
clock = pygame.time.Clock()
FPS = 30


lutador1 = CR7(cr7)
lutador2 = JB(jb)

while game:
    clock.tick(FPS)
    #eventos
    for event in pygame.event.get():
        #consequências
        if event.type == pygame.QUIT:
            game = False
            #saída 
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                lutador1.speedx -= 25
            if event.key == pygame.K_RIGHT:
                lutador1.speedx += 25
            if event.key == pygame.K_UP:
                lutador1.speedy = -50
                lutador1.rect.y += -30
            if event.key == pygame.K_w:
                lutador2.speedy = -50
                lutador2.rect.y += -30
            if event.key == pygame.K_a:
                lutador2.speedx -= 25
            if event.key == pygame.K_d:
                lutador2.speedx += 25
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                lutador1.speedx += 25
            if event.key == pygame.K_RIGHT:
                lutador1.speedx -= 25
            # if event.key == pygame.K_w:
            #     lutador2.speedy += 100
            # if event.key == pygame.K_UP:
            #     lutador1.speedy += 100
            if event.key == pygame.K_a:
                lutador2.speedx += 25
            if event.key == pygame.K_d:
                lutador2.speedx -= 25

    window.blit(Fd,(0,0))
    #atualiza
    lutador1.update()
    lutador2.update()
    window.blit(lutador1.image, lutador1.rect)
    window.blit(lutador2.image, lutador2.rect)
    pygame.display.update() 
#fim
pygame.quit() 


