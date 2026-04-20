import pygame,random,math
from pygame.locals import *
from pygame.math import Vector2
pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont(None, 40)

gameLoop = True
playerSpeed = 3
grounded = False
fallSpeed = 9

#Hover the player to see collision wireframes
        
human = pygame.image.load("human.png")
city_background = pygame.image.load("city_background.png")
objects = pygame.image.load("objects.png")

FPS = 100
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800),pygame.RESIZABLE)
w, h = pygame.display.get_surface().get_size()
mousePos = pygame.mouse.get_pos()
offset = pygame.math.Vector2(0,0)
world = pygame.math.Vector2(w/2,h/2)

drawWireFrames = True

playerSize = 200
playerRect = pygame.Rect(w/2,h/2,playerSize,playerSize)
playerCollision = pygame.Rect(0,0,0,0)
playerStep = pygame.Rect(0,0,0,0)

cityRect = pygame.Rect(world.x-1000,world.y-1000,2000,2000)

house = pygame.Rect(world.x,world.y+100,200,400)
houseFoundation = pygame.Rect(house.x,house.y+150,200,100)
houseSiding = pygame.Rect(0,0,0,0)

#didn't have time to replace the animation variables with these class variables
class Image:
    def __init__(self, sheetW,sheetH,sheetRows,sheetColumns,X,Y,counter, directionFacing):
        self.sheetW = sheetW,
        self.sheetH = sheetH,
        self.sheetRows = sheetRows,
        self.sheetColumns = sheetColumns,
        self.X = X,
        self.Y = Y,
        self.counter = counter,
        self.directionFacing = directionFacing
    def draw(self):
        pass
humanSheetW, humanSheetH = human.get_size()
humanSheetRows = 4
humanSheetColumns = 8
humanImageX = 0
humanImageY = 0
humanSheetCounter = 0
directionFacing = "down"

def handleInputs():
    global gameLoop,world,directionFacing,walking
    keys = pygame.key.get_pressed()
    walking = False
    directionFacing = "standingStill"
    if keys[pygame.K_w]:
        offset.y += playerSpeed
        directionFacing = "up"
        walking = True
    if keys[pygame.K_s]:
        offset.y -= playerSpeed
        directionFacing = "down"
        walking = True
    if keys[pygame.K_a]:
        offset.x += playerSpeed
        directionFacing = "left"
        walking = True
    if keys[pygame.K_d]:
        offset.x -= playerSpeed
        directionFacing = "right"
        walking = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameLoop = False
subArea = human.subsurface((humanImageX,humanImageY,(humanSheetW/humanSheetColumns),(humanSheetH/humanSheetRows)))
scaledHuman = pygame.transform.scale(subArea,playerRect.size)
def animate():
    global humanImageX,humanImageY,humanSheetCounter,playerRect,humanSheetW,drawWireFrames
    global humanSheetH,humanSheetColumns,scaledHuman,subArea,directionFacing,walking
    drawWireFrames = False
    if playerRect.contains(mousePos,(1,1)):
        drawWireFrames=True
    humanSheetCounter +=8
    
    if humanSheetCounter % (humanSheetW/humanSheetColumns) == 0:
        humanImageX=humanSheetCounter
    if humanSheetCounter>=humanSheetW-(humanSheetW/humanSheetColumns):
        humanSheetCounter=0
        
    if not walking:
        humanImageX=0
    
    if directionFacing == "up":
        humanImageY = (humanSheetH/humanSheetRows)*1
    if directionFacing == "down":
        humanImageY = (humanSheetH/humanSheetRows)*0
    if directionFacing == "left":
        humanImageY = (humanSheetH/humanSheetRows)*3
    if directionFacing == "right":
        humanImageY = (humanSheetH/humanSheetRows)*2
    subArea = human.subsurface((humanImageX,humanImageY,(humanSheetW/humanSheetColumns),(humanSheetH/humanSheetRows)))
    scaledHuman = pygame.transform.scale(subArea,playerRect.size)

    if drawWireFrames:
        pygame.draw.rect(screen, ('orange'), (playerRect),1,10)
        pygame.draw.rect(screen, ('red'), (playerCollision),1,10)
        pygame.draw.rect(screen, ('green'), (playerStep),1,10)

    screen.blit(scaledHuman,playerRect)

def drawBackground():
    screen.blit(city_background,cityRect)

def drawBuilding():
    global drawWireFrames
    offsetX=160
    offsetY=5
    subArea = objects.subsurface((offsetX,offsetY,(objects.get_width()-offsetX),(objects.get_height()-offsetY)))
    #newArea = subArea.subsurface(subArea)
    houseImage = pygame.transform.scale(subArea,(house.w*1.5,house.h*1.5))
    
    screen.blit(houseImage,house)
    if drawWireFrames:
        pygame.draw.rect(screen, ('brown'), house, 1, 5)
        pygame.draw.rect(screen, ('peru'), houseFoundation, 1, 5)
        pygame.draw.rect(screen, 'mistyrose', houseSiding, 1, 5)
    
def collidePlayer(self,player):
    global offset,grounded,mousePos,inRange,drawWireFrames
    if self.colliderect(player):
        leftOverlap = player.right - self.left
        rightOverlap = self.right - player.left
        topOverlap = player.bottom - self.top
        bottomOverlap = self.bottom - player.top
        min_overlap = min(leftOverlap, rightOverlap, topOverlap, bottomOverlap)
        if min_overlap == topOverlap:
            offset.y += topOverlap
            grounded = True
        elif min_overlap == bottomOverlap:
            offset.y -= bottomOverlap
        elif min_overlap == leftOverlap:
            offset.x += leftOverlap
        elif min_overlap == rightOverlap:
            offset.x -= rightOverlap
while gameLoop:
    pygame.display.set_caption(f"directionFacing:{directionFacing}")
    
    mousePos = pygame.mouse.get_pos()
    handleInputs()
    
    w, h = pygame.display.get_surface().get_size()
    
    playerRect = pygame.Rect(w/2-playerRect.w/2,h/2-playerRect.h/2,playerSize,playerSize)
    playerCollision = pygame.Rect(playerRect.x + playerSize/4,playerRect.y,playerSize/2,playerSize)
    playerStep = pygame.Rect(playerCollision.x,playerCollision.centery+playerSize/4,playerSize/2,playerSize/4)
    
    world = pygame.Vector2(playerRect.x+offset.x,playerRect.y+offset.y)
    cityRect = pygame.Rect(world.x-1000,world.y-1000,2000,2000)
    
    house = pygame.Rect(world.x- 100,world.y+150,400,400)
    houseFoundation = pygame.Rect(house.x,house.bottom+house.h/4,400,50)
    houseSiding = pygame.Rect(house.x+house.w,houseFoundation.y,50,playerSpeed)

    collidePlayer(houseFoundation,playerStep)
    collidePlayer(houseSiding,playerStep)
    screen.fill('black')
    
    clock.tick(FPS)
    drawBackground()
    if playerStep.top<houseFoundation.top:#when you have a list of all your houses, loop through all houses
        animate()
        drawBuilding()

    else:
        drawBuilding()
        animate()

    pygame.display.flip()
    

pygame.quit()
