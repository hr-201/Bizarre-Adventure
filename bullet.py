from pygame import *

class Bullet(sprite.Sprite):
	def __init__(self, x_pos, y_pos):
		sprite.Sprite.__init__(self)
		# Bullet settings
		self.first_bullet = image.load('Sprites/bullet_first.png')
		self.second_bullet = image.load('Sprites/bullet_second.png')
		self.third_bullet = image.load('Sprites/bullet_third.png')
		self.image = Surface((10, 6))
		self.rect = self.image.get_rect()
		self.rect.centery = y_pos + 20
		self.rect.centerx = x_pos + 10
		self.speed = 25
		self.image.blit(self.first_bullet, (0, 0))

	def update(self):
		self.rect.x += self.speed
		if self.rect.x > 810:
			self.kill()