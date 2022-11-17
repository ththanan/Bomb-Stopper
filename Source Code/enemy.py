import pygame
from random import randint, choice
from player import Player

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, max_x, max_y, player_x, player_y, slow_status):
        super().__init__()
        run0 = pygame.image.load('../Infographics/enemy/enemy0.png').convert_alpha()
        run1 = pygame.image.load('../Infographics/enemy/enemy1.png').convert_alpha()
        run2 = pygame.image.load('../Infographics/enemy/enemy2.png').convert_alpha()
        run3 = pygame.image.load('../Infographics/enemy/enemy3.png').convert_alpha()

        self.run = [run0, run1, run2 ,run3]

        self.frame_index = 0
        self.image = self.run[self.frame_index]
        self.rect = self.image.get_rect(center=(pos))

        self.max_x = max_x
        self.max_y = max_y

        self.num = randint(60, 100)
        self.enemy_speed = 2
        self.enemy_y_status = 0
        self.enemy_get_player_y_delay = 20

        self.enemy_y_up_time = choice((0, randint(20, 30)))
        if self.enemy_y_up_time == 0: self.enemy_y_down_time = randint(20, 30)
        elif self.enemy_y_up_time > 0: self.enemy_y_down_time = 0

        #slow
        self.enemy_is_slow = slow_status

        #player
        self.player = Player(self.max_x, self.max_y)
        self.player_x = player_x
        self.player_y = player_y

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= self.max_x:
            self.rect.right = self.max_x
        elif self.rect.top <= 50:
            self.rect.top = 50
        elif self.rect.bottom >= self.max_y - 100:
            self.rect.bottom = self.max_y - 100

    def enemy_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.run):
            self.frame_index = 0
        self.image = self.run[int(self.frame_index)]

    def enemy_move(self):
        self.enemy_get_player_y_delay -= 1
        if self.rect.x >= self.player_x:
            self.rect.x -= self.enemy_speed
        elif self.rect.x < self.player_x:
            self.rect.x += self.enemy_speed

        if self.rect.y >= self.player_y and self.enemy_y_up_time > 0: y_down_time = randint(20, 30)
        elif self.rect.y >= self.player_y and self.enemy_y_down_time > 0: y_up_time = randint(90, 100)
        elif self.rect.y < self.player_y and self.enemy_y_up_time > 0: y_down_time = randint(90, 100)
        elif self.rect.y < self.player_y and self.enemy_y_down_time > 0: y_up_time = randint(20, 30)

        if self.enemy_y_up_time > 0:
            self.rect.y -= self.enemy_speed
            self.enemy_y_up_time -= 1
            if self.enemy_y_up_time == 0:
                self.enemy_y_down_time = y_down_time
        elif self.enemy_y_down_time > 0:
            self.rect.y += self.enemy_speed
            self.enemy_y_down_time -= 1
            if self.enemy_y_down_time == 0:
                self.enemy_y_up_time = y_up_time

    def enemy_slow(self):
        if self.enemy_is_slow:
            self.enemy_speed = 1

    def update(self):
        self.constraint()
        self.enemy_animation()
        self.enemy_move()
        self.enemy_slow()