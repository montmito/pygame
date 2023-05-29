import pygame
import sys

pygame.init()
pygame.mixer.init()

#gerando tela inicial
chao = 350
comprimento = 800
altura = 600
window = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('XD fighter')
g = 15
#imagens!!!
xd = pygame.image.load('Imagens pygame/xdreal.png').convert_alpha()
xd = pygame.transform.scale(xd, (200, 200))
fighter = pygame.image.load('Imagens pygame/fighter-logo-png-transparent.png').convert_alpha()
fighter = pygame.transform.scale(fighter, (200, 200))
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
soco_cr7 = pygame.image.load('Imagens pygame/cr7_s_d.png').convert_alpha()
soco_cr7 = pygame.transform.scale(soco_cr7, (75, 75))
shot = pygame.image.load('Imagens pygame/jb_t_e.png').convert_alpha()
shot = pygame.transform.scale(shot, (75, 75))
siuuu = pygame.mixer.Sound('Som pygame/cr_suuu.mp3')
bang = pygame.mixer.Sound('Som pygame/tiro.mp3')
grupo_tiros = pygame.sprite.Group()
cr7_victory = pygame.image.load('Imagens pygame/cristiano.png').convert_alpha()
cr7_victory = pygame.transform.scale(cr7_victory, (comprimento, altura))
jb_victory = pygame.image.load('Imagens pygame/james-bond.png').convert_alpha()
jb_victory = pygame.transform.scale(jb_victory, (comprimento, altura))
jump = pygame.mixer.Sound('Som pygame/smw_jump.wav')

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
        self.health = 100 
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
        self.health = 100
        self.direction = 'esquerda'

    def atirar(self):
        tiro_jb = Tiro(bala, self.rect.x, self.rect.y, self.direction)
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
        if self.speedx <=0:
            self.direction = 'esquerda'
        else:
            self.direction = 'direita'



def teladeinicio():
    
    instructions_font = pygame.font.Font (None, 32 )

    pygame.mixer.music.load('Som pygame/08 Guile.mp3')
    pygame.mixer.music.play(-1)


    
    instructions_text = instructions_font.render("Click para iniciar", True, (255, 255, 255))

    window.blit(Fd, (0, 0))
    window.blit(xd, (comprimento // 2 - xd.get_width() // 2, altura // 2 - 100))
    window.blit(fighter, (comprimento // 2 - fighter.get_width() // 2, altura // 2 ))
    window.blit(instructions_text, (comprimento // 2 - instructions_text.get_width() // 2, altura // 2 + 200 ))
    pygame.display.update()

    waiting = True
    while waiting:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


    pygame.mixer.music.stop()
        

def healthbars(window, x, y, comprimento, altura, health):
    BORDER_COLOR = (255, 255, 255)
    HEALTH_COLOR = (0, 255, 0)
    BORDER_WIDTH = 2

    # Draw the border of the health bar
    pygame.draw.rect(window, BORDER_COLOR, (x, y, comprimento, altura), BORDER_WIDTH)

    # Calculate the width of the health bar based on the health value
    health_width = (health / 100) * (comprimento - 2 * BORDER_WIDTH)

    # Draw the current health level
    pygame.draw.rect(window, HEALTH_COLOR, (x + BORDER_WIDTH, y + BORDER_WIDTH, health_width, altura - 2 * BORDER_WIDTH))

    # Set the font and size for the text
    font = pygame.font.Font(None, 24)

#começo !!!
teladeinicio()


game = True
#ajustes
clock = pygame.time.Clock()
FPS = 30

vida_cr7 = 100
vida_jb = 100

lutador1 = CR7(cr7)
lutador2 = JB(jb)
sprite_lutador1 = pygame.sprite.Group()
sprite_lutador1.add(lutador1)
sprite_lutador2 = pygame.sprite.Group()
sprite_lutador2.add(lutador2)
while game: 
    clock.tick(FPS)
    #eventos
    flip = False
    for event in pygame.event.get():
        #consequências
        if event.type == pygame.QUIT:
            game = False
            #saída 
        if lutador1.rect.x > lutador2.rect.x:
            cr7 = pygame.transform.flip(cr7, True, False)
            jb = pygame.transform.flip(jb, True, False)
            flip = True
            # chute_cr7 = pygame.transform.flip(chute_cr7, True, False)
            # chute_jb = pygame.transform.flip(chute_jb, True, False)
            # soco_cr7 = pygame.transform.flip(soco_cr7, True, False)
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
                    jump.play()
                    lutador1.podepular = False
            if event.key == pygame.K_e:
                lutador1.chutou = True
                if flip == True:
                    
                    lutador1.image = pygame.transform.flip(chute_cr7, True, False)
                else:
                    lutador1.image = chute_cr7
                siuuu.play()
            if event.key == pygame.K_w:
                if lutador2.podepular == True:
                    lutador2.speedy = -50
                    lutador2.rect.y += -30
                    jump.play()
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
        hits = pygame.sprite.spritecollide(lutador1, sprite_lutador2, True)
        hit2 = []
        if hits != hit2:
            vida_cr7 -= 10
            vida_jb -= 10
            print(vida_jb)
            print(hits)
            hit2 = hits
            print(hit2)





    window.blit(Fd,(0,0))
    healthbars(window, 50, 30, 200, 20, lutador1.health)  
    healthbars(window, comprimento - 250, 30, 200, 20, lutador2.health)  
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


