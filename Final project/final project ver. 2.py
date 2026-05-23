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
    global game_state, feedback, user_input, border, paused, player_imagex, player_imagey, collision, saving, loading, screen_objects, counter, talking, offset, cooldown, rock_list, holding_rock, picking_up_rock, king, enemy_list, rotated_npc, player_on_battlefield, rotation_counter, mini_map, departing, killcount, game_over
    pygame.mixer.music.load(resource_path("exploring_song.wav"))
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
    enemy_list = []
    rotated_npc = None
    rotation_counter = 0
    selected = None
    grid = []
    departing = False
    killcount = 0
    game_over = False

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
            game_data["name"] = user_input
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

def draw_back_button():
    global back_button
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

def spawn_enemy():
    global current_map, enemy_list, killcount
    if game_data["mission"] == 1:
        enemies_to_spawn = killcount // 7 + 2
    elif game_data["mission"] == 2:
        enemies_to_spawn = 5
    if enemies_to_spawn + killcount + len(enemy_list) > 30 + 1:
        enemies_to_spawn = 30 - killcount - len(enemy_list) + 1
    for n in range(enemies_to_spawn):
        number = random.randint(1, 2)
        if number == 1:
            try:
                x = random.randint(100, game_data["worldx"])
            except:
                x = random.randint(game_data["worldx"] + width, 3500)
        else:
            try:
                x = random.randint(game_data["worldx"] + width, 3500)
            except:
                x = random.randint(100, game_data["worldx"])
        number = random.randint(1, 2)
        if number == 1:
            try:
                y = random.randint(500, game_data["worldy"])
            except:
                y = random.randint(game_data["worldy"] + height, 3500)
        else:
            try:
                y = random.randint(game_data["worldy"] + height, 3500)
            except:
                y = random.randint(500, game_data["worldy"])
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
        if game_data["mission"] == 1:
            imagey = 192
        if game_data["mission"] == 2:
            imagey = 768
        new_enemy = enemy(x, y, 0, imagey, "north")
        enemy_list.append(new_enemy)

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
            elif game_data["mission"] == 1.5:
                words = random.sample(npc1_insults[1.5], 5)
            elif game_data["mission"] == 2:
                words = random.sample(npc1_insults[2], 5)
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
            elif game_data["mission"] == 1.5:
                words = random.sample(npc2_insults[1.5], 5)
            elif game_data["mission"] == 2:
                words = random.sample(npc2_insults[2], 5)
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
            elif game_data["mission"] == 1.5:
                words = random.sample(npc3_insults[1.5], 5)
            elif game_data["mission"] == 2:
                words = random.sample(npc3_insults[2], 5)
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
            elif game_data["mission"] == 1.5:
                words = random.sample(npc4_insults[1.5], 5)
            elif game_data["mission"] == 2:
                words = random.sample(npc4_insults[2], 5)
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

class enemy():
    def __init__(self, x, y, imagex, imagey, direction):
        self.x = x
        self.y = y
        self.imagex = imagex
        self.imagey = imagey
        self.direction = direction
        self.rotated = None
        self.alive = True

city_map = {(0, 0, 200, 7600): "wall", (0, 7400, 7600, 200): "wall", (7400, 0, 200, 7600): "wall", (0, 0, 7600, 200): "wall", (500, 1200, 768, 768):"house", (700, 7000, 768, 768): "house", (800, 6400, 768, 768): "house", (6000, 5000, 768, 768): "house", (4000, 2700, 768, 768): "building", (4500, 600, 768, 768): "building", (700, 750, 768, 768): "building", (4500, 6000, 768, 768): "tree", (300, 400, 768, 768): "tree", (6000, 7500, 768, 768): "tree", (500, 4000, 768, 768): "tree", (3300, 2000, 1440, 1840): "castle"}
castle_map = {(0, 0, 100, 3000): "wall", (0, 2900, 2000, 100): "wall", (1900, 0, 100, 3000): "wall", (0, 0, 2000, 100): "wall"}
throne_room_map = {(0, 0, 1000, 100): "wall", (0, 0, 100, 1000): "wall", (990, 0, 100, 1090): "wall", (0, 990, 1000, 100): "wall"}
grass_map = {(-760, 200, 4000, 200): "wall"}

city_door = pygame.Rect(1500, 3100, 384, 384)
castle_door = pygame.Rect(3876, 3530, 384, 384)
throne_room_door = pygame.Rect(1500, 200, 384, 384)
castle_entry_way_door = pygame.Rect(1150, 1190, 384, 384)
city_gate = pygame.Rect(3850, 7705, 384, 384)
outside_city_gate = pygame.Rect(2000, 500, 384, 384)
reset_button = pygame.Rect(0, 0, 0, 0)
level_1_button = pygame.Rect(0, 0, 0, 0)
level_2_button = pygame.Rect(0, 0, 0, 0)
level_3_button = pygame.Rect(0, 0, 0, 0)
level_4_button = pygame.Rect(0, 0, 0, 0)
level_5_button = pygame.Rect(0, 0, 0, 0)

npc1_insults = {0: ["I heard the king has a really important mission for you.", "Howdy!", "Don't you have something better to do?", "The castle's up north if that's where your headed", "Shouldn't you be going to the castle?", "What are you up to?", "That's it. Nap time.", "You're lucky you get to go inside the castle, no one's allowed in there.", "The Castle's North. that big building you LITTERALLY can't miss!"], 1: ["Those monsters destroyed my garden last night!", "What happened in the castle?", "Howdy!", "What's up?", "Someone needs to get rid of those monsters...", "I need a nap...", "If you're looking for the city gate, it's south, at the end of the road.", "Please don't throw a rock at me!"], 1.5: ["Be careful with those rocks, buddy!", "Did you kill the monsters?", "I hope you got rid of the monsters.", "Hey, you're back... alive?", "You actually survived?"], 2: ["You're going to goblin valley?!", "be careful with those rocks!", "Hi!", "I think there are still more bunnies near the city.", "The king sent you on another mission?"]}
npc2_insults = {0: ["What?", "What do you want?", "Don't you have something better to do?", "What is it this time?", "Hello.", "If you're looking for the castle, just follow the road north.", "Nice hair.", "You're lucky the king summoned you to the castle, he doesn't let anyone else in.", "looking for the castle? it's the big building you can see from anywhere in town."], 1: ["Hello!", "The city gate is south. Just follow the road.", "My garden was devestated by those horrible monsters!", "How'd it go in the castle?", "What?", "The city gate is at the end of the road.", "Be careful with those rocks!"], 1.5: ["Watch it, you keep hitting people with rocks!", "Did you kill all those monsters?", "Hi!", "What?", "You really killed the monsters?"], 2: ["I heard Goblin Valley is really dangerous", "be careful with those rocks!", "What?", "More bunnies attacked my garden while you were gone.", "Hello!"]}
npc3_insults = {0: ["Yo!", "Sup?", "The castle's north, at the end of the road.", "Hey.", "Do I know you?", "Be careful in the castle, I don't trust the king one bit.", "The castle's up north. Just follow the road.", "Suspicious the king only lets you in the castle...", "You can't find the castle? Are you blind?"], 1: ["That king is suspicious...", "So, what is this secret mission of yours, mercenary?", "Yo!", "Sup?", "The city gate is south. But why were you sent out of town?", "If you throw a rock at me, I'll sue you!"], 1.5: ["Yo!", "I still think the king is suspicious", "How are you still alive?", "You made it back alive?! Oh well, there's always next time...", "Nice rock you got there."], 2: ["I wonder why the king wants all the goblins dead...", "Sup?", "Yo!", "Hey, great job fighting off those bunnies", "I still don't trust that king"]}
npc4_insults = {0: ["The road's over there. Use it.", "I gotta go, I'm late for nap time.", "Looking for the castle? Just follow the road north.", "If the king sent for you, you'd better get to the castle.", "Don't you have somewhere to be?", "What do you want, peasant?", "Goodbye.", "You're actually allowed in the castle?!", "The sooner you get to the castle, the sooner you can stop hassling me."], 1: ["I gotta go, nap time.", "Hi", "The road's over there. Use it.", "Some monsters attacked my garden last night.", "I'll kill those little monsters next time they go near my garden!", "Hi! Oh, that's a nice rock there..."], 1.5: ["Hello!", "You really killed all those horrible monsters?", "Hey, you made it back!", "You didn't die? Too bad... I mean welcome back!", "Please be careful with those rocks."], 2: ["You're going to Goblin Valley? No one has ever escaped there alive!", "Goodbye", "Please stop with the rock throwing.", "Those bunnies returned. They just keep coming", "What is it this time?"]}
city_background = pygame.image.load(resource_path("city_background.png"))
city_background = pygame.transform.scale(city_background, (9000, 9000))
grass_background = city_background.subsurface(0, 0, 4000, 4000)
dirt_background = pygame.image.load(resource_path("dirt.png"))
dirt_background = pygame.transform.scale(dirt_background, (4000, 4000))
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
enemies = pygame.transform.scale(enemies, (1536, 1536))
mouse_pointer = pygame.image.load(resource_path("sword.png"))
mouse_pointer = pygame.transform.rotate(mouse_pointer, 35)
rock_hits_npc = pygame.mixer.Sound(resource_path("rock_hits_npc.wav"))

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
player_rect = pygame.Rect(width // 2 - 96, height // 2 - 96, 192, 192)
window = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.Surface((width, height))
pygame.display.set_caption("Pebble Power")
##pygame.display.set_icon(pygame.image.load(resource_path("icon.ico")))
pygame.mouse.set_visible(False)
reset()

running = True
while running == True:
    mousex, mousey = pygame.mouse.get_pos()
    mouse_pos = (mousex * (width / screen_width), mousey * (height / screen_height))
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
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            elif game_data["area"] == "castle":
                                background = castle_background
                                current_map = castle_map
                            elif game_data["area"] == "throne room":
                                background = castle_background
                                current_map = throne_room_map
                            elif game_data["area"] == "grass":
                                background = grass_background
                                current_map = grass_map
                            if game_data["race"] == "human":
                                player_sprite = human
                            if game_data["race"] == "elf":
                                player_sprite = elf
                            if game_data["race"] == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                            pygame.mixer.music.play(-1)
                    if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                        if file2["name"] != "empty":
                            game_data = file2
                            game_state = "exploring"
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            elif game_data["area"] == "castle":
                                background = castle_background
                                current_map = castle_map
                            elif game_data["area"] == "throne room":
                                background = castle_background
                                current_map = throne_room_map
                            elif game_data["area"] == "grass":
                                background = grass_background
                                current_map = grass_map
                            if game_data["race"] == "human":
                                player_sprite = human
                            if game_data["race"] == "elf":
                                player_sprite = elf
                            if game_data["race"] == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                            pygame.mixer.music.play(-1)
                    if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                        if file3["name"] != "empty":
                            game_data = file3
                            game_state = "exploring"
                            if game_data["area"] == "city":
                                background = city_background
                                current_map = city_map
                            elif game_data["area"] == "castle":
                                background = castle_background
                                current_map = castle_map
                            elif game_data["area"] == "throne room":
                                background = castle_background
                                current_map = throne_room_map
                            elif game_data["area"] == "grass":
                                background = grass_background
                                current_map = grass_map
                            if game_data["race"] == "human":
                                player_sprite = human
                            if game_data["race"] == "elf":
                                player_sprite = elf
                            if game_data["race"] == "dwarf":
                                player_sprite = dwarf
                            spawn_npc()
                            pygame.mixer.music.play(-1)
                elif game_state == "choose name":
                    if mouse_pos[0] < submit_button.right and mouse_pos[0] > submit_button.left and mouse_pos[1] > submit_button.top and mouse_pos[1] < submit_button.bottom:
                        submit_input(user_input)
                elif game_state == "choose race":
                    if mouse_pos[0] < human_button.right and mouse_pos[0] > human_button.left and mouse_pos[1] > human_button.top and mouse_pos[1] < human_button.bottom:
                        game_data["race"] = "human"
                        player_sprite = human
                        game_state = "intro"
                    elif mouse_pos[0] < elf_button.right and mouse_pos[0] > elf_button.left and mouse_pos[1] > elf_button.top and mouse_pos[1] < elf_button.bottom:
                        game_data["race"] = "elf"
                        player_sprite = elf
                        game_state = "intro"
                    elif mouse_pos[0] < dwarf_button.right and mouse_pos[0] > dwarf_button.left and mouse_pos[1] > dwarf_button.top and mouse_pos[1] < dwarf_button.bottom:
                        game_data["race"] = "dwarf"
                        player_sprite = dwarf
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
                    if mouse_pos[0] < reset_button.right and mouse_pos[0] > reset_button.left and mouse_pos[1] > reset_button.top and mouse_pos[1] < reset_button.bottom and game_over == True:
                        reset()
                    if paused == True:
                        if saving == False and loading == False:
                            if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
                                paused = False
                            if mouse_pos[0] < save_button.right and mouse_pos[0] > save_button.left and mouse_pos[1] > save_button.top and mouse_pos[1] < save_button.bottom:
                                if game_data["area"] == "city" or game_data["area"] == "castle" or game_data["area"] == "throne room":
                                    saving = True
                                    counter = 0
                                    feedback = ""
                                else:
                                    feedback = "you can't save here"
                                    counter = 0
                            if mouse_pos[0] < load_button.right and mouse_pos[0] > load_button.left and mouse_pos[1] > load_button.top and mouse_pos[1] < load_button.bottom:
                                loading = True
                                counter = 0
                                feedback = ""
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
                                    enemy_list = []
                                    game_data = load("file1")
                                    if game_data["race"] == "elf":
                                        player_sprite = elf
                                    elif game_data["race"] == "human":
                                        player_sprite == human
                                    elif game_data["race"] == "dwarf":
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
                                    elif game_data["area"] == "grass":
                                        background = grass_background
                                        current_map = grass_map
                                    feedback = ""
                                    loading = False
                                    paused = False
                                    talking = False
                                if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                                    feedback = "loading..."
                                    enemy_list = []
                                    game_data = load("file2")
                                    if game_data["race"] == "elf":
                                        player_sprite = elf
                                    elif game_data["race"] == "human":
                                        player_sprite == human
                                    elif game_data["race"] == "dwarf":
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
                                    elif game_data["area"] == "grass":
                                        background = grass_background
                                        current_map = grass_map
                                    feedback = ""
                                    loading = False
                                    paused = False
                                    talking = False
                                if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                                    feedback = "loading..."
                                    enemy_list = []
                                    game_data = load("file3")
                                    if game_data["race"] == "elf":
                                        player_sprite = elf
                                    elif game_data["race"] == "human":
                                        player_sprite == human
                                    elif game_data["race"] == "dwarf":
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
                                    elif game_data["area"] == "grass":
                                        background = grass_background
                                        current_map = grass_map
                                    feedback = ""
                                    loading = False
                                    paused = False
                                    talking = False
                                if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                                    feedback = ""
                                    loading = False
                    else:
                        if talking == False:
                            for NPC in npc_list:
                                npc_rect = pygame.Rect(NPC.x - game_data["worldx"], NPC.y - game_data["worldy"], 192, 192)
                                if mouse_pos[0] < npc_rect.right and mouse_pos[0] > npc_rect.left and mouse_pos[1] > npc_rect.top and mouse_pos[1] < npc_rect.bottom:
                                    npc_words = random.sample(NPC.words, 1)
                                    talking = True
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
                                if game_data["mission"] == 0:
                                    npc_words = [f"So {game_data['name']}, you finally decided to show up."]
                                elif game_data["mission"] == 1.5:
                                    npc_words = ["You're back. Took you long enough."]
                                elif game_data["mission"] == 1 or game_data["mission"] == 2 or game_data["mission"] == 3:
                                    npc_words = ["What are you doing here? Hurry up and finish your mission!"]
                                elif game_data["mission"] == 2.5:
                                    npc_words = ["So you survived. You seem to be more capable then I thought."]
                                talking = True
                            if mouse_pos[0] < city_gate.right - game_data["worldx"] and mouse_pos[0] > city_gate.left - game_data["worldy"] and mouse_pos[1] > city_gate.top - game_data["worldy"] and mouse_pos[1] < city_gate.bottom - game_data["worldy"] and game_data["area"] == "city" and cooldown < 1:
                                if game_data["mission"] == 0:
                                    npc_words = ["Where do you think you're going? Get to the castle!"]
                                    talking = True
                                else:
                                    departing = True
                            if mouse_pos[0] < outside_city_gate.right - game_data["worldx"] and mouse_pos[0] > outside_city_gate.left - game_data["worldx"] and mouse_pos[1] > outside_city_gate.top - game_data["worldy"] and mouse_pos[1] < outside_city_gate.bottom - game_data["worldy"] and game_data["area"] == "grass" and cooldown < 1:
                                background = city_background
                                current_map = city_map
                                game_data["worldx"] = city_gate.x + 192 - (width // 2)
                                game_data["worldy"] = city_gate.bottom - 10 - (width // 2)
                                pygame.mixer.music.load(resource_path("exploring_song.wav"))
                                pygame.mixer.music.play(-1)
                                game_data["area"] = "city"
                            if departing == True:
                                if mouse_pos[0] < level_1_button.right and mouse_pos[0] > level_1_button.left and mouse_pos[1] > level_1_button.top and mouse_pos[1] < level_1_button.bottom:
                                    background = grass_background
                                    current_map = grass_map
                                    game_data["area"] = "grass"
                                    game_data["worldx"] = outside_city_gate.x + 192 - (width // 2)
                                    game_data["worldy"] = outside_city_gate.bottom + 362 - (width // 2)
                                    npc_list = []
                                    spawn_enemy()
                                    pygame.mixer.music.load(resource_path("battle_song.wav"))
                                    pygame.mixer.music.play(-1)
                                    departing = False
                                if mouse_pos[0] < level_2_button.right and mouse_pos[0] > level_2_button.left and mouse_pos[1] > level_2_button.top and mouse_pos[1] < level_2_button.bottom:
                                    background = dirt_background
                                    current_map = {}
                                    game_data["area"] = "goblin valley"
                                    game_data["worldx"] = 2000
                                    game_data["worldy"] = 2000
                                    npc_list = []
                                    spawn_enemy()
                                    pygame.mixer.music.load(resource_path("battle_song.wav"))
                                    pygame.mixer.music.play(-1)
                                    departing = False
                                if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                                    departing = False
                        else:
                            if npc_words == [f"So {game_data['name']}, you finally decided to show up."]:
                                npc_words = ["I have a very important mission for you."]
                            elif npc_words == ["I have a very important mission for you."]:
                                npc_words = ["There are monsters outside the city. They have been destroying our crops."]
                            elif npc_words == ["There are monsters outside the city. They have been destroying our crops."]:
                                npc_words = ["You need to go kill them before they attack the city again."]
                            elif npc_words == ["You need to go kill them before they attack the city again."]:
                                npc_words = ["If you don't have any weapons, just throw some rocks or something."]
                            elif npc_words == ["If you don't have any weapons, just throw some rocks or something."]:
                                npc_words = ["(Press space to pick up rocks and throw them)"]
                            elif npc_words == ["(Press space to pick up rocks and throw them)"]:
                                npc_words = ["If you survive... I mean, when you come back, I'll give you another mission."]
                                game_data["mission"] = 1
                            elif npc_words == ["If you survive... I mean, when you come back, I'll give you another mission."]:
                                npc_words = ["(go south and click the city gate to attempt your mission)"]
                            elif npc_words == ["You're back. Took you long enough."]:
                                npc_words = ["I have another mission for you."]
                            elif npc_words == ["I have another mission for you."]:
                                npc_words = ["Go to the goblin valley and kill all the goblins. They're annoying."]
                                game_data["mission"] = 2
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
                if event.key == K_ESCAPE and talking == False and game_over == False:
                    feedback = ""
                    paused = not paused
                if event.key == K_SPACE and picking_up_rock == False and game_over == False:
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
                    elif game_data["area"] != "castle" and game_data["area"] != "throne room":
                        player_imagey += 768
                        player_imagex = 0
                        picking_up_rock = True
    screen.fill(pygame.Color(0, 0, 0))
    if game_state == "menu":
        text = huge_font.render("Pebble Power", False, pygame.Color(255, 255, 255))
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
        draw_back_button()
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
        text = huge_font.render("Choose a character", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 250)
        screen.blit(text, text_rect)
        try:
            if mouse_pos[0] < human_button.right and mouse_pos[0] > human_button.left and mouse_pos[1] > human_button.top and mouse_pos[1] < human_button.bottom:
                pygame.draw.rect(screen, pygame.Color(180, 180, 180), (human_button.x, human_button.y, 192, 192), width=5)
        except:
            pass
        human_button = screen.blit(human, (400, height // 2), area=(0, 0, 192, 192))
        try:
            if mouse_pos[0] < elf_button.right and mouse_pos[0] > elf_button.left and mouse_pos[1] > elf_button.top and mouse_pos[1] < elf_button.bottom:
                pygame.draw.rect(screen, pygame.Color(180, 180, 180), (elf_button.x, elf_button.y, 192, 192), width=5)
        except:
            pass
        elf_button = screen.blit(elf, (width // 2 - 96, height // 2), area=(0, 0, 192, 192))
        try:
            if mouse_pos[0] < dwarf_button.right and mouse_pos[0] > dwarf_button.left and mouse_pos[1] > dwarf_button.top and mouse_pos[1] < dwarf_button.bottom:
                pygame.draw.rect(screen, pygame.Color(180, 180, 180), (dwarf_button.x, dwarf_button.y, 192, 192), width=5)
        except:
            pass
        dwarf_button = screen.blit(dwarf, (width - 596, height // 2), area=(0, 0, 192, 192))
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
        if paused == False and talking == False:
            collision = False
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
            if keys[K_w] == True and picking_up_rock == False and game_over == False:
                if collision == False:
                    player_imagey = 192
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    game_data["worldy"] -= 10
                    if keys[K_a] == False and keys[K_s] == False and keys[K_d] == False and collision == False and game_over == False:
                        game_data["worldy"] -= 4
            if keys[K_a] == True and picking_up_rock == False and game_over == False:
                if collision == False:
                    player_imagey = 576
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    game_data["worldx"] -= 10
                    if keys[K_w] == False and keys[K_s] == False and keys[K_d] == False and collision == False and game_over == False:
                        game_data["worldx"] -= 4
            if keys[K_s] == True and picking_up_rock == False and game_over == False:
                if collision == False:
                    player_imagey = 0
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    game_data["worldy"] += 10
                    if keys[K_a] == False and keys[K_w] == False and keys[K_d] == False and collision == False and game_over == False:
                        game_data["worldy"] += 4
            if keys[K_d] == True and picking_up_rock == False and game_over == False:
                if collision == False:
                    player_imagey = 384
                    if player_imagex < 1344:
                        player_imagex += 50
                    else:
                        player_imagex = 0
                    game_data["worldx"] += 10
                    if keys[K_a] == False and keys[K_s] == False and keys[K_w] == False and collision == False and game_over == False:
                        game_data["worldx"] += 4
            if keys[K_w] == False and keys[K_a] == False and keys[K_s] == False and keys[K_d] == False and picking_up_rock == False:
                player_imagex = 0
            elif (game_data["worldx"] < -760 or game_data["worldx"] > 3240 or game_data["worldy"] < -760 or game_data["worldy"] > 3600) and game_data["area"] != "city" and game_data["area"] != "castle" and game_data["area"] != "throne room":
                game_data["worldx"] = old_worldx
                game_data["worldy"] = old_worldy
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
                        try:
                            rock_list.remove(rocks)
                        except ValueError:
                            pass
                for target in npc_list[:]:
                    if rock_rect.colliderect(pygame.Rect(target.x - game_data["worldx"], target.y - game_data["worldy"], 192, 192)):
                        try:
                            rock_list.remove(rocks)
                        except ValueError:
                            pass
                        target.direction = rocks.direction
                        rotation_counter = 0
                        target.alive = False
                        rock_hits_npc.play()
                for target in enemy_list[:]:
                    if rock_rect.colliderect(pygame.Rect(target.x - game_data["worldx"], target.y - game_data["worldy"], 192, 192)):
                        try:
                            rock_list.remove(rocks)
                        except ValueError:
                            pass
                        target.direction = rocks.direction
                        rotation_counter = 0
                        target.alive = False
                        rock_hits_npc.play()
                        killcount += 1
                        if game_data["mission"] == 1:
                            if killcount < 30:
                                spawn_enemy()
                        elif game_data["mission"] == 2:
                            if killcount < 20:
                                spawn_enemy()
            for e in enemy_list:
                if e.alive == True:
                    if e.imagex > 1344:
                        e.imagex = 0
                    else:
                        e.imagex += 50
                    if e.y > game_data["worldy"] + (height // 2) - 96:
                        e.y -= 5
                        if game_data["mission"] == 2:
                            e.y -= 4
                        e.direction = "north"
                        if e.imagey <= 578:
                            e.imagey = 192
                    if e.y < game_data["worldy"] + (height // 2) - 96:
                        e.y += 5
                        if game_data["mission"] == 2:
                            e.y += 4
                        e.direction = "south"
                        if e.imagey <= 578:
                            e.imagey = 0
                    if e.x < game_data["worldx"] + (width // 2) - 96:
                        e.x += 5
                        if game_data["mission"] == 2:
                            e.x += 4
                        e.direction = "east"
                        if e.imagey <= 578:
                            e.imagey = 384
                    if e.x > game_data["worldx"] + (width // 2) - 96:
                        e.x -= 5
                        if game_data["mission"] == 2:
                            e.x -= 4
                        e.direction = "west"
                        if e.imagey <= 578:
                            e.imagey = 576
                    elif e.x >= game_data["worldx"] + (width // 2) - 96 and e.x <= game_data["worldx"] + (width // 2) - 96 and e.y >= game_data["worldy"] + (height // 2) - 96:
                        e.imagex = 0
                    if abs((game_data["worldx"] + (width // 2) - 96) - e.x) > abs((game_data["worldy"] + (height // 2) - 96) - e.y):
                        if e.x < game_data["worldx"] + (width // 2) - 96:
                            e.direction = "east"
                            if e.imagey <= 578:
                                e.imagey = 384
                        if e.x > game_data["worldx"] + (width // 2) - 96:
                            e.direction = "west"
                            if e.imagey <= 578:
                                e.imagey = 576
                    else:
                        if e.y > game_data["worldy"] + (height // 2) - 96:
                            e.direction = "north"
                            if e.imagey <= 578:
                                e.imagey = 192
                        if e.y < game_data["worldy"] + (height // 2) - 96:
                            e.direction = "south"
                            if e.imagey <= 578:
                                e.imagey = 0
                else:
                    if e.direction == "north":
                        e.y -= 50
                    elif e.direction == "east":
                        e.x += 50
                    elif e.direction == "west":
                        e.x -= 50
                    elif e.direction == "south":
                        e.y += 50
            if enemy_list == [] and (game_data["area"] == "grass" or game_data["area"] == "goblin valley") and (game_data["mission"] == 1 or game_data["mission"] == 2):
                if game_data["mission"] == 1 and killcount >= 30 and game_data["area"] == "grass":
                    npc_words = ["You did it! Now go back to the castle and talk to the king."]
                    game_data["mission"] = 1.5
                elif game_data["mission"] == 2 and killcount >= 20 and game_data["area"] == "goblin valley":
                    npc_words = ["You win! Return to the castle for your next mission."]
                    game_data["mission"] = 2.5
                talking = True
        for NPC in npc_list[:]:
            if NPC.alive == True:
                screen.blit(npc, (NPC.x - game_data["worldx"], NPC.y - game_data["worldy"]), area=(192*round(NPC.imagex/192), NPC.imagey, 192, 192))
            else:
                rotation_counter += 1
                NPC.rotated = npc.subsurface((0, NPC.imagey, 192, 192))
                NPC.rotated = pygame.transform.rotate(NPC.rotated, 20 * rotation_counter)
                screen.blit(NPC.rotated, (NPC.x - game_data["worldx"], NPC.y - game_data["worldy"]))
        player_rect = screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
        for e in enemy_list[:]:
            if e.alive == True:
                screen.blit(enemies, (e.x - game_data["worldx"], e.y - game_data["worldy"]), area=(192*round(e.imagex/192), e.imagey, 192, 192))
                enemy_rect = pygame.Rect(e.x - game_data["worldx"] + 96, e.y - game_data["worldy"] + 30, 5, 132)
                if enemy_rect.colliderect(player_rect):
                    pygame.mixer.music.load(resource_path("womp-womp.mp3"))
                    pygame.mixer.music.play(1)
                    game_over = True
            else:
                rotation_counter += 1
                e.rotated = enemies.subsurface((0, e.imagey, 192, 192))   
                e.rotated = pygame.transform.rotate(e.rotated, 20 * rotation_counter)
                screen.blit(e.rotated, (e.x - game_data["worldx"], e.y - game_data["worldy"]))
                if e.x < -100 or e.x > 4100 or e.y < 0 or e.y > 4100:
                    enemy_list.remove(e)
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
            if player_rect.colliderect(king.inflate(-192, -192)):
                collision = True
                game_data["worldx"] = old_worldx
                game_data["worldy"] = old_worldy
        if game_data["area"] == "city":
            screen.blit(doors, (city_gate.x - game_data["worldx"], city_gate.y - game_data["worldy"]), area=(0, 0, 384, 384)) # city_gate
        if game_data["area"] == "grass":
            screen.blit(doors, (outside_city_gate.x - game_data["worldx"], outside_city_gate.y - game_data["worldy"]), area=(0, 0, 384, 384))
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
        if game_data["area"] == "grass":
            if game_over == False:
                text = medium_font.render(f"objective: destroy all bunnies   killcount: {killcount}", False, pygame.Color(255, 255, 255))
            else:
                text = medium_font.render(f"objective: destroy all bunnies   killcount: {killcount}   FAILED", False, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.left = 20
            text_rect.top = 20
            screen.blit(text, text_rect)
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
                draw_back_button()
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
                    if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom and file3["name"] != "empty" and (feedback == "" or feedback == "saved!"):
                        file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    file3_button = draw_button(f"file 3: {file3['name']}", height/2 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                draw_back_button()
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
                text = big_font.render(feedback, False, pygame.Color(255, 255, 255))
                text_rect = text.get_rect()
                text_rect.center = (width/2, height - 100)
                screen.blit(text, text_rect)
        if departing == True:
            text = huge_font.render("Where do you want to go?", False, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (width/2, height/2 - 350)
            screen.blit(text, text_rect)
            try:
                if mouse_pos[0] < level_1_button.right and mouse_pos[0] > level_1_button.left and mouse_pos[1] > level_1_button.top and mouse_pos[1] < level_1_button.bottom:
                    level_1_button = draw_button("Outside the city (mission 1)", height/3 - 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                else:
                    level_1_button = draw_button("Outside the city (mission 1)", height/3 - 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            except NameError:
                level_1_button = draw_button("Outside the city (mission 1)", height/3 - 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            if game_data["mission"] > 1.5:
                try:
                    if mouse_pos[0] < level_2_button.right and mouse_pos[0] > level_2_button.left and mouse_pos[1] > level_2_button.top and mouse_pos[1] < level_2_button.bottom:
                        level_2_button = draw_button("Goblin Valley (mission 2)", height/3, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        level_2_button = draw_button("Goblin Valley (mission 2)", height/3, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    level_2_button = draw_button("Goblin Valley (mission 2)", height/3, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            if game_data["mission"] > 2.5:
                try:
                    if mouse_pos[0] < level_3_button.right and mouse_pos[0] > level_3_button.left and mouse_pos[1] > level_3_button.top and mouse_pos[1] < level_3_button.bottom:
                        level_3_button = draw_button("Right outside the city (mission 3)", height/3 + 100, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        level_3_button = draw_button("Right outside the city (mission 3)", height/3 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    level_3_button = draw_button("Right outside the city (mission 3)", height/3 + 100, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            if game_data["mission"] > 3.5:
                try:
                    if mouse_pos[0] < level_4_button.right and mouse_pos[0] > level_4_button.left and mouse_pos[1] > level_4_button.top and mouse_pos[1] < level_4_button.bottom:
                        level_4_button = draw_button("Right outside the city (mission 4)", height/3 + 200, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        level_4_button = draw_button("Right outside the city (mission 4)", height/3 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    level_4_button = draw_button("Right outside the city (mission 4)", height/3 + 200, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            if game_data["mission"] > 4.5:
                try:
                    if mouse_pos[0] < level_5_button.right and mouse_pos[0] > level_5_button.left and mouse_pos[1] > level_5_button.top and mouse_pos[1] < level_5_button.bottom:
                        level_5_button = draw_button("Right outside the city (mission 5)", height/3 + 300, pygame.Color(255, 255, 255), pygame.Color(180, 180, 180))
                    else:
                        level_5_button = draw_button("Right outside the city (mission 5)", height/3 + 300, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
                except NameError:
                    level_5_button = draw_button("Right outside the city (mission 5)", height/3 + 300, pygame.Color(255, 255, 255), pygame.Color(150, 150, 150))
            draw_back_button()
        elif talking == True and paused == False:
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
    if game_over == True:
        text = huge_font.render("GAME OVER", False, pygame.Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width // 2, height // 2 - 50)
        screen.blit(text, text_rect)
        if mouse_pos[0] < reset_button.right and mouse_pos[0] > reset_button.left and mouse_pos[1] > reset_button.top and mouse_pos[1] < reset_button.bottom:
            reset_button = draw_button("return to title screen", height // 2 + 50, pygame.Color(255, 0, 0), pygame.Color(180, 180, 180))
        else:
            reset_button = draw_button("return to title screen", height // 2 + 50, pygame.Color(255, 0, 0), pygame.Color(150, 150, 150))
    window.blit(pygame.transform.scale(screen, (screen_width, screen_height)), (0, 0))
    window.blit(mouse_pointer, (mousex, mousey))
    pygame.display.update()
    clock.tick(32)
pygame.quit()
sys.exit()
