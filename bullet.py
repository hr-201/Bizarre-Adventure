from pygame import *

class Bullet(sprite.Sprite):
	def __init__(self, x_pos, y_pos, rand_num):
		sprite.Sprite.__init__(self)
		# Bullet settings
		self.first_bullet = image.load('Sprites/bullet_first.png')
		self.second_bullet = image.load('Sprites/bullet_second.png')
		self.third_bullet = image.load('Sprites/bullet_third.png')
		self.image = Surface((10, 6))
		self.rect = self.image.get_rect()
		self.rect.centery = y_pos + 20
		self.rect.centerx = x_pos + 10
		self.speed = 10
		self.rand_num = rand_num

		# Defolt image
		self.def_image = None
		if self.rand_num == 0:
			self.def_image = self.first_bullet
		elif self.rand_num == 1:
			self.def_image = self.second_bullet
		else:
			self.def_image = self.third_bullet

		self.image.blit(self.def_image, (0, 0))

	def update(self):
		self.rect.x += self.speed
		if self.rect.x > 810:
			self.kill()