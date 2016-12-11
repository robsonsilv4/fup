import pygame
import pygame.gfxdraw
import math

pygame.init()

tela = pygame.display.set_mode((800, 600))
fps = pygame.time.Clock()

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
azul = (0, 0, 255)
azul_claro = (0, 255, 255)
roxo = (255, 0, 255)

# Jogadores
jogador1 = {'pos': {'x': 40, 'y': 300}, 'raio': 15}
jogador2 = {'pos': {'x': 760, 'y': 300}, 'raio': 15}
# bala = {'pos': {'x': 40, 'y': 300}, 'vel': 15}

balas = []
ang = 45
vel = 30
max_balas = 5

def desenha_jogadores(per, raio, cor):
    pygame.gfxdraw.filled_circle(
        tela,
        per['pos']['x'],
        per['pos']['y'],
        raio,
        cor)

    # Limites da tela
    if per['pos']['x'] - per['raio'] < 0:
        print('Saiu x')
    if per['pos']['y'] - per['raio'] > 800:
        print('Saiu x')
    if per['pos']['y'] - per['raio'] < 0:
        print("Saiu y")
    if per['pos']['y'] - per['raio'] > 600:
        print('Saiu y')


def desenha_bala(bala, raio, cor):
    pygame.gfxdraw.filled_circle(
        tela,
        bala['pos']['x'],
        bala['pos']['y'],
        raio,
        cor)

def ataliza_bala(bala):
    bala['vel']['y'] += 1
    bala['pos']['x'] += bala['vel']['x']
    bala['pos']['y'] += bala['vel']['y']

def limita_bala(bala):
    if bala['pos']['y'] - raio < 0:
        bala['pos']['y'] = 0 + raio
        bala['vel']['y'] *= -1
    if bala['pos']['y'] + raio > 600:
        bala['pos']['y'] = 600 - raio
        bala['vel']['y'] *= -1
    if bala['pos']['x'] - raio < 0:
        bala['pos']['x'] = 0 + raio
        bala['vel']['x'] *= -1
    if bala['pos']['y'] - raio > 0:
        bala['pos']['y'] = 800 - raio
        bala['vel']['y'] *= -1

def colisao_bala(bala, jogador):
    i


def atirar(jogador):
    bala['pos']['x'] = jogador['pos']['x'] + jogador['raio']


def colisao(obj1, obj2):
    colh = obj2['pos']['x'] - obj1['pos']['x']
    colv = obj2['pos']['y'] - obj1['pos']['y']
    res = math.sqrt(colh * colh + colv * colv)
    return res

# Tratamento de colisão
# Com base nas funções do Rubens


def colisao_jogs(jog1, jog2):
    if colisao(jog1, jog2) <= jog1['raio'] + jog2['raio']:
        print('Colidiu')

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Função do Pygame para fechar a janela
            pygame.quit()

        elif evento.type == pygame.KEYDOWN:

            # Interação do Jogador 1
            if evento.key == pygame.K_RIGHT:
                jogador1["pos"]['x'] += 10
            elif evento.key == pygame.K_LEFT:
                jogador1["pos"]['x'] -= 10
            elif evento.key == pygame.K_UP:
                jogador1["pos"]['y'] -= 10
            elif evento.key == pygame.K_DOWN:
                jogador1["pos"]['y'] += 10
            elif evento.key == pygame.K_RCTRL:
                atirar(jogador1)

            # Interação Jogador 2
            elif evento.key == pygame.K_d:
                jogador2["pos"]['x'] += 10
            elif evento.key == pygame.K_a:
                jogador2["pos"]['x'] -= 10
            elif evento.key == pygame.K_w:
                jogador2["pos"]['y'] -= 10
            elif evento.key == pygame.K_s:
                jogador2["pos"]['y'] += 10
            elif evento.key == pygame.K_f:
                atirar(jogador2)

    tela.fill(branco)
    desenha_jogadores(jogador1, 15, azul)
    desenha_jogadores(jogador2, 15, vermelho)
    # desenha_bala(bala, 5, amarelo)
    colisao_jogs(jogador1, jogador2)
    pygame.display.update()
    fps.tick(30)
