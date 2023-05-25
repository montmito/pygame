import pygame

pygame.init()
pygame.mixer.init()

#gerando tela inicial
chao = 350
comprimento = 800
altura = 600
window = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('XD fighter')
g = 15
#gerando imagem(fd,cr7,jb)
Fd = pygame.image.load('Imagens pygame/fd_pixel2.png').convert_alpha()
cr7 = pygame.image.load('Imagens pygame/cr7_neutro_pixel.png').convert_alpha()
jb = pygame.image.load('Imagens pygame/jb_n_e.png').convert_alpha()
bala = pygame.image.load('Imagens pygame/bala.png').convert_alpha()
cr7 = pygame.transform.scale(cr7, (75, 75))
Fd = pygame.transform.scale(Fd, (comprimento, altura))
jb = pygame.transform.scale(jb,(75, 75))
chute_cr7 = pygame.image.load('Imagens pygame/cr7_c_d.png').convert_alpha()
chute_cr7 = pygame.transform.scale(chute_cr7, (75,75))
chute_jb = pygame.image.load('Imagens pygame/jb_c_e.png').convert_alpha()
chute_jb = pygame.transform.scale(chute_jb, (75,75))
shot = pygame.image.load('Imagens pygame/jb_t_e.png').convert_alpha()
shot = pygame.transform.scale(shot, (75, 75))
siuuu = pygame.mixer.Sound('Som pygame/cr_suuu.mp3')
bang = pygame.mixer.Sound('Som pygame/tiro.mp3')
grupo_tiros = pygame.sprite.Group()

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
        self.podepular = True
        self.chutou = False
        self.deschutou = 0
    def update(self):
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.speedy += g

        if self.rect.bottom >= chao:
            self.rect.y = chao
            self.podepular = True
        if self.rect.x > 600:
            self.rect.x = 600
        if self.rect.x < 150:
            self.rect.x = 150

        agora = pygame.time.get_ticks()
        if agora - self.deschutou >= 1000:
            self.chutou = False
            self.image = cr7
            self.deschutou = agora





class Tiro(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y, direcao):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speedx = 10  # Ajuste a velocidade conforme necessário
        self.direcao = direcao  # 'esquerda' ou 'direita' dependendo da direção do tiro

    def update(self):
        if self.direcao == 'esquerda':
            self.rect.x -= self.speedx
        elif self.direcao == 'direita':
            self.rect.x += self.speedx



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
        self.podepular = True
        self.chutou = False
        self.deschutou = 0

    def atirar(self):
        tiro_jb = Tiro(bala, self.rect.x, self.rect.y, 'direita')
        grupo_tiros.add(tiro_jb)

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.speedy += g

        if self.rect.bottom >= chao:
            self.rect.y = chao
            self.podepular = True
        if self.rect.x > 600:
            self.rect.x = 600
        if self.rect.x < 150:
            self.rect.x = 150

        agora = pygame.time.get_ticks()
        if agora - self.deschutou >= 1000:
            self.chutou = False
            self.image = jb
            self.deschutou = agora
            

#começo !!!

game = True
#ajustes
clock = pygame.time.Clock()
FPS = 30


lutador1 = CR7(cr7)
lutador2 = JB(jb,)


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
                if lutador1.podepular == True:
                    lutador1.speedy = -50
                    lutador1.rect.y += -30
                    lutador1.podepular = False
            if event.key == pygame.K_e:
                lutador1.chutou = True
                lutador1.image = chute_cr7
                siuuu.play()
            if event.key == pygame.K_w:
                if lutador2.podepular == True:
                    lutador2.speedy = -50
                    lutador2.rect.y += -30
                    lutador2.podepular = False
            if event.key == pygame.K_a:
                lutador2.speedx -= 25
            if event.key == pygame.K_d:
                lutador2.speedx += 25
            if event.key == pygame.K_p:
                lutador2.chutou = True
                lutador2.image = chute_jb
            if event.key == pygame.K_o:
                lutador2.image = shot
                lutador2.atirar()
                bang.play()
                
                


            
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                lutador1.speedx += 25
            if event.key == pygame.K_RIGHT:
                lutador1.speedx -= 25
            if event.key == pygame.K_a:
                lutador2.speedx += 25
            if event.key == pygame.K_d:
                lutador2.speedx -= 25

    window.blit(Fd,(0,0))
    #atualiza
    lutador1.update()
    lutador2.update()
    grupo_tiros.update()
    window.blit(lutador1.image, lutador1.rect)
    window.blit(lutador2.image, lutador2.rect)
    grupo_tiros.draw(window)
    pygame.display.update() 
#fim
pygame.quit() 


