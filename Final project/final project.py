import pygame, sys, os, random, json
from pygame.locals import *
pygame.init()
pygame.mixer.init()

def resource_path(filename):
    try:
        base_path = sys.MEIPATH
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)

def reset():
    global game_state, feedback, user_input, border, paused, player_imagex, player_imagey, collision, saving, loading, screen_objects, counter, talking, offset
    game_state = "menu"
    feedback = ""
    user_input = ""
    paused = False
    player_imagex = 0
    player_imagey = 0
    collision = False
    saving = False
    loading = False
    screen_objects = {}
    counter = 8
    talking = False
    offset = 0

def save(data, name, folder=None):
    if folder != None:
        path = os.path.join(folder, name)
        if not os.path.exists(resource_path(path)):
            os.makedirs(path)
    else:
        path = resource_path(name)
    if not os.path.exists(resource_path("save_data")):
        os.makedirs(resource_path("save_data"))
    filepath = os.path.join(resource_path("save_data"), name)
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        return None

def load(data, folder=None):
    if folder != None:
        path = os.path.join("save_data", folder, data)
    else:
        path = os.path.join("save_data", data)
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                saved_data = json.load(f)
            return saved_data
        except (IOError, json.JSONDecodeError):
            return None
    else:
        return None

def submit_input(x):
    global game_state, feedback, user_input, player, game_data
    if game_state == "choose name":
        if len(x) < 1:
            number = random.randint(0, len(too_short_name_insults) - 1)
            feedback = too_short_name_insults[number]
        elif len(x) > 17:
            number = random.randint(0, len(too_long_name_insults) - 1)
            feedback = too_long_name_insults[number]
        else:
            player = character(user_input, None, None)
            game_data["name"] = user_input
            game_data["player"] = player.dict
            user_input = ""
            game_state = "choose race"

def draw_button(words, y, color=pygame.Color(255, 255, 255), bg=pygame.Color(150, 150, 150), button_width=500, button_height=80): #dict of the text and the y position of the button
    global small_font, medium_font, big_font, huge_font, width
    text = medium_font.render(words, False, color)
    text_rect = text.get_rect()
    button = pygame.Rect(0, 0, button_width, button_height)
    button.center = (width // 2, y)
    button = pygame.draw.rect(screen, bg, button)
    screen.blit(text, (((button.x + (button.width // 2)) - (text_rect.width // 2)), button.y + (button.height // 4)))
    return button

def spawn_npc():
    global current_map, npc_list
    npc_list = []
    if current_map == city_map:
        number = random.randint(10, 30)
    else:
        number = random.randint(10, 30)
    for n in range(number):
        new_npc = None
        if current_map == city_map:
            x = random.randint(0, 8000)
            y = random.randint(0, 8000)
        while new_npc == None:
            for thing in current_map.keys():
                rect = pygame.Rect(x - 192, y - 192, 384, 384)
                if rect.colliderect(thing):
                    x = random.randint(0, 8000)
                    y = random.randint(0, 8000)
                else:
                    other_number = random.randint(1, 4)
                    if other_number == 1:
                        direction = "north"
                    elif other_number == 2:
                        direction = "east"
                    elif other_number == 3:
                        direction = "west"
                    elif other_number == 4:
                        direction = "south"
                    new_number = random.randint(1, 4)
                    if new_number == 1:
                        words = random.sample(npc1_insults, 5)
                        if direction == "north":    
                            imagey = 192
                        elif direction == "east":    
                            imagey = 384
                        elif direction == "west":    
                            imagey = 576
                        elif direction == "south":    
                            imagey = 0
                    elif new_number == 2:
                        words = random.sample(npc2_insults, 5)
                        if direction == "north":    
                            imagey = 768
                        elif direction == "east":    
                            imagey = 1152
                        elif direction == "west":    
                            imagey = 1344
                        elif direction == "south":    
                            imagey = 960
                    elif new_number == 3:
                        words = random.sample(npc3_insults, 5)
                        if direction == "north":    
                            imagey = 1728
                        elif direction == "east":    
                            imagey = 1920
                        elif direction == "west":    
                            imagey = 2112
                        elif direction == "south":    
                            imagey = 1536
                    elif new_number == 4:
                        words = random.sample(npc4_insults, 5)
                        if direction == "north":    
                            imagey = 2496
                        elif direction == "east":    
                            imagey = 2688
                        elif direction == "west":    
                            imagey = 2880
                        elif direction == "south":    
                            imagey = 2304
                    new_npc = NPC_class(x, y, 0, imagey, random.randint(5, 10), direction, words)
                    npc_list.append(new_npc)

class NPC_class():
    def __init__(self, x, y, imagex, imagey, speed, direction, words):
        self.x = x
        self.y = y
        self.imagex = imagex
        self.imagey = imagey
        self.speed = speed
        self.direction = direction
        self.words = words

class character():
    def __init__(self, name, race, Class, health=10, gold=0, inventory=[], level=1, stats={}, weapon_equiped=None, armor_equiped=None, accessory_equiped=None):
        self.name = name
        self.race = race
        self.Class = Class
        self.health = health
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.stats = stats
        self.weapon_equiped = weapon_equiped
        self.armor_equiped = armor_equiped
        self.accessory_equiped = accessory_equiped
        self.alive = True
        self.dict = {"name": self.name, "race": self.race, "Class": self.Class, "health": self.health, "gold": self.gold, "inventory": self.inventory, "level": self.level, "stats": self.stats, "weapon_equiped": self.weapon_equiped, "armor_equiped": self.armor_equiped, "accessory_equiped": self.accessory_equiped}
    def update(self):
        self.dict = {"name": self.name, "race": self.race, "Class": self.Class, "health": self.health, "gold": self.gold, "inventory": self.inventory, "level": self.level, "stats": self.stats, "weapon_equiped": self.weapon_equiped, "armor_equiped": self.armor_equiped, "accessory_equiped": self.accessory_equiped}
    
#8000 X 8000 pixels
city_map = {(0, 0, 200, 7600): "wall", (0, 7400, 7600, 200): "wall", (7400, 0, 200, 7600): "wall", (0, 0, 7600, 200): "wall", (500, 1200, 768, 768):"house", (700, 7000, 768, 768): "house", (800, 6400, 768, 768): "house", (6000, 5000, 768, 768): "house", (4000, 3700, 768, 768): "building", (6500, 400, 768, 768): "building", (500, 1750, 768, 768): "building"}

npc1_insults = ["Get off my lawn, you whippersnapper!", "Howdy!", "Don't you have something better to do?", "hrrmmm...", "Oh it's you again... I'm gonna go take a nap.", "What are you up to?", "That's it. Nap time."]
npc2_insults = ["What?", "What do you want?", "Don't you have something better to do?", "What is it this time?", "I gotta go, bye.", "Goodbye.", "Nice hair."]
npc3_insults = ["Yo!", "Sup?", "Hey, are you looking at me weird? You jealous of my sick pants, huh?", "Beat it, stalker", "Do I know you?", "Hey, *cough* *cough* nerd.", "Why are you here? What do you think this is, some kind of game?"]
npc4_insults = ["I went to college!", "Don't touch my dress, it's dry clean only!", "Don't be mean to me, I'm rich!", "Go away, peasant", "Go back to grad school!", "What do you want, peasant?", "Goodbye, peasant."]
city_background = pygame.image.load(resource_path("city_background.png"))
city_background = pygame.transform.scale(city_background, (9000, 9000))
objects = pygame.image.load(resource_path("objects.png"))
objects = pygame.transform.scale(objects, (2304, 2304))
human = pygame.image.load(resource_path("human.png"))
elf = pygame.image.load(resource_path("elf.png"))
dwarf = pygame.image.load(resource_path("dwarf.png"))
human = pygame.transform.scale(human, (1536, 768))
elf = pygame.transform.scale(elf, (1536, 768))
dwarf = pygame.transform.scale(dwarf, (1536, 768))
npc = pygame.image.load(resource_path("npc.png"))
npc = pygame.transform.scale(npc, (1536, 3072))
mouse_pointer = pygame.image.load(resource_path("sword.png"))
mouse_pointer = pygame.transform.rotate(mouse_pointer, 35)

too_long_name_insults = ["enter a name, not a book", "nope, too long", "you know what a name is, right?", "do you want to play the game or type all day?", "stop spazzing, start holding backspace"]
too_short_name_insults = ["that's not a name", "nope", "you have a name, right?", "try again", "just push some buttons"]
small_font = pygame.font.SysFont(None, 30, bold=False)
medium_font = pygame.font.SysFont(None, 50, bold=False)
big_font = pygame.font.SysFont(None, 60, bold=False)
huge_font = pygame.font.SysFont(None, 80, bold=True)
clock = pygame.time.Clock()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 50
player_rect = pygame.Rect(width // 2 - 96, height // 2 - 96, 192, 192)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("")
##pygame.display.set_icon(pygame.image.load(resource_path("icon.ico")))
pygame.mouse.set_visible(False)
reset()

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if game_state == "menu":
                    if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
                        game_state = "continue"
                    elif mouse_pos[0] < new_game_button.right and mouse_pos[0] > new_game_button.left and mouse_pos[1] > new_game_button.top and mouse_pos[1] < new_game_button.bottom:
                        game_state = "new_game"
                    elif mouse_pos[0] < quit_button.right and mouse_pos[0] > quit_button.left and mouse_pos[1] > quit_button.top and mouse_pos[1] < quit_button.bottom:
                        running = False
                elif game_state == "new_game":
                    if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                        game_state = "menu"
                    if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom:
                        file1 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
                        game_data = file1
                        background = city_background
                        current_map = city_map
                        game_state = "choose name"
                    if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                        file2 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
                        game_data = file2
                        background = city_background
                        current_map = city_map
                        game_state = "choose name"
                    if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                        file3 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
                        game_data = file3
                        background = city_background
                        current_map = city_map
                        game_state = "choose name"
                elif game_state == "continue":
                    if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                        game_state = "menu"
                    if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom:
                        if file1["name"] != "empty":
                            game_data = file1
                            game_state = "exploring"
                            worldx = game_data["worldx"]
                            worldy = game_data["worldy"]
                            player = character(*tuple(game_data["player"].values()))
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            if player.race == "human":
                                player_sprite = human
                            if player.race == "elf":
                                player_sprite = elf
                            if player.race == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                    if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                        if file2["name"] != "empty":
                            game_data = file2
                            game_state = "exploring"
                            worldx = game_data["worldx"]
                            worldy = game_data["worldy"]
                            player = character(*tuple(game_data["player"].values()))
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            if player.race == "human":
                                player_sprite = human
                            if player.race == "elf":
                                player_sprite = elf
                            if player.race == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                    if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                        if file3["name"] != "empty":
                            game_data = file3
                            game_state = "exploring"
                            worldx = game_data["worldx"]
                            worldy = game_data["worldy"]
                            player = character(*tuple(game_data["player"].values()))
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            if player.race == "human":
                                player_sprite = human
                            elif player.race == "elf":
                                player_sprite = elf
                            elif player.race == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                elif game_state == "choose name":
                    if mouse_pos[0] < submit_button.right and mouse_pos[0] > submit_button.left and mouse_pos[1] > submit_button.top and mouse_pos[1] < submit_button.bottom:
                        submit_input(user_input)
                elif game_state == "choose race":
                    if mouse_pos[0] < human_button.right and mouse_pos[0] > human_button.left and mouse_pos[1] > human_button.top and mouse_pos[1] < human_button.bottom:
                        player.race = "human"
                        player_sprite = human
                        player.stats = {"attack": 10, "defense": 10, "accuracy": 10, "avoidance": 10, "magic": 10, "resistance": 10}
                        game_state = "choose class"
                    elif mouse_pos[0] < elf_button.right and mouse_pos[0] > elf_button.left and mouse_pos[1] > elf_button.top and mouse_pos[1] < elf_button.bottom:
                        player.race = "elf"
                        player_sprite = elf
                        game_state = "choose class"
                        player.stats = {"attack": 8, "defense": 8, "accuracy": 12, "avoidance": 10, "magic": 12, "resistance": 12}
                    elif mouse_pos[0] < dwarf_button.right and mouse_pos[0] > dwarf_button.left and mouse_pos[1] > dwarf_button.top and mouse_pos[1] < dwarf_button.bottom:
                        player.race = "dwarf"
                        player_sprite = dwarf
                        game_state = "choose class"
                        player.stats = {"attack": 13, "defense": 15, "accuracy": 10, "avoidance": 8, "magic": 6, "resistance": 8}
                elif game_state == "choose class":
                    if mouse_pos[0] < fighter_button.right and mouse_pos[0] > fighter_button.left and mouse_pos[1] > fighter_button.top and mouse_pos[1] < fighter_button.bottom:
                        player.Class = "fighter"
                        player.inventory.append("shortsword")
                        player.stats["attack"] += 2
                        player.stats["defense"] += 2
                        player.stats["magic"] -= 2
                        player.stats["resistance"] -= 2
                        player.update()
                        game_data["player"] = player.dict
                        game_state = "intro"
                    elif mouse_pos[0] < mage_button.right and mouse_pos[0] > mage_button.left and mouse_pos[1] > mage_button.top and mouse_pos[1] < mage_button.bottom:
                        player.Class = "mage"
                        game_data["player.Class"] = "mage"
                        player.inventory.append("magic wand")
                        game_state = "intro"
                        player.stats["attack"] -= 2
                        player.stats["defense"] -= 2
                        player.stats["magic"] += 2
                        player.stats["resistance"] += 2
                        player.update()
                        game_data["player"] = player.dict
                        game_state = "intro"
                    elif mouse_pos[0] < thief_button.right and mouse_pos[0] > thief_button.left and mouse_pos[1] > thief_button.top and mouse_pos[1] < thief_button.bottom:
                        player.Class = "thief"
                        game_data["player.Class"] = "thief"
                        player.inventory.append("dagger")
                        game_state = "intro"
                        player.stats["accuracy"] += 2
                        player.stats["avoidance"] += 2
                        player.stats["resistance"] -= 2
                        player.stats["defense"] -= 2
                        player.update()
                        game_data["player"] = player.dict
                        game_state = "intro"
                elif game_state == "intro":
                    if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
                        spawn_npc()
                        worldx = 3300
                        worldy = 5000
                        game_data["area"] = "city"
                        current_map = city_map
                        background = city_background
                        game_state = "exploring"
                elif game_state == "exploring":
                    if paused == True:
                        if saving == False and loading == False:
                            if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
                                paused = False
                            if mouse_pos[0] < save_button.right and mouse_pos[0] > save_button.left and mouse_pos[1] > save_button.top and mouse_pos[1] < save_button.bottom:
                                saving = True
                                counter = 0
                            if mouse_pos[0] < load_button.right and mouse_pos[0] > load_button.left and mouse_pos[1] > load_button.top and mouse_pos[1] < load_button.bottom:
                                loading = True
                                counter = 0
                            if mouse_pos[0] < exit_button.right and mouse_pos[0] > exit_button.left and mouse_pos[1] > exit_button.top and mouse_pos[1] < exit_button.bottom:
                                reset()
                        if saving == True:
                            if counter == 8:
                                if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom:
                                    feedback = "saving..."
                                    save(game_data, "file1")
                                    feedback = "saved!"
                                if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                                    feedback = "saving..."
                                    save(game_data, "file2")
                                    feedback = "saved!"
                                if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                                    feedback = "saving..."
                                    save(game_data, "file3")
                                    feedback = "saved!"
                                if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                                    feedback = ""
                                    saving = False
                        if loading == True:
                            if counter == 8:
                                if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom:
                                    feedback = "loading..."
                                    game_data = load("file1")
                                    player = character(*tuple(game_data["player"].values()))
                                    player.update()
                                    feedback = ""
                                    loading = False
                                    paused = False
                                if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                                    feedback = "loading..."
                                    game_data = load("file2")
                                    player = character(*tuple(game_data["player"].values()))
                                    player.update()
                                    feedback = ""
                                    loading = False
                                    paused = False
                                if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                                    feedback = "loading..."
                                    game_data = load("file3")
                                    player = character(*tuple(game_data["player"].values()))
                                    player.update()
                                    feedback = ""
                                    loading = False
                                    paused = False
                                if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                                    feedback = ""
                                    loading = False
                    else:
                        if talking == False:
                            for NPC in npc_list:
                                npc_rect = pygame.Rect(NPC.x - worldx, NPC.y - worldy, 192, 192)
                                if mouse_pos[0] < npc_rect.right and mouse_pos[0] > npc_rect.left and mouse_pos[1] > npc_rect.top and mouse_pos[1] < npc_rect.bottom:
                                    talking = True
                                    npc_words = random.sample(NPC.words, 1)
                        else:
                            talking = False
        if event.type == pygame.KEYDOWN:
            if game_state == "choose name":
                if event.key == K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == K_RETURN:
                    submit_input(user_input)
                else:
                    if len(user_input) < 18:
                        user_input += str(event.unicode)
                    else:
                        number = random.randint(0, len(too_long_name_insults) - 1)
                        feedback = too_long_name_insults[number]
            if game_state == "exploring":
                if event.key == K_ESCAPE:
                    feedback = ""
                    paused = not paused
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(pygame.Color(0, 0, 0))
    if game_state == "menu":
        text = huge_font.render("Game Name Here", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/3)
        screen.blit(text, text_rect)
        try:
            if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
                continue_button = draw_button("continue", height/2, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                continue_button = draw_button("continue", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            continue_button = draw_button("continue", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        try:
            if mouse_pos[0] < new_game_button.right and mouse_pos[0] > new_game_button.left and mouse_pos[1] > new_game_button.top and mouse_pos[1] < new_game_button.bottom:
                new_game_button = draw_button("new game", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                new_game_button = draw_button("new game", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            new_game_button = draw_button("new game", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        try:
            if mouse_pos[0] < quit_button.right and mouse_pos[0] > quit_button.left and mouse_pos[1] > quit_button.top and mouse_pos[1] < quit_button.bottom:
                quit_button = draw_button("quit", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                quit_button = draw_button("quit", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            quit_button = draw_button("quit", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
    elif game_state == "continue" or game_state == "new_game":
        text = huge_font.render("choose a file", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/3)
        screen.blit(text, text_rect)
        file1 = load("file1")
        if file1 == None:
            file1 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
        try:
            if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom and (file1["name"] != "empty" or game_state == "new_game"):
                file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        file2 = load("file2")
        if file2 == None:
            file2 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
        try:
            if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom and (file2["name"] != "empty" or game_state == "new_game"):
                file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        file3 = load("file3")
        if file3 == None:
            file3 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
        try:
            if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom and (file3["name"] != "empty" or game_state == "new_game"):
                file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        text = medium_font.render("back", False, pygame.Color(255, 255, 255))
        back_button = text.get_rect()
        back_button.center = (50, height - 75)
        back_button.width += 50
        back_button.height += 20
        if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
            back_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), back_button)
        else:
            back_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), back_button)
        screen.blit(text, (back_button.x + 25, back_button.y + 10))
    elif game_state == "choose name":
        text = huge_font.render("What's your name?", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 50)
        screen.blit(text, text_rect)
        text_box = pygame.draw.rect(screen, pygame.Color(180, 180, 180), (width/2 - 250, height/2 + 25, 500, 75))
        text = medium_font.render(user_input, False, pygame.Color(255, 255, 255))
        screen.blit(text, (text_box.x, text_box.y + (text_box.height/4)))
        text = medium_font.render(feedback, False, pygame.Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 250)
        screen.blit(text, text_rect)
        text = medium_font.render(" Continue ", False, pygame.Color(255, 255, 255))
        submit_button = text.get_rect()
        submit_button.x = width - (submit_button.width + 50)
        submit_button.y = height - (submit_button.height + 50)
        submit_button.height += 20
        if mouse_pos[0] < submit_button.right and mouse_pos[0] > submit_button.left and mouse_pos[1] > submit_button.top and mouse_pos[1] < submit_button.bottom:
            submit_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), submit_button)
        else:
            submit_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), submit_button)
        screen.blit(text, (submit_button.x, submit_button.y + (submit_button.height/2 - 17)))
    elif game_state == "choose race":
        text = huge_font.render("Choose a race", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 250)
        screen.blit(text, text_rect)
        try:
            if mouse_pos[0] < human_button.right and mouse_pos[0] > human_button.left and mouse_pos[1] > human_button.top and mouse_pos[1] < human_button.bottom:
                human_button = draw_button("human", height/2, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                human_button = draw_button("human", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            human_button = draw_button("human", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        try:
            if mouse_pos[0] < elf_button.right and mouse_pos[0] > elf_button.left and mouse_pos[1] > elf_button.top and mouse_pos[1] < elf_button.bottom:
                elf_button = draw_button("elf", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                elf_button = draw_button("elf", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            elf_button = draw_button("elf", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        try:
            if mouse_pos[0] < dwarf_button.right and mouse_pos[0] > dwarf_button.left and mouse_pos[1] > dwarf_button.top and mouse_pos[1] < dwarf_button.bottom:
                dwarf_button = draw_button("dwarf", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                dwarf_button = draw_button("dwarf", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            dwarf_button = draw_button("dwarf", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
    elif game_state == "choose class":
        text = huge_font.render("Choose a class", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 250)
        screen.blit(text, text_rect)
        try:
            if mouse_pos[0] < fighter_button.right and mouse_pos[0] > fighter_button.left and mouse_pos[1] > fighter_button.top and mouse_pos[1] < fighter_button.bottom:
                fighter_button = draw_button("fighter", height/2, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                fighter_button = draw_button("fighter", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            fighter_button = draw_button("fighter", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        try:
            if mouse_pos[0] < mage_button.right and mouse_pos[0] > mage_button.left and mouse_pos[1] > mage_button.top and mouse_pos[1] < mage_button.bottom:
                mage_button = draw_button("mage", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                mage_button = draw_button("mage", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            mage_button = draw_button("mage", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        try:
            if mouse_pos[0] < thief_button.right and mouse_pos[0] > thief_button.left and mouse_pos[1] > thief_button.top and mouse_pos[1] < thief_button.bottom:
                thief_button = draw_button("thief", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
            else:
                thief_button = draw_button("thief", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        except NameError:
            thief_button = draw_button("thief", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
    elif game_state == "intro":
        text = huge_font.render("You are a mercenary that works for King", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 100)
        screen.blit(text, text_rect)
        text = huge_font.render("Tyrannus. Go to the castle to recieve", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 25)
        screen.blit(text, text_rect)
        text = huge_font.render("your first mission, or be executed.", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 50)
        screen.blit(text, text_rect)
        text = huge_font.render("(press esc to pause the game)", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 125)
        screen.blit(text, text_rect)
        text = medium_font.render(" Continue ", False, pygame.Color(255, 255, 255))
        continue_button = text.get_rect()
        continue_button.x = width - (continue_button.width + 50)
        continue_button.y = height - (continue_button.height + 50)
        continue_button.height += 20
        if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
            continue_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), continue_button)
        else:
            continue_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), continue_button)
        screen.blit(text, (continue_button.x, continue_button.y + (continue_button.height/2 - 17)))
    elif game_state == "exploring":
        keys = pygame.key.get_pressed()
        old_worldx = worldx
        old_worldy = worldy
        if paused == False and talking == False:
            for NPC in npc_list:
                NPC.imagex += 5
                if NPC.imagex >= 1344:
                    NPC.imagex = 0
                number = random.randint(1, 50)
                if number == 1:
                    NPC.direction = "north"
                    if NPC.imagey <= 576:
                        NPC.imagey = 192
                    elif NPC.imagey <= 1152:
                        NPC.imagey = 960
                    elif NPC.imagey <= 1344:
                        NPC.imagey = 1728
                    else:
                        NPC.imagey = 2496
                elif number == 2:
                    NPC.direction = "east"
                    if NPC.imagey <= 576:
                        NPC.imagey = 384
                    elif NPC.imagey <= 1152:
                        NPC.imagey = 1152
                    elif NPC.imagey <= 1344:
                        NPC.imagey = 1920
                    else:
                        NPC.imagey = 1688
                elif number == 3:
                    NPC.direction = "west"
                    if NPC.imagey <= 576:
                        NPC.imagey = 576
                    elif NPC.imagey <= 1152:
                        NPC.imagey = 1344
                    elif NPC.imagey <= 1344:
                        NPC.imagey = 2112
                    else:
                        NPC.imagey = 1880
                elif number == 4:
                    NPC.direction = "south"
                    if NPC.imagey <= 576:
                        NPC.imagey = 0
                    elif NPC.imagey <= 1152:
                        NPC.imagey = 768
                    elif NPC.imagey <= 1344:
                        NPC.imagey = 1537
                    else:
                        NPC.imagey = 2304
                elif number < 30:
                    NPC.imagex = 0
                else:
                    old_npc_x = NPC.x
                    old_npc_y = NPC.y
                    if NPC.direction == "north":
                        NPC.y -= NPC.speed
                    elif NPC.direction == "west":
                        NPC.x -= NPC.speed
                    elif NPC.direction == "east":
                        NPC.x += NPC.speed
                    elif NPC.direction == "south":
                        NPC.y += NPC.speed
            if keys[K_w] == True:
                if collision == False:
                    player_imagey = 192
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    worldy -= 10
                    if keys[K_a] == False and keys[K_s] == False and keys[K_d] == False and collision == False:
                        worldy -= 4
            if keys[K_a] == True:
                if collision == False:
                    player_imagey = 576
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    worldx -= 10
                    if keys[K_w] == False and keys[K_s] == False and keys[K_d] == False and collision == False:
                        worldx -= 4
            if keys[K_s] == True:
                if collision == False:
                    player_imagey = 0
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    worldy += 10
                    if keys[K_a] == False and keys[K_w] == False and keys[K_d] == False and collision == False:
                        worldy += 4
            if keys[K_d] == True:
                if collision == False:
                    player_imagey = 384
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    worldx += 10
                    if keys[K_a] == False and keys[K_s] == False and keys[K_w] == False and collision == False:
                        worldx += 4
            if keys[K_w] == False and keys[K_a] == False and keys[K_s] == False and keys[K_d] == False:
                player_imagex = 0
        screen.blit(background, (0, 0), area=(worldx, worldy, width, height))
        for NPC in npc_list:
            screen.blit(npc, (NPC.x - worldx, NPC.y - worldy), area=(192*round(NPC.imagex/192), NPC.imagey, 192, 192))
        screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
        screen_objects = {}
        for obstacle in current_map.keys():
            obstacle_rect = pygame.Rect(obstacle)
            if current_map[obstacle] == "wall":
                screen_object_rect = pygame.draw.rect(screen, pygame.Color(150, 150, 150), (obstacle_rect.x - worldx + (width/2), obstacle_rect.y - worldy + (height/2), obstacle_rect.width, obstacle_rect.height))
                screen_object = tuple(screen_object_rect)
                screen_objects[screen_object] = "wall"
                if player_rect.top < screen_object_rect.top and player_rect.colliderect(screen_object_rect):
                    screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
            elif current_map[obstacle] == "house":
                screen_object_rect = screen.blit(objects, (obstacle_rect.x - worldx + (width/2), obstacle_rect.y - worldy + (height/2)), area=(0, 0, 768, 768))
                screen_object = tuple(screen_object_rect)
                screen_objects[screen_object] = "house"
                if player_rect.top < screen_object_rect.top and player_rect.colliderect(screen_object_rect):
                    screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
            elif current_map[obstacle] == "building":
                screen_object_rect = screen.blit(objects, (obstacle_rect.x - worldx + (width/2), obstacle_rect.y - worldy + (height/2)), area=(768, 0, 768, 768))
                screen_object = tuple(screen_object_rect)
                screen_objects[screen_object] = "building"
                if player_rect.top < screen_object_rect.top and player_rect.colliderect(screen_object_rect):
                    screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
        for obstacle in screen_objects.keys():
            if screen_objects[obstacle] == "house":
                new_obstacle_rect = pygame.Rect(obstacle[0] + 300, (obstacle[1] + obstacle[3]) - 100, obstacle[2] // 3, 100)
            elif screen_objects[obstacle] == "building":
                new_obstacle_rect = pygame.Rect(obstacle[0] + 200, (obstacle[1] + obstacle[3]) - 50, obstacle[2] // 3, 100)
            else:
                new_obstacle_rect = pygame.Rect(obstacle)
            if player_rect.colliderect(pygame.Rect(obstacle)):
                if screen_objects[obstacle] == "house" or screen_objects[obstacle] == "building":
                    if player_rect.colliderect(new_obstacle_rect):
                        if player_rect.bottom >= new_obstacle_rect.bottom:
                            pass
                        else:
                            collision = True
                            worldx = old_worldx
                            worldy = old_worldy
                    if player_rect.bottom > new_obstacle_rect.top + 15 or player_rect.left > new_obstacle_rect.right:
                        screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
                else:
                    if player_rect.colliderect(new_obstacle_rect):
                        if player_rect.bottom > new_obstacle_rect.top:
                            screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
                        collision = True
                        worldx = old_worldx
                        worldy = old_worldy
            for NPC in npc_list:
                npc_rect = pygame.Rect(NPC.x - worldx + (width // 2), NPC.y - worldy + (height // 2), 192, 192)
                if npc_rect.colliderect(pygame.Rect(obstacle)):
                    if screen_objects[obstacle] == "house" or screen_objects[obstacle] == "building":
                        if npc_rect.colliderect(new_obstacle_rect):
                            if npc_rect.bottom >= new_obstacle_rect.bottom:
                                pass
                            else:
                                worldx = old_worldx
                                worldy = old_worldy
                        if npc_rect.bottom > new_obstacle_rect.top + 15 or npc_rect.left > new_obstacle_rect.right:
                            screen.blit(npc, ((width / 2) - 96, (height / 2) - 96), area=(192*round(NPC.imagex/192), NPC.imagey, 192, 192))
                    else:
                        if npc_rect.colliderect(new_obstacle_rect):
                            if npc_rect.bottom > new_obstacle_rect.top:
                                screen.blit(npc, ((width / 2) - 96, (height / 2) - 96), area=(192*round(NPC.imagex/192), NPC.imagey, 192, 192))
                            NPC.x = old_npc_x
                            NPC.y = old_npc_y
                            number = random.randint(1, 4)
                            if number == 1:
                                NPC.direction = "north"
                            elif number == 2:
                                NPC.direction = "east"
                            elif number == 3:
                                NPC.direction = "west"
                            elif number == 4:
                                NPC.direction = "south"
        if talking == True:
            if offset == 10:
                difference = -1
            elif offset == 0:
                difference = 1
            offset += difference
            pygame.draw.rect(screen, pygame.Color(150, 150, 150), (100, height - 200, width - 200, 100))
            text = medium_font.render(npc_words[0], pygame.Color(255, 255, 255), False)
            text_rect = text.get_rect()
            text_rect.center = (width // 2, height - 150)
            screen.blit(text, text_rect)
            pygame.draw.polygon(screen, pygame.Color(100, 100, 100), (((width - 150) - offset, (height - 140)), ((width - 180) + offset, (height - 140)), ((width - 165), (height - 110) - offset)))
        game_data["worldx"] = worldx
        game_data["worldy"] = worldy
        collision = False
        if paused == True:
            if counter < 8:
                counter += 1
            if saving == True:
                text = huge_font.render("Choose a file to save", False, pygame.Color(255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (width/2, height/2 - 350)
                screen.blit(text, text_rect)
                file1 = load("file1")
                if file1 == None:
                    file1 = {"name": "empty"}
                try:
                    if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom and (feedback == "" or feedback == "saved!"):
                        file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                file2 = load("file2")
                if file2 == None:
                    file2 = {"name": "empty"}
                try:
                    if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom and (feedback == "" or feedback == "saved!"):
                        file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                file3 = load("file3")
                if file3 == None:
                    file3 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
                try:
                    if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom and (feedback == "" or feedback == "saved!"):
                        file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                text = medium_font.render("back", False, pygame.Color(255, 255, 255))
                back_button = text.get_rect()
                back_button.center = (50, height - 75)
                back_button.width += 50
                back_button.height += 20
                if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom and (feedback == "" or feedback == "saved!"):
                    back_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), back_button)
                else:
                    back_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), back_button)
                screen.blit(text, (back_button.x + 25, back_button.y + 10))
                text = big_font.render(feedback, False, pygame.Color(255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (width/2, height - 100)
                screen.blit(text, text_rect)
            elif loading == True:
                text = huge_font.render("Choose a file to load", False, pygame.Color(255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (width/2, height/2 - 350)
                screen.blit(text, text_rect)
                file1 = load("file1")
                if file1 == None:
                    file1 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
                try:
                    if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom and file1["name"] != "empty" and (feedback == "" or feedback == "saved!"):
                        file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    file1_button = draw_button(f"file 1: {file1['name']}", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                file2 = load("file2")
                if file2 == None:
                    file2 = {"name": "empty", "area": "city", "worldx": 3300, "worldy": 5000}
                try:
                    if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom and file2["name"] != "empty" and (feedback == "" or feedback == "saved!"):
                        file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    file2_button = draw_button(f"file 2: {file2['name']}", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                file3 = load("file3")
                if file3 == None:
                    file3 = {"name": "empty"}
                try:
                    if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom and file2["name"] != "empty" and (feedback == "" or feedback == "saved!"):
                        file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                text = medium_font.render("back", False, pygame.Color(255, 255, 255))
                back_button = text.get_rect()
                back_button.center = (50, height - 75)
                back_button.width += 50
                back_button.height += 20
                if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                    back_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), back_button)
                else:
                    back_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), back_button)
                screen.blit(text, (back_button.x + 25, back_button.y + 10))
                text = big_font.render(feedback, False, pygame.Color(255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (width/2, height - 100)
                screen.blit(text, text_rect)
            else:
                text = huge_font.render("Paused", False, pygame.Color(255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (width/2, height/2 - 350)
                screen.blit(text, text_rect)
                try:
                    if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
                        continue_button = draw_button("continue", height/2 - 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        continue_button = draw_button("continue", height/2 - 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    continue_button = draw_button("continue", height/2 - 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                try:
                    if mouse_pos[0] < save_button.right and mouse_pos[0] > save_button.left and mouse_pos[1] > save_button.top and mouse_pos[1] < save_button.bottom:
                        save_button = draw_button("save", height/2, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        save_button = draw_button("save", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    save_button = draw_button("save", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                try:
                    if mouse_pos[0] < load_button.right and mouse_pos[0] > load_button.left and mouse_pos[1] > load_button.top and mouse_pos[1] < load_button.bottom:
                        load_button = draw_button("load", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        load_button = draw_button("load", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    load_button = draw_button("load", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                try:
                    if mouse_pos[0] < exit_button.right and mouse_pos[0] > exit_button.left and mouse_pos[1] > exit_button.top and mouse_pos[1] < exit_button.bottom:
                        exit_button = draw_button("exit", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        exit_button = draw_button("exit", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    exit_button = draw_button("exit", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
    screen.blit(mouse_pointer, mouse_pos)
    pygame.display.update()
    clock.tick(32)
pygame.quit()
sys.exit()
