import pygame, random, time
pygame.init()

def next_level():
    global level, FPS, screen, timer, cutscene
    level += 1
    FPS += FPS
    screen.fill(pygame.Color(0, 0, 0))
    font = pygame.font.SysFont(None, 50, bold=True)
    text = font.render(f"Level {level}", True, pygame.Color(0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    screen.blit(text, text_rect)
    cutscene = True

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h - 50
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Button Masher")
font = pygame.font.SysFont(None, 20, bold=True)
FPS = 2
level = 1
menu = True
cutscene = False
running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        try:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu == True:
                    font = pygame.font.SysFont(None, 20, bold=True)
                    menu = False
                elif cutscene == True:
                    font = pygame.font.SysFont(None, 20, bold=True)
                    cutscene = False
                else:
                    mousex, mousey = pygame.mouse.get_pos()
                    if mousex < (x + 60) and mousex > (x - 60) and mousey < (y + 60) and mousey > (y - 60):
                        next_level()
        except:
            pass
    if menu == True:
        screen.fill(pygame.Color(0, 0, 0))
        font = pygame.font.SysFont(None, 70, bold=True)
        text = font.render("Button Masher", True, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, (height/2 - 50))
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 30, bold=True)
        text = font.render("Try to push the button", True, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, (height/2))
        screen.blit(text, text_rect)
        text = font.render("Push the mouse button to play", True, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, (height/2 + 50))
        screen.blit(text, text_rect)
    elif cutscene == True:
        screen.fill(pygame.Color(0, 0, 0))
        font = pygame.font.SysFont(None, 50, bold=True)
        text = font.render(f"Level {level}", True, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, height/2)
        screen.blit(text, text_rect)
        font = pygame.font.SysFont(None, 30, bold=True)
        text = font.render("Press the mouse button to continue", True, pygame.Color(255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (width/2, (height/2 + 50))
        screen.blit(text, text_rect)
            
    else:
        number = random.randint(1, 10)
        if number == 1:
            color = pygame.Color(255, 0, 0) #red
        elif number == 2:
            color = pygame.Color(255, 153, 51) #orange
        elif number == 3:
            color = pygame.Color(255, 255, 0) #yellow
        elif number == 4:
            color = pygame.Color(51, 204, 51) #green
        elif number == 5:
            color = pygame.Color(0, 102, 255) #blue
        elif number == 6:
            color = pygame.Color(153, 51, 255) #purple
        elif number == 7:
            color = pygame.Color(255, 0, 255) #pink
        elif number == 9:
            color = pygame.Color(0, 0, 0) #black
        elif number == 10:
            color = pygame.Color(153, 52, 51) #brown
        color2 = color
        while color == color2:
            number = random.randint(1, 9)
            if number == 1:
                color = pygame.Color(255, 0, 0) #red
            elif number == 2:
                color = pygame.Color(255, 153, 51) #orange
            elif number == 3:
                color = pygame.Color(255, 255, 0) #yellow
            elif number == 4:
                color = pygame.Color(51, 204, 51) #green
            elif number == 5:
                color = pygame.Color(0, 102, 255) #blue
            elif number == 6:
                color = pygame.Color(153, 51, 255) #purple
            elif number == 7:
                color = pygame.Color(255, 0, 255) #pink
            elif number == 8:
                color = pygame.Color(255, 255, 255) #white
            elif number == 9:
                color = pygame.Color(0, 0, 0) #black
            elif number == 10:
                color = pygame.Color(153, 52, 51) #brown
        number = random.randint(1, 6)
        screen.fill(pygame.Color(255, 255, 255))
        x = random.randint(0, width)
        y = random.randint(0, height)
        if number == 1:
            words = "Click me!"
        elif number == 2:
            words = "Too slow!"
        elif number == 3:
            words = "Push the button!"
        elif number == 4:
            words = "Over here!"
        elif number == 5:
            words = "You missed!"
        elif number == 6:
            words = "Come get me!"
        font = pygame.font.SysFont(None, 30, bold=True)
        text = font.render(f"Level {level}", True, pygame.Color(0, 0, 0))
        screen.blit(text, (10, (height - 50)))
        font = pygame.font.SysFont(None, 20, bold=True)
        text = font.render(words, True, pygame.Color(color))
        number = random.randint(1, 10)
        pygame.draw.circle(screen, pygame.Color(color2), (x, y), 60)
        text_rect = text.get_rect(center = (x, y))
        screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
pygame.quit()
exit()
