import pygame
from pygame import mixer
from pygame import Surface
from random import randint

pygame.init()

# Nome do jogo
pygame.display.set_caption('Halloween Hippie')

# Tela principal --> onde ocorre a gameplay
janela = pygame.display.set_mode((500, 500))

# Tela de repeat
sup = Surface((300, 300))

# Boolean que diz a situação do jogo. Se está em andamento ou não
situation = True

# Imagem de fundo
fundo = pygame.image.load("Assets/images/fundo.png")

# Configurações de font-style, font-size
font = pygame.font.SysFont('arial black', 15)
fontGameOver = pygame.font.SysFont('arial black', 40)
fontPontuacaoSup = pygame.font.SysFont('arial', 18)
fontReiniciar = pygame.font.SysFont('arial black', 23)

# Quantidade de pontos em que o player inicia o jogo
pontos = 0

# Quantidade de vidas em que o player inicia o jogo
vidas = 3

# Int auxiliar
qtd = 0

# Pontos_txt
texto = font.render("Pontos: 0", True, (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (40, 10)

# Vidas_txt
vida = font.render("Vidas: " + str(vidas), True, (0, 0, 0))
pos_vida = texto.get_rect()
pos_vida.center = (40, 35)

# GameOver_txt
gameOver = fontGameOver.render("GAME OVER", True, (255, 165, 0))
pos_gameOver = gameOver.get_rect()
pos_gameOver.center = (150, 45)

# Reiniciar_txt
reiniciar = fontReiniciar.render("Reiniciar", True, (0, 0, 0))
pos_reiniciar = reiniciar.get_rect()
pos_reiniciar.center = (150, 210)

# PontuaçãoFinal_txt
pos_pontuacaoSup = texto.get_rect()
pos_pontuacaoSup.center = (130, 110)

# Backgroud music
pygame.mixer.music.load('Assets/sounds/fundo_Theme.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Colet music
colet_music = mixer.Sound('Assets/sounds/coletado.wav')
colet_music.set_volume(0.1)

# Forgot music
forgot_music = mixer.Sound('Assets/sounds/exemplo.wav')

# Lost music
lost_music = mixer.Sound('Assets/sounds/lost.wav')

janela_aberta = True


class Maça(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Assets/images/maça.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20, 450)
        self.rect[1] = 0

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        elif situation == False:
            self.rect[1] = 0
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = randint(-200, -100)

    def death(self):
        del self

    def voltar(self):
        self.rect[1] = randint(-200, -100)
        self.rect[0] = randint(20, 450)


class Melancia(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Assets/images/melancia.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20, 450)
        self.rect[1] = -300

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        elif situation == False:
            self.rect[1] = -10
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = -300

    def death(self):
        del self

    def voltar(self):
        self.rect[1] = randint(-1000, -300)
        self.rect[0] = randint(20, 450)


class Abacaxi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Assets/images/abacaxi.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20, 450)
        self.rect[1] = -700

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        elif situation == False:
            self.rect[1] = 0
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = -700

    def death(self):
        del self

    def voltar(self):
        self.rect[1] = randint(-500, -100)
        self.rect[0] = randint(20, 450)


class Banana(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Assets/images/banana.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20, 450)
        self.rect[1] = -2000

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        elif situation == False:
            self.rect[1] = 0
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = -2000

    def death(self):
        del self

    def voltar(self):
        self.rect[1] = randint(-700, -300)
        self.rect[0] = randint(20, 450)


class Morango(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Assets/images/morango.png")
        self.rect = self.image.get_rect()
        self.rect[0] = randint(20, 450)
        self.rect[1] = -1000

    def update(self):
        pass

    def velocidade(self):
        if pontos >= 30:
            self.rect[1] += 7
        elif situation == False:
            self.rect[1] = 0
        else:
            self.rect[1] += 5

    def verificar(self):
        if self.rect[1] >= 420:
            self.rect[1] = -1000

    def death(self):
        del self

    def voltar(self):
        self.rect[1] = randint(-900, -300)
        self.rect[0] = randint(20, 450)


class Chao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Assets/images/chao.png")
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = 470

    def update(self):
        pass


class Cesta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Assets/images/cesta.png")
        self.rect = self.image.get_rect()
        self.rect[0] = 225
        self.rect[1] = 410

    def update(self):
        pass

    def direita(self):
        if self.rect[0] < 450:
            self.rect[0] += 15

    def esquerda(self):
        if self.rect[0] > 10:
            self.rect[0] -= 15


maca_group = pygame.sprite.Group()
maca = Maça()
maca_group.add(maca)

melancia_group = pygame.sprite.Group()
melancia = Melancia()
melancia_group.add(melancia)

abacaxi_group = pygame.sprite.Group()
abacaxi = Abacaxi()
abacaxi_group.add(abacaxi)

banana_group = pygame.sprite.Group()
banana = Banana()
banana_group.add(banana)

morango_group = pygame.sprite.Group()
morango = Morango()
morango_group.add(morango)

chao_group = pygame.sprite.Group()
chao = Chao()
chao_group.add(chao)

cesta_group = pygame.sprite.Group()
cesta = Cesta()
cesta_group.add(cesta)

# Loop do game
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Armazena qual tecla foi pressionada
    comandos = pygame.key.get_pressed()

    # Esse if não deixa movimentar a cesta quando a tela de gameover estiver sendo exibida
    if situation:
        # Configura a seta direita para movimentar a cesta
        if comandos[pygame.K_RIGHT]:
            Cesta.direita(cesta)

        # Configura a seta esquerda para movimentar a cesta
        if comandos[pygame.K_LEFT]:
            Cesta.esquerda(cesta)

    # Colisão da Cesta com a Maçã
    if pygame.sprite.groupcollide(cesta_group, maca_group, False, False, ):
        pontos += 1
        Maça.voltar(maca)
        texto = font.render("Pontos: " + str(pontos), True, (0, 0, 0))

        if situation:
            colet_music.play()

        else:
            colet_music.stop()

    # Colisão da Cesta com o Melancia
    elif pygame.sprite.groupcollide(cesta_group, melancia_group, False, False, ):
        pontos += 1
        Melancia.voltar(melancia)
        texto = font.render("Pontos: " + str(pontos), True, (0, 0, 0))

        if situation:
            colet_music.play()

        else:
            colet_music.stop()

    # Colisão da Cesta com o Abacaxi
    elif pygame.sprite.groupcollide(cesta_group, abacaxi_group, False, False, ):
        pontos += 1
        Abacaxi.voltar(abacaxi)
        texto = font.render("Pontos: " + str(pontos), True, (0, 0, 0))

        if situation:
            colet_music.play()

        else:
            colet_music.stop()

    # Colisão da Cesta com o Banana
    elif pygame.sprite.groupcollide(cesta_group, banana_group, False, False, ):
        pontos += 1
        Banana.voltar(banana)
        texto = font.render("Pontos: " + str(pontos), True, (0, 0, 0))

        if situation:
            colet_music.play()

        else:
            colet_music.stop()

    # Colisão da Cesta com o Morango
    elif pygame.sprite.groupcollide(cesta_group, morango_group, False, False, ):
        pontos += 1
        Morango.voltar(morango)
        texto = font.render("Pontos: " + str(pontos), True, (0, 0, 0))

        if situation:
            colet_music.play()

        else:
            colet_music.stop()

    # Colisão do Chão com a Maçã
    if pygame.sprite.groupcollide(chao_group, maca_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (0, 0, 0))
        Maça.verificar(maca)

        if situation:
            forgot_music.play()

        else:
            forgot_music.stop()

    # Colisão do Chão com a Melancia
    elif pygame.sprite.groupcollide(chao_group, melancia_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (0, 0, 0))
        Melancia.verificar(melancia)

        if situation:
            forgot_music.play()

        else:
            forgot_music.stop()

    # Colisão do Chão com o Abacaxi
    elif pygame.sprite.groupcollide(chao_group, abacaxi_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (0, 0, 0))
        Abacaxi.verificar(abacaxi)

        if situation:
            forgot_music.play()

        else:
            forgot_music.stop()

    # Colisão do Chão com a Banana
    elif pygame.sprite.groupcollide(chao_group, banana_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (0, 0, 0))
        Banana.verificar(banana)

        if situation:
            forgot_music.play()

        else:
            forgot_music.stop()

    # Colisão do Chão com o Morango
    elif pygame.sprite.groupcollide(chao_group, morango_group, False, False, ):
        vidas -= 1
        vida = font.render("Vidas: " + str(vidas), True, (0, 0, 0))
        Morango.verificar(morango)

        if situation:
            forgot_music.play()

        else:
            forgot_music.stop()

    # .velocidade() --> configura a velocidade inicial das frutas que aumenta conforme os pontos sobe
    Maça.velocidade(maca)
    Melancia.velocidade(melancia)
    Abacaxi.velocidade(abacaxi)
    Banana.velocidade(banana)
    Morango.velocidade(morango)

    pygame.display.update()

    # background tela
    janela.blit(fundo, (0, 0))

    # txt dos pontos na tela
    janela.blit(texto, pos_texto)

    # txt das vidas na tela
    janela.blit(vida, pos_vida)

    # Esse if não deixa as frutas aparecerem na tela enquanto a tela de gameover estiver sendo exibida
    if situation:
        # .draw mostra as frutas, a cesta e o chao na tela
        morango_group.draw(janela)
        banana_group.draw(janela)
        abacaxi_group.draw(janela)
        melancia_group.draw(janela)
        maca_group.draw(janela)

    cesta_group.draw(janela)
    chao_group.draw(janela)

    # Este if exibe a tela de gameOver quando as vidas chegarem a 0, mostra a pontuação final e um botão para recomeçar o jogo
    if vidas <= 0:
        situation = False
        pontuacaoSup = fontPontuacaoSup.render("Pontuação: " + str(pontos), True, (255, 165, 0))

        janela.blit(sup, [100, 100])
        sup.blit(gameOver, pos_gameOver)

        sup.blit(pontuacaoSup, pos_pontuacaoSup)
        mixer.music.stop()
        if qtd == 0:
            lost_music.play()
            qtd += 1

        # Remove essas informações da tela enquanto a tela de gameover estiver sendo exibida
        texto = font.render(" ", True, (0, 0, 0))
        vida = font.render(" ", True, (0, 0, 0))

        # Retângulo laranja que criamos para servir de botão para reiniciar o jogo
        ret = pygame.Rect(35, 200, 230, 25)

        # Exibe p retângulo na tela
        pygame.draw.rect(sup, (255, 165, 0), ret)
        sup.blit(reiniciar, pos_reiniciar)

        # .voltar() --> faz com que todas as frutas que estão na tela volte para o inicio
        Maça.voltar(maca)
        Morango.voltar(morango)
        Abacaxi.voltar(abacaxi)
        Melancia.voltar(melancia)
        Banana.voltar(banana)


        # Trata-se do .click do botão de Jogar novamente
        if event.type == pygame.MOUSEBUTTONDOWN:
            qtd = 0

            # Coordenada no eixo x do mouse
            x = pygame.mouse.get_pos()[0]

            # Coordenada no eixo y do mouse
            y = pygame.mouse.get_pos()[1]

            # Retângulo preto que criamos por cima da pontuaçãoSup
            ret = pygame.Rect(100, 100, 150, 100)
            pygame.draw.rect(sup, (0, 0, 0), ret)

            # Coordenada do botão Reiniciar
            if x > 135 and y > 300 and x < 363 and y < 323:
                situation = True
                pontos = 0
                vidas = 3
                texto = font.render("Pontos: " + str(pontos), True, (0, 0, 0))
                vida = font.render("Vidas: " + str(vidas), True, (0, 0, 0))

                # .velocidade() --> configura a velocidade inicial das frutas que aumenta conforme os pontos sobe
                Maça.velocidade(maca)
                Melancia.velocidade(melancia)
                Abacaxi.velocidade(abacaxi)
                Banana.velocidade(banana)
                Morango.velocidade(morango)

                # background tela
                janela.blit(fundo, (0, 0))

                # txt dos pontos na tela
                janela.blit(texto, pos_texto)

                # txt das vidas na tela
                janela.blit(vida, pos_vida)

                # .draw mostra as frutas, a cesta e o chao na tela
                morango_group.draw(janela)
                banana_group.draw(janela)
                abacaxi_group.draw(janela)
                melancia_group.draw(janela)
                maca_group.draw(janela)
                cesta_group.draw(janela)
                chao_group.draw(janela)

pygame.quit()
