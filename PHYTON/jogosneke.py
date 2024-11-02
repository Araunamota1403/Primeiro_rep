#bibliotecas
import pygame
import random

#tela do jogo
pygame.init()
pygame.display.set_caption('Jogo da cobrinha')

largura, altura = 1700,900
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()


#cores
preto = (0,0,0)
laranja = (255, 127, 80)
branco = ( 250, 250, 250)
verde = ( 189,236, 182 )

#paremetros cobra
tamanho_rad = 15
velocidade_de_atualizacao = 15

#paremetro comida
def gerar_comida(x_cobra, y_cobra):
    while True:
        comida_x = random.randrange(0, largura // tamanho_rad) * tamanho_rad
        comida_y = random.randrange(0, altura // tamanho_rad) * tamanho_rad
        
        # Verifica se a nova posição da comida está na mesma posição da cobra
        if comida_x != x_cobra or comida_y != y_cobra:
            break

    return comida_x, comida_y

#velocidade e direcao
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        veloc_x = 0
        veloc_y = tamanho_rad

        
    elif tecla == pygame.K_UP:
        veloc_x = 0
        veloc_y = -tamanho_rad


    elif tecla == pygame.K_LEFT:
        veloc_x = -tamanho_rad
        veloc_y = 0


    elif tecla == pygame.K_RIGHT:
        veloc_x = tamanho_rad
        veloc_y = 0



    return veloc_x, veloc_y

#desenhar coomida
def desenhar_comida(tamanho_rad, comida_x, comida_y):
    pygame.draw.rect(tela,verde, [comida_x, comida_y, tamanho_rad, tamanho_rad ])

#desenhar cobra
def desenhar_cobra(tamanho_rad, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, laranja, [pixel[0], pixel[1], tamanho_rad, tamanho_rad] )


#desenhar pontos
def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont ('Helvetica',30)
    texto = fonte.render(f'Pontos: {int(pontuacao/5)}', True, branco)
    tela.blit(texto, [775, 1])


#jogo
def rodar_jogo():
    fim_jogo = False
    
    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    #comida inicial
    comida_x, comida_y = gerar_comida(x,y)

    #rodando
    while not fim_jogo:
        tela.fill(preto)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)


        #desenhar comida
        desenhar_comida(tamanho_rad, comida_x, comida_y)

        #atualizar a posicao
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        x += velocidade_x
        y += velocidade_y

        #desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra: 
            del pixels[0]

        #se a cobra bateu no proprio corpo
        for pixel  in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        
        desenhar_cobra(tamanho_rad, pixels)

        #desenhar pontos
        desenhar_pontuacao(tamanho_cobra - 1)

        #atualização da tela
        pygame.display.update()

        #gerar nova comida

        if pygame.Rect(x, y, tamanho_rad, tamanho_rad).colliderect(pygame.Rect(comida_x, comida_y, tamanho_rad, tamanho_rad)):
            tamanho_cobra += 5
            comida_x, comida_y = gerar_comida(x,y)



        relogio.tick(velocidade_de_atualizacao)


rodar_jogo()