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
    global game_state, feedback, user_input, border, paused, player_imagex, player_imagey, collision, saving, loading, screen_objects, counter, talking, offset, cooldown, rock_list, holding_rock, picking_up_rock, king, looking_at_inventory, departing, enemy_list, rotated_npc, player_on_battlefield, rotation_counter, selected
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
    cooldown = 0
    rock_list = []
    holding_rock = False
    picking_up_rock = False
    king = pygame.Rect(0, 0, 0, 0)
    looking_at_inventory = False
    departing = False
    enemy_list = []
    rotated_npc = None
    player_on_battlefield = pygame.Rect(0, 0, 0, 0)
    rotation_counter = 0
    selected = None

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
        path = resource_path(os.path.join("save_data", folder, data))
    else:
        path = resource_path(os.path.join("save_data", data))
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
            game_data["mission"] = 0
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
    if game_data["area"] == "city":
        number = random.randint(20, 50)
    else:
        number = 0
    for n in range(number):
        new_npc = None
        if current_map == city_map:
            x = random.randint(0, 8000)
            y = random.randint(0, 8000)
        while True:
            collision = False
            for thing in current_map.keys():
                rect = pygame.Rect(x - 192, y - 192, 384, 384)
                if rect.colliderect(thing):
                    x = random.randint(0, 7000)
                    y = random.randint(0, 7000)
                    collision = True
            if collision == False:
                break
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
            if game_data["mission"] == 0:
                words = random.sample(npc1_insults[0], 5)
            elif game_data["mission"] == 1:
                words = random.sample(npc1_insults[1], 5)
            if direction == "north":    
                imagey = 192
            elif direction == "east":    
                imagey = 384
            elif direction == "west":    
                imagey = 576
            elif direction == "south":    
                imagey = 0
        elif new_number == 2:
            if game_data["mission"] == 0:
                words = random.sample(npc2_insults[0], 5)
            elif game_data["mission"] == 1:
                words = random.sample(npc2_insults[1], 5)
            if direction == "north":    
                imagey = 768
            elif direction == "east":    
                imagey = 1152
            elif direction == "west":    
                imagey = 1344
            elif direction == "south":    
                imagey = 960
        elif new_number == 3:
            if game_data["mission"] == 0:
                words = random.sample(npc3_insults[0], 5)
            elif game_data["mission"] == 1:
                words = random.sample(npc3_insults[1], 5)
            if direction == "north":    
                imagey = 1728
            elif direction == "east":    
                imagey = 1920
            elif direction == "west":    
                imagey = 2112
            elif direction == "south":    
                imagey = 1536
        elif new_number == 4:
            if game_data["mission"] == 0:
                words = random.sample(npc4_insults[0], 5)
            elif game_data["mission"] == 1:
                words = random.sample(npc4_insults[1], 5)
            if direction == "north":    
                imagey = 2496
            elif direction == "east":    
                imagey = 2688
            elif direction == "west":    
                imagey = 2880
            elif direction == "south":    
                imagey = 2304
        new_npc = NPC_class(x, y, 0, imagey, random.randint(3, 5), direction, words)
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
        self.timer = 0
        self.moving = False
        self.alive = True
        self.rotated = None
        self.old_npc_x = x
        self.old_npc_y = y

class rock():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

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

class enemy():
    def __init__(self, x, y, direction, name, health, gold, item, stats, weapon, armor):
        self.x = x
        self.y = y
        self.direction = direction
        self.name = name
        self.health = health
        self.gold = gold
        self.item = item
        self.stats = stats
        self.weapon = weapon
        self.armor = armor
        self.alive = True
    
city_map = {(0, 0, 200, 7600): "wall", (0, 7400, 7600, 200): "wall", (7400, 0, 200, 7600): "wall", (0, 0, 7600, 200): "wall", (500, 1200, 768, 768):"house", (700, 7000, 768, 768): "house", (800, 6400, 768, 768): "house", (6000, 5000, 768, 768): "house", (4000, 2700, 768, 768): "building", (4500, 600, 768, 768): "building", (700, 750, 768, 768): "building", (4500, 6000, 768, 768): "tree", (300, 400, 768, 768): "tree", (6000, 7500, 768, 768): "tree", (500, 4000, 768, 768): "tree", (4500, 4500, 768, 768): "armory", (3300, 2000, 1440, 1840): "castle"}
castle_map = {(0, 0, 100, 3000): "wall", (0, 2900, 2000, 100): "wall", (1900, 0, 100, 3000): "wall", (0, 0, 2000, 100): "wall"}
throne_room_map = {(0, 0, 1000, 100): "wall", (0, 0, 100, 1000): "wall", (990, 0, 100, 1090): "wall", (0, 990, 1000, 100): "wall"}

city_door = pygame.Rect(1500, 3100, 384, 384)
castle_door = pygame.Rect(3876, 3530, 384, 384)
throne_room_door = pygame.Rect(1500, 200, 384, 384)
castle_entry_way_door = pygame.Rect(1150, 1190, 384, 384)
city_gate = pygame.Rect(3850, 7705, 384, 384)

npc1_insults = {0: ["I heard the king has a really important mission for you.", "Howdy!", "Don't you have something better to do?", "The castle's up north if that's where your headed", "Shouldn't you be going to the castle?", "What are you up to?", "That's it. Nap time.", "You're lucky you get to go inside the castle, no one's allowed in there.", "The Castle's North. that big building you LITTERALLY can't miss!"], 1: ["Those monsters destroyed my garden last night!", "What happened in the castle?", "Howdy!", "What's up?", "Someone needs to get rid of those monsters...", "I need a nap...", "If you're looking for the city gate, it's south, at the end of the road."]}
npc2_insults = {0: ["What?", "What do you want?", "Don't you have something better to do?", "What is it this time?", "Hello.", "If you're looking for the castle, just follow the road north.", "Nice hair.", "You're lucky the king summoned you to the castle, he doesn't let anyone else in.", "looking for the castle? it's the big building you can see from anywhere in town."], 1: ["Hello!", "The city gate is south. Just follow the road.", "My garden was devestated by those horrible monsters!", "How'd it go in the castle?", "What?", "The city gate is at the end of the road."]}
npc3_insults = {0: ["Yo!", "Sup?", "The castle's north, at the end of the road.", "Hey.", "Do I know you?", "Be careful in the castle, I don't trust the king one bit.", "The castle's up north. Just follow the road.", "Suspicious the king only lets you in the castle...", "You can't find the castle? Are you blind?"], 1: ["That king is suspicious...", "So, what is this secret mission of yours, mercenary?", "Yo!", "Sup?", "The city gate is south. But why were you sent out of town?"]}
npc4_insults = {0: ["The road's over there. Use it.", "I gotta go, I'm late for nap time.", "Looking for the castle? Just follow the road north.", "If the king sent for you, you'd better get to the castle.", "Don't you have somewhere to be?", "What do you want, peasant?", "Goodbye.", "You're actually allowed in the castle?!", "The sooner you get to the castle, the sooner you can stop hassling me."], 1: ["I gotta go, nap time.", "Hi", "The road's over there. Use it.", "Some monsters attacked my garden last night.", "I'll kill those little monsters next time they go near my garden!"]}
city_background = pygame.image.load(resource_path("city_background.png"))
city_background = pygame.transform.scale(city_background, (9000, 9000))
castle_background = pygame.image.load(resource_path("castle_background.png"))
castle_background = pygame.transform.scale(castle_background, (4000, 4000))
objects = pygame.image.load(resource_path("objects.png"))
objects = pygame.transform.scale(objects, (1536, 1536))
doors = pygame.image.load(resource_path("doors.png"))
doors = pygame.transform.scale(doors, (768, 384))
castle_image = pygame.image.load(resource_path("castle.png"))
castle_image = pygame.transform.scale(castle_image, (1440, 1840))
human = pygame.image.load(resource_path("human.png"))
elf = pygame.image.load(resource_path("elf.png"))
dwarf = pygame.image.load(resource_path("dwarf.png"))
human = pygame.transform.scale(human, (1536, 1536))
elf = pygame.transform.scale(elf, (1536, 1536))
dwarf = pygame.transform.scale(dwarf, (1536, 1536))
npc = pygame.image.load(resource_path("npc.png"))
npc = pygame.transform.scale(npc, (1536, 3264))
king_image = npc.subsurface((0, 3072, 192, 192))
king_image = pygame.transform.scale(king_image, (384, 384))
enemies = pygame.image.load(resource_path("enemies.png"))
mouse_pointer = pygame.image.load(resource_path("sword.png"))
mouse_pointer = pygame.transform.rotate(mouse_pointer, 35)
pygame.mixer.music.load(resource_path("exploring_song.wav"))

too_long_name_insults = ["enter a name, not a book", "nope, too long", "you know what a name is, right?", "do you want to play the game or type all day?", "stop spazzing, start holding backspace", "That's a computer, not a punching bag"]
too_short_name_insults = ["that's not a name", "nope", "you have a name, right?", "try again", "just push some buttons", "try hitting a few keys, see what happens"]
small_font = pygame.font.SysFont(None, 30, bold=False)
medium_font = pygame.font.SysFont(None, 50, bold=False)
big_font = pygame.font.SysFont(None, 60, bold=False)
huge_font = pygame.font.SysFont(None, 80, bold=True)
sprite_size = 192
clock = pygame.time.Clock()
width = 1536
height = 814
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h - 50
if width > height:
    size = height - 50
else:
    size = width - 50
small_human = pygame.transform.scale(human, (size // 10 * 8, size // 10 * 8))
small_elf = pygame.transform.scale(elf, (size // 10 * 8, size // 10 * 8))
small_dwarf = pygame.transform.scale(dwarf, (size // 10 * 8, size // 10 * 8))
enemies = pygame.transform.scale(enemies, (size // 10 * 8, size // 10 * 8))
player_rect = pygame.Rect(width // 2 - 96, height // 2 - 96, 192, 192)
window = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.Surface((width, height))
pygame.display.set_caption("Hounder")
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
                            player = character(*tuple(game_data["player"].values()))
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            elif game_data["area"] == "castle":
                                background = castle_background
                                current_map = castle_map
                            elif game_data["area"] == "throne room":
                                background = castle_background
                                current_map = throne_room_map
                            if player.race == "human":
                                player_sprite = human
                            if player.race == "elf":
                                player_sprite = elf
                            if player.race == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                            pygame.mixer.music.play(-1)
                    if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                        if file2["name"] != "empty":
                            game_data = file2
                            game_state = "exploring"
                            player = character(*tuple(game_data["player"].values()))
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            elif game_data["area"] == "castle":
                                background = castle_background
                                current_map = castle_map
                            elif game_data["area"] == "throne room":
                                background = castle_background
                                current_map = throne_room_map
                            if player.race == "human":
                                player_sprite = human
                            if player.race == "elf":
                                player_sprite = elf
                            if player.race == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                            pygame.mixer.music.play(-1)
                    if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                        if file3["name"] != "empty":
                            game_data = file3
                            game_state = "exploring"
                            player = character(*tuple(game_data["player"].values()))
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            elif game_data["area"] == "castle":
                                background = castle_background
                                current_map = castle_map
                            elif game_data["area"] == "throne room":
                                background = castle_background
                                current_map = throne_room_map
                            if player.race == "human":
                                player_sprite = human
                            elif player.race == "elf":
                                player_sprite = elf
                            elif player.race == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                            pygame.mixer.music.play(-1)
                elif game_state == "choose name":
                    if mouse_pos[0] < submit_button.right and mouse_pos[0] > submit_button.left and mouse_pos[1] > submit_button.top and mouse_pos[1] < submit_button.bottom:
                        submit_input(user_input)
                elif game_state == "choose race":
                    if mouse_pos[0] < human_button.right and mouse_pos[0] > human_button.left and mouse_pos[1] > human_button.top and mouse_pos[1] < human_button.bottom:
                        player.race = "human"
                        player_sprite = human
                        player.stats = {"attack": 10, "defense": 10, "accuracy": 10, "avoidance": 10, "magic": 10, "resistance": 10, "movement": 2}
                        game_state = "choose class"
                    elif mouse_pos[0] < elf_button.right and mouse_pos[0] > elf_button.left and mouse_pos[1] > elf_button.top and mouse_pos[1] < elf_button.bottom:
                        player.race = "elf"
                        player_sprite = elf
                        game_state = "choose class"
                        player.stats = {"attack": 8, "defense": 8, "accuracy": 12, "avoidance": 10, "magic": 12, "resistance": 12, "movement": 3}
                    elif mouse_pos[0] < dwarf_button.right and mouse_pos[0] > dwarf_button.left and mouse_pos[1] > dwarf_button.top and mouse_pos[1] < dwarf_button.bottom:
                        player.race = "dwarf"
                        player_sprite = dwarf
                        game_state = "choose class"
                        player.stats = {"attack": 13, "defense": 15, "accuracy": 10, "avoidance": 8, "magic": 6, "resistance": 8, "movement": 1}
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
                        game_data["worldx"] = 3300
                        game_data["worldy"] = 5000
                        game_data["area"] = "city"
                        current_map = city_map
                        background = city_background
                        pygame.mixer.music.play(-1)
                        game_state = "exploring"
                elif game_state == "exploring":
                    if paused == True:
                        if saving == False and loading == False and looking_at_inventory == False:
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
                            if mouse_pos[0] < inventory_button.right and mouse_pos[0] > inventory_button.left and mouse_pos[1] > inventory_button.top and mouse_pos[1] < inventory_button.bottom:
                                looking_at_inventory = True
                        if saving == True:
                            if counter == 8:
                                if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom:
                                    feedback = "saving..."
                                    player.update()
                                    game_data["player"] = player.dict
                                    save(game_data, "file1")
                                    feedback = "saved!"
                                if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                                    feedback = "saving..."
                                    player.update()
                                    game_data["player"] = player.dict
                                    save(game_data, "file2")
                                    feedback = "saved!"
                                if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                                    feedback = "saving..."
                                    player.update()
                                    game_data["player"] = player.dict
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
                                    if player.race == "elf":
                                        player_sprite = elf
                                    elif player.race == "human":
                                        player_sprite == human
                                    elif player.race == "dwarf":
                                        player_sprite = dwarf
                                    if game_data["area"] == "city":
                                        background = city_background
                                        current_map = city_map
                                    elif game_data["area"] == "castle":
                                        background = castle_background
                                        current_map = castle_map
                                    elif game_data["area"] == "throne room":
                                        background = castle_background
                                        current_map = throne_room_map
                                    player.update()
                                    feedback = ""
                                    loading = False
                                    paused = False
                                if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                                    feedback = "loading..."
                                    game_data = load("file2")
                                    player = character(*tuple(game_data["player"].values()))
                                    if player.race == "elf":
                                        player_sprite = elf
                                    elif player.race == "human":
                                        player_sprite == human
                                    elif player.race == "dwarf":
                                        player_sprite = dwarf
                                    if game_data["area"] == "city":
                                        background = city_background
                                        current_map = city_map
                                    elif game_data["area"] == "castle":
                                        background = castle_background
                                        current_map = castle_map
                                    elif game_data["area"] == "throne room":
                                        background = castle_background
                                        current_map = throne_room_map
                                    player.update()
                                    feedback = ""
                                    loading = False
                                    paused = False
                                if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                                    feedback = "loading..."
                                    game_data = load("file3")
                                    player = character(*tuple(game_data["player"].values()))
                                    if player.race == "elf":
                                        player_sprite = elf
                                    elif player.race == "human":
                                        player_sprite == human
                                    elif player.race == "dwarf":
                                        player_sprite = dwarf
                                    if game_data["area"] == "city":
                                        background = city_background
                                        current_map = city_map
                                    elif game_data["area"] == "castle":
                                        background = castle_background
                                        current_map = castle_map
                                    elif game_data["area"] == "throne room":
                                        background = castle_background
                                        current_map = throne_room_map
                                    player.update()
                                    feedback = ""
                                    loading = False
                                    paused = False
                                if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                                    feedback = ""
                                    loading = False
                        if looking_at_inventory == True:
                            if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                                 looking_at_inventory = False
                    else:
                        if talking == False:
                            for NPC in npc_list:
                                npc_rect = pygame.Rect(NPC.x - game_data["worldx"], NPC.y - game_data["worldy"], 192, 192)
                                if mouse_pos[0] < npc_rect.right and mouse_pos[0] > npc_rect.left and mouse_pos[1] > npc_rect.top and mouse_pos[1] < npc_rect.bottom:
                                    talking = True
                                    npc_words = random.sample(NPC.words, 1)
                            if mouse_pos[0] < castle_door.right - game_data["worldx"] and mouse_pos[0] > castle_door.left - game_data["worldx"] and mouse_pos[1] > castle_door.top - game_data["worldy"] and mouse_pos[1] < castle_door.bottom - game_data["worldy"] and game_data["area"] == "city" and cooldown < 1:
                                game_data["area"] = "castle"
                                game_data["worldx"] = city_door.x + 192 - (width // 2)
                                game_data["worldy"] = city_door.top - 10 - (height // 2)
                                current_map = castle_map
                                background = castle_background
                                cooldown = 5
                                npc_list = []
                            if mouse_pos[0] < city_door.right - game_data["worldx"] and mouse_pos[0] > city_door.left - game_data["worldx"] and mouse_pos[1] > city_door.top - game_data["worldy"] and mouse_pos[1] < city_door.bottom - game_data["worldy"] and game_data["area"] == "castle" and cooldown < 1:
                                game_data["area"] = "city"
                                game_data["worldx"] = castle_door.x + 192 - (width // 2)
                                game_data["worldy"] = castle_door.bottom + 10 - (height // 2)
                                current_map = city_map
                                background = city_background
                                cooldown = 5
                                spawn_npc()
                            if mouse_pos[0] < throne_room_door.right - game_data["worldx"] and mouse_pos[0] > throne_room_door.left - game_data["worldx"] and mouse_pos[1] > throne_room_door.top - game_data["worldy"] and mouse_pos[1] < throne_room_door.bottom - game_data["worldy"] and game_data["area"] == "castle" and cooldown < 1:
                                game_data["area"] = "throne room"
                                game_data["worldx"] = castle_entry_way_door.x + 192 - (width // 2)
                                game_data["worldy"] = castle_entry_way_door.top - 10 - (height // 2)
                                current_map = throne_room_map
                                cooldown = 5
                            if mouse_pos[0] < castle_entry_way_door.right - game_data["worldx"] and mouse_pos[0] > castle_entry_way_door.left - game_data["worldx"] and mouse_pos[1] > castle_entry_way_door.top - game_data["worldy"] and mouse_pos[1] < castle_entry_way_door.bottom - game_data["worldy"] and game_data["area"] == "throne room" and cooldown < 1:
                                game_data["area"] = "castle"
                                game_data["worldx"] = throne_room_door.x + 192 - (width // 2)
                                game_data["worldy"] = throne_room_door.bottom + 10 - (height // 2)
                                current_map = castle_map
                                cooldown = 5
                            if mouse_pos[0] < king.right and mouse_pos[0] > king.left and mouse_pos[1] > king.top and mouse_pos[1] < king.bottom and game_data["area"] == "throne room":
                                talking = True
                                if game_data["mission"] == 0:
                                    npc_words = [f"So {game_data['name']}, you finally decided to show up."]
                                elif game_data["mission"] == 1:
                                    npc_words = ["What are you doing here? Hurry up and finish your mission!"]
                            if mouse_pos[0] < city_gate.right - game_data["worldx"] and mouse_pos[0] > city_gate.left - game_data["worldx"] and mouse_pos[1] > city_gate.top - game_data["worldy"] and mouse_pos[1] < city_gate.bottom - game_data["worldy"] and game_data["area"] == "city" and cooldown < 1:
                                if game_data["mission"] == 0:
                                    npc_words = ["Where do you think you're going? Get to the castle!"]
                                    talking = True
                                else:
                                    departing = True
                            if departing == True:
                                try:
                                    if mouse_pos[0] < yes_button.right and mouse_pos[0] > yes_button.left and mouse_pos[1] > yes_button.top and mouse_pos[1] < yes_button.bottom and game_data["area"] == "city" and cooldown < 1:
                                        if game_data["mission"] == 1:
                                            background = city_background
                                            player_battlefieldx = 4
                                            player_battlefieldy = 9
                                            player_imagex = 0
                                            player_imagey = size // 10
                                            player_destinationx = 0
                                            player_destinationy = size // 10
                                            enemy_list = [enemy(2, 0, "south", "bunny", 10, 0, None, {"attack": 5, "defence": 7, "accuracy": 15, "avoidance": 30, "magic": 0, "resistance": 7, "movement": 4}, None, None), enemy(8, 1, "south", "bunny", 10, 0, None, {"attack": 5, "defence": 7, "accuracy": 15, "avoidance": 30, "magic": 0, "resistance": 7, "movement": 4}, None, None), enemy(6, 0, "south", "bunny", 10, 0, None, {"attack": 5, "defence": 7, "accuracy": 15, "avoidance": 30, "magic": 0, "resistance": 7, "movement": 4}, None, None), enemy(4, 1, "south", "bunny", 10, 0, None, {"attack": 5, "defence": 7, "accuracy": 15, "avoidance": 30, "magic": 0, "resistance": 7, "movement": 4}, None, None)]
                                            npc_words = ["You must kill all the monsters to win the battle."]
                                            talking = True
                                        departing = False
                                        item_buttons = []
                                        pygame.mixer.music.load(resource_path("battle_song.wav"))
                                        pygame.mixer.music.play(-1)
                                        players_turn = True
                                        game_state = "battle"
                                    if mouse_pos[0] < no_button.right and mouse_pos[0] > no_button.left and mouse_pos[1] > no_button.top and mouse_pos[1] < no_button.bottom and game_data["area"] == "city" and cooldown < 1:
                                        departing = False
                                except NameError:
                                    pass
                        else:
                            if npc_words == [f"So {game_data['name']}, you finally decided to show up."]:
                                npc_words = ["I have a very important mission for you."]
                            elif npc_words == ["I have a very important mission for you."]:
                                npc_words = ["There are monsters outside the city. They have been destroying our crops."]
                            elif npc_words == ["There are monsters outside the city. They have been destroying our crops."]:
                                npc_words = ["You need to go kill them before they attack the city again."]
                            elif npc_words == ["You need to go kill them before they attack the city again."]:
                                npc_words = ["And you can take this dog with you, if you need help. It's annoying."]
                            elif npc_words == ["And you can take this dog with you, if you need help. It's annoying."]:
                                npc_words = ["*You stuff the dog in your pocket*"]
                                player.inventory.append("dog")
                                player.update()
                            elif npc_words == ["*You stuff the dog in your pocket*"]:
                                npc_words = ["If you survive... I mean, when you come back, I'll give you another mission."]
                                game_data["mission"] = 1
                            else:
                                talking = False
                elif game_state == "battle":
                    if talking == True:
                        if npc_words == ["You must kill all the monsters to win the battle."]:
                            npc_words = ["Click the player to move around and attack"]
                        elif npc_words == ["Click the player to move around and attack"]:
                            npc_words = ["Click the items button to use your items"]
                        elif npc_words == ["Click the items button to use your items"]:
                            npc_words = ["You can throw pets and they'll fight for you (like that dog the king gave you)"]
                        elif npc_words == ["You can throw pets and they'll fight for you (like that dog the king gave you)"]:
                            npc_words = ["Good luck! (You're gonna need it)"]
                        else:
                            talking = False
                    else:
                        if mouse_pos[0] < retreat_button.right and mouse_pos[0] > retreat_button.left and mouse_pos[1] > retreat_button.top and mouse_pos[1] < retreat_button.bottom and looking_at_inventory == False and players_turn == True:
                            background = city_background
                            current_map = city_map
                            player_imagex = 0
                            player_imagey = 192
                            game_state = "exploring"
                            pygame.mixer.music.load(resource_path("exploring_song.wav"))
                            pygame.mixer.music.play(-1)
                            departing = False
                        if mouse_pos[0] < player_on_battlefield.right and mouse_pos[0] > player_on_battlefield.left and mouse_pos[1] > player_on_battlefield.top and mouse_pos[1] < player_on_battlefield.bottom:
                            selected = "player"
                        for e in enemy_list:
                            enemy_rect = pygame.Rect(e.x * (size // 10) + (width // 2 - size // 2), e.y * (size // 10) + (height // 2 - size // 2), size // 10, size // 10)
                            if mouse_pos[0] < enemy_rect.right and mouse_pos[0] > enemy_rect.left and mouse_pos[1] > enemy_rect.top and mouse_pos[1] < enemy_rect.bottom:
                                selected = e
                        if selected == "player":
                            if mouse_pos[0] > width // 2 - size // 2 and mouse_pos[0] < ((width // 2) + size) - (size // 2) + size and mouse_pos[1] > height // 2 - size // 2 and mouse_pos[1] < ((height // 2) + size) - (size // 2) + size:
                                possible_player_destinationx = mouse_pos[0] // size + (width // 2 - size // 2)
                                possible_player_destinationy = mouse_pos[1] // size + (height // 2 - size // 2)
                                if possible_player_destinationx > player_battlefieldx + (size // 10 * player.stats["movement"]) or possible_player_destinationx < player_battlefieldy - (size // 10 * player.stats["movement"]):
                                    pass
                                else:
                                    player_destinationx = possible_player_destinationx
                                    player_destinationy = possible_player_destinationy
                        if looking_at_inventory == True:
                            if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                                item_buttons = []
                                looking_at_inventory = False
                        else:
                            if mouse_pos[0] < items_button.right and mouse_pos[0] > items_button.left and mouse_pos[1] > items_button.top and mouse_pos[1] < items_button.bottom:
                                item_buttons = []
                                looking_at_inventory = True
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
                if event.key == K_ESCAPE and departing == False and talking == False:
                    feedback = ""
                    paused = not paused
                if event.key == K_SPACE and picking_up_rock == False:
                    if holding_rock == True:
                        if player_imagey == 0 or player_imagey == 768:
                            thrown_rock = rock(game_data["worldx"] + (width // 2) - 30, game_data["worldy"] + (height // 2) + 40, "south")
                        elif player_imagey == 192 or player_imagey == 960:
                            thrown_rock = rock(game_data["worldx"] + (width // 2) + 35, game_data["worldy"] + (height // 2) + 40, "north")
                        elif player_imagey == 384 or player_imagey == 1152:
                            thrown_rock = rock(game_data["worldx"] + (width // 2) + 50, game_data["worldy"] + (height // 2), "east")
                        elif player_imagey == 576 or player_imagey == 1344:
                            thrown_rock = rock(game_data["worldx"] + (width // 2) - 50, game_data["worldy"] + (height // 2), "west")
                        rock_list.append(thrown_rock)
                        holding_rock = False
                    else:
                        player_imagey += 768
                        player_imagex = 0
                        picking_up_rock = True
    mousex, mousey = pygame.mouse.get_pos()
    mouse_pos = (mousex * (width / screen_width), mousey * (height / screen_height))
    screen.fill(pygame.Color(0, 0, 0))
    if game_state == "menu":
        text = huge_font.render("Hounder", False, pygame.Color(255, 255, 255))
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
        text = big_font.render("(press esc to pause the game, use the WASD keys to move,", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 125)
        screen.blit(text, text_rect)
        text = big_font.render("and click the left mouse button to interact with things)", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 + 200)
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
        if cooldown > 0:
            cooldown -= 1
        keys = pygame.key.get_pressed()
        old_worldx = game_data["worldx"]
        old_worldy = game_data["worldy"]
        screen.blit(background, (0, 0), area=(game_data["worldx"], game_data["worldy"], width, height))
        if paused == False and talking == False and departing == False:
            for NPC in npc_list:
                if NPC.alive == True:
                    NPC.old_npc_x = NPC.x
                    NPC.old_npc_y = NPC.y
                    if NPC.timer <= 0:
                        NPC.imagex += 40
                        if NPC.imagex >= 1344:
                            NPC.imagex = 0
                        number = random.randint(1, 100)
                        if number == 1:
                            NPC.direction = "north"
                            if NPC.imagey < sprite_size * 4:
                                NPC.imagey = sprite_size
                            elif NPC.imagey < sprite_size * 8:
                                NPC.imagey = sprite_size * 5 
                            elif NPC.imagey < sprite_size * 12:
                                NPC.imagey = sprite_size * 9
                            else:
                                NPC.imagey = sprite_size * 13
                        elif number == 2:
                            NPC.direction = "east"
                            if NPC.imagey < sprite_size * 4:
                                NPC.imagey = sprite_size * 2
                            elif NPC.imagey < sprite_size * 8:
                                NPC.imagey = sprite_size * 6
                            elif NPC.imagey < sprite_size * 12:
                                NPC.imagey = sprite_size * 10
                            else:
                                NPC.imagey = sprite_size * 14
                        elif number == 3:
                            NPC.direction = "west"
                            if NPC.imagey < sprite_size * 4:
                                NPC.imagey = sprite_size * 3
                            elif NPC.imagey < sprite_size * 8:
                                NPC.imagey = sprite_size * 7
                            elif NPC.imagey < sprite_size * 12:
                                NPC.imagey = sprite_size * 11
                            else:
                                NPC.imagey = sprite_size * 15
                        elif number == 4:
                            NPC.direction = "south"
                            if NPC.imagey < sprite_size * 4:
                                NPC.imagey = 0
                            elif NPC.imagey < sprite_size * 8:
                                NPC.imagey = sprite_size * 4
                            elif NPC.imagey < sprite_size * 12:
                                NPC.imagey = sprite_size * 8
                            else:
                                NPC.imagey = sprite_size * 12
                        elif number < 10:
                            NPC.imagex = 0
                            NPC.moving = False
                            NPC.timer = random.randint(20, 100)
                        else:
                            NPC.moving = True
                            NPC.timer = random.randint(20, 100)
                    else:
                        if NPC.moving == False:
                            NPC.timer -= 1
                        else:
                            if NPC.direction == "north":
                                NPC.y -= NPC.speed
                            elif NPC.direction == "west":
                                NPC.x -= NPC.speed
                            elif NPC.direction == "east":
                                NPC.x += NPC.speed
                            elif NPC.direction == "south":
                                NPC.y += NPC.speed
                            NPC.imagex += 40
                            if NPC.imagex >= 1344:
                                NPC.imagex = 0
                            NPC.timer -= 1
                else:
                    if NPC.direction == "north":
                        NPC.y -= 50
                    elif NPC.direction == "west":
                        NPC.x -= 50
                    elif NPC.direction == "east":
                        NPC.x += 50
                    elif NPC.direction == "south":
                        NPC.y += 50
                    if NPC.x - game_data["worldx"] < - 192 or NPC.x - game_data["worldx"] > width + 192 or NPC.y - game_data["worldy"] < - 192 or NPC.y - game_data["worldy"] > height + 192:
                        npc_list.remove(NPC)
            if keys[K_w] == True and picking_up_rock == False:
                if collision == False:
                    player_imagey = 192
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    game_data["worldy"] -= 10
                    if keys[K_a] == False and keys[K_s] == False and keys[K_d] == False and collision == False:
                        game_data["worldy"] -= 4
            if keys[K_a] == True and picking_up_rock == False:
                if collision == False:
                    player_imagey = 576
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    game_data["worldx"] -= 10
                    if keys[K_w] == False and keys[K_s] == False and keys[K_d] == False and collision == False:
                        game_data["worldx"] -= 4
            if keys[K_s] == True and picking_up_rock == False:
                if collision == False:
                    player_imagey = 0
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    game_data["worldy"] += 10
                    if keys[K_a] == False and keys[K_w] == False and keys[K_d] == False and collision == False:
                        game_data["worldy"] += 4
            if keys[K_d] == True and picking_up_rock == False:
                if collision == False:
                    player_imagey = 384
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    game_data["worldx"] += 10
                    if keys[K_a] == False and keys[K_s] == False and keys[K_w] == False and collision == False:
                        game_data["worldx"] += 4
            if keys[K_w] == False and keys[K_a] == False and keys[K_s] == False and keys[K_d] == False and picking_up_rock == False:
                player_imagex = 0
            if picking_up_rock == True:
                player_imagex += 50
                if player_imagex < 1344:
                    player_imagex += 50
                else:
                    player_imagex = 0
                    player_imagey -= 768
                    picking_up_rock = False
                    holding_rock = True
            for rocks in rock_list[:]:
                if rocks.direction == "north":
                    rocks.y -= 30
                elif rocks.direction == "south":
                    rocks.y += 30
                elif rocks.direction == "east":
                    rocks.x += 30
                elif rocks.direction == "west":
                    rocks.x -= 30
                if rocks.x - game_data["worldx"] > width + 10 or rocks.x - game_data["worldx"] < -10 or rocks.y - game_data["worldy"] > height + 10 or rocks.y - game_data["worldy"] < -10:
                    rock_list.remove(rocks)
                rock_rect = pygame.draw.circle(screen, pygame.Color(200, 200, 200), (rocks.x - game_data["worldx"], rocks.y - game_data["worldy"]), 5)
                for obstacle in screen_objects.keys():
                    if rock_rect.colliderect(pygame.Rect(obstacle)):
                        rock_list.remove(rocks)
                for target in npc_list[:]:
                    if rock_rect.colliderect(pygame.Rect(target.x - game_data["worldx"], target.y - game_data["worldy"], 192, 192)):
                        rock_list.remove(rocks)
                        target.direction = rocks.direction
                        rotation_counter = 0
                        target.alive = False
        for NPC in npc_list[:]:
            if NPC.alive == True:
                screen.blit(npc, (NPC.x - game_data["worldx"], NPC.y - game_data["worldy"]), area=(192*round(NPC.imagex/192), NPC.imagey, 192, 192))
            else:
                rotation_counter += 1
                NPC.rotated = npc.subsurface((0, NPC.imagey, 192, 192))
                NPC.rotated = pygame.transform.rotate(NPC.rotated, 20 * rotation_counter)
                screen.blit(NPC.rotated, (NPC.x - game_data["worldx"], NPC.y - game_data["worldy"]))
        screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
        if holding_rock == True:
            if player_imagey == 0:
                pygame.draw.circle(screen, pygame.Color(200, 200, 200), (width // 2 - 30, height // 2 + 40), 5)
            elif player_imagey == 192:
                pygame.draw.circle(screen, pygame.Color(200, 200, 200), (width // 2 + 35, height // 2 + 40), 5)
            elif player_imagey == 384:
                pygame.draw.circle(screen, pygame.Color(200, 200, 200), (width // 2 + 30, height // 2), 5)
            elif player_imagey == 576:
                pygame.draw.circle(screen, pygame.Color(200, 200, 200), (width // 2 - 30, height // 2), 5)
        screen_objects = {}
        for obstacle in current_map.keys():
            obstacle_rect = pygame.Rect(obstacle)
            if current_map[obstacle] == "wall":
                screen_object_rect = pygame.draw.rect(screen, pygame.Color(150, 150, 150), (obstacle_rect.x - game_data["worldx"] + (width/2), obstacle_rect.y - game_data["worldy"] + (height/2), obstacle_rect.width, obstacle_rect.height))
                screen_object = tuple(screen_object_rect)
                screen_objects[screen_object] = "wall"
                if player_rect.top < screen_object_rect.top and player_rect.colliderect(screen_object_rect):
                    screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
            elif current_map[obstacle] == "house":
                screen_object_rect = screen.blit(objects, (obstacle_rect.x - game_data["worldx"] + (width/2), obstacle_rect.y - game_data["worldy"] + (height/2)), area=(0, 0, 768, 768))
                screen_object = tuple(screen_object_rect)
                screen_objects[screen_object] = "house"
                if player_rect.top < screen_object_rect.bottom and player_rect.colliderect(screen_object_rect):
                    screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
            elif current_map[obstacle] == "building":
                screen_object_rect = screen.blit(objects, (obstacle_rect.x - game_data["worldx"] + (width/2), obstacle_rect.y - game_data["worldy"] + (height/2)), area=(768, 0, 768, 768))
                screen_object = tuple(screen_object_rect)
                screen_objects[screen_object] = "building"
                if player_rect.top < screen_object_rect.bottom and player_rect.colliderect(screen_object_rect):
                    screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
            elif current_map[obstacle] == "castle":
                screen_object_rect = pygame.Rect(obstacle_rect.x - game_data["worldx"], obstacle_rect.y - game_data["worldy"], obstacle_rect.width, obstacle_rect.height)
                screen_object = tuple(screen_object_rect)
                screen_objects[screen_object] = "castle"
                screen.blit(castle_image, (screen_object_rect.x, screen_object_rect.y))
                screen.blit(doors, (screen_object_rect.x + (screen_object_rect.width // 2.5), screen_object_rect.bottom - 310), area=(384, 0, 384, 384)) # castle_door
                if player_rect.top < screen_object_rect.bottom and player_rect.colliderect(screen_object_rect):
                    screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
            elif current_map[obstacle] == "tree":
                screen_object_rect = pygame.Rect(obstacle_rect.x - game_data["worldx"], obstacle_rect.y - game_data["worldy"], obstacle_rect.width, obstacle_rect.height)
                screen_object = tuple(screen_object_rect)
                screen_objects[screen_object] = "tree"
                screen.blit(objects, (screen_object_rect.x, screen_object_rect.y), area=(768, 0, 768, 768))
                if player_rect.top < screen_object_rect.bottom and player_rect.colliderect(screen_object_rect):
                    screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
        if game_data["area"] == "castle":
            screen.blit(doors, (city_door.x - game_data["worldx"], city_door.y - game_data["worldy"]), area=(384, 0, 384, 384)) # city_door
            screen.blit(doors, (throne_room_door.x - game_data["worldx"], throne_room_door.y - game_data["worldy"]), area=(384, 0, 384, 384)) # throne_room_door
        if game_data["area"] == "throne room":
            screen.blit(doors, (castle_entry_way_door.x - game_data["worldx"], castle_entry_way_door.y - game_data["worldy"]), area=(384, 0, 384, 384)) # castle_entry_way_door
            king = screen.blit(king_image, (1150 - game_data["worldx"], 500 - game_data["worldy"]))
        if game_data["area"] == "city":
            screen.blit(doors, (city_gate.x - game_data["worldx"], city_gate.y - game_data["worldy"]), area=(0, 0, 384, 384)) # city_gate
        for obstacle in screen_objects.keys():
            if screen_objects[obstacle] == "house":
                new_obstacle_rect = pygame.Rect(obstacle[0] + 300, (obstacle[1] + obstacle[3]) - 100, obstacle[2] // 3, 100)
            elif screen_objects[obstacle] == "building":
                new_obstacle_rect = pygame.Rect(obstacle[0] + 200, (obstacle[1] + obstacle[3]) - 50, obstacle[2] // 3, 100)
            elif screen_objects[obstacle] == "castle":
                new_obstacle_rect = pygame.Rect(obstacle[0] + 125, obstacle[1] + 500, obstacle[2] - 300, obstacle[3] - 500)
            elif screen_objects[obstacle] == "tree":
                new_obstacle_rect = pygame.Rect(obstacle[0] + 200, obstacle[1] + obstacle[3] - 50, obstacle[2] - 500, 100)
            else:
                new_obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle[2] - 50, obstacle[3] - 10)
            if player_rect.colliderect(pygame.Rect(obstacle)):
                if screen_objects[obstacle] == "house" or screen_objects[obstacle] == "building" or screen_objects[obstacle] == "castle" or screen_objects[obstacle] == "tree":
                    if player_rect.colliderect(new_obstacle_rect):
                        if player_rect.bottom >= new_obstacle_rect.bottom:
                            pass
                        else:
                            collision = True
                            game_data["worldx"] = old_worldx
                            game_data["worldy"] = old_worldy
                    if player_rect.bottom > new_obstacle_rect.top + 100 or player_rect.left > new_obstacle_rect.right:
                        screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
                else:
                    if player_rect.colliderect(new_obstacle_rect):
                        if player_rect.bottom > new_obstacle_rect.top:
                            screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
                        collision = True
                        game_data["worldx"] = old_worldx
                        game_data["worldy"] = old_worldy
            for NPC in npc_list[:]:
                npc_rect = pygame.Rect(NPC.x - game_data["worldx"], NPC.y - game_data["worldy"], 192, 192)
                if NPC.alive == True:
                    if npc_rect.colliderect(pygame.Rect(obstacle)):
                        if screen_objects[obstacle] == "house" or screen_objects[obstacle] == "building" or screen_objects[obstacle] == "castle":
                            if npc_rect.colliderect(new_obstacle_rect):
                                if npc_rect.bottom >= new_obstacle_rect.bottom:
                                    pass
                                else:
                                    NPC.x = NPC.old_npc_x
                                    NPC.y = NPC.old_npc_y
                                    NPC.timer = 0
                            if npc_rect.bottom > new_obstacle_rect.top + 15 or npc_rect.left > new_obstacle_rect.right:
                                screen.blit(npc, (NPC.x - game_data["worldx"], NPC.y - game_data["worldy"]), area=(192*round(NPC.imagex/192), NPC.imagey, 192, 192))
                        else:
                            if npc_rect.colliderect(new_obstacle_rect):
                                if npc_rect.bottom > new_obstacle_rect.top:
                                    screen.blit(npc, (NPC.x - game_data["worldx"], NPC.y - game_data["worldy"]), area=(192*round(NPC.imagex/192), NPC.imagey, 192, 192))
                                NPC.x = NPC.old_npc_x
                                NPC.y = NPC.old_npc_y
                                NPC.timer = 0
                else:
                    if npc_rect.colliderect(pygame.Rect(obstacle)):
                        npc_list.remove(NPC)
        if player_rect.colliderect(king.inflate(-192, -192)):
            collision = True
            game_data["worldx"] = old_worldx
            game_data["worldy"] = old_worldy
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
            elif looking_at_inventory == True:
                screen.fill(pygame.Color(200, 200, 200))
                text = big_font.render(f"name: {player.name}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 20))
                if player.race == "human":
                    screen.blit(human, (width // 8, 70), area=(0, 0, 192, 192))
                elif player.race == "elf":
                    screen.blit(elf, (width // 8, 70), area=(0, 0, 192, 192))
                elif player.race == "dwarf":
                    screen.blit(dwarf, (width // 8, 70), area=(0, 0, 192, 192))
                text = medium_font.render(f"race: {player.race}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 282))
                text = medium_font.render(f"class: {player.Class}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 332))
                text = medium_font.render(f"level {player.level}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 382))
                text = medium_font.render(f"health: {player.health}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 432))
                text = medium_font.render(f"attack: {player.stats['attack']}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 482))
                text = medium_font.render(f"defense: {player.stats['defense']}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 532))
                text = medium_font.render(f"accuracy: {player.stats['accuracy']}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 582))
                text = medium_font.render(f"avoidance: {player.stats['avoidance']}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 632))
                text = medium_font.render(f"magic: {player.stats['magic']}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 682))
                text = medium_font.render(f"resistance: {player.stats['resistance']}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width // 8, 732))
                text = big_font.render("inventory", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width *.75, 20))
                text = medium_font.render(f"gold: {player.gold}", False, pygame.Color(255, 255, 255))
                screen.blit(text, (width *.75, 70))
                for item in player.inventory:
                    if item == player.armor_equiped or item == player.weapon_equiped or item == player.accessory_equiped:
                        text = medium_font.render(f"{item} E", False, pygame.Color(255, 255, 255))
                    else:
                        text = medium_font.render(f"{item}", False, pygame.Color(255, 255, 255))
                    screen.blit(text, (width * .75, 70 + (player.inventory.index(item) + 1) * 50))
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
                    if mouse_pos[0] < inventory_button.right and mouse_pos[0] > inventory_button.left and mouse_pos[1] > inventory_button.top and mouse_pos[1] < inventory_button.bottom:
                        inventory_button = draw_button("inventory", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        inventory_button = draw_button("inventory", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    inventory_button = draw_button("inventory", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                try:
                    if mouse_pos[0] < exit_button.right and mouse_pos[0] > exit_button.left and mouse_pos[1] > exit_button.top and mouse_pos[1] < exit_button.bottom:
                        exit_button = draw_button("exit", height/2 + 300, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        exit_button = draw_button("exit", height/2 + 300, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    exit_button = draw_button("exit", height/2 + 300, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
        if departing == True:
            text = huge_font.render("Do you want to attempt your mission?", False, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (width/2, height/2 - 350)
            screen.blit(text, text_rect)
            try:
                if mouse_pos[0] < yes_button.right and mouse_pos[0] > yes_button.left and mouse_pos[1] > yes_button.top and mouse_pos[1] < yes_button.bottom:
                    yes_button = draw_button("Yeah, let's go!", height/2, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                else:
                    yes_button = draw_button("Yeah, let's go!", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            except NameError:
                yes_button = draw_button("Yeah, let's go!", height/2, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            try:
                if mouse_pos[0] < no_button.right and mouse_pos[0] > no_button.left and mouse_pos[1] > no_button.top and mouse_pos[1] < no_button.bottom:
                    no_button = draw_button("No, I'm feeling lazy.", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                else:
                    no_button = draw_button("No, I'm feeling lazy.", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            except NameError:
                no_button = draw_button("No, I'm feeling lazy.", height/2 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
    elif game_state == "battle":
        screen.fill(pygame.Color(200, 200, 200))
        if width > height:
            size = height - 50
        else:
            size = width - 50
        screen.blit(background, (width // 2 - size // 2, height // 2 - size // 2), area=(0, 0, size - 5, size - 5))
        for rect in range(10):
            for inside_rect in range(10):
                rectangle = pygame.Rect(size // 10 * rect + (width // 2 - size // 2), size // 10 * inside_rect + (height // 2 - size // 2), size // 10, size // 10)
                if mouse_pos[0] < rectangle.right and mouse_pos[0] > rectangle.left and mouse_pos[1] > rectangle.top and mouse_pos[1] < rectangle.bottom:
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0), rectangle, width = 1)
                else:
                    pygame.draw.rect(screen, pygame.Color(200, 200, 200), rectangle, width = 1)
        if game_data["mission"] == 1:
            text = medium_font.render("Mission 1 objective:", False, pygame.Color(255, 255, 255))
            screen.blit(text, (20, 30))
            text = medium_font.render("Rout all enemies", False, pygame.Color(255, 255, 255))
            screen.blit(text, (20, 60))
        text = medium_font.render("Enemies:", False, pygame.Color(255, 255, 255))
        screen.blit(text, (20, 120))
        for e in enemy_list:
            if e.alive == True:
                text = small_font.render(e.name, False, pygame.Color(255, 255, 255))
                screen.blit(text, (20, 170 + enemy_list.index(e) * 30))
        text = medium_font.render("retreat", False, pygame.Color(255, 255, 255))
        retreat_button = text.get_rect()
        retreat_button.center = (50, height - 75)
        retreat_button.width += 50
        retreat_button.height += 20
        if mouse_pos[0] < retreat_button.right and mouse_pos[0] > retreat_button.left and mouse_pos[1] > retreat_button.top and mouse_pos[1] < retreat_button.bottom and talking == False:
            retreat_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), retreat_button)
        else:
            retreat_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), retreat_button)
        screen.blit(text, (retreat_button.x + 25, retreat_button.y + 10))
        text = medium_font.render("items", False, pygame.Color(255, 255, 255))
        items_button = text.get_rect()
        items_button.center = (width - (items_button.width + 50) // 2 - 50, height - 75)
        items_button.width += 80
        items_button.height += 20
        if mouse_pos[0] < items_button.right and mouse_pos[0] > items_button.left and mouse_pos[1] > items_button.top and mouse_pos[1] < items_button.bottom and talking == False:
            items_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), items_button)
        else:
            items_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), items_button)
        screen.blit(text, (items_button.x + 25, items_button.y + 10))
        if player.race == "human":
            player_on_battlefield = screen.blit(small_human, (player_battlefieldx * (size // 10)  + (width // 2 - size // 2), player_battlefieldy * (size // 10) + (height // 2 - size // 2)), area=(player_imagex, player_imagey, size // 10, size // 10))
        if player.race == "elf":
            player_on_battlefield = screen.blit(small_elf, (player_battlefieldx * (size // 10)  + (width // 2 - size // 2), player_battlefieldy * (size // 10) + (height // 2 - size // 2)), area=(player_imagex, player_imagey, size // 10, size // 10))
        if player.race == "dwarf":
            player_on_battlefield = screen.blit(small_dwarf, (player_battlefieldx * (size // 10)  + (width // 2 - size // 2), player_battlefieldy * (size // 10) + (height // 2 - size // 2)), area=(player_imagex, player_imagey, size // 10, size // 10))
        for e in enemy_list:
            if e.name == "bunny":
                if e.direction == "north":
                    screen.blit(enemies, (e.x * (size // 10) + (width // 2 - size // 2), (e.y * (size // 10) + (height // 2 - size // 2))), area=(0, size // 10, size // 10, size // 10))
                elif e.direction == "south":
                    screen.blit(enemies, (e.x * (size // 10) + (width // 2 - size // 2), (e.y * (size // 10) + (height // 2 - size // 2))), area=(0, 0, size // 10, size // 10))
                elif e.direction == "west":
                    screen.blit(enemies, (e.x * (size // 10) + (width // 2 - size // 2), (e.y * (size // 10) + (height // 2 - size // 2))), area=(0, size // 10 * 3, size // 10, size // 10))
                elif e.direction == "east":
                    screen.blit(enemies, (e.x * (size // 10) + (width // 2 - size // 2), (e.y * (size // 10) + (height // 2 - size // 2))), area=(0, size // 10 * 2, size // 10, size // 10))
        if players_turn == True:
            text = medium_font.render("Player's Turn", False, pygame.Color(255, 255, 255))
##            if player_destinationy > player_battlefieldy:
##                player_battlefieldy += 5
##                player_imagex += 10
##                if player_imagex >= size // 10 * 7:
##                    player_imagex = 0
##                player_imagey = 192
##            elif player_destinationy < player_battlefieldy:
##                player_battlefieldy -= 5
##                player_imagex += 10
##                if player_imagex >= size // 10 * 7:
##                    player_imagex = 0
##                player_imagey = 0
##            elif player_destinationx < player_battlefieldx:
##                player_battlefieldx -= 5
##                player_imagex += 10
##                if player_imagex >= size // 10 * 7:
##                    player_imagex = 0
##                player_imagey = 384
##            elif player_destinationx > player_battlefieldx:
##                player_battlefieldx += 5
##                player_imagex += 10
##                if player_imagex >= size // 10 * 7:
##                    player_imagex = 0
##                player_imagey = 576
##            else:
##                player_imagex = 0
        else:
            text = medium_font.render("Enemies Turn", False, pygame.Color(255, 255, 255))
        screen.blit(text, (width - 20 - text.get_rect().width, 30))
        if selected != None:
            if type(selected) == enemy:
                text = medium_font.render(f"{selected.name} is selected", False, pygame.Color(255, 255, 255))
            else:
                text = medium_font.render(f"{selected} is selected", False, pygame.Color(255, 255, 255))
            screen.blit(text, (width - 20 - text.get_rect().width, 80))
        if looking_at_inventory == True:
            pygame.draw.rect(screen, pygame.Color(200, 200, 200), ((width - (width // 4)) // 2, 150, width // 4, height * .75))
            text = huge_font.render("items", False, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (width // 2, 200)
            screen.blit(text, text_rect)
            for item in player.inventory:
                try:
                    if mouse_pos[0] < items_buttons[player.inventory.index(item) - 1].right and mouse_pos[0] > items_buttons[player.inventory.index(item) - 1].left and mouse_pos[1] > items_buttons[player.inventory.index(item) - 1].top and mouse_pos[1] < items_buttons[player.inventory.index(item) - 1].bottom:
                        text = big_font.render(item, False, pygame.Color(0, 0, 0))
                    else:
                        text = big_font.render(item, False, pygame.Color(255, 255, 255))
                except NameError:
                    text = big_font.render(item, False, pygame.Color(255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (width // 2, 300 + (player.inventory.index(item) - 1) * 40)
                screen.blit(text, text_rect)
                item_buttons.append(text_rect)
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
    if talking == True and paused == False and departing == False and (game_state == "exploring" or game_state == "battle"):
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
    window.blit(pygame.transform.scale(screen, (screen_width, screen_height)), (0, 0))
    window.blit(mouse_pointer, (mousex, mousey))
    pygame.display.update()
    clock.tick(32)
pygame.quit()
sys.exit()
