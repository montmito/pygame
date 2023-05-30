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
fightprompt = pygame.image.load('Imagens pygame/fightprompt.png')

fightprompt = pygame.transform.scale(fightprompt, (200, 200))

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

muchasgracias = pygame.mixer.Sound('Som pygame/muchasgracias.mp3')

bang = pygame.mixer.Sound('Som pygame/tiro.mp3')

shaokahn = pygame.mixer.Sound('Som pygame/shaokahn.mp3')

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

        self.socou = False

        self.deschutou = 0

        self.dessocou = False

        self.health = 100

        self.direction = 'direita'

        self.previous_direction = self.direction

        self.image_direita = img

        self.image_esquerda = pygame.transform.flip(img, True, False)

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



        if self.chutou:

            if self.direction == 'direita':

                self.image = chute_cr7

            elif self.direction == 'esquerda':

                self.image = pygame.transform.flip(chute_cr7, True, False)

        if self.socou:

            if self.direction == 'direita':

                self.image = soco_cr7

            elif self.direction == 'esquerda':

                self.image = pygame.transform.flip(soco_cr7, True, False)



        agora = pygame.time.get_ticks()

        if agora - self.deschutou >= 1000:

            self.chutou = False

            if self.direction == 'direita':

                self.image = self.image_direita

            elif self.direction == 'esquerda':

                self.image = self.image_esquerda

            self.deschutou = agora

 

        if agora - self.dessocou >= 800:

            self.socou = False

            if self.direction == 'direita':

                self.image = self.image_direita

            elif self.direction == 'esquerda':

                self.image = self.image_esquerda

            self.dessocou = agora

    def receber_dano(self, dano):

        self.health -= dano


class Tiro(pygame.sprite.Sprite):

    def __init__(self, img, pos_x, pos_y, direcao):

        pygame.sprite.Sprite.__init__(self)

        self.image = img

        self.rect = self.image.get_rect()

        self.rect.x = pos_x

        self.rect.y = pos_y

        self.speedx = 20  # Ajuste a velocidade conforme necessário

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

        self.atirou = False

        self.desatirou = 0

        self.health = 100

        self.direction = 'esquerda'

        self.previous_direction = self.direction

        self.image_direita = pygame.transform.flip(img, True, False)

        self.image_esquerda = img

 

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

 

        if self.chutou:

            if self.direction == 'direita':

                self.image = pygame.transform.flip(chute_jb, True, False)

            elif self.direction == 'esquerda':

                self.image = chute_jb

 

        if self.atirou:

            if self.direction == 'direita':

                self.image = pygame.transform.flip(shot, True, False)

            elif self.direction == 'esquerda':

                self.image = shot

 

        agora = pygame.time.get_ticks()

        if agora - self.deschutou >= 1000:

            self.chutou = False

            if self.direction == 'direita':

                self.image = self.image_direita

            elif self.direction == 'esquerda':

                self.image = self.image_esquerda

            self.deschutou = agora

        if agora - self.desatirou >= 1380:

            self.atirou = False

            if self.direction == 'direita':

                self.image = self.image_direita

            elif self.direction == 'esquerda':

                self.image = self.image_esquerda

            self.desatirou = agora

    def receber_dano(self, dano):

        self.health -= dano


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


def vitoriacr7():

    instructions_font = pygame.font.Font (None, 32 )

    instructions_text = instructions_font.render("VITORIA CR7", True, (255, 255, 255))

    window.blit(cr7_victory, (0,0))

    window.blit(instructions_text, (comprimento // 2 - instructions_text.get_width() // 2, altura // 2 + 200 ))

    pygame.display.update()

def vitoriajb():

    instructions_font = pygame.font.Font (None, 32 )

    instructions_text = instructions_font.render("VITORIA JB", True, (255, 255, 255))

    window.blit(jb_victory, (0,0))

    window.blit(instructions_text, (comprimento // 2 - instructions_text.get_width() // 2, altura // 2 + 200 ))

    pygame.display.update()
 

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

shaokahn.play()

 

#ajustes

clock = pygame.time.Clock()

FPS = 30

 

vida_cr7 = 100

vida_jb = 100

 

lutador1 = CR7(cr7)

lutador2 = JB(jb)

 

all_sprite = pygame.sprite.Group()

all_sprite.add(lutador1, lutador2)

#all_sprite.add(lutador1)

jogador_atacante = None

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

 

                lutador1.speedx -= 15

                lutador1.image = lutador1.image_esquerda

                lutador1.direction = 'esquerda'

 

            if event.key == pygame.K_RIGHT:

                lutador1.speedx += 15

                lutador1.image =lutador1.image_direita

                lutador1.direction = 'direita'

 

            if event.key == pygame.K_UP:

                if lutador1.podepular == True:

                    lutador1.speedy = -72

                    lutador1.rect.y += -15

                    jump.play()

                    lutador1.podepular = False

            if event.key == pygame.K_p:

                lutador1.chutou = True

                lutador1.image = chute_cr7

                siuuu.play()

                jogador_atacante = lutador1

            if event.key == pygame.K_o:

                lutador1.socou = True

                lutador1.image = soco_cr7

                muchasgracias.play()

                jogador_atacante = lutador1

            if event.key == pygame.K_w:

 

                if lutador2.podepular == True:

                    lutador2.speedy = -60

                    lutador2.rect.y += -20

                    jump.play()

                    lutador2.podepular = False

            if event.key == pygame.K_a:

                lutador2.speedx -= 15
                lutador2.image = lutador2.image_esquerda

                lutador2.direction = 'esquerda'

            if event.key == pygame.K_d:

                lutador2.speedx += 15

                lutador2.image = lutador2.image_direita

                lutador2.direction = 'direita'

 

            if event.key == pygame.K_e:

                lutador2.chutou = True

                lutador2.image = chute_jb

                jogador_atacante = lutador2
            if event.key == pygame.K_q:

                lutador2.atirou = True

                lutador2.image = shot

                lutador2.atirar()

                bang.play()

                jogador_atacante = lutador2
        # Verifica se soltou alguma tecla.

        if event.type == pygame.KEYUP:

            # Dependendo da tecla, altera a velocidade.

            if event.key == pygame.K_LEFT:

                lutador1.speedx += 15

            if event.key == pygame.K_RIGHT:

                lutador1.speedx -= 15

            if event.key == pygame.K_a:

                lutador2.speedx += 15

            if event.key == pygame.K_d:

                lutador2.speedx -= 15

        if pygame.sprite.collide_rect(lutador1, lutador2):

            if jogador_atacante == lutador2:

                lutador1.receber_dano(1)  # Jogador 1 acertou o Jogador 2

                vida_cr7 -= 1

            if jogador_atacante == lutador1:

                lutador2.receber_dano(3)   # Jogador 2 acertou o Jogador 1

                vida_jb -= 3

        # if pygame.sprite.collide_rect(lutador1, all_tiro):

        #     lutador2.receber_dano(7)

        if vida_jb <= 0 or vida_cr7 <= 0:

            game = False

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

if vida_cr7 <= 0:

    vitoriajb()

if vida_jb <= 0:

    vitoriacr7()

pygame.quit()