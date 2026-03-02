import pygame, random, string, math
from pygame.locals import *
pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 50
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cypher Smasher")
clock = pygame.time.Clock()
letters = string.ascii_lowercase
valid_multiplicative_keys = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
cheat_code = [K_SPACE, K_k, K_e, K_y]
texts = ["this is the secret message.", "congratulations! you solved it!", "this is an extremely easy cypher.", "and that's why no one uses this cypher anymore.", "encrypt this if you can. Oh wait, you already did", "You can never have too much encryption.", "Cryptography is cool!", "Julius Ceaser was the one who came up with the ceaser cypher.", "AES stands for advanced encryption standard.", "The one-time pad is the only unbreakable cypher.", "The word cypher comes from the Arabic sifr, meaning zero.", "The Vigenere cipher was once called the the indecipherable cipher.", "A brute-force attack means trying every possible key until something works.", "Some cyphers have so many keys, you can't brute-force attack them.", "A cypher should rely on the key being secret, not the algerithm.", "Cryptanalysis is the art of breaking crypto.", "Cryptography is mostly complicated math equations.", "A keyspace is the total number of possible keys.", "A substitution cypher has so many keys, you can't brute force attack it.", "Many security failures are implementation flaws.", "It's usually a bad idea to use your own algerithms for security.", "Cryptanalysis often exploits human mistakes.", "Good cyphers assume attackers know the algorithm.", "HTTPS is HTTP encrypted with TLS.", "A cypher is only ever as strong as its implementation.", "Modern encryption is so strong it would take billions of years to brute-force.", "Even your Wi-Fi password uses cryptography.", "You can encrypt with a public key, but only a private key can decrypt.", "Without cyphers, the internet wouldn’t be safe to use.", "Cryptocurrencies rely on cryptography.", "Governments use cryptography for classified communication.", "The US government uses the AES cypher for sending sensitive info.", "A VPN uses cyphers to hide your internet traffic.", "The padlock on HTTPS means your connection is encrypted."]
def reset():
    global font, cutscene, level, cyphertype, user_input, timer, won, lost, victory, hard_mode
    font = pygame.font.SysFont(None, 80, bold=True)
    cutscene = True
    cyphertype = "ceaser"
    level = 1
    user_input = ""
    timer = 0
    won = False
    lost = False
    victory = False
    hard_mode = False

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val == char:
                return r, c
    return None

def rotate(rotor, steps):
    steps = ord(steps.upper()) - 65 if isinstance(steps, str) else steps
    return rotor[steps:] + rotor[:steps]

def plugboard_swap(char, plugboard):
    return plugboard.get(char, char)

def encrypt(text, cypher, key="random"):
    global letters
    text = text.lower()
    encrypted = ""
    if key == "random":
        if cypher == "ceaser":
            key = random.randint(1, 25)
        elif cypher == "substitution":
            key_list = list(letters)
            random.shuffle(key_list)
            key = "".join(key_list).lower()
        elif cypher == "multiplicative":
            number = random.randint(0, len(valid_multiplicative_keys)-1)
            key = valid_multiplicative_keys[number]
        elif cypher == "affine":
            number = random.randint(0, len(valid_multiplicative_keys)-1)
            keya = valid_multiplicative_keys[number]
            keyb = random.randint(1, 25)
        elif cypher == "vigenere" or cypher == "transposition":
            length = random.randint(3, len(text))
            key = "".join(random.choice(letters) for x in range(length)).lower()
        elif cypher == "playfair":
            key_list = list("abcdefghiklmnopqrstuvwxyz")
            random.shuffle(key_list)
            key = "".join(key_list).lower()
        elif cypher == "hill":
            while True:
                a, b, c, d = [random.randint(0,25) for _ in range(4)]
                det = (a*d - b*c) % 26
                if det != 0 and math.gcd(det,26) == 1:
                    key = [[a,b],[c,d]]
                    break
        elif cypher == "enigma":
            ROTORS = ["I", "II", "III"]
            rotor_order = random.sample(ROTORS, 3)
            rotor_positions = [random.choice(string.ascii_uppercase) for _ in range(3)]
            ring_settings = [random.randint(1, 26) for _ in range(3)]
            letters_for_plugboard = list(string.ascii_uppercase)
            random.shuffle(letters_for_plugboard)
            num_pairs = random.randint(0, 10)
            plugboard = {}
            for i in range(0, min(num_pairs*2, len(letters_for_plugboard)-1), 2):
                a, b = letters_for_plugboard[i], letters_for_plugboard[i+1]
                plugboard[a] = b
                plugboard[b] = a
            key = {"rotor_order": rotor_order, "rotor_positions": rotor_positions, "ring_settings": ring_settings, "plugboard": plugboard}
    text = text.lower()
    key = key.lower() if isinstance(key,str) else key
    if cypher == "ceaser":
        shifted = letters[key:] + letters[:key]
        table = str.maketrans(letters, shifted)
        encrypted = text.translate(table)
    elif cypher == "atbash":
        reversed_alphabet = letters[::-1]
        table = str.maketrans(letters, reversed_alphabet)
        encrypted = text.translate(table)
    elif cypher == "substitution":
        encrypt_map = dict(zip(letters, key))
        encrypted = ""
        for char in text.lower():
            if char in encrypt_map:
                encrypted += encrypt_map[char]
            else:
                encrypted += char
    elif cypher == "multiplicative":
        encrypted = "".join(letters[(letters.index(c)*key)%26] if c in letters else c for c in text)
    elif cypher == "affine":
        encrypted = "".join(letters[(letters.index(c)*keya + keyb)%26] if c in letters else c for c in text)
    elif cypher == "vigenere":
        key_index = 0
        encrypted = []
        for symbol in text:
            if symbol.isalpha():
                num = letters.find(symbol.lower())
                num += letters.find(key[key_index % len(key)])
                num %= len(letters)
                encrypted.append(letters[num].lower())
                key_index += 1
            else:
                encrypted.append(symbol)
        encrypted = "".join(encrypted)
    elif cypher == "transposition":
        plaintext = text.replace(" ", "").upper()
        num_cols = len(key)
        num_rows = math.ceil(len(plaintext) / num_cols)
        padded_length = num_rows * num_cols
        plaintext += "X" * (padded_length - len(plaintext))
        grid = [plaintext[i:i+num_cols] for i in range(0, len(plaintext), num_cols)]
        key_order = sorted(range(len(key)), key=lambda k: key[k])
        encrypted = ""
        for col_index in key_order:
            for row in grid:
                encrypted += row[col_index]
    elif cypher == "playfair":
        key = key.replace("j", "i")
        alphabet = "abcdefghiklmnopqrstuvwxyz"
        seen = set()
        key_unique = ""
        for char in key:
            if char in alphabet and char not in seen:
                seen.add(char)
                key_unique += char
        for char in alphabet:
            if char not in seen:
                key_unique += char
        matrix = [list(key_unique[i:i+5]) for i in range(0, 25, 5)]
        plaintext = text.replace("j", "i")
        plaintext = "".join(filter(str.isalpha,text.replace("j","i")))
        i=0
        pairs=[]
        while i<len(plaintext):
            a=plaintext[i]
            b=plaintext[i+1] if i+1<len(plaintext) else "x"
            if a==b: b="x"; i+=1
            else: i+=2
            pairs.append((a,b))
        if len(pairs[-1]) == 1:
            pairs[-1] += "x"
        encrypted = ""
        for pair in pairs:
            r1, c1 = find_position(matrix, pair[0])
            r2, c2 = find_position(matrix, pair[1])
            if r1 == r2:
                encrypted += matrix[r1][(c1 + 1) % 5]
                encrypted += matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                encrypted += matrix[(r1 + 1) % 5][c1]
                encrypted += matrix[(r2 + 1) % 5][c2]
            else:
                encrypted += matrix[r1][c2]
                encrypted += matrix[r2][c1]
    elif cypher == "hill":
        plaintext = "".join(filter(str.isalpha, text.upper()))
        if len(plaintext) % 2 != 0:
            plaintext += "X"
        a,b = key[0]
        c,d = key[1]
        for i in range(0,len(plaintext),2):
            x = ord(plaintext[i])-65
            y = ord(plaintext[i+1])-65
            new_x = (a*x+b*y)%26
            new_y = (c*x+d*y)%26
            encrypted += chr(new_x+65)+chr(new_y+65)
    elif cypher == "enigma":
        ALPHABET = string.ascii_uppercase
        ROTOR_WIRINGS = {"I":   "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "II":  "AJDKSIRUXBLHWTMCQGZNPYFVOE", "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO"}
        REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        rotor_order = key["rotor_order"]
        positions = key["rotor_positions"]
        plugboard = key["plugboard"]
        rotors = [rotate(ROTOR_WIRINGS[r], p) for r, p in zip(rotor_order, positions)]
        encrypted = ""
        rotor_positions_indices = [ALPHABET.index(p) for p in positions]
        for char in text.upper():
            if char not in ALPHABET:
                encrypted += char
                continue
            char = plugboard.get(char, char)
            for rotor in rotors:
                char = rotor[ALPHABET.index(char)]
            char = REFLECTOR_B[ALPHABET.index(char)]
            for rotor in reversed(rotors):
                char = ALPHABET[rotor.index(char)]
            char = plugboard_swap(char, plugboard)
            encrypted += char
            rotor_positions_indices[0] = (rotor_positions_indices[0] + 1) % 26
            rotors[0] = rotate(ROTOR_WIRINGS[rotor_order[0]], ALPHABET[rotor_positions_indices[0]])
    return encrypted.lower()

def save(data):
    pass

def load(data):
    pass

def submit_input(answer):
    global won, lost, timer, plaintext, user_input
    timer = 0
    clean_answer = "".join(char.lower() for char in answer if char.isalnum())
    clean_plaintext = "".join(char.lower() for char in plaintext if char.isalnum())
    if clean_answer.lower() == clean_plaintext.lower():
        user_input = ""
        won = True
    else:
        lost = True

def level_up():
    global cutscene, level, plaintext, cyphertext, cyphertype, victory
    user_input = ""
    number = random.randint(1, len(texts))
    plaintext = texts[number - 1]
    print(plaintext)
    if hard_mode == True:
        plaintext = "".join(char for char in plaintext if char.isalpha()).lower()
    texts.remove(texts[number - 1])
    if cutscene == True:
        cutscene = False
        cyphertype = "ceaser"
        level = 1
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 1:
        level = 2
        cyphertype = "atbash"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 2:
        level = 3
        cyphertype = "substitution"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 3:
        level = 4
        cyphertype = "multiplicative"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 4:
        level = 5
        cyphertype = "affine"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 5:
        level = 6
        cyphertype = "vigenere"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 6:
        level = 7
        cyphertype = "transposition"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 7:
        level = 8
        cyphertype = "playfair"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 8:
        level = 9
        cyphertype = "hill"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 9:
        level = 10
        cyphertype = "enigma"
        cyphertext = encrypt(plaintext, cyphertype)
    elif level == 10:
        victory = True

reset()
running = True
while running == True:
    screen.fill(pygame.Color(0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if cutscene == True:
                if easy_buttonx <= mouse_x <= easy_buttonx + 300 and easy_buttony <= mouse_y <= easy_buttony + 100:
                    hard_mode = False
                    level_up()
                    font = pygame.font.SysFont(None, 60, bold=True)
                if hard_buttonx <= mouse_x <= hard_buttonx + 300 and hard_buttony <= mouse_y <= hard_buttony + 100:
                    hard_mode = True
                    level_up()
                    font = pygame.font.SysFont(None, 60, bold=True)
            if victory == True:
                if buttonx <= mouse_x <= buttonx + 300 and buttony <= mouse_y <= buttony + 100:
                    reset()
        if cutscene == False:
            if event.type == pygame.KEYDOWN:
                if event.key == K_BACKSPACE:
                    user_input = user_input[:-1]
                elif event.key == K_RETURN:
                    submit_input(user_input)
                else:
                    user_input += str(event.unicode)
        keys = pygame.key.get_pressed()
        if keys[K_f] == True and keys[K_SPACE] == True and keys[K_RIGHT] == True and cutscene == False and victory == False and won == False:
            level_up()
    if cutscene == True:
        text = font.render("Cypher Smasher", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 150)
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 60, bold=True)
        text = font.render("You found a series of encrypted", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 50)
        screen.blit(text, text_rect)
        text = font.render("texts and you must decrypt them", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2)
        screen.blit(text, text_rect)
        hard_buttonx = (width - 300) // 2
        hard_buttony = (height + 100) // 2
        pygame.draw.rect(screen, pygame.Color(180, 180, 180), (hard_buttonx, hard_buttony, 300, 100))
        text = font.render("Hard mode", False, Color(37, 92, 50))
        text_rect = text.get_rect()
        text_rect.center = (hard_buttonx + 150, hard_buttony + 50)
        screen.blit(text, text_rect)
        easy_buttonx = (width - 300) // 2
        easy_buttony = (height + 400) // 2
        pygame.draw.rect(screen, pygame.Color(180, 180, 180), (easy_buttonx, easy_buttony, 300, 100))
        text = font.render("Easy mode", False, Color(37, 92, 50))
        text_rect = text.get_rect()
        text_rect.center = (easy_buttonx + 150, easy_buttony + 50)
        screen.blit(text, text_rect)
    elif victory == True:
        font = pygame.font.SysFont(None, 200, bold=True)
        text = font.render("You win!", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2)
        screen.blit(text, text_rect)
        buttonx = (width - 300) // 2
        buttony = (height + 400) // 2
        pygame.draw.rect(screen, pygame.Color(180, 180, 180), (buttonx, buttony, 300, 100))
        font = pygame.font.SysFont(None, 50, bold=True)
        text = font.render("Play again", False, Color(37, 92, 50))
        text_rect = text.get_rect()
        text_rect.center = (buttonx + 150, buttony + 50)
        screen.blit(text, text_rect)

    else:
        font = pygame.font.SysFont(None, 60, bold=True)
        text = font.render(f"Level {level}:", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, 50)
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 60, bold=True)
        text = font.render(f"{cyphertype} cypher", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, 100)
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 40, bold=True)
        text = font.render(f"secret message: {cyphertext}", False, Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, 150)
        screen.blit(text, text_rect)
        rectx = (width - (round(width*.75))) // 2
        recty = (height - 100) // 2
        pygame.draw.rect(screen, pygame.Color(37, 92, 50), (rectx, recty, round(width*.75), 100), width=10)
        text = font.render(user_input, False, pygame.Color(255, 255, 255))
        screen.blit(text, (rectx + 50, recty + 40))
    if won == True:
        timer += 1
        font = pygame.font.SysFont(None, 50, bold=True)
        text = font.render("Correct!", True, Color(37, 92, 50))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 100)
        screen.blit(text, text_rect)
        if timer >= 32:
            level_up()
            won = False
    elif lost == True:
        timer += 1
        font = pygame.font.SysFont(None, 50, bold=True)
        text = font.render("Wrong!", True, Color(255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2 - 100)
        screen.blit(text, text_rect)
        if timer >= 32:
            lost = False
    pygame.display.update()
    clock.tick(32)
pygame.quit()
exit()
