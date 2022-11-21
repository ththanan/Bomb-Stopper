import pygame, sys
from gamerun import Gamerun

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bomb Stopper')
icon_pic = pygame.image.load('../Infographics/bomb/bomb0.png')
pygame.display.set_icon(icon_pic)
clock = pygame.time.Clock()

gamerun = Gamerun(screen, screen_width, screen_height, clock)
gamestatus = 1
prev_player_score = 0
new_player_score = 0

font = pygame.font.Font('../Infographics/mago3.ttf', 50)
scores = []
rankscores = []
show = 0

bg_music = pygame.mixer.Sound('../Infographics/audio/Track 6 (Traffic Lights).wav')
bg_music.set_volume(0.3)
bg_music.play(loops=-1)

gamestart_sound = pygame.mixer.Sound('../Infographics/audio/game_start.wav')
gamestart_sound.set_volume(0.6)

def ranking():
    global scores, rankscores, show
    if show != 1:
        scores = []
        rankscores = []
        with open('score.txt') as file:
            for line in file:
                name, score = line.split(',')
                score = int(score)
                scores.append((name, score))
            scores.sort(key=lambda s: s[1])
            scores.reverse()
            for num in range(0, 5):
                rankscores.insert(num, scores[num])
            file.flush()
            show = 1

def display_rank():
    ranking()
    space = 0
    for i in range(0, 5):
        draw_text_rank(f'{rankscores[i][0]}', ('#61452C'), 50, screen, (screen_width / 2 - 250 + 3, 230 + 3 + space))
        draw_text_rank(f'{rankscores[i][0]}', ('#FFF4EB'), 50, screen, (screen_width / 2 - 250, 230 + space))
        space += 50

    space = 0
    for i in range(0, 5):
        draw_text_rank(f'{rankscores[i][1]}', ('#61452C'), 50, screen, (screen_width / 2 + 200 + 3, 230 + 3 + space))
        draw_text_rank(f'{rankscores[i][1]}', ('#FFF4EB'), 50, screen, (screen_width / 2 + 200, 230 + space))
        space += 50

def draw_text(text, color, size, screen, pos):
    global screen_width, screen_height
    font = pygame.font.Font('../Infographics/mago3.ttf', size)
    textobj = font.render(text, False, color)
    textrect = textobj.get_rect(center = pos)
    screen.blit(textobj, textrect)

def draw_text_rank(text, color, size, screen, pos):
    global screen_width, screen_height
    font = pygame.font.Font('../Infographics/mago3.ttf', size)
    textobj = font.render(text, False, color)
    textrect = textobj.get_rect(midleft = pos)
    screen.blit(textobj, textrect)

def menu():
    while True:
        global screen_width, screen_height, show, prev_player_score, new_player_score
        show = 0
        prev_player_score = 0
        new_player_score = 0
        background_image = pygame.image.load('../Infographics/bg1.png')
        screen.blit(background_image, (0, 0))

        draw_text('BOMB STOPPER', ('#61452C'), 160, screen, (screen_width/2 +3, screen_height/2 - 100 +3))
        draw_text('BOMB STOPPER', ('#FFF4EB'), 160, screen, (screen_width/2, screen_height/2 - 100))

        draw_text('BY 65010434 THANANYA CEMARKHARN', ('#61452C'), 40, screen, (screen_width/2 +3, screen_height/2 + 20 +3))
        draw_text('BY 65010434 THANANYA CEMARKHARN', ('#FAECDA'), 40, screen, (screen_width/2, screen_height/2 + 20))

        game_button = pygame.Rect((420, 450), (150, 50))
        rank_button = pygame.Rect((710, 450), (150, 50))
        pygame.draw.rect(screen, ('#61452C'), game_button)
        pygame.draw.rect(screen, ('#61452C'), rank_button)

        draw_text('PLAY', ('#FFF4EB'), 50, screen, (500, 473))
        draw_text('RANK', ('#FFF4EB'), 50, screen, (790, 473))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if game_button.collidepoint((mx, my)):
                    gamestart_sound.play()
                    game()
                if rank_button.collidepoint((mx, my)):
                    rank()

        pygame.display.update()
        clock.tick(60)

def game():
    while True:
        global gamestatus, prev_player_score, new_player_score
        new_player_score = gamerun.score
        if new_player_score >= prev_player_score:
            prev_player_score = new_player_score

        if gamestatus == 1:
            gamerun.run()
            gamestatus = gamerun.player_status
        if gamestatus == 0:
            gameover()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def rank():
    while True:
        background_image = pygame.image.load('../Infographics/bg1.png')
        screen.blit(background_image, (0, 0))

        draw_text('RANK', ('#61452C'), 100, screen, (screen_width/2 +3, 140 +3))
        draw_text('RANK', ('#FFF4EB'), 100, screen, (screen_width/2, 140))

        menu_button = pygame.Rect((950, 500), (150, 50))
        pygame.draw.rect(screen, ('#61452C'), menu_button)

        draw_text('BACK', ('#FFF4EB'), 50, screen, (1030, 523))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if menu_button.collidepoint((mx, my)):
                    menu()

        display_rank()

        pygame.display.update()
        clock.tick(60)

def gameover():
    user_ip = ''
    text_box = pygame.Rect((screen_width/2 - 350/2, screen_height/2 - 20), (350, 50))
    active = False
    while True:
        global gamestatus, gamerun

        gamerun = Gamerun(screen, screen_width, screen_height, clock)
        gamestatus = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if text_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if menu_button.collidepoint((mx, my)):
                    file = open('score.txt', 'a')
                    file.write(f'{user_ip}, {prev_player_score}\n')
                    file.flush()
                    file.close()
                    menu()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_ip = user_ip[:-1]
                    else:
                        user_ip += event.unicode
                        if surf.get_width() > text_box.w - 20:
                            user_ip = user_ip[:-1]


        background_image = pygame.image.load('../Infographics/bg1.png')
        screen.blit(background_image, (0, 0))
        draw_text('GAMEOVER', ('#F7EDDC'), 100, screen, (screen_width / 2 + 3, 140 + 3))
        draw_text('GAMEOVER', ('#FF4133'), 100, screen, (screen_width / 2, 140))

        draw_text(f'score : {prev_player_score}', ('#996633'), 50, screen, (screen_width/2 +3, 195 +3))
        draw_text(f'score : {prev_player_score}', ('#F7EDDC'), 50, screen, (screen_width/2, 195))

        draw_text('TYPE YOUR NAME', ('#996633'), 50, screen, (screen_width/2 +3, 300 +3))
        draw_text('TYPE YOUR NAME', ('#F7EDDC'), 50, screen, (screen_width/2, 300))

        menu_button = pygame.Rect((920, 500), (200, 50))
        pygame.draw.rect(screen, ('#61452C'), menu_button)
        draw_text('CONTINUE', ('#FFF4EB'), 50, screen, (1020, 523))

        if active:
            color = pygame.Color('#FFF1E6')
        else:
            color = pygame.Color('#AE7A4D')

        pygame.draw.rect(screen, color, text_box)
        surf = font.render(user_ip, True, '#7D5536')
        screen.blit(surf, (text_box.x + 5, text_box.y + 5))

        pygame.display.update()
        clock.tick(60)

menu()