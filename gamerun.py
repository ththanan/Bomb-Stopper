import pygame, sys
from random import randint, choice
from player import Player
from enemy import Enemy
from bomb import Bomb
from slow import Slow
from heart import Heart
from strong import Strong
from coin import Coin

def draw_text(text, color, size, screen, pos):
    global screen_width, screen_height
    font = pygame.font.Font('assets/mago3.ttf', size)
    textobj = font.render(text, False, color)
    textrect = textobj.get_rect(center = pos)
    screen.blit(textobj, textrect)

class Gamerun():
    def __init__(self, screen, screen_width, screen_height, clock):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clock = clock

        self.bg_image = pygame.image.load('assets/bg1.png')

        #player
        player_sprite = Player(self.screen_width, self.screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.player_stutus = 1

        #player's live
        self.life = pygame.Surface((7, 10))
        self.life.fill('#bb4343')
        self.player_life = 10
        self.player_life_cal = 1
        self.life_bg = pygame.Surface((70, 10))
        self.life_bg.fill('#696868')

        #slow
        self.enemy_is_slow = False
        self.slow = pygame.sprite.Group()
        self.slow_adding_time = randint(500, 1000)
        self.slow_using_time = 500

        #enemy
        self.random_x_enemy = choice([0, self.screen_width])
        self.random_y_enemy = randint(0, self.screen_height)
        enemy_sprite = Enemy((choice([80, 1200]), randint(250, 350)), self.screen_width, self.screen_height, self.player.sprite.rect.x, self.player.sprite.rect.y, self.enemy_is_slow)
        self.enemy = pygame.sprite.Group(enemy_sprite)
        self.enemy_adding_time = 100
        self.enemy_speed = 1
        self.enemy_count_num = 1

        self.enemy_get_player_y_delay = 20
        self.enemy_get_player_y = self.player.sprite.rect.y

        #bomb
        self.bomb = pygame.sprite.Group()
        self.bomb.update()
        self.bomb_adding_time = 0

        #heart
        self.heart = pygame.sprite.Group()
        self.heart_adding_time = randint(500, 1000)

        #strong
        self.strong = pygame.sprite.Group()
        self.strong_adding_time = randint(1500, 2000)
        self.strong_using_time = 500
        self.player_is_strong = False

        #coin
        self.coin = pygame.sprite.Group()
        self.coin_adding_time = randint(200, 500)

        #score
        self.score = 0

        #skull
        self.skull = pygame.sprite.Group()
        self.having_skull = 0

        #audio
        self.coin_sound = pygame.mixer.Sound('assets/audio/coin.wav')
        self.coin_sound.set_volume(4)

        self.heart_sound = pygame.mixer.Sound('assets/audio/heart.wav')
        self.heart_sound.set_volume(0.8)

        self.item_sound = pygame.mixer.Sound('assets/audio/item_collect_sound.wav')
        self.item_sound.set_volume(1)

        self.die_sound = pygame.mixer.Sound('assets/audio/die.wav')
        self.die_sound.set_volume(0.2)

        self.enemy_sound = pygame.mixer.Sound('assets/audio/bullet.wav')
        self.enemy_sound.set_volume(0.2)

        self.bomb_stop_sound = pygame.mixer.Sound('assets/audio/bomb_stop.wav')
        self.bomb_stop_sound.set_volume(0.5)

        self.explosion_sound = pygame.mixer.Sound('assets/audio/explosion.wav')
        self.explosion_sound.set_volume(0.5)

    #life
    def check_life(self):
        if self.player_life <= 0: self.gameisover()

    def display_life(self):
        if self.player_stutus == 1:
            self.screen.blit(self.life_bg, (self.player.sprite.rect.x, self.player.sprite.rect.y - 15))
            for each_life in range(self.player_life):
                x = self.player.sprite.rect.x + (each_life * (self.life.get_size()[0]))
                self.screen.blit(self.life, (x, self.player.sprite.rect.y - 15))


    #score
    def display_score(self):
        draw_text(f'score : {self.score}', ('#F7EDDC'), 40, self.screen, (self.screen_width/2, self.screen_height - 35))


    #skull
    def display_skull(self):
        self.skull_bg1 = pygame.image.load('assets/skull/skull_bg0.png').convert_alpha()
        self.skull_bg1_rect = self.skull_bg1.get_rect(center = (50, self.screen_height - 35))
        self.screen.blit(self.skull_bg1, self.skull_bg1_rect)

        self.skull_bg2 = pygame.image.load('assets/skull/skull_bg0.png').convert_alpha()
        self.skull_bg2_rect = self.skull_bg2.get_rect(center = (100, self.screen_height - 35))
        self.screen.blit(self.skull_bg2, self.skull_bg2_rect)

        self.skull_bg3 = pygame.image.load('assets/skull/skull_bg0.png').convert_alpha()
        self.skull_bg3_rect = self.skull_bg3.get_rect(center = (150, self.screen_height - 35))
        self.screen.blit(self.skull_bg3, self.skull_bg3_rect)

        if self.having_skull == 1:
            self.skull1 = pygame.image.load('assets/skull/skull0.png').convert_alpha()
            self.skull1_rect = self.skull1.get_rect(center=(50, self.screen_height - 35))
            self.screen.blit(self.skull1, self.skull1_rect)
        if self.having_skull == 2:
            self.skull1 = pygame.image.load('assets/skull/skull0.png').convert_alpha()
            self.skull1_rect = self.skull1.get_rect(center=(50, self.screen_height - 35))
            self.screen.blit(self.skull1, self.skull1_rect)
            self.skull2 = pygame.image.load('assets/skull/skull0.png').convert_alpha()
            self.skull2_rect = self.skull2.get_rect(center=(100, self.screen_height - 35))
            self.screen.blit(self.skull2, self.skull2_rect)
        if self.having_skull == 3:
            self.skull1 = pygame.image.load('assets/skull/skull0.png').convert_alpha()
            self.skull1_rect = self.skull1.get_rect(center=(50, self.screen_height - 35))
            self.screen.blit(self.skull1, self.skull1_rect)
            self.skull2 = pygame.image.load('assets/skull/skull0.png').convert_alpha()
            self.skull2_rect = self.skull2.get_rect(center=(100, self.screen_height - 35))
            self.screen.blit(self.skull2, self.skull2_rect)
            self.skull3 = pygame.image.load('assets/skull/skull0.png').convert_alpha()
            self.skull3_rect = self.skull3.get_rect(center=(150, self.screen_height - 35))
            self.screen.blit(self.skull3, self.skull3_rect)

    def check_skull(self):
        if self.having_skull > 3: self.gameisover()


    #enemy
    def add_enemy(self):
        self.enemy_adding_time -= 1
        if self.enemy_adding_time <= 0:
            self.enemy.add(Enemy((choice([80, 1200]),randint(250, 350)), self.screen_width, self.screen_height, self.player.sprite.rect.x, self.player.sprite.rect.y, self.enemy_is_slow))
            self.enemy_adding_time = randint(50, 150)

            if self.score >= (1000 * self.enemy_count_num):
                self.enemy_adding_time -= 5 * self.enemy_count_num
                if self.score >= (1000 * self.enemy_count_num) + 1000:
                    self.enemy_count_num += 1

            if self.enemy_adding_time <= 5:
                self.enemy_adding_time = 5

    def update_player_pos(self):
        for enemy in self.enemy:
            enemy.player_x = self.player.sprite.rect.x
            enemy.player_y = self.player.sprite.rect.y

    def get_new_enemy_adding_time(self):
        num = 1
        if self.score >= 100 * num:
            self.enemy_adding_time -= 5 * num
            num += 1

    #bomb
    def add_bomb(self):
        if self.bomb_adding_time <= 0:
            self.bomb.add(Bomb((randint(150, self.screen_width-150), randint(150, self.screen_height-150))))
            self.bomb_adding_time = 600
        self.bomb_adding_time -= 1

    def display_countdown(self):
        for bomb in self.bomb:
            draw_text(f'{round(self.bomb_adding_time/60)}', ('#F7EDDC'), 40, self.screen, (bomb.rect.midtop[0], bomb.rect.midtop[1] - 15))

    def kill_bomb(self):
        if self.bomb_adding_time <= 0:
            for bomb in self.bomb:
                bomb.kill()
            self.explosion_sound.play()
            self.having_skull += 1

    def bomb_stop_working(self):
        self.bomb_adding_time += 2


    #slow
    def add_slow(self):
        if self.slow_adding_time <= 0:
            self.slow.add(Slow((randint(200, self.screen_width - 200), randint(200, self.screen_height - 200))))
            self.slow_adding_time = randint(2000, 4000)
        self.slow_adding_time -= 1

    def enemy_slow_status(self):
        if self.enemy_is_slow:
            for enemy in self.enemy:
                enemy.enemy_speed = 1
            self.slow_using_time -= 1
            if self.slow_using_time <= 0:
                self.enemy_is_slow = False
                for enemy in self.enemy:
                    enemy.enemy_speed = 2
                    enemy.enemy_is_slow = False
                self.slow_using_time = 500


    #heart
    def add_heart(self):
        if self.heart_adding_time <= 0:
            self.heart.add(Heart((randint(200, self.screen_width - 200), randint(200, self.screen_height - 200))))
            self.heart_adding_time = randint(1000, 1500)
        self.heart_adding_time -= 1


    #strong
    def add_strong(self):
        if self.strong_adding_time <= 0:
            self.strong.add(Strong((randint(200, self.screen_width - 200), randint(200, self.screen_height - 200))))
            self.strong_adding_time = randint(1500, 2000)
        self.strong_adding_time -= 1

    def strong_status(self):
        if self.player_is_strong:
            self.player_life_cal = 0
            self.strong_using_time -= 1
        if self.strong_using_time <= 0:
            self.player_is_strong = False
            self.player_life_cal = 1
            self.strong_using_time = 500


    #slow and strong status
    def slow_strong_status(self):
        slow_image_status = pygame.image.load('assets/slow/slow_status_color.png')
        slow_image_status_white = pygame.image.load('assets/slow/slow_status_white.png')
        strong_image_status = pygame.image.load('assets/strong/strong_status_color.png')
        strong_image_status_white = pygame.image.load('assets/strong/strong_status_white.png')

        if self.enemy_is_slow and not self.player_is_strong:
            self.screen.blit(slow_image_status, (self.screen_width - 60, self.screen_height - 60))
            if 20 <= self.slow_using_time <= 40 or 60 <= self.slow_using_time <= 80 or 100 <= self.slow_using_time <= 120:
                self.screen.blit(slow_image_status_white, (self.screen_width - 60, self.screen_height - 60))

        elif self.player_is_strong and not self.enemy_is_slow:
            self.screen.blit(strong_image_status, (self.screen_width - 60, self.screen_height - 50))
            if 20 <= self.strong_using_time <= 40 or 60 <= self.strong_using_time <= 80 or 100 <= self.strong_using_time <= 120:
                self.screen.blit(strong_image_status_white, (self.screen_width - 60, self.screen_height - 50))

        elif self.player_is_strong and self.enemy_is_slow:
            self.screen.blit(slow_image_status, (self.screen_width - 60, self.screen_height - 60))
            self.screen.blit(strong_image_status, (self.screen_width - 120, self.screen_height - 50))
            if 20 <= self.slow_using_time <= 40 or 60 <= self.slow_using_time <= 80 or 100 <= self.slow_using_time <= 120:
                self.screen.blit(slow_image_status_white, (self.screen_width - 60, self.screen_height - 60))
            if 20 <= self.strong_using_time <= 40 or 60 <= self.strong_using_time <= 80 or 100 <= self.strong_using_time <= 120:
                self.screen.blit(strong_image_status_white, (self.screen_width - 120, self.screen_height - 50))


    #coin
    def add_coin(self):
        if self.coin_adding_time <= 0:
            self.coin.add(Coin((randint(200, self.screen_width - 200), randint(200, self.screen_height - 200))))
            self.coin_adding_time = randint(500, 700)
        self.coin_adding_time -= 1


    #collision
    def collision(self):
        keys = pygame.key.get_pressed()
        if self.player.sprite.bullet:
            for bullet in self.player.sprite.bullet:
                if pygame.sprite.spritecollide(bullet, self.enemy, True):
                    bullet.kill()
                    self.enemy_sound.play()

        if self.enemy:
            for enemy in self.enemy:
                if pygame.sprite.spritecollide(enemy, self.player, False):
                    enemy.kill()
                    self.player_life -= self.player_life_cal
                    if not self.player_is_strong: self.die_sound.play()
                    else: self.enemy_sound.play()

        if self.bomb:
            for bomb in self.bomb:
                if pygame.sprite.spritecollide(bomb, self.player, False) and keys[pygame.K_e]:
                    bomb.kill()
                    self.score += 10
                    self.bomb_adding_time = 0
                    self.bomb_stop_sound.play()

        if self.slow:
            for slow in self.slow:
                if pygame.sprite.spritecollide(slow, self.player, False):
                    slow.kill()
                    self.enemy_is_slow = True
                    self.item_sound.play()

        if self.heart:
            for heart in self.heart:
                if pygame.sprite.spritecollide(heart, self.player, False):
                    heart.kill()
                    if self.player_life < 10:
                        self.player_life += 1
                    self.heart_sound.play()

        if self.strong:
            for strong in self.strong:
                if pygame.sprite.spritecollide(strong, self.player, False):
                    strong.kill()
                    self.player_is_strong = True
                    self.item_sound.play()

        if self.coin:
            for coin in self.coin:
                if pygame.sprite.spritecollide(coin, self.player, False):
                    coin.kill()
                    self.score += 20
                    self.coin_sound.play()


    #gameover
    def gameisover(self):
        self.player_stutus = 0

    def run(self):
        self.screen.blit(self.bg_image, (0,0))

        self.player.update()
        self.enemy.update()

        self.display_countdown()
        self.display_score()
        self.display_skull()

        #draw on screen
        self.bomb.draw(self.screen)
        self.slow.draw(self.screen)
        self.heart.draw(self.screen)
        self.strong.draw(self.screen)
        self.coin.draw(self.screen)
        self.enemy.draw(self.screen)
        self.player.draw(self.screen)
        self.player.sprite.bullet.draw(self.screen)

        #life
        self.check_life()
        self.display_life()

        #enemy
        self.add_enemy()
        self.update_player_pos()

        #bomb
        self.add_bomb()
        self.kill_bomb()
        self.bomb.update()

        #skull
        self.check_skull()
        self.display_skull()

        #slow
        self.add_slow()
        self.enemy_slow_status()
        self.slow.update()

        #heart
        self.add_heart()
        self.heart.update()

        #strong
        self.add_strong()
        self.strong_status()
        self.strong.update()

        self.slow_strong_status()

        #coin
        self.add_coin()
        self.coin.update()

        self.collision()