import pygame

# Inicialização do Pygame
pygame.init()

tela = pygame.display.set_mode((800, 600))
fps = pygame.time.Clock()

while True:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			# Função do Pygame para fechar a janela
			pygame.quit()