import pygame as pg

from bullet import Bullet

class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		# Player settings
		self.width = 40
		self.height = 40
		self.image = pg.image.load('Sprites/player.png')
		self.x_pos = 100 - self.width
		self.y_pos = 300 + self.height
		self.player = pg.Surface((self.x_pos, self.y_pos))
		self.go_right = False
		self.speed = 3

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
			self.player = pg.image.load('Sprites/player_up.png')
			self.go_right = False
		else:
			self.player = pg.image.load('Sprites/player.png')

	def move(self):
		keys = pg.key.get_pressed()
		if (keys[pg.K_LEFT] or keys[pg.K_a]) and self.x_pos > 0:
			self.x_pos -= self.speed
			self.go_right = False
		if (keys[pg.K_RIGHT] or keys[pg.K_d]) and self.x_pos < 800 - 20:
			self.x_pos += self.speed
			self.go_right = True
		if (keys[pg.K_UP] or keys[pg.K_w]) and self.y_pos > 0:
			self.y_pos -= self.speed
			self.go_right = False
		if (keys[pg.K_DOWN] or keys[pg.K_s]) and self.y_pos < 600 - 40:
			self.y_pos += self.speed
			self.go_right = False

		if self.x_pos > 0:
			self.x_pos -= 1

	def shoot(self, all_sprites, bullets, rand_num):
		self.rand_num = rand_num
		bullet = Bullet(self.rect.centerx, self.rect.centery, self.rand_num)
		all_sprites.add(bullet)
		bullets.add(bullet)

		pg.mixer.music.load('Sounds/Shoot.wav')
		pg.mixer.music.play()

		return all_sprites, bullets	