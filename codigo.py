import pygame
import pygame.gfxdraw

# Inicialização do Pygame
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


def desenha_personagem(per, cor):
    pygame.gfxdraw.filled_circle(
        tela,
        per['pos']['x'],
        per['pos']['y'],
        per['raio'],
        cor)

    if per['pos']['y'] - per['raio'] < 0:
    	print("Saiu y")
    if per['pos']['y'] - per['raio'] > 600:
    	print('Saiu y')
    if per['pos']['x'] - per['raio'] < 0:
    	print('Saiu x')
    if per['pos']['y'] - per['raio'] > 800:
    	print('Saiu x')

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

            # Interação Jogador 2
            elif evento.key == pygame.K_d:
                jogador2["pos"]['x'] += 10
            elif evento.key == pygame.K_a:
                jogador2["pos"]['x'] -= 10
            elif evento.key == pygame.K_w:
                jogador2["pos"]['y'] -= 10
            elif evento.key == pygame.K_s:
                jogador2["pos"]['y'] += 10

    tela.fill(branco)
    desenha_personagem(jogador1, azul)
    desenha_personagem(jogador2, vermelho)
    pygame.display.update()
    fps.tick(30)
