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
    #pygame.draw.circle(
    #    tela,
    #    cor,
    #    (per['pos']['x'],
    #     per['pos']['y']),
    #    per['raio'])

    pygame.gfxdraw.filled_circle(
        tela,
        per['pos']['x'],
        per['pos']['y'],
        per['raio'],
        cor)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Função do Pygame para fechar a janela
            pygame.quit()

    tela.fill(branco)
    desenha_personagem(jogador1, azul)
    desenha_personagem(jogador2, vermelho)
    pygame.display.update()
    fps.tick(30)
