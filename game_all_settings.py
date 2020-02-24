import pygame

from random import randrange

def check_events(player, all_sprites, bullets):
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_SPACE:
				rand_num = randrange(0, 3)
				player.shoot(all_sprites, bullets, rand_num)

def draw(x, all_sprites, player, display, display_bg):
	player.draw(display)
	
	all_sprites.draw(display)