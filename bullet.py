import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, facing_right, max_x):
        super().__init__()
        idle = pygame.image.load('assets/bullet/bullet0.png').convert_alpha()
        self.idle = [idle]

        self.frame_index = 0
        self.image = self.idle[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.max_x = max_x

        self.speed = 20
        self.shoot_right = facing_right

    def destroy(self):
        if self.rect.x < 0 or self.rect.x > self.max_x:
            self.kill()

    def moving(self):
        if self.shoot_right:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

    def update(self):
        self.moving()
        self.destroy()