import pygame

# Inicialização do Pygame
pygame.init()

tela = pygame.display.set_mode((800, 600))
fps = pygame.time.Clock()

# Jogadores
jogador1 = {'posicao': {'x': 40, 'y': 300}, 'raio': 15}
jogador2 = {'posicao': {'x': 760, 'y': 300}, 'raio': 15}


def desenha_personagem(personagem, cor):
    pygame.draw.circle(
        tela,
        cor,
        (personagem['posicao']['x'],
         personagem['poscao']['y']),
        personagem['raio'])

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Função do Pygame para fechar a janela
            pygame.quit()
