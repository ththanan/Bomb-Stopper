import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, max_x, max_y):
        super().__init__()
        idle0 = pygame.image.load('../Infographics/player/player_idle0.png')
        idle1 = pygame.image.load('../Infographics/player/player_idle1.png')
        idle2 = pygame.image.load('../Infographics/player/player_idle2.png')
        idle3 = pygame.image.load('../Infographics/player/player_idle3.png')
        idle4 = pygame.image.load('../Infographics/player/player_idle4.png')
        idle5 = pygame.image.load('../Infographics/player/player_idle5.png')
        idle6 = pygame.image.load('../Infographics/player/player_idle6.png')
        idle7 = pygame.image.load('../Infographics/player/player_idle7.png')
        self.idle = [idle0, idle1, idle2, idle3, idle4, idle5, idle6, idle7]

        run0 = pygame.image.load('../Infographics/player/player0.png')
        run1 = pygame.image.load('../Infographics/player/player1.png')
        run2 = pygame.image.load('../Infographics/player/player2.png')
        run3 = pygame.image.load('../Infographics/player/player3.png')
        self.run = [run0, run1, run2, run3, run0, run1, run2, run3]

        self.frame_index = 0
        self.image = self.idle[self.frame_index]
        self.rect = self.image.get_rect(center=(max_x/2, max_y/2))

        self.direction = pygame.math.Vector2()

        self.max_x = max_x
        self.max_y = max_y

        #player status
        self.is_running_x = False
        self.is_running_y = False

        self.facing_left = True

        #player movement
        self.speed = 5

        #bullet
        self.ready = True
        self.bullet_facing_right = True
        self.bullet_time = 0
        self.bullet_cooldown = 300
        self.bullet = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.ready:
            self.bullet_facing_right = False
            self.shoot_bullet()
            self.ready = False
            self.bullet_time = pygame.time.get_ticks()
        elif keys[pygame.K_RIGHT] and self.ready:
            self.bullet_facing_right = True
            self.shoot_bullet()
            self.ready = False
            self.bullet_time = pygame.time.get_ticks()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_left = False
            self.image = self.run[int(self.frame_index)]
            self.is_running_x = True
            self.running()
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_left = True
            self.image = self.run[int(self.frame_index)]
            self.is_running_x = True
            self.running()
        else:
            self.direction.x = 0
            self.is_running_x = False

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.image = self.run[int(self.frame_index)]
            self.is_running_y = True
            self.running()
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.image = self.run[int(self.frame_index)]
            self.is_running_y = True
            self.running()
        else:
            self.direction.y = 0
            self.is_running_y = False

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        if self.is_running_x:
            self.rect.x += self.direction.x * speed
        if self.is_running_y:
            self.rect.y += self.direction.y * speed

    def left_right(self):
        if self.facing_left:
            self.image = self.image
        else:
            self.image = pygame.transform.flip(self.image, True, False)

    def idling(self):
        if self.is_running_x == False and self.is_running_y == False:
            self.frame_index += 0.2
            if self.frame_index >= len(self.idle):
                self.frame_index = 0
            self.image = self.idle[int(self.frame_index)]

    def running(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.run):
            self.frame_index = 0
        self.image = self.run[int(self.frame_index)]

    def constraint(self):
        if self.rect.left <= 100:
            self.rect.left = 100
        elif self.rect.right >= self.max_x - 100:
            self.rect.right = self.max_x - 100
        if self.rect.top <= 50:
            self.rect.top = 50
        elif self.rect.bottom >= self.max_y - 100:
            self.rect.bottom = self.max_y - 100

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.bullet_time >= self.bullet_cooldown:
                self.ready = True

    def shoot_bullet(self):
        self.bullet.add(Bullet(self.rect.center, self.bullet_facing_right, self.max_x))

    def update(self):
        self.get_input()
        self.move(self.speed)
        self.left_right()
        self.idling()
        self.constraint()
        self.recharge()
        self.bullet.update()