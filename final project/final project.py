import pygame, sys, os, random
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
    global game_state, feedback, user_input, border, paused, player_imagex, player_imagey
    game_state = "menu"
    feedback = ""
    user_input = ""
    paused = False
    player_imagex = 0
    player_imagey = 0

def save(data, name, folder=None):
    if folder != None:
        path = os.path.join(folder, data)
        if not os.path_exists(resource_path(path)):
            os.makedirs(resource_path(path))
    else:
        path = data
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
        path = os.path.join(folder, data)
    else:
        path = data
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
    global game_state, feedback, user_input, player
    if game_state == "choose name":
        if len(x) < 1:
            number = random.randint(0, len(too_short_name_insults) - 1)
            feedback = too_short_name_insults[number]
        elif len(x) > 17:
            number = random.randint(0, len(too_long_name_insults) - 1)
            feedback = too_long_name_insults[number]
        else:
            player = character(user_input, None, None)
            user_input = ""
            game_state = "choose race"

class character():
    def __init__(self, name, race, Class, health=10, gold=0, inventory=[], level=1, stats={}, weapon_equiped=None, armor_equiped=None, accessory_equiped=None):
        self.name = name
        self.health = health
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.stats = stats
        self.weapon_equiped = weapon_equiped
        self.armor_equiped = armor_equiped
        self.accessory_equiped = accessory_equiped
        self.alive = True

#8000 X 8000 pixels
city_map = {(0, 0, 200, 8000): "wall", (0, 7800, 8000, 200): "wall", (7800, 0, 200, 8000): "wall", (7800, 7800, 200, 8000): "wall", (500, 1200, 0, 0):"house", (700, 7000, 0, 0): "house", (800, 6400, 0, 0): "house", (6000, 5000, 0, 0): "house", (4000, 3700, 0, 0): "building", (6500, 400, 0, 0): "building", (300, 2500, 0, 0): "building"}

city_background = pygame.image.load(resource_path("city_background.png"))
city_background = pygame.transform.scale(city_background, (8000, 8000))
objects = pygame.image.load(resource_path("objects.png"))
objects = pygame.transform.scale(objects, (1536, 768))
human = pygame.image.load(resource_path("human.png"))
elf = pygame.image.load(resource_path("elf.png"))
dwarf = pygame.image.load(resource_path("dwarf.png"))
human = pygame.transform.scale(human, (1536, 768))
elf = pygame.transform.scale(elf, (1536, 768))
dwarf = pygame.transform.scale(dwarf, (1536, 768))
mouse_pointer = pygame.image.load(resource_path("sword.png"))
mouse_pointer = pygame.transform.rotate(mouse_pointer, 35)

too_long_name_insults = ["enter a name, not a book", "nope, too long", "you know what a name is, right?", "do you want to play the game or type all day?"]
too_short_name_insults = ["that's not a name", "nope", "you have a name, right?", "try again"]
small_font = pygame.font.SysFont(None, 30, bold=False)
medium_font = pygame.font.SysFont(None, 50, bold=False)
big_font = pygame.font.SysFont(None, 60, bold=False)
huge_font = pygame.font.SysFont(None, 80, bold=True)
clock = pygame.time.Clock()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 50
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
                        game_data = file1
                        game_state = "choose name"
                    if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom:
                        game_data = file2
                        game_state = "choose name"
                    if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom:
                        game_data = file3
                        game_state = "choose name"
                elif game_state == "continue":
                    if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
                        game_state = "menu"
                elif game_state == "choose name":
                    if mouse_pos[0] < submit_button.right and mouse_pos[0] > submit_button.left and mouse_pos[1] > submit_button.top and mouse_pos[1] < submit_button.bottom:
                        submit_input(user_input)
                elif game_state == "choose race":
                    if mouse_pos[0] < human_button.right and mouse_pos[0] > human_button.left and mouse_pos[1] > human_button.top and mouse_pos[1] < human_button.bottom:
                        player.race = "human"
                        player_sprite = human
                        game_state = "choose class"
                    elif mouse_pos[0] < elf_button.right and mouse_pos[0] > elf_button.left and mouse_pos[1] > elf_button.top and mouse_pos[1] < elf_button.bottom:
                        player.race = "elf"
                        player_sprite = elf
                        game_state = "choose class"
                    elif mouse_pos[0] < dwarf_button.right and mouse_pos[0] > dwarf_button.left and mouse_pos[1] > dwarf_button.top and mouse_pos[1] < dwarf_button.bottom:
                        player.race = "dwarf"
                        player_sprite = dwarf
                        game_state = "choose class"
                elif game_state == "choose class":
                    if mouse_pos[0] < fighter_button.right and mouse_pos[0] > fighter_button.left and mouse_pos[1] > fighter_button.top and mouse_pos[1] < fighter_button.bottom:
                        player.Class = "fighter"
                        player.inventory.append("shortsword")
                        game_state = "intro"
                    elif mouse_pos[0] < mage_button.right and mouse_pos[0] > mage_button.left and mouse_pos[1] > mage_button.top and mouse_pos[1] < mage_button.bottom:
                        player.Class = "mage"
                        player.inventory.append("magic wand")
                        game_state = "intro"
                    elif mouse_pos[0] < thief_button.right and mouse_pos[0] > thief_button.left and mouse_pos[1] > thief_button.top and mouse_pos[1] < thief_button.bottom:
                        player.Class = "thief"
                        player.inventory.append("dagger")
                        game_state = "intro"
                elif game_state == "intro":
                    if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
                        worldx = 4000
                        worldy = 4000
                        current_map = city_map
                        background = city_background
                        game_state = "exploring"
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
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(pygame.Color(0, 0, 0))
    if game_state == "menu":
        text = huge_font.render("Game Name Here", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/3)
        screen.blit(text, text_rect)
        text = medium_font.render("  continue  ", False, pygame.Color(255, 255, 255))
        continue_button = text.get_rect()
        continue_button.center = (width/2 - 50, height/2)
        continue_button.width += 100
        continue_button.height += 50
        if mouse_pos[0] < continue_button.right and mouse_pos[0] > continue_button.left and mouse_pos[1] > continue_button.top and mouse_pos[1] < continue_button.bottom:
            pygame.draw.rect(screen, pygame.Color(150, 150, 150), continue_button)
        else:
            pygame.draw.rect(screen, pygame.Color(180, 180, 180), continue_button)
        screen.blit(text, (continue_button.x + 50, continue_button.y + 25))
        text = medium_font.render(" new game ", False, pygame.Color(255, 255, 255))
        new_game_button = text.get_rect()
        new_game_button.center = (width/2 - 50, height/2 + 100)
        new_game_button.width += 100
        new_game_button.height += 50
        if mouse_pos[0] < new_game_button.right and mouse_pos[0] > new_game_button.left and mouse_pos[1] > new_game_button.top and mouse_pos[1] < new_game_button.bottom:
            pygame.draw.rect(screen, pygame.Color(150, 150, 150), new_game_button)
        else:
            pygame.draw.rect(screen, pygame.Color(180, 180, 180), new_game_button)
        screen.blit(text, (new_game_button.x + 50, new_game_button.y + 25))
        text = medium_font.render("       quit       ", False, pygame.Color(255, 255, 255))
        quit_button = text.get_rect()
        quit_button.center = (width/2 - 50, height/2 + 200)
        quit_button.width += 100
        quit_button.height += 50
        if mouse_pos[0] < quit_button.right and mouse_pos[0] > quit_button.left and mouse_pos[1] > quit_button.top and mouse_pos[1] < quit_button.bottom:
            pygame.draw.rect(screen, pygame.Color(150, 150, 150), quit_button)
        else:
            pygame.draw.rect(screen, pygame.Color(180, 180, 180), quit_button)
        screen.blit(text, (quit_button.x + 50, quit_button.y + 25))
    elif game_state == "continue" or game_state == "new_game" or game_state == "are you sure?":
        text = huge_font.render("choose a file", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/3)
        screen.blit(text, text_rect)
        file1 = load("file1", "file1")
        if file1 == None:
            file1 = {"name": "empty"}
        text = medium_font.render(f"file 1: {file1['name']}", False, pygame.Color(255, 255, 255))
        file1_button = text.get_rect()
        file1_button.center = (width/2 - 50, height/2)
        file1_button.width += 100
        file1_button.height += 50
        if mouse_pos[0] < file1_button.right and mouse_pos[0] > file1_button.left and mouse_pos[1] > file1_button.top and mouse_pos[1] < file1_button.bottom and (file1["name"] != "empty" or game_state == "new_game"):
            pygame.draw.rect(screen, pygame.Color(150, 150, 150), file1_button)
        else:
            pygame.draw.rect(screen, pygame.Color(180, 180, 180), file1_button)
        screen.blit(text, (file1_button.x + 50, file1_button.y + 25))
        file2 = load("file2", "file2")
        if file2 == None:
            file2 = {"name": "empty"}
        text = medium_font.render(f"file 2: {file2['name']}", False, pygame.Color(255, 255, 255))
        file2_button = text.get_rect()
        file2_button.center = (width/2 - 50, height/2 + 100)
        file2_button.width += 100
        file2_button.height += 50
        if mouse_pos[0] < file2_button.right and mouse_pos[0] > file2_button.left and mouse_pos[1] > file2_button.top and mouse_pos[1] < file2_button.bottom and (file2["name"] != "empty" or game_state == "new_game"):
            pygame.draw.rect(screen, pygame.Color(150, 150, 150), file2_button)
        else:
            pygame.draw.rect(screen, pygame.Color(180, 180, 180), file2_button)
        screen.blit(text, (file2_button.x + 50, file2_button.y + 25))
        file3 = load("file3", "file3")
        if file3 == None:
            file3 = {"name": "empty"}
        text = medium_font.render(f"file 3: {file3['name']}", False, pygame.Color(255, 255, 255))
        file3_button = text.get_rect()
        file3_button.center = (width/2 - 50, height/2 + 200)
        file3_button.width += 100
        file3_button.height += 50
        if mouse_pos[0] < file3_button.right and mouse_pos[0] > file3_button.left and mouse_pos[1] > file3_button.top and mouse_pos[1] < file3_button.bottom and (file3["name"] != "empty" or game_state == "new_game"):
            pygame.draw.rect(screen, pygame.Color(150, 150, 150), file3_button)
        else:
            pygame.draw.rect(screen, pygame.Color(180, 180, 180), file3_button)
        screen.blit(text, (file3_button.x + 50, file3_button.y + 25))
        text = medium_font.render("back", False, pygame.Color(255, 255, 255))
        back_button = text.get_rect()
        back_button.center = (50, height - 75)
        back_button.width += 50
        back_button.height += 20
        if mouse_pos[0] < back_button.right and mouse_pos[0] > back_button.left and mouse_pos[1] > back_button.top and mouse_pos[1] < back_button.bottom:
            back_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), back_button)
        else:
            back_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), back_button)
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
        text = big_font.render("  Human  ", False, pygame.Color(255, 255, 255))
        human_button = text.get_rect()
        human_button.width += 300
        human_button.height += 100
        human_button.center = (width/2, height/2 - 100)
        if mouse_pos[0] < human_button.right and mouse_pos[0] > human_button.left and mouse_pos[1] > human_button.top and mouse_pos[1] < human_button.bottom:
            human_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), human_button)
        else:
            human_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), human_button)
        screen.blit(text, (human_button.x + 10, human_button.y + (human_button.height/4)))
        text = big_font.render("  Elf         ", False, pygame.Color(255, 255, 255))
        elf_button = text.get_rect()
        elf_button.width += 300
        elf_button.height += 100
        elf_button.center = (width/2, height/2 + 75)
        if mouse_pos[0] < elf_button.right and mouse_pos[0] > elf_button.left and mouse_pos[1] > elf_button.top and mouse_pos[1] < elf_button.bottom:
            elf_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), elf_button)
        else:
            elf_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), elf_button)
        screen.blit(text, (elf_button.x + 10, elf_button.y + (elf_button.height/4)))
        text = big_font.render("   Dwarf   ", False, pygame.Color(255, 255, 255))
        dwarf_button = text.get_rect()
        dwarf_button.width += 300
        dwarf_button.height += 100
        dwarf_button.center = (width/2, height/2 + 250)
        if mouse_pos[0] < dwarf_button.right and mouse_pos[0] > dwarf_button.left and mouse_pos[1] > dwarf_button.top and mouse_pos[1] < dwarf_button.bottom:
            human_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), dwarf_button)
        else:
            human_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), dwarf_button)
        screen.blit(text, (dwarf_button.x + 10, dwarf_button.y + (dwarf_button.height/4)))
    elif game_state == "choose class":
        text = huge_font.render("Choose a class", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 250)
        screen.blit(text, text_rect)
        text = big_font.render("  Fighter", False, pygame.Color(255, 255, 255))
        fighter_button = text.get_rect()
        fighter_button.width += 300
        fighter_button.height += 100
        fighter_button.center = (width/2, height/2 - 100)
        if mouse_pos[0] < fighter_button.right and mouse_pos[0] > fighter_button.left and mouse_pos[1] > fighter_button.top and mouse_pos[1] < fighter_button.bottom:
            fighter_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), fighter_button)
        else:
            fighter_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), fighter_button)
        screen.blit(text, (fighter_button.x + 10, fighter_button.y + (fighter_button.height/4)))
        text = big_font.render("  Mage   ", False, pygame.Color(255, 255, 255))
        mage_button = text.get_rect()
        mage_button.width += 300
        mage_button.height += 100
        mage_button.center = (width/2, height/2 + 75)
        if mouse_pos[0] < mage_button.right and mouse_pos[0] > mage_button.left and mouse_pos[1] > mage_button.top and mouse_pos[1] < mage_button.bottom:
            mage_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), mage_button)
        else:
            mage_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), mage_button)
        screen.blit(text, (mage_button.x + 10, mage_button.y + (mage_button.height/4)))
        text = big_font.render("  Thief   ", False, pygame.Color(255, 255, 255))
        thief_button = text.get_rect()
        thief_button.width += 300
        thief_button.height += 100
        thief_button.center = (width/2, height/2 + 250)
        if mouse_pos[0] < thief_button.right and mouse_pos[0] > thief_button.left and mouse_pos[1] > thief_button.top and mouse_pos[1] < thief_button.bottom:
            thief_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), thief_button)
        else:
            thief_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), thief_button)
        screen.blit(text, (thief_button.x + 10, thief_button.y + (thief_button.height/4)))
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
            continue_button = pygame.draw.rect(screen, pygame.Color(150, 150, 150), continue_button)
        else:
            continue_button = pygame.draw.rect(screen, pygame.Color(180, 180, 180), continue_button)
        screen.blit(text, (continue_button.x, continue_button.y + (continue_button.height/2 - 17)))
    elif game_state == "exploring":
        keys = pygame.key.get_pressed()
        player_rect = pygame.Rect(width/2, height/2, 192, 192)
        if paused == False:
            if keys[K_w] == True:
                player_imagey = 192
                if player_imagex < 1344:
                    player_imagex += 50
                else:
                    player_imagex = 0
                worldy += 2
                if keys[K_a] == False and keys[K_s] == False and keys[K_d] == False:
                    worldy += 2
                for obstacle in current_map.keys():
                    obstacle_rect = pygame.Rect(obstacle)
                    if player_rect.top >= (worldy - obstacle_rect.bottom):
                        worldy -= 4
            if keys[K_a] == True:
                player_imagey = 576
                if player_imagex < 1344:
                    player_imagex += 50
                else:
                    player_imagex = 0
                worldx += 2
                if keys[K_w] == False and keys[K_s] == False and keys[K_d] == False:
                    worldx += 2
                for obstacle in current_map.keys():
                    obstacle_rect = pygame.Rect(obstacle)
                    if player_rect.left >= (worldx - obstacle_rect.right):
                        worldx -= 4
            if keys[K_s] == True:
                player_imagey = 0
                if player_imagex < 1344:
                    player_imagex += 50
                else:
                    player_imagex = 0
                worldy -= 2
                if keys[K_a] == False and keys[K_w] == False and keys[K_d] == False:
                    worldy -= 2
                for obstacle in current_map.keys():
                    obstacle_rect = pygame.Rect(obstacle)
                    if (player_rect.bottom >= (worldy - obstacle_rect.top) and current_map[obstacle] == "wall") or (player_rect.top >= (worldy - obstacle_rect.top) and current_map[obstacle] != "wall"):
                        worldy += 4
            if keys[K_d] == True:
                player_imagey = 384
                if player_imagex < 1344:
                    player_imagex += 50
                else:
                    player_imagex = 0
                worldx -= 2
                if keys[K_a] == False and keys[K_s] == False and keys[K_w] == False:
                    worldx -= 2
                for obstacle in current_map.keys():
                    obstacle_rect = pygame.Rect(obstacle)
                    if player_rect.right >= (worldx - obstacle_rect.left):
                        worldx += 4
            if keys[K_w] == False and keys[K_a] == False and keys[K_s] == False and keys[K_d] == False:
                player_imagex = 0
        screen.blit(background, (0, 0), area=(worldx, worldy, width, height))
        screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
        for obstacle in current_map.keys():
            obstacle_rect = pygame.Rect(obstacle)
            if current_map[obstacle] == "wall":
                pygame.draw.rect(screen, pygame.Color(150, 150, 150), (obstacle_rect.x - worldx + (width/2), obstacle_rect.y - worldy + (height/2), obstacle_rect.width, obstacle_rect.height))
            elif current_map[obstacle] == "house":
                screen.blit(objects, (obstacle_rect.x - worldx + (width/2), obstacle_rect.y - worldy + (height/2)), area=(0, 0, 768, 768))
            elif current_map[obstacle] == "building":
                screen.blit(objects, (obstacle_rect.x - worldx + (width/2), obstacle_rect.y - worldy + (height/2)), area=(768, 0, 768, 768))
        if player_rect.bottom >= (worldy - obstacle_rect.top):
            screen.blit(player_sprite, ((width / 2) - 96, (height / 2) - 96), area=(192*round(player_imagex/192), player_imagey, 192, 192))
    screen.blit(mouse_pointer, mouse_pos)
    pygame.display.update()
    clock.tick(32)
pygame.quit()
sys.exit()
