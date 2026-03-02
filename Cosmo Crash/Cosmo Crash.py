import pygame, random, time, threading, json, os, math
from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 50
clock = pygame.time.Clock()
insults = ["You can open your eyes now, just don't look at your score.", "Were your eyes closed?", "Are you blind?", "You know, you're not supposed to aim for the asteroids.", "I hope you have insurance.", "Nice try! Just try steering next time", "Congratulations! You got a new low score!", "womp womp whaaaa...", "Use the force", "Oh come on! It's only rocket science!", "Wow! You're only a million points away from a million points!", "Your supposed to aim for the coins, not the asteroids.", "Wow, that was fast! I thought you'd last at least 12 seconds!", "Try shooting the asteroids, instead of giving them a hug.", "Back already? I'll call the ambulance.", "Ouch! You might need to increase your insurance policy after that one.", "That was great! Next time, just try to hit the coins instead of the asteroids.", "Player: 0; Asteroids: ummm... I lost count.", "I can't tell if you have more rocks smashing your ship or in your head.", "That was dumber than a box of asteroids.", "Oh come on! A box of asteroids could've done better!", "Giant flaming asteroids are bad. Free money is good. Not the other way around.", "You know, there are better ways to get rid of a spaceship.", "Nice try! Just learn how to fly a spaceship and you'll do great!", "I'd tell you to read the instructions to that spaceship, but I don't want you to blow them up.", "Why don't you try blowing up the asteroids instead of the spaceship next time?"]
cheat_code = [K_BACKSPACE, K_SPACE, K_BACKSLASH, K_MINUS, K_c]
hard_mode_code = [K_h, K_a, K_r, K_d, K_SPACE]

def reset():
    global px, py, player_imagex, star_list, enemy_list, asteroid_masks, stars, enemies, dead, game_over, difficulty, points, font, coin_imagex, coins, coin_list, counter, invincible, key_list, cooldown, comet_spawned, Comet, Powerup, powerup_spawned, powerup_imagex, bullet_list, speed_boost, rapid_fire, high_score, hard_mode
    px = round(width/2 - 80)
    py = round(height - 250)
    player_imagex = 0
    coin_imagex = 0
    star_list = []
    enemy_list = []
    coin_list = []
    bullet_list = []
    coins = 0
    stars = 0
    enemies = 0
    points = 0
    counter = 0
    dead = False
    game_over = False
    difficulty = 1
    invincible = False
    cooldown = False
    comet_spawned = False
    Comet = None
    powerup_spawned = False
    Powerup = None
    speed_boost = False
    rapid_fire = False
    hard_mode = False
    powerup_imagex = 0
    key_list = []
    font = pygame.font.SysFont(None, 70, bold=True)
    pygame.mixer.music.load("Cosmo_Crash_song.mp3")
    high_score = load("high score", "Cosmo_Crash_save_data")

def handle_input():
    global px, py, cooldown, bulletx, bullety, speed_boost, rapid_fire, cutscene, game_over, dead, difficulty
    if cutscene == False and game_over == False and dead == False:
        keys = pygame.key.get_pressed()
        if keys[K_a] == True and px > 0:
            if speed_boost == True:
                px -= 15*difficulty
            px -= 10*difficulty
        if keys[K_d] == True and px < (width - 160):
            if speed_boost == True:
                px += 10
            px += 15*difficulty
        if keys[K_w] == True and py > 0:
            if speed_boost == True:
                py -= 15
            py -= 20*difficulty
        if keys[K_s] == True and py < (height - 160):
            if speed_boost == True:
                py += 8
            py += 13*difficulty
        else:
            try:
                for joystick in joysticks:
                    if joystick.get_axis(0) < -.25 and px > 0:
                        if speed_boost == True:
                            px -= 15
                        px -= 15*difficulty
                    if joystick.get_axis(0) > .25 and px < (width - 160):
                        if speed_boost == True:
                            px += 15
                        px += 15*difficulty
                    if joystick.get_axis(1) > .25 and py < (height - 160):
                        if speed_boost == True:
                            py += 13
                        py += 13*difficulty
                    if joystick.get_axis(1) < -.25 and py > 0:
                        if speed_boost == True:
                            py -= 20
                        py -= 20*difficulty
            except IndexError:
                pass
    try:
        for joystick in joysticks:
            name = joystick.get_name().lower()
            if (joystick.get_button(7) and "xbox" in name) or (joystick.get_button(6) and "nano" in name) or (joystick.get_button(7) and "nano" not in name and "xbox" not in name):
                if cutscene == True:
                    font = pygame.font.SysFont(None, 40, bold=True)
                    pygame.mixer.music.play(-1)
                    difficulty = 1
                    counter = 0
                    cutscene = False
                if game_over == True:
                    reset()
                    pygame.mixer.music.play(-1)
                if cutscene == True or game_over == True:
                    cutscene = False
                    game_over = False
                    difficulty = 1
                    counter = 0
                    pygame.mixer.music.play(-1)
            if joystick.get_button(0):
                if rapid_fire == True or (cooldown == False and bullet_list == []):
                    laser_sound.play()
                    Bullet = bullet(px + 80, py)
                    bullet_list.append(Bullet)
    except IndexError:
        pass

def save(data, name):
    if not os.path.exists("Cosmo_Crash_save_data"):
        os.makedirs("Cosmo_Crash_save_data")
    filepath = os.path.join("Cosmo_Crash_save_data", name)
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        return None

def load(data, folder=None):
    if folder != None:
        path = os.path.join(folder, data)
    else:
        path = data
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                saved_data = json.load(f)
            return saved_data
        except (IOError, json.JSONDecodeError):
            return 0
    else:
        return 0

def time_invinciblity(seconds):
    global invincible
    time.sleep(seconds)
    invincible = False

def time_rapid_fire(seconds):
    global rapid_fire
    time.sleep(seconds)
    rapid_fire = False

def time_speed_boost(seconds):
    global speed_boost
    time.sleep(seconds)
    speed_boost = False

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
        self.dead = False
    def move(e, *args):
        global difficulty, enemies, enemy_list, direction, dead, spaceship, px, py, direction, rotation, counter, invincible, cooldown, points, bullet_list
        e.y += 40*difficulty
        e.enemy_imagex += e.size
        if e.enemy_imagex >= ((e.size*7) - e.size):
            if e.dead == False:
                e.enemy_imagex = 0
            else:
                enemies -= 1
                enemy_list.remove(e)
        resized_asteroid = pygame.transform.scale(asteroids, (e.size*8, e.size*2))
        resized_asteroid.set_colorkey(Color(255, 255, 255))
        if e.dead == False:
            screen.blit(resized_asteroid, (e.x, e.y), area=(e.size*round(e.enemy_imagex/e.size), 0, e.size, e.size))
        else:
            screen.blit(resized_asteroid, (e.x, e.y), area=(e.size*round(e.enemy_imagex/e.size), e.size, e.size, e.size))
        if e.y > height:
            enemies -= 1
            enemy_list.remove(e)
        if dead == False:
            if invincible == False:
                if e.dead == False:
                    asteroid_sprite = resized_asteroid.subsurface((e.size*round(e.enemy_imagex/e.size), 0, e.size, e.size))
                    mask = pygame.mask.from_surface(asteroid_sprite)
                    asteroid_rect = asteroid_sprite.get_rect(topleft=(e.x, e.y))
                    spaceship_sprite = spaceship.subsurface((160*round(player_imagex/160), 0, 160, 160))
                    resized_spaceship_sprite = pygame.transform.scale(spaceship_sprite, (60, 130))
                    spaceship_mask = pygame.mask.from_surface(resized_spaceship_sprite)
                    spaceship_rect = resized_spaceship_sprite.get_rect(topleft=((px+50), (py+15)))
                    offset = (spaceship_rect.x - asteroid_rect.x, spaceship_rect.y - asteroid_rect.y)
                    if mask.overlap(spaceship_mask, offset):
                        if px > asteroid_rect.x:
                            direction = "right"
                            rotation = -20
                        else:
                            direction = "left"
                            rotation = 20
                        pygame.mixer.music.load("womp-womp.mp3")
                        pygame.mixer.music.play(1)
                        dead = True
            try:
                for bullets in bullet_list:
                    if bullets.rect.colliderect(asteroid_rect):
                        points += 5
                        e.dead = True
                        explosion_sound.play()
                        bullet_list.remove(bullets)
                        if rapid_fire == False or bullet_list == []:
                            cooldown = False
            except NameError:
                pass
            except AttributeError:
                pass

class comet:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.imagex = 0
    def move(c, *args):
        global dead, invincible, px, py, player_imagex, spaceship, direction, rotation, cooldown, Comet, comet_spawned
        c.y += c.speed
        c.imagex += c.size/2
        resized_comet = pygame.transform.scale(comet_spritesheet, (c.size*9, c.size))
        screen.blit(resized_comet, (c.x, c.y), area=(c.size*round(c.imagex/c.size), 0, c.size, c.size))
        if c.y > height+c.size:
            Comet = None
            comet_spawned = False
        if dead == False:
            try:
                comet_sprite = resized_comet.subsurface((c.size*round(c.imagex/c.size), 0, c.size, c.size))
                comet_rect = comet_sprite.get_rect(center=((c.x+c.size/2),(c.y+c.size/2)))
                if invincible == False:
                    mask = pygame.mask.from_surface(comet_sprite)
                    spaceship_sprite = spaceship.subsurface((160*round(player_imagex/160), 0, 160, 160))
                    spaceship_mask = pygame.mask.from_surface(spaceship_sprite)
                    offset = (c.x - px, c.y - py)
                    if mask.overlap(spaceship_mask, offset):
                        if px > comet_rect.x:
                            direction = "right"
                            rotation = -20
                        else:
                            direction = "left"
                            rotation = 20
                        pygame.mixer.music.load("womp-womp.mp3")
                        pygame.mixer.music.play(1)
                        dead = True
            except:
                pass
            try:
                for bullets in bullet_list:
                    if bullets.rect.colliderect(comet_rect):
                        bullet_list.remove(bullets)
                        if rapid_fire == False or bullet_list == []:
                            cooldown = False
            except (NameError, AttributeError):
                pass

class money:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        global coins, coin_list, coin_imagex, points
        self.y += 40*difficulty
        coin_imagex += 32
        if coin_imagex >= 864:
            coin_imagex = 0
        screen.blit(coin, (self.x, self.y), area=(96*round(coin_imagex/96), 0, 96, 96))
        if self.y > height:
            coins -= 1
            coin_list.remove(self)
        coin_sprite = coin.subsurface((96*round(coin_imagex/96), 0, 96, 96))
        coin_rect = coin_sprite.get_rect(center=((self.x+96/2),(self.y+96/2)))
        mask = pygame.mask.from_surface(coin_sprite)
        spaceship_sprite = spaceship.subsurface((160*round(player_imagex/160), 0, 160, 160))
        spaceship_mask = pygame.mask.from_surface(spaceship_sprite)
        offset = (self.x - px, self.y - py)
        for bullets in bullet_list:
            try:
                if bullets.rect.colliderect(coin_rect):
                    coins -= 1
                    try:
                        coin_list.remove(self)
                    except ValueError:
                        pass
            except (NameError, AttributeError):
                pass
        if dead == False:
            if mask.overlap(spaceship_mask, offset):
                coins -= 1
                try:
                    coin_list.remove(self)
                except ValueError:
                    pass
                points += 10

class bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(b, *args):
        global cooldown, bullet_list
        b.y -= 35
        bullet = pygame.draw.circle(screen, pygame.Color(255, 180, 0), (b.x, b.y), 15)
        b.rect = bullet
        if b.y < -10:
            bullet_list.remove(b)
            if rapid_fire == False:
                cooldown = False
        if bullet_list == []:
            cooldown = False

class PowerUp:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def move(p, *args):
        global powerup_imagex, difficulty, powerup_spawned, powerup, Powerup, invincible, powerup_type, speed_boost, rapid_fire, invincible
        p.y += 20*difficulty
        powerup_imagex += 32
        if powerup_imagex >= 512:
            powerup_imagex = 0
        screen.blit(power_ups, (p.x, p.y), area=(128*round(powerup_imagex/128), powerup_type*128-128, 128, 128))
        if p.y > height:
            powerup_spawned = False
            Powerup = None
        powerup_sprite = power_ups.subsurface((128*round(powerup_imagex/128), powerup_type*128-128, 128, 128))
        mask = pygame.mask.from_surface(powerup_sprite)
        spaceship_sprite = spaceship.subsurface((160*round(player_imagex/160), 0, 160, 160))
        spaceship_mask = pygame.mask.from_surface(spaceship_sprite)
        offset = (p.x - px, p.y - py)
        if dead == False:
            if mask.overlap(spaceship_mask, offset):
                Powerup = None
                powerup_spawned = False
                if powerup_type == 1:
                    if invincible == False:
                        invincible = True
                        threading.Thread(target=time_invinciblity, args=(random.randint(5, 10),)).start()
                if powerup_type == 2:
                    rapid_fire = True
                    threading.Thread(target=time_rapid_fire, args=(random.randint(10, 12),)).start()
                if powerup_type == 3:
                    speed_boost = True
                    threading.Thread(target=time_speed_boost, args=(random.randint(10, 13),)).start()

def spawn():
    global stars, enemy_list, enemies, stars, star_list, spaceship, coins, coin_list, comet_spritesheet, comet_spawned, Comet, powerup_spawned, Powerup, powerup_type
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
    number = random.randint(1, 7)
    if number <= math.ceil(difficulty):
        another_number = random.randint(1, 2)
        if another_number == 1:
            e_number = random.randint(0, width)
        else:
            e_number = px + random.randint(-200, 200)
        asize = random.randint(round(50+difficulty), round(200+difficulty))
        Enemy = asteroid(e_number, -asize, 0, asize)
        enemy_list.append(Enemy)
        enemies += 1
    if number == 1:
        new_number = random.randint(1, 10)
        if new_number > 7:
            c_number = random.randint(0, width)
            Coin = money(c_number, -96)
            coin_list.append(Coin)
            coins += 1
    number = random.randint(1, 50)
    if number == 1 and difficulty > 1.2:
        size = random.randint(round(200+difficulty), round(220+difficulty))
        cometx = px
        if comet_spawned == False:
            Comet = comet(cometx, -size, size, random.randint(round(41*difficulty), round(43*difficulty)))
            comet_spawned = True
    if comet_spawned == True and Comet != None:
        Comet.move(Comet)
    if powerup_spawned == False and difficulty > 1.1:
        number = random.randint(1, 60)
        if number == 1:
            powerup_spawned = True
            powerup_type = random.randint(1, 3)
            Powerup = PowerUp(random.randint(0, width), -256, random.randint(20, 25))
    if powerup_spawned == True and Powerup != None:
        Powerup.move(Powerup)
    size = random.randint(0, 2)
    number = random.randint(1, width)
    Star = star(number, 0, color, size)
    star_list.append(Star)
    for s in range(stars):
        try:
            star_list[s].move(star_list[s - 1])
        except IndexError:
            pass
    if dead == False:
        screen.blit(spaceship, (px, py), area=(160*round(player_imagex/160), 0, 160, 160))
    for enemy in enemy_list[:]:
        enemy.move()
    for c in range(coins):
        try:
            coin_list[c].move()
        except IndexError:
            pass

reset()
cutscene = True
image = pygame.image.load("spaceship_spritesheet.png")
spaceship = pygame.transform.scale(image, (1120, 160))
spaceship.set_colorkey(Color(0, 0, 0))
asteroids = pygame.image.load("asteroid_spritesheet.png")
asteroids.set_colorkey(Color(255, 255, 255))
coin = pygame.image.load("spinning_coin.png")
coin = pygame.transform.scale(coin, (960, 96))
coin.set_colorkey(Color(255, 255, 255))
power_ups = pygame.image.load("power_ups.png")
power_ups = pygame.transform.scale(power_ups, (768, 384))
power_ups.set_colorkey(Color(0, 0, 0))
comet_spritesheet = pygame.image.load("comet.png")
comet_spritesheet.set_colorkey(Color(0, 0, 0))
laser_sound = pygame.mixer.Sound("laser.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cosmo Crash")

running = True
while running == True:
    counter += 1
    if counter % 100 == 0:
        difficulty += .1
    player_imagex += 100
    if player_imagex >= 960:
        player_imagex = 0
    key_list = key_list[-5:]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYDEVICEADDED:
            joystick = pygame.joystick.Joystick(event.device_index)
            joystick.init()
            joysticks.append(joystick)
        if event.type == pygame.JOYDEVICEREMOVED:
            joysticks.remove(event.device_index)
        if cutscene == True or game_over == True:
            if event.type == pygame.KEYDOWN:
                key_list.append(event.key)
            if key_list == cheat_code:
                key_list = []
                invincible = True
                font = pygame.font.SysFont(None, 40, bold=True)
                pygame.mixer.music.play(-1)
                difficulty = 1
                counter = 0
                cutscene = False
            if key_list == hard_mode_code:
                reset()
                hard_mode = True
                key_list = []
                font = pygame.font.SysFont(None, 40, bold=True)
                pygame.mixer.music.play(-1)
                difficulty = 3
                counter = 0
                cutscene = False
                game_over = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE and game_over == False and dead == False and cutscene == False:
                if rapid_fire == True or (cooldown == False and bullet_list == []):
                    laser_sound.play()
                    Bullet = bullet(px + 80, py)
                    bullet_list.append(Bullet)
    screen.fill(pygame.Color(0, 0, 0))
    handle_input()
    if cutscene == True:
        font = pygame.font.SysFont(None, 120, bold=True)
        text = font.render("Cosmo Crash", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 100)
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 70, bold=True)
        text = font.render("Dodge the Asteroids and collect the coins!", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2)
        screen.blit(text, text_rect)
        text = font.render("Use the WASD keys or the joystick to move", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 50)
        screen.blit(text, text_rect)
        text = font.render("and the spacebar or the A button to fire", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 100)
        screen.blit(text, text_rect)
        text = font.render("Press enter or start to play", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 150)
        screen.blit(text, text_rect)
        keys = pygame.key.get_pressed()
        if keys[K_RETURN] == True:
            font = pygame.font.SysFont(None, 40, bold=True)
            pygame.mixer.music.play(-1)
            difficulty = 1
            counter = 0
            cutscene = False
    elif game_over == True:
        font = pygame.font.SysFont(None, 200, bold=True)
        text = font.render("Game Over", False, Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 50)
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 70, bold=True)
        text = font.render(f"Your score: {points}", False, Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 50)
        screen.blit(text, text_rect)
        text = font.render(f"High score: {high_score}", False, Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 100)
        screen.blit(text, text_rect)
        text = font.render("Press enter or start to play again", False, Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 150)
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 50, bold=True)
        text = font.render(insult, False, Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 200)
        screen.blit(text, text_rect)
        keys = pygame.key.get_pressed()
        if keys[K_RETURN] == True:
            reset()
            pygame.mixer.music.play(-1)
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
        if points >= high_score:
            text = font.render(f"Score: {points}  High: {points}", False, Color(255, 0, 0))
        else:
            text = font.render(f"Score: {points}  High: {high_score}", False, Color(255, 0, 0))
        screen.blit(text, (0, 0))
        if px > width+320 or px < -320 or py < -320:
            number = random.randint(1, len(insults))
            insult = insults[number-1]
            if points >= high_score:
                high_score = points
                save(high_score, "high score")
            else:
                high_score = load("high score", "Cosmo_Crash_save_data")
            game_over = True
    else:
        spawn()
        if points >= high_score:
            text = font.render(f"Score: {points}  High: {points}", False, Color(255, 0, 0))
        else:
            text = font.render(f"Score: {points}  High: {high_score}", False, Color(255, 0, 0))
        screen.blit(text, (0, 0))
    if game_over == False:
        for bullets in bullet_list:
            bullets.move(bullets)
    pygame.display.update()
    if hard_mode == False:
        clock.tick(20)
    else:
        clock.tick(60)
pygame.quit()
exit()
