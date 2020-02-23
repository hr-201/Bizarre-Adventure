from pygame import *

from bullet import Bullet

class Player(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		# Player settings
		self.width = 40
		self.height = 40
		self.image = image.load('Sprites/player.png')
		self.x_pos = 100 - self.width
		self.y_pos = 300 + self.height
		self.player = Surface((self.x_pos, self.y_pos))
		self.go_right = False
		self.speed = 15

	def draw(self, display):
		# Draw player
		self.rect = self.player.get_rect()
		self.rect.centerx = self.x_pos
		self.rect.centery = self.y_pos

		self.player.blit(self.image, (0, 0))
		self.display = display
		self.display.blit(self.player, (self.rect.centerx,
								   self.rect.centery))

		if self.go_right:
			self.player = image.load('Sprites/player_up.png')
			self.go_right = False
		else:
			self.player = image.load('Sprites/player.png')

	def move(self):
		keys = key.get_pressed()
		if (keys[K_LEFT] or keys[K_a]) and self.x_pos > 0:
			self.x_pos -= self.speed
			self.go_right = False
		if (keys[K_RIGHT] or keys[K_d]) and self.x_pos < 800 - 20:
			self.x_pos += self.speed
			self.go_right = True
		if (keys[K_UP] or keys[K_w]) and self.y_pos > 0:
			self.y_pos -= self.speed
			self.go_right = False
		if (keys[K_DOWN] or keys[K_s]) and self.y_pos < 600 - 20:
			self.y_pos += self.speed
			self.go_right = False

	def shoot(self, all_sprites, bullets):
		bullet = Bullet(self.rect.centerx, self.rect.centery)
		all_sprites.add(bullet)
		bullets.add(bullet)

		return all_sprites, bullets	