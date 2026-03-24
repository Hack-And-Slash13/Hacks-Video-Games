import pygame, requests, sys, random, math, json, os
from io import BytesIO
pygame.init()
pygame.mixer.init()

try:
    print("Loading...")
except:
    pass

def save(data, name):
    if not os.path.exists(resource_path("Bible_Trivia_Game_save_data")):
        os.makedirs(resource_path("Bible_Trivia_Game_save_data"))
    filepath = os.path.join(resource_path("Bible_Trivia_Game_save_data"), name)
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

def resource_path(filename):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)

questions = requests.get("https://raw.githubusercontent.com/Hack-And-Slash13/bible-trivia-game/main/questions.json")
questions = questions.json()
random.shuffle(questions)
background = requests.get("https://raw.githubusercontent.com/Hack-And-Slash13/bible-trivia-game/main/bible_pic.png")
background = BytesIO(background.content)
background = pygame.image.load(background)
music = requests.get("https://raw.githubusercontent.com/Hack-And-Slash13/bible-trivia-game/main/song.ogg")
music = BytesIO(music.content)
music = pygame.mixer.Sound(music)
high_score = load("high_score", "Bible_Trivia_Game_save_data")
music.play(loops=-1)
answered = False
cutscene = True
number = 0
score = 0
time = 10
clock = pygame.time.Clock()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 50
if width > height:
    background = pygame.transform.scale(background, (width, width))
else:
    background = pygame.transform.scale(background, (height, height))
button_rects = [(width/2, height/2 - 150), (width/2, height/2 - 50), (width/2, height/2 + 50), (width/2, height/2 + 150)]
random.shuffle(button_rects)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bible Trivia Game")
small_font = pygame.font.SysFont("Courier New", 20, bold=False)
medium_font = pygame.font.SysFont("Courier New", 30, bold=True)
big_font = pygame.font.SysFont("Courier New", 40, bold=True)
huge_font = pygame.font.SysFont("Courier New", 80, bold=True)

def parse_text(original_text, text, rect):
    original_text = str(original_text)
    space = original_text.find(" ", len(original_text) // 2)+1
    text_rect = text.get_rect()
    if text_rect.width > rect.width:
        parsed_text = (original_text[:space], original_text[space:])
        return parsed_text
    else:
        return None

running = True
while running == True:
    screen.fill(pygame.Color(0, 0, 0))
    background_rect = background.get_rect()
    background_rect.center = (width/2, height/2)
    screen.blit(background, background_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cutscene == False:
                if event.pos[0] < next_button.right and event.pos[0] > next_button.left and event.pos[1] > next_button.top and event.pos[1] < next_button.bottom:
                    time = 10
                    answered = False
                    if number < len(questions):
                        random.shuffle(button_rects)
                        number += 1
                    else:
                        random.shuffle(questions)
                        score = 0
                        number = 0
                if answered == False:
                    if event.pos[0] < answer_button1.right and event.pos[0] > answer_button1.left and event.pos[1] > answer_button1.top and event.pos[1] < answer_button1.bottom:
                        if time > 8:
                            score += 2
                            feedback = "correct! Speed bonus +1"
                        else:
                            score += 1
                            feedback = "correct!"
                        color = pygame.Color(0, 255, 80)
                        answered = True
                    if event.pos[0] < answer_button2.right and event.pos[0] > answer_button2.left and event.pos[1] > answer_button2.top and event.pos[1] < answer_button2.bottom:
                        color = pygame.Color(255, 0, 0)
                        feedback = "wrong!"
                        answered = True
                    if event.pos[0] < answer_button3.right and event.pos[0] > answer_button3.left and event.pos[1] > answer_button3.top and event.pos[1] < answer_button3.bottom:
                        color = pygame.Color(255, 0, 0)
                        feedback = "wrong!"
                        answered = True
                    if event.pos[0] < answer_button4.right and event.pos[0] > answer_button4.left and event.pos[1] > answer_button4.top and event.pos[1] < answer_button4.bottom:
                        color = pygame.Color(255, 0, 0)
                        feedback = "wrong!"
                        answered = True
            elif event.pos[0] < play_button.right and event.pos[0] > play_button.left and event.pos[1] > play_button.top and event.pos[1] < play_button.bottom:
                cutscene = False
    mouse_pos = pygame.mouse.get_pos()
    if cutscene == True:
        text = huge_font.render("Bible Trivia Game", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/4)
        screen.blit(text, text_rect)
        text = big_font.render("answer the questions quickly to get points", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/4+60)
        screen.blit(text, text_rect)
        text = medium_font.render("play", False, pygame.Color(255, 255, 255))
        play_button = text.get_rect()
        play_button.center = (width/2 - 50, height/2)
        play_button.width += 100
        play_button.height += 50
        if mouse_pos[0] < play_button.right and mouse_pos[0] > play_button.left and mouse_pos[1] > play_button.top and mouse_pos[1] < play_button.bottom:
            pygame.draw.rect(screen, pygame.Color(150, 150, 150), play_button)
        else:
            pygame.draw.rect(screen, pygame.Color(180, 180, 180), play_button)
        screen.blit(text, (play_button.x + 50, play_button.y + 25))
    else:
        if number >= len(questions):
            text = huge_font.render("GAME OVER", False, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (width/2, height/4)
            screen.blit(text, text_rect)
            if score > high_score:
                high_score = score
            save(high_score, "high_score")
            text = big_font.render(f"Your score: {score}", False, pygame.Color(180, 180, 180))
            text_rect = text.get_rect()
            text_rect.center = (width/2, height/4 + 100)
            screen.blit(text, text_rect)
            text = big_font.render(f"High score: {high_score}", False, pygame.Color(180, 180, 180))
            text_rect = text.get_rect()
            text_rect.center = (width/2, height/4 + 150)
            screen.blit(text, text_rect)
        else:
            if time > 0 and answered == False:
                time -= .03125
            elif time <= 0:
                color = pygame.Color(255, 0, 0)
                feedback = "time's up!"
                answered = True
            text = big_font.render(questions[number]["question"], False, pygame.Color(255, 255, 255))
            text_rect = text.get_rect()
            text_rect.center = (width/2, height/4 - (text_rect.height + 30))
            screen.blit(text, text_rect)
            if time > 3:
                text = medium_font.render(f"time: {math.ceil(time)}", False, pygame.Color(255, 255, 255))
            else:
                text = medium_font.render(f"time: {math.ceil(time)}", False, pygame.Color(255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (width/2, height/4 - text_rect.height)
            screen.blit(text, text_rect)
            if answered == False:
                text = medium_font.render(questions[number]["correct_answer"], False, pygame.Color(255, 255, 255))
            else:
                text = medium_font.render(questions[number]["correct_answer"], False, pygame.Color(0, 255, 80))
            answer_button1 = pygame.Rect(0, 0, 500, 50)
            answer_button1.center = (button_rects[0])
            parsed_text = parse_text(questions[number]["correct_answer"], text, answer_button1)
            if parsed_text != None:
                if mouse_pos[0] < answer_button1.right and mouse_pos[0] > answer_button1.left and mouse_pos[1] > answer_button1.top and mouse_pos[1] < answer_button1.bottom and answered == False:
                    pygame.draw.rect(screen, pygame.Color(220, 220, 220), (answer_button1.x, answer_button1.y - answer_button1.height/2, answer_button1.width, answer_button1.height*2))
                else:
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180), (answer_button1.x, answer_button1.y - answer_button1.height/2, answer_button1.width, answer_button1.height*2))
                if answered == False:
                    text = medium_font.render(parsed_text[0], False, pygame.Color(255, 255, 255))
                    text2 = medium_font.render(parsed_text[1], False, pygame.Color(255, 255, 255))
                else:
                    text = medium_font.render(parsed_text[0], False, pygame.Color(0, 255, 80))
                    text2 = medium_font.render(parsed_text[1], False, pygame.Color(0, 255, 80))
                screen.blit(text, (answer_button1.x, answer_button1.y - answer_button1.height/2))
                screen.blit(text2, (answer_button1.x, answer_button1.y + answer_button1.height/2))
            else:
                if mouse_pos[0] < answer_button1.right and mouse_pos[0] > answer_button1.left and mouse_pos[1] > answer_button1.top and mouse_pos[1] < answer_button1.bottom and answered == False:
                    pygame.draw.rect(screen, pygame.Color(220, 220, 220), answer_button1)
                else:
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180), answer_button1)
                screen.blit(text, answer_button1)
            if answered == False:
                text = medium_font.render(questions[number]["incorrect_answer1"], False, pygame.Color(255, 255, 255))
            else:
                text = medium_font.render(questions[number]["incorrect_answer1"], False, pygame.Color(255, 0, 0))
            answer_button2 = pygame.Rect(0, 0, 500, 50)
            answer_button2.center = (button_rects[1])
            parsed_text = parse_text(questions[number]["incorrect_answer1"], text, answer_button1)
            if parsed_text != None:
                if mouse_pos[0] < answer_button2.right and mouse_pos[0] > answer_button2.left and mouse_pos[1] > answer_button2.top and mouse_pos[1] < answer_button2.bottom and answered == False:
                    pygame.draw.rect(screen, pygame.Color(220, 220, 220), (answer_button2.x, answer_button2.y - answer_button3.height/2, answer_button2.width, answer_button2.height*2))
                else:
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180), (answer_button2.x, answer_button2.y - answer_button2.height/2, answer_button2.width, answer_button2.height*2))
                if answered == False:
                    text = medium_font.render(parsed_text[0], False, pygame.Color(255, 255, 255))
                    text2 = medium_font.render(parsed_text[1], False, pygame.Color(255, 255, 255))
                else:
                    text = medium_font.render(parsed_text[0], False, pygame.Color(255, 0, 0))
                    text2 = medium_font.render(parsed_text[1], False, pygame.Color(255, 0, 0))
                screen.blit(text, (answer_button2.x, answer_button3.y - answer_button3.height/2))
                screen.blit(text2, (answer_button2.x, answer_button3.y + answer_button3.height/2))
            else:
                if mouse_pos[0] < answer_button2.right and mouse_pos[0] > answer_button2.left and mouse_pos[1] > answer_button2.top and mouse_pos[1] < answer_button2.bottom and answered == False:
                    pygame.draw.rect(screen, pygame.Color(220, 220, 220), answer_button2)
                else:
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180), answer_button2)
                screen.blit(text, answer_button2)
            if answered == False:
                text = medium_font.render(questions[number]["incorrect_answer2"], False, pygame.Color(255, 255, 255))
            else:
                text = medium_font.render(questions[number]["incorrect_answer2"], False, pygame.Color(255, 0, 0))
            answer_button3 = pygame.Rect(0, 0, 500, 50)
            answer_button3.center = (button_rects[2])
            parsed_text = parse_text(questions[number]["incorrect_answer2"], text, answer_button3)
            if parsed_text != None:
                if mouse_pos[0] < answer_button3.right and mouse_pos[0] > answer_button3.left and mouse_pos[1] > answer_button3.top and mouse_pos[1] < answer_button3.bottom and answered == False:
                    pygame.draw.rect(screen, pygame.Color(220, 220, 220), (answer_button3.x, answer_button3.y - answer_button4.height/2, answer_button3.width, answer_button3.height*2))
                else:
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180), (answer_button3.x, answer_button3.y - answer_button3.height/2, answer_button3.width, answer_button3.height*2))
                if answered == False:
                    text = medium_font.render(parsed_text[0], False, pygame.Color(255, 255, 255))
                    text2 = medium_font.render(parsed_text[1], False, pygame.Color(255, 255, 255))
                else:
                    text = medium_font.render(parsed_text[0], False, pygame.Color(255, 0, 0))
                    text2 = medium_font.render(parsed_text[1], False, pygame.Color(255, 0, 0))
                screen.blit(text, (answer_button3.x, answer_button3.y - answer_button3.height/2))
                screen.blit(text2, (answer_button3.x, answer_button3.y + answer_button3.height/2))
            else:
                if mouse_pos[0] < answer_button3.right and mouse_pos[0] > answer_button3.left and mouse_pos[1] > answer_button3.top and mouse_pos[1] < answer_button3.bottom and answered == False:
                    pygame.draw.rect(screen, pygame.Color(220, 220, 220), answer_button3)
                else:
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180), answer_button3)
                screen.blit(text, answer_button3)
            if answered == False:
                text = medium_font.render(questions[number]["incorrect_answer3"], False, pygame.Color(255, 255, 255))
            else:
                text = medium_font.render(questions[number]["incorrect_answer3"], False, pygame.Color(255, 0, 0))
            answer_button4 = pygame.Rect(0, 0, 500, 50)
            answer_button4.center = (button_rects[3])
            parsed_text = parse_text(questions[number]["incorrect_answer3"], text, answer_button4)
            if parsed_text != None:
                if mouse_pos[0] < answer_button4.right and mouse_pos[0] > answer_button4.left and mouse_pos[1] > answer_button4.top and mouse_pos[1] < answer_button4.bottom and answered == False:
                    pygame.draw.rect(screen, pygame.Color(220, 220, 220), (answer_button4.x, answer_button4.y - answer_button4.height/2, answer_button4.width, answer_button4.height*2))
                else:
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180), (answer_button4.x, answer_button4.y - answer_button4.height/2, answer_button4.width, answer_button4.height*2))
                if answered == False:
                    text = medium_font.render(parsed_text[0], False, pygame.Color(255, 255, 255))
                    text2 = medium_font.render(parsed_text[1], False, pygame.Color(255, 255, 255))
                else:
                    text = medium_font.render(parsed_text[0], False, pygame.Color(255, 0, 0))
                    text2 = medium_font.render(parsed_text[1], False, pygame.Color(255, 0, 0))
                screen.blit(text, (answer_button4.x, answer_button4.y - answer_button4.height/2))
                screen.blit(text2, (answer_button4.x, answer_button4.y + answer_button4.height/2))
            else:
                if mouse_pos[0] < answer_button4.right and mouse_pos[0] > answer_button4.left and mouse_pos[1] > answer_button4.top and mouse_pos[1] < answer_button4.bottom and answered == False:
                    pygame.draw.rect(screen, pygame.Color(220, 220, 220), answer_button4)
                else:
                    pygame.draw.rect(screen, pygame.Color(180, 180, 180), answer_button4)
                screen.blit(text, answer_button4)
            if answered == True:
                text = medium_font.render(feedback, False, color)
                text_rect = text.get_rect()
                text_rect.center = (width/2, height - 50)
                screen.blit(text, text_rect)
        next_button = pygame.Rect((width - 450, height - 100), (400, 50))
        if mouse_pos[0] < next_button.right and mouse_pos[0] > next_button.left and mouse_pos[1] > next_button.top and mouse_pos[1] < next_button.bottom:
            pygame.draw.rect(screen, pygame.Color(220, 220, 220), next_button)
        else:
            pygame.draw.rect(screen, pygame.Color(180, 180, 180), next_button)
        if number == len(questions)-1:
            text = small_font.render("submit", False, pygame.Color(255, 255, 255))
        elif number >= len(questions):
            text = small_font.render("play again", False, pygame.Color(255, 255, 255))
        else:
            text = small_font.render("next question ->", False, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = next_button.center
        screen.blit(text, text_rect)
        text = small_font.render(f"score: {score}", False, pygame.Color(255, 255, 255))
        screen.blit(text, (50, height - 75, 400, 50))
        if number <= len(questions)-1:
            text = small_font.render(f"question: {number+1}/{len(questions)}", False, pygame.Color(255, 255, 255))
        else:
            text = small_font.render(f"question: {len(questions)}/{len(questions)}", False, pygame.Color(255, 255, 255))
        screen.blit(text, (200, height - 75, 400, 50))
    pygame.display.update()
    clock.tick(32)
pygame.quit()
sys.exit()
