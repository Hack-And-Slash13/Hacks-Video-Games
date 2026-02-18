import pygame, random, threading, time
from pygame.locals import *
pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 50
clock = pygame.time.Clock()

def reset():
    global px, py, player_imagex, star_list, enemy_list, asteroid_masks, stars, enemies, dead, game_over, difficulty
    px = round(width/2 - 80)
    py = round(height - 250)
    player_imagex = 0
    star_list = []
    enemy_list = []
    stars = 0
    enemies = 0
    dead = False
    game_over = False
    difficulty = 1
def move():
    global px, py
    keys = pygame.key.get_pressed()
    if keys[K_a] == True and px > 0:
        px -= 15
    if keys[K_d] == True and px < (width - 160):
        px += 15
    if keys[K_w] == True and py > 0:
        py -= 20
    if keys[K_s] == True and py < (height - 160):
        py += 13
    else:
        try:
            if joysticks[0].get_axis(0) < -.25 and px > 0:
                px -= 15
            if joysticks[0].get_axis(0) > .25 and px < (width - 160):
                px += 15
            if joysticks[0].get_axis(1) > .25 and py < (height - 160):
                py += 13
            if joysticks[0].get_axis(1) < -.25 and py > 0:
                py -= 20
        except IndexError:
            pass
class star:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
    def move(thing, *args):
        global stars, star_list
        thing.y += 50
        pygame.draw.polygon(screen, thing.color, ((thing.x - thing.size, thing.y), (thing.x, thing.y - thing.size), (thing.x + thing.size, thing.y), (thing.x, thing.y + thing.size)))
        if thing.y > height:
            stars -= 1
            star_list.remove(thing)

class asteroid:
    def __init__(self, x, y, enemy_imagex, size):
        self.x = x
        self.y = y
        self.enemy_imagex = enemy_imagex
        self.size = size
    def move(e, *args):
        global difficulty, enemies, enemy_list, direction, dead, spaceship, px, py, direction, rotation, counter
        e.y += 40*difficulty
        e.enemy_imagex += e.size
        if e.enemy_imagex >= ((e.size*7) - e.size):
            e.enemy_imagex = 0
        resized_asteroid = pygame.transform.scale(asteroids, (e.size*7, e.size))
        resized_asteroid.set_colorkey(Color(255, 255, 255))
        screen.blit(resized_asteroid, (e.x, e.y), area=(e.size*round(e.enemy_imagex/e.size), 0, e.size, e.size))
        if e.y > height:
            enemies -= 1
            enemy_list.remove(e)
        if dead == False:
            counter = 1
            asteroid_sprite = resized_asteroid.subsurface((e.size*round(e.enemy_imagex/e.size), 0, e.size, e.size))
            mask = pygame.mask.from_surface(asteroid_sprite)
            spaceship_sprite = spaceship.subsurface((160*round(player_imagex/160), 0, 160, 160))
            spaceship_mask = pygame.mask.from_surface(spaceship_sprite)
            asteroid_rect = mask.get_rect(center=((e.x+e.size/2),(e.y+e.size/2)))
            offset = (e.x - px, e.y - py)
            if mask.overlap(spaceship_mask, offset):
                if px > asteroid_rect.x:
                    direction = "right"
                    rotation = -20
                else:
                    direction = "left"
                    rotation = 20
                dead = True

def spawn():
    global stars, enemy_list, enemies, stars, star_list, spaceship
    number = random.randint(1, 5)
    if number == 1:
        color = pygame.Color(255, 244, 232)
    elif number == 2:
        color = pygame.Color(244, 244, 0)
    elif number == 3:
        color = pygame.Color(255, 241, 223)
    elif number == 4:
        color = pygame.Color(255, 235, 209)
    elif number == 5:
        color = pygame.Color(244, 86, 0)
    if number > 2:
        stars += 1
        number = random.randint(1, 5)
    if number <= difficulty:
        e_number = random.randint(0, width)
        asize = random.randint(50, 200)
        Enemy = asteroid(e_number, -asize, 0, asize)
        enemy_list.append(Enemy)
        enemies += 1
    number = random.randint(0, width)
    size = random.randint(0, 2)
    Star = star(number, 0, color, size)
    star_list.append(Star)
    for s in range(stars):
        try:
            star_list[s].move(star_list[s - 1])
        except IndexError:
            pass
    if dead == False:
        screen.blit(spaceship, (px, py), area=(160*round(player_imagex/160), 0, 160, 160))
    for e in range(enemies):
        try:
            enemy_list[e].move(enemy_list[e -1])
        except IndexError:
            pass

def increase_difficulty():
    global difficulty, dead
    while dead == False:
        time.sleep(10)
        difficulty += 1

reset()
cutscene = True
image = pygame.image.load("spaceship_spritesheet.png")
spaceship = pygame.transform.scale(image, (1120, 160))
spaceship.set_colorkey(Color(0, 0, 0))
asteroids = pygame.image.load("asteroid_spritesheet.png")
asteroids.set_colorkey(Color(255, 255, 255))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cosmo Crash")

running = True
while running == True:
    player_imagex += 100
    if player_imagex >= 960:
        player_imagex = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYDEVICEADDED:
            joysticks.append(pygame.joystick.Joystick(event.device_index))
    screen.fill(pygame.Color(0, 0, 0))
    if cutscene == True:
        font = pygame.font.SysFont(None, 100, bold=True)
        text = font.render("Cosmo Crash", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 100)
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 70, bold=True)
        text = font.render("Dodge the Asteroids!", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2)
        screen.blit(text, text_rect)
        text = font.render("Press enter to play", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 50)
        screen.blit(text, text_rect)
        keys = pygame.key.get_pressed()
        if keys[K_RETURN] == True:
            threading.Thread(target=increase_difficulty).start()
            cutscene = False
    elif game_over == True:
        text = font.render("Game Over", False, Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 50)
        screen.blit(text, text_rect)
        text = font.render("Press enter to play again", False, Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 50)
        screen.blit(text, text_rect)
        keys = pygame.key.get_pressed()
        if keys[K_RETURN] == True:
            reset()
    elif dead == True:
        spawn()
        if direction == "right":
            px += 40
        else:
            px -= 40
        counter += 1
        py -= 30
        rotated_spaceship = pygame.surface.Surface((1120, 1600))
        sprite = spaceship.subsurface((160, 0, 160, 160))
        sprite = pygame.transform.rotozoom(sprite, rotation*counter, 1)
        sprite.set_colorkey(Color(0, 0, 0))
        screen.blit(sprite, (px, py))
        if px > width+320 or px < -320 or py < -320:
            game_over = True
    else:
        move()
        spawn()
    pygame.display.update()
    clock.tick(20)
pygame.quit()
exit()
