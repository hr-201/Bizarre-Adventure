# Bizarre Adventure v_0.1
import pygame

from player import Player
import game_all_settings as game_set

from random import randrange

pygame.init()
pygame.joystick.init()

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

# Background position
x = 0
y = 0

while True:
	# Checking all events
	game_set.check_events(player, all_sprites, bullets)

	x -= 10
	if x == -(6400 - 800):
		x = 0 

	display.blit(display_bg, (x, 0))

	all_sprites.update()

	# Draw objects
	game_set.draw(x, player, all_sprites, display, display_bg)

	player.move()

	clock.tick(FPS)
	pygame.display.update()