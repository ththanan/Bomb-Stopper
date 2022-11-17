import pygame

class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        idle0 = pygame.image.load('../Infographics/bomb/bomb0.png').convert_alpha()
        idle1 = pygame.image.load('../Infographics/bomb/bomb1.png').convert_alpha()
        idle2 = pygame.image.load('../Infographics/bomb/bomb2.png').convert_alpha()
        idle3 = pygame.image.load('../Infographics/bomb/bomb3.png').convert_alpha()

        self.idle = [idle0, idle1, idle2, idle3]

        self.frame_index = 0
        self.image = self.idle[self.frame_index]
        self.pos = pos
        self.rect = self.image.get_rect(center = (pos))

    def bomb_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.idle):
            self.frame_index = 0
        self.image = self.idle[int(self.frame_index)]

    def update(self):
        self.bomb_animation()