import pygame
pygame.init()

win = pygame.display.set_mode((1200, 650))

pygame.display.set_caption("cubes game")

walkRight = [pygame.image.load('walking00.png'), pygame.image.load('walking01.png'),
             pygame.image.load('walking02.png'), pygame.image.load('walking03.png'),
             pygame.image.load('walking04.png'), pygame.image.load('walking05.png'),
             pygame.image.load('walking06.png'), pygame.image.load('walking07.png'),
             pygame.image.load('walking08.png'), pygame.image.load('walking09.png'),
             pygame.image.load('walking10.png'), pygame.image.load('walking11.png')]

walkLeft = [pygame.image.load('walkingleft00.png'), pygame.image.load(
    'walkingleft01.png'), pygame.image.load('walkingleft02.png'), pygame.image.load(
    'walkingleft03.png'), pygame.image.load('walkingleft04.png'), pygame.image.load(
    'walkingleft05.png'), pygame.image.load('walkingleft06.png'), pygame.image.load(
    'walkingleft07.png'), pygame.image.load('walkingleft08.png'), pygame.image.load(
    'walkingleft09.png'), pygame.image.load('walkingleft10.png'), pygame.image.load(
    'walkingleft11.png')]

bg = pygame.image.load('bg.png')
playerStand = pygame.image.load('walking00.png')

clock = pygame.time.Clock()

x = 20
y = 525
widht = 70
height = 70
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"

class snr():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
    global animCount

    win.blit(bg, (0, 0))

    if animCount + 1 >=30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount//5], (x,y))
        animCount +=1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)



    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 1200 and bullet.x >0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 20:
            bullets.append(snr(round(x + widht // 2), (round(y + height // 2)), 5, (255, 0, 0), facing))

    if keys[pygame.K_a] and x>5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_d]and x< 1200 - widht:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount <0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2)/2
            jumpCount -=1

        else:
            isJump = False
            jumpCount = 10


    drawWindow()
pygame.quit()