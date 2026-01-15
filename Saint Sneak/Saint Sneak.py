import pygame, time
from pygame.locals import *
pygame.init()
pygame.mixer.init()
length = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 50
counter = 0
player_stepx = round(432/3)
player_stepy = round(782/5)
enemy_stepx = round(1296/5)
enemy_stepy = round(2346/12)
px = 100
py = height - player_stepy - 30
player_imagex = player_stepx
player_imagey = player_stepx
e1x = 500
e1y = 20
e2x = length - 500
e2y = height + 100
e3x = 750
e3y = 575
hit_box = pygame.Rect((px, py, player_stepx, player_stepy))
enemy1_imagex = 0
enemy1_imagey = 0
enemy2_imagex = 0
enemy2_imagey = enemy_stepy * 3
enemy3_imagex = 0
enemy3_imagey = enemy_stepy * 3
enemy1_direction = "down"
enemy2_direction = "up"
enemy3_direction = "right"
caught = False
game_over = False
victory = False
cut_scene = True
dead = False
font = pygame.font.SysFont(None, 50, bold=False)
enemy = pygame.image.load("knight_spritesheet.png")
player = pygame.image.load("priest_spritesheet.png")
resized_player = pygame.transform.scale(player, (432, 782))
resized_enemy = pygame.transform.scale(enemy, (1296, 2346))
resized_enemy.set_colorkey(Color(255, 255, 255))
resized_player.set_colorkey(Color(255, 255, 255))
screen = pygame.display.set_mode((length, height))
screen.fill(Color(0, 0, 0))
pygame.display.set_caption("Saint Sneak")
pygame.mixer.music.load("rock_song.mp3")
pygame.mixer.music.play(-1)
running = True
while running == True:
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if cut_scene == True:
        screen.fill(Color(0, 0, 0))
        counter += 1
        text = font.render("You are a preist. Get to the house to do mass in", False, Color(255, 255, 255))
        text2 = font.render("secret without getting caught by the guards!", False, Color(255, 255, 255))
        text3 = font.render("Use the arrow keys to move.", False, Color(255, 255, 255))
        screen.blit(text, (length/4, height/3))
        screen.blit(text2, (length/4, height/3 + 50))
        screen.blit(text3, (length/3, height/3 + 100))
        if counter >= 256:
            counter = 0
            cut_scene = False
    else:
        if caught == True:
            if e1x > px + 50:
                enemy1_direction = "left"
                enemy1_imagey = enemy_stepy * 2
                enemy1_imagex += 50
                e1x -= 25
            elif e1x < px - 50:
                enemy1_direction = "right"
                enemy1_imagey = enemy_stepy * 3
                enemy1_imagex += 50
                e1x += 25
            elif e1y < py - 50:
                enemy1_direction = "down"
                enemy1_imagey = 0
                enemy1_imagex += 50
                e1y += 25
            elif e1y > py + 50:
                enemy1_direction = "up"
                enemy1_imagey = enemy_stepy
                enemy1_imagex += 50
                e1y -= 25
            else:
                game_over = True
                if e1x > px:
                    enemy1_direction = "left"
                    enemy1_imagey = enemy_stepy * 6
                elif e1x < px:
                    enemy1_direction = "right"
                    enemy1_imagey = enemy_stepy * 7
                elif e1y > py:
                    enemy1_direction = "down"
                    enemy1_imagey = enemy_stepy * 4
                elif e1y < py:
                    enemy1_direction = "up"
                    enemy1_imagey = enemy_stepy * 5
                enemy1_imagex += 60
                player_imagey = player_stepy * 4
                if player_imagex < 432 - player_stepx:
                    player_imagex += 10
            if e2x > px + 50:
                enemy2_direction = "left"
                enemy2_imagey = enemy_stepy * 2
                enemy2_imagex += 50
                e2x -= 25
            elif e2x < px - 50:
                enemy2_direction = "right"
                enemy2_imagey = enemy_stepy * 3
                enemy2_imagex += 50
                e2x += 25
            elif e2y > py + 50:
                enemy2_direction = "up"
                enemy2_imagey = enemy_stepy
                enemy2_imagex += 50
                e2y -= 25
            elif e2y < py - 50:
                enemy2_direction = "down"
                enemy2_imagey = 0
                enemy2_imagex += 50
                e2y += 25
            else:
                game_over = True
                if e2x > px:
                    enemy2_direction = "left"
                    enemy2_imagey = enemy_stepy * 6
                elif e2x < px:
                    enemy2_direction = "right"
                    enemy2_imagey = enemy_stepy * 7
                elif e2y > py:
                    enemy2_direction = "down"
                    enemy2_imagey = enemy_stepy * 4
                elif e2y < py:
                    enemy2_direction = "up"
                    enemy2_imagey = enemy_stepy * 5
                enemy2_imagex += 60
                player_imagey = player_stepy * 4
                if player_imagex < 432 - player_stepx:
                    player_imagex += 10
            if e3x > px + 50:
                enemy3_direction = "left"
                enemy3_imagey = enemy_stepy * 2
                enemy3_imagex += 50
                e3x -= 25
            elif e3x < px - 50:
                enemy3_direction = "right"
                enemy3_imagey = enemy_stepy * 3
                enemy3_imagex += 50
                e3x += 25
            elif e3y > py + 50:
                enemy3_direction = "up"
                enemy3_imagey = enemy_stepy
                enemy3_imagex += 50
                e3y -= 25
            elif e3y < py - 50:
                enemy3_direction = "down"
                enemy3_imagey = 0
                enemy3_imagex += 50
                e3y += 25
            else:
                game_over = True
                if e3x > px:
                    enemy3_direction = "left"
                    enemy3_imagey = enemy_stepy * 6
                elif e3x < px:
                    enemy3_direction = "right"
                    enemy3_imagey = enemy_stepy * 7
                elif e1y > py:
                    enemy3_direction = "down"
                    enemy3_imagey = enemy_stepy * 4
                if e3y < py:
                    enemy3_direction = "up"
                    enemy3_imagey = enemy_stepy * 5
                enemy3_imagex += 60
                player_imagey = player_stepy * 4
                if player_imagex < 432 - player_stepx:
                    player_imagex += 10
        if enemy1_imagex >= 1296 - enemy_stepx:
            enemy1_imagex = 0
        if enemy2_imagex >= 1296 - enemy_stepx:
            enemy2_imagex = 0
        if enemy3_imagex >= 1296 - enemy_stepx:
            enemy3_imagex = 0
        if game_over == True and dead == False:
            dead = True
            pygame.mixer.music.load("womp-womp.mp3")
            pygame.mixer.music.play(1)
        keys = pygame.key.get_pressed()
        if dead == True or victory == True:
            if keys[pygame.K_q]:
                running = False
            elif keys[pygame.K_p]:
                screen.fill(Color(0, 0, 0))
                pygame.display.set_caption("Saint Sneak")
                px = 100
                py = height - player_stepy - 30
                player_imagex = player_stepx
                player_imagey = player_stepx
                e1x = 500
                e1y = 20
                e2x = length - 500
                e2y = height + 100
                e3x = 750
                e3y = 575
                hit_box = pygame.Rect((px, py, player_stepx, player_stepy))
                enemy1_imagex = 0
                enemy1_imagey = 0
                enemy2_imagex = 0
                enemy2_imagey = enemy_stepy * 3
                enemy3_imagex = 0
                enemy3_imagey = enemy_stepy * 3
                enemy1_direction = "down"
                enemy2_direction = "up"
                enemy3_direction = "right"
                caught = False
                game_over = False
                victory = False
                cut_scene = True
                dead = False
                font = pygame.font.SysFont(None, 50, bold=False)
                counter = 0
                pygame.mixer.music.stop()
                pygame.mixer.music.load("rock_song.mp3")
                pygame.mixer.music.play(-1)
        if keys[pygame.K_LEFT] and game_over == False and victory == False:
            if px > -30:
                px -= 10
            player_imagex += 20
            player_imagey = player_stepy*3
        if keys[pygame.K_RIGHT] and game_over == False and victory == False:
            if px < length - player_stepx + 20:
                px += 10
            player_imagex += 20
            player_imagey = player_stepy
        if keys[pygame.K_DOWN] and game_over == False and victory == False:
            if py < height - player_stepy:
                py += 10
            player_imagex += 20
            player_imagey = player_stepy*2
        if keys[pygame.K_UP] and game_over == False and victory == False:
            if py > -30:
                py -= 10
            player_imagex += 20
            player_imagey = 0
        if player_imagex >= 144 + player_stepx and game_over == False:
            player_imagex = 0
        if px > length - 220 and py < 210 and caught == False:
            victory = True
        drawn_hit_box = pygame.draw.rect(screen, Color(0, 128, 64, 0), (px, py, player_stepx, player_stepy))
        e1circle = pygame.draw.circle(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), 200)
        e2circle = pygame.draw.circle(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), 200)
        e3circle = pygame.draw.circle(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), 200)
        if enemy1_direction == "down":
            e1line_of_sight1 = pygame.draw.line(screen, Color(0, 128, 64, 0), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 - 500, e1y + enemy_stepy/2 + 1000), 10)
            e1line_of_sight2 = pygame.draw.line(screen, Color(0, 128, 64, 0), (e1x + enemy_stepx/2 - 500, e1y + enemy_stepy/2 + 1000), (e1x + enemy_stepx/2 + 500, e1y - enemy_stepy/2 + 1000), 10)
            e1line_of_sight3 = pygame.draw.line(screen, Color(0, 128, 64, 0), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 + 500, e1y - enemy_stepy/2 + 1000), 10)
            e1line_of_sight4 = pygame.draw.line(screen, Color(0, 128, 64, 0), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2, e1y - enemy_stepy/2 + 1000), 10)
            e1line_of_sight5 = pygame.draw.line(screen, Color(0, 128, 64, 0), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 + 250, e1y - enemy_stepy/2 + 1000), 10)
            e1line_of_sight6 = pygame.draw.line(screen, Color(0, 128, 64, 0), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 - 250, e1y - enemy_stepy/2 + 1000), 10)
        elif enemy1_direction == "left":
            e1line_of_sight1 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 - 1000, e1y + enemy_stepy/2 - 500), 10)
            e1line_of_sight2 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2 - 1000, e1y + enemy_stepy/2 - 500), (e1x + enemy_stepx/2 - 1000, e1y + enemy_stepy/2 + 500), 10)
            e1line_of_sight3 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 - 1000, e1y + enemy_stepy/2 + 500), 10)
            e1line_of_sight4 = pygame.draw.line(screen, Color(0, 128, 64, 0), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 - 1000, e1y - enemy_stepy/2), 10)
            e1line_of_sight5 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 - 1000, e1y + enemy_stepy/2 + 250), 10)
            e1line_of_sight6 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 - 1000, e1y + enemy_stepy/2 - 250), 10)
        else:
            e1line_of_sight1 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 + 1000, e1y + enemy_stepy/2 + 500), 10)
            e1line_of_sight2 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2 + 1000, e1y + enemy_stepy/2 + 500), (e1x + enemy_stepx/2 + 1000, e1y + enemy_stepy/2 - 500), 10)
            e1line_of_sight3 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 + 1000, e1y + enemy_stepy/2 + 500), 10)
            e1line_of_sight4 = pygame.draw.line(screen, Color(0, 128, 64, 0), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 + 1000, e1y - enemy_stepy/2), 10)
            e1line_of_sight5 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 + 1000, e1y + enemy_stepy/2 + 250), 10)
            e1line_of_sight6 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e1x + enemy_stepx/2, e1y + enemy_stepy/2), (e1x + enemy_stepx/2 + 1000, e1y + enemy_stepy/2 - 250), 10)
        if enemy2_direction == "up":
           e2line_of_sight1 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2 - 500, e2y + enemy_stepy/2 - 1000), 10)
           e2line_of_sight2 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2 - 500, e2y + enemy_stepy/2 - 1000), (e2x + enemy_stepx/2 + 500, e2y - enemy_stepy/2 - 1000), 10)
           e2line_of_sight3 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2 + 500, e2y - enemy_stepy/2 - 1000), 10)
           e2line_of_sight4 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2, e2y - enemy_stepy/2 - 1000), 10)
           e2line_of_sight5 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2 + 250, e2y - enemy_stepy/2 - 1000), 10)
           e2line_of_sight6 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2 - 250, e2y - enemy_stepy/2 - 1000), 10)
        else:
            e2line_of_sight1 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2 - 500, e2y + enemy_stepy/2 + 1000), 10)
            e2line_of_sight2 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2 - 500, e2y + enemy_stepy/2 + 1000), (e2x + enemy_stepx/2 + 500, e2y + enemy_stepy/2 + 1000), 10)
            e2line_of_sight3 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2 + 500, e2y + enemy_stepy/2 + 1000), 10)
            e2line_of_sight4 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2, e2y + enemy_stepy/2 + 1000), 10)
            e2line_of_sight5 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2 + 250, e2y + enemy_stepy/2 + 1000), 10)
            e2line_of_sight6 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e2x + enemy_stepx/2, e2y + enemy_stepy/2), (e2x + enemy_stepx/2 - 250, e2y + enemy_stepy/2 + 1000), 10)
        if enemy3_direction == "left":
            e3line_of_sight1 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2 - 1000, e3y + enemy_stepy/2 - 500), (e3x + enemy_stepx/2 - 1000, e3y - enemy_stepy/2 + 500), 10)
            e3line_of_sight2 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 - 1000, e3y + enemy_stepy/2 - 500), 10)
            e3line_of_sight3 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 - 1000, e3y - enemy_stepy/2 + 500), 10)
            e3line_of_sight4 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 - 1000, e3y - enemy_stepy/2), 10)
            e3line_of_sight5 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 - 1000, e3y - enemy_stepy/2 + 250), 10)
            e3line_of_sight6 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 - 1000, e3y - enemy_stepy/2 - 250), 10)
        elif enemy3_direction == "up":
            e3line_of_sight1 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 - 500, e3y + enemy_stepy/2 - 1000), 10)
            e3line_of_sight2 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2 - 500, e3y + enemy_stepy/2 - 1000), (e3x + enemy_stepx/2 + 500, e3y - enemy_stepy/2 - 1000), 10)
            e3line_of_sight3 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 + 500, e3y - enemy_stepy/2 - 1000), 10)
            e3line_of_sight4 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2, e3y - enemy_stepy/2 - 1000), 10)
            e3line_of_sight5 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 + 250, e3y - enemy_stepy/2 - 1000), 10)
            e3line_of_sight6 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 - 250, e3y - enemy_stepy/2 - 1000), 10)
        else:
            e3line_of_sight1 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 + 1000, e3y + enemy_stepy/2 + 500), 10)
            e3line_of_sight2 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2 + 1000, e3y + enemy_stepy/2 + 500), (e3x + enemy_stepx/2 + 1000, e3y + enemy_stepy/2 - 500), 10)
            e3line_of_sight3 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 + 1000, e3y + enemy_stepy/2 - 500), 10)
            e3line_of_sight4 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 + 1000, e3y + enemy_stepy/2), 10)
            e3line_of_sight5 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 + 1000, e3y + enemy_stepy/2 + 250), 10)
            e3line_of_sight6 = pygame.draw.line(screen, (Color(0, 128, 64, 0)), (e3x + enemy_stepx/2, e3y + enemy_stepy/2), (e3x + enemy_stepx/2 + 1000, e3y + enemy_stepy/2 - 250), 10)
        screen.fill(Color(0, 128, 64))
        pygame.draw.polygon(screen, Color(100, 65, 45), ((0, height), (length - 220, 200), (length, 200), (400, height)))
        pygame.draw.rect(screen, Color(150, 150, 150), (length - 220, 0, 200, 200))
        pygame.draw.rect(screen, Color(100, 100, 100), (length - 20, 0, 50, 200))
        pygame.draw.rect(screen, Color(200, 100, 0), (length - 150, 100, 50, 100))
        pygame.draw.circle(screen, Color(80, 20, 0), (length - 115, 160), 5)
        if victory == False:
            screen.blit(resized_player, (px, py), (player_stepx*round(player_imagex/player_stepx), player_stepy*round(player_imagey/player_stepy), player_stepx, player_stepy))
        screen.blit(resized_enemy, (e1x, e1y), (enemy_stepx*round(enemy1_imagex/enemy_stepx), enemy_stepy*round(enemy1_imagey/enemy_stepy), enemy_stepx, enemy_stepy))
        screen.blit(resized_enemy, (e2x, e2y), (enemy_stepx*round(enemy2_imagex/enemy_stepx), enemy_stepy*round(enemy2_imagey/enemy_stepy), enemy_stepx, enemy_stepy))
        screen.blit(resized_enemy, (e3x, e3y), (enemy_stepx*round(enemy3_imagex/enemy_stepx), enemy_stepy*round(enemy3_imagey/enemy_stepy), enemy_stepx, enemy_stepy))
        if victory == False:
            if drawn_hit_box.x >= e1x + 100 and hit_box.x <= e1x - 100:
                caught = True
            if drawn_hit_box.y >= e1y + 100 and hit_box.y <= e1y - 100:
                caught = True
            if drawn_hit_box.x >= e2x + 100 and hit_box.x <= e2x - 100:
                caught = True
            if drawn_hit_box.y >= e2y + 100 and hit_box.y <= e2y - 100:
                caught = True
            if drawn_hit_box.x >= e3x + 100 and hit_box.x <= e3x - 100:
                caught = True
            if drawn_hit_box.y >= e3y + 100 and hit_box.y <= e3y - 100:
                caught = True
            if drawn_hit_box.colliderect(e1line_of_sight1):
                caught = True
            if drawn_hit_box.colliderect(e1line_of_sight2):
                caught = True
            if drawn_hit_box.colliderect(e1line_of_sight3):
                caught = True
            if drawn_hit_box.colliderect(e2line_of_sight1):
                caught = True
            if drawn_hit_box.colliderect(e2line_of_sight2):
                caught = True
            if drawn_hit_box.colliderect(e2line_of_sight3):
                caught = True
            if drawn_hit_box.colliderect(e3line_of_sight1):
                caught = True
            if drawn_hit_box.colliderect(e3line_of_sight2):
                caught = True
            if drawn_hit_box.colliderect(e3line_of_sight3):
                caught = True
            if drawn_hit_box.colliderect(e1line_of_sight4):
                caught = True
            if drawn_hit_box.colliderect(e2line_of_sight4):
                caught = True
            if drawn_hit_box.colliderect(e3line_of_sight4):
                caught = True
            if drawn_hit_box.colliderect(e1line_of_sight5):
                caught = True
            if drawn_hit_box.colliderect(e2line_of_sight5):
                caught = True
            if drawn_hit_box.colliderect(e3line_of_sight5):
                caught = True
            if drawn_hit_box.colliderect(e1line_of_sight6):
                caught = True
            if drawn_hit_box.colliderect(e2line_of_sight6):
                caught = True
            if drawn_hit_box.colliderect(e3line_of_sight6):
                caught = True
        if game_over == True:
            font = pygame.font.SysFont(None, 100, bold=True)
            text = font.render("Game Over", False, Color(255, 0, 0))
            font = pygame.font.SysFont(None, 50, bold=False)
            text2 = font.render("Press P to play again. Press Q to quit", False, Color(255, 0, 0))
            screen.blit(text, (length/2 - 170, height/2 - 100))
            screen.blit(text2, (length/4 + 80, height/2))
        if victory == True:
            font = pygame.font.SysFont(None, 100, bold=True)
            text = font.render("YOU WIN!!!", False, Color(255, 255, 255))
            font = pygame.font.SysFont(None, 50, bold=False)
            text2 = font.render("Press P to play again. Press Q to quit", False, Color(255, 255, 255))
            screen.blit(text, (length/2 - 170, height/2 - 100))
            screen.blit(text2, (length/4 + 80 , height/2))
        if game_over == False and victory == False:
            enemy2_imagex += 25
            if e2y < 15:
                enemy2_imagey = 0
                enemy2_direction = "down"
            elif e2y > height - enemy_stepy - 15:
                enemy2_imagey = enemy_stepy
                enemy2_direction = "up"
            if enemy2_direction == "up":
                e2y -= 5
            else:
                e2y += 5
            if enemy2_imagex >= 1296 - enemy_stepx:
                enemy2_imagex = 0
            if counter == 80:
                enemy1_imagey = enemy_stepy * 2
                enemy1_direction = "left"
                enemy3_imagey = enemy_stepy
                enemy3_direction = "up"
            if counter == 160:
                enemy3_imagey = enemy_stepy * 2
                enemy3_direction = "left"
            if counter == 240:
                enemy1_imagey = enemy_stepy * 3
                enemy1_direction = "right"
                enemy3_imagey = enemy_stepy
                enemy3_direction = "up"
            if counter == 320:
                counter = 0
                enemy3_imagey = enemy_stepy * 3
                enemy3_direction = "right"
    pygame.display.update()
    pygame.time.Clock().tick(32)
pygame.quit()
exit()
