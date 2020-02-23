# Bizarre Adventure v_0.1
import pygame

from time import sleep
from player import Player

pygame.init()

# FPS
FPS = 60
clock = pygame.time.Clock()

# Display settings
display_width = 800
display_height = 600
display_bg = pygame.image.load('Sprites/bg.png')
display_size = (display_width, display_height)

# Display
display = pygame.display.set_mode(display_size)
pygame.display.set_caption("Bizarre Adventure")		

player = Player()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_SPACE:
				player.shoot(all_sprites, bullets)

	all_sprites.update()

	display.blit(display_bg, (0, 0))

	player.move()
	player.draw(display)
	
	all_sprites.draw(display)

	clock.tick(FPS)
	pygame.display.update()