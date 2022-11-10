import pygame

class Heart(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        idle0 = pygame.image.load('assets/heart/heart0.png').convert_alpha()
        idle1 = pygame.image.load('assets/heart/heart1.png').convert_alpha()
        idle2 = pygame.image.load('assets/heart/heart2.png').convert_alpha()
        idle3 = pygame.image.load('assets/heart/heart3.png').convert_alpha()
        self.idle = [idle0, idle1 , idle2, idle3]

        self.frame_index = 0
        self.image = self.idle[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.staying_time = 500

    def heart_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.idle):
            self.frame_index = 0
        self.image = self.idle[int(self.frame_index)]

    def delete(self):
        self.staying_time -= 1
        if self.staying_time <= 0:
            self.kill()
            self.staying_time = 500

    def update(self):
        self.heart_animation()
        self.delete()