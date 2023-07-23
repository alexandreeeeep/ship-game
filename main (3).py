import pygame
import random
import time
import pygame.font
pygame.init()
pygame.display.init()
font = pygame.font.Font('freesansbold.ttf', 32)
size = 700
win = pygame.display.set_mode((size, size))
pygame.display.set_caption("gamergame")
ev = pygame.event.get()
black = (0, 0, 0)
die = False
Diff = 0
X = 0
Y = 0
robotexist = False
firsttime = True
firstheal = True
sauceranimation = 0
#loading exesive quantities of sprites
backbutton = pygame.image.load('Back button-1.png.png')
difficulties = [
    pygame.image.load('Difficulty -1.png.png'),
    pygame.image.load('Difficulty -2.png.png'),
    pygame.image.load('Difficulty -3.png.png'),
    pygame.image.load('Difficulty -4.png.png')
]
bosssheild = pygame.image.load('Sheild-1.png.png')
laserbullet = pygame.image.load('Laserbullet.png.png')
finalboss = [
    pygame.image.load('Finalboss-1.png.png'),
    pygame.image.load('Finalboss-2.png.png'),
    pygame.image.load('Finalboss-3.png.png'),
    pygame.image.load('Finalboss-4.png.png'),
    pygame.image.load('Finalboss-5.png.png')    
]
rightarm = [
  pygame.image.load('Right arm-1.png.png'),
  pygame.image.load('Right arm-2.png.png'),
  pygame.image.load('Right arm-3.png.png'),
  pygame.image.load('Right arm-4.png.png'),
  pygame.image.load('Right arm-5.png.png')
]
leftarm = [
  pygame.image.load('Left arm-1.png.png'),
  pygame.image.load('Left arm-2.png.png'),
  pygame.image.load('Left arm-3.png.png'),
  pygame.image.load('Left arm-4.png.png'),
  pygame.image.load('Left arm-5.png.png')
]
largecity = [
   pygame.image.load('Largecity-1.png.png'),
   pygame.image.load('Largecity-2.png.png')]
redship = [
    pygame.image.load('Red ship-1.png.png'),
    pygame.image.load('Red ship-2.png.png'),
]
redshipsheild =  pygame.image.load('Red ship sheild-1.png.png')
leg = pygame.image.load('Leg.png.png')
redshipland = pygame.image.load('Red ship-1.png1.png')
beam = [
    pygame.image.load('Beam-1.png.png'),
    pygame.image.load('Beam-2.png.png'),
    pygame.image.load('Beam-3.png.png'),pygame.image.load('Beam-4.png.png')
]
roborobotdie = [
    pygame.image.load('Robot destroyed-1.png (1).png'),
    pygame.image.load('Robot destroyed-1.png.png'),
    pygame.image.load('Robot destroyed-2.png.png'),
    pygame.image.load('Robot destroyed-3.png.png'),
    pygame.image.load('Robot destroyed-4.png.png'),
    pygame.image.load('Robot destroyed-5.png.png')
    ]
robotexplotion = [
    pygame.image.load('Robo Explotion-1.png.png'),
    pygame.image.load('Robo Explotion-2.png.png'),
    pygame.image.load('Robo Explotion-3.png.png'),
    pygame.image.load('Robo Explotion-4.png.png'),
    pygame.image.load('Robo Explotion-5.png.png'),
    pygame.image.load('Robo Explotion-6.png.png'),
    pygame.image.load('Robo Explotion-7.png.png')
    ]
robothandlaser = pygame.image.load('Robot laser-1.png.png')
robothandlaser = pygame.transform.scale(robothandlaser,(1400,700))
playerimage = [pygame.image.load('player-1.png.png'),pygame.image.load('player-2.png.png')]
brokenship = pygame.image.load('Ship burn backround-1.png.png')
orangelaser = pygame.image.load('orange laser-1.png.png')
reactor = [pygame.image.load('Reactor-1.png.png'),pygame.image.load('Reactor-2.png.png')]
rockp1 = [pygame.image.load('Giant rock-1.png.png'),pygame.image.load('Giant rock-2.png.png')]
rockp2 = [pygame.image.load('Other part of rock-1.png.png' ),pygame.image.load('Other part of rock-2.png.png')]
eye = [pygame.image.load('eye-1.png.png'),
    pygame.image.load('eye-2.png.png')]
redmissle = [
    pygame.image.load('Misile-1.png.png'),
    pygame.image.load('Misile-2.png.png')]
robot = [
    pygame.image.load('Robot-1.png.png'),
    pygame.image.load('Robot-2.png.png'),
    pygame.image.load('Robot-3.png.png')]
city = [
    pygame.image.load('City-1.png.png'),
    pygame.image.load('City-2.png.png')]
winscene = [
    pygame.image.load('Win-1.png.png'),
    pygame.image.load('Win-2.png.png'),
    pygame.image.load('Win-3.png.png'),
    pygame.image.load('Win-4.png.png'),
    pygame.image.load('Win-5.png.png'),
    pygame.image.load('Win-6.png.png'),
    pygame.image.load('Win-7.png.png'),
    pygame.image.load('Win-8.png.png'),
    pygame.image.load('Win-9.png.png'),
    pygame.image.load('Win-10.png.png')]
lasercannon = [
    pygame.image.load('Laser cannon-1.png.png'),
    pygame.image.load('Laser cannon-2.png.png'),
    pygame.image.load('Laser cannon-3.png.png'),
    pygame.image.load('Laser cannon-4.png.png'),
    pygame.image.load('Laser cannon-5.png.png'),
    pygame.image.load('Laser cannon-6.png.png'),
    pygame.image.load('Laser cannon-7.png.png')]
astroids = [
    pygame.image.load('asstroid-1.png.png'),
    pygame.image.load('asstroid-2.png.png'),
    pygame.image.load('asstroid-3.png.png'),
    pygame.image.load('asstroid-4.png.png'),
    pygame.image.load('asstroid-5.png.png'),
    pygame.image.load('asstroid-6.png.png'),
    pygame.image.load('asstroid-7.png.png')]

headlaser = [
    pygame.image.load('Head laser-1.png.png'),
    pygame.image.load('Head laser-2.png.png'),
    pygame.image.load('Head laser-3.png.png'),
    pygame.image.load('Head laser-4.png.png'),
    pygame.image.load('Head laser-5.png.png'),
    pygame.image.load('Head laser-6.png.png'),
    pygame.image.load('Head laser-7.png.png')
    ]
greenship = [
    pygame.image.load('Green ship-1.png.png'),
    pygame.image.load('Green ship-2.png.png'),
    pygame.image.load('Green ship-3.png.png'),
    pygame.image.load('Green ship-4.png.png'),
    pygame.image.load('Green ship-5.png.png'),
    pygame.image.load('Green ship-6.png.png')
]
blueship = [
    pygame.image.load('Blue ship-1.png.png'),
    pygame.image.load('Blue ship-2.png.png'),
    pygame.image.load('Blue ship-3.png.png'),
    pygame.image.load('Blue ship-4.png.png'),
    pygame.image.load('Blue ship-5.png.png')
]
orangeship = [
    pygame.image.load('Orange ship-1.png.png'),
    pygame.image.load('Orange ship-2.png.png'),
    pygame.image.load('Orange ship-3.png.png'),
    pygame.image.load('Orange ship-4.png.png')
]
destroyer = [
    pygame.image.load('Destroyer-1.png.png'),
    pygame.image.load('Destroyer-2.png.png'),
    pygame.image.load('Destroyer-3.png.png'),
    pygame.image.load('Destroyer-4.png.png'),
    pygame.image.load('Destroyer-5.png.png')
]
blueexplotionlaser=[
pygame.image.load('Blueexplotionlaser-1.png.png'),
pygame.image.load('Blueexplotionlaser-2.png.png')
]
characters = [
    pygame.image.load('Sprites-1.png.png'),
    pygame.image.load('Sprites-2.png.png'),
    pygame.image.load('Sprites-3.png.png')
]
level = [
    pygame.image.load('Level-1.png.png'),
    pygame.image.load('Level-2.png.png'),
    pygame.image.load('Level-3.png.png')
]
bluelaser = [
    pygame.image.load('Blue laser-1.png.png'),
    pygame.image.load('Blue laser-2.png.png'),
    pygame.image.load('Blue laser-3.png.png'),
    pygame.image.load('Blue laser-4.png.png')
]
bluebomb = [
    pygame.image.load('bluebomb-1.png.png'),
    pygame.image.load('bluebomb-2.png.png'),
    pygame.image.load('bluebomb-3.png.png'),
    pygame.image.load('bluebomb-4.png.png')
]
lasergun = [
    pygame.image.load('Laserbeam-1.png.png'),
    pygame.image.load('Laserbeam-2.png.png'),
    pygame.image.load('Laserbeam-3.png.png'),
    pygame.image.load('Laserbeam-4.png.png'),
    pygame.image.load('Laserbeam-5.png.png')
]
shipbackround = [
    pygame.image.load('Large ship-1.png.png'),
    pygame.image.load('Large ship-2.png.png'),
    pygame.image.load('Large ship-3.png.png'),
    pygame.image.load('Large ship-4.png.png')
]
mouse = pygame.image.load('Level-4.png.png')
redbullet = [
    pygame.image.load('bullet-1.png (1).png'),
    pygame.image.load('bullet-2.png (1).png'),
    pygame.image.load('bullet-3.png(1).png'),
    pygame.image.load('bullet-4.png(1).png'),
    pygame.image.load('bullet-5.png(1).png')]
missle = [
    pygame.image.load('Missile-1.png.png'),
    pygame.image.load('Missile-2.png.png'),
    pygame.image.load('Missile-3.png.png'),
    pygame.image.load('Missile-4.png.png'),
    pygame.image.load('Missile-5.png.png'),
    pygame.image.load('Missile-6.png.png')
]
firing = [
    pygame.image.load('Bullet-1.png.png'),
    pygame.image.load('Bullet-2.png.png'),
    pygame.image.load('Bullet-3.png.png'),
    pygame.image.load('Bullet-5.png.png'),
    pygame.image.load('Bullet-6.png.png'),
    pygame.image.load('Bullet-7.png.png'),
    pygame.image.load('Bullet-8.png.png')
]
explotion = [
    pygame.image.load('Green explotion-1.png.png'),
    pygame.image.load('Green explotion-2.png.png'),
    pygame.image.load('Green explotion-3.png.png'),
    pygame.image.load('Green explotion-5.png.png'),
    pygame.image.load('Green explotion-6.png.png'),
    pygame.image.load('Green explotion-7.png.png'),
    pygame.image.load('Green explotion-8.png.png'),
    pygame.image.load('Green explotion-9.png.png')
]
target = [
    pygame.image.load('Target-1.png.png'),
    pygame.image.load('Target-2.png.png'),
    pygame.image.load('Target-3.png.png'),
    pygame.image.load('Target-4.png.png'),
    pygame.image.load('Target-5.png.png'),
    pygame.image.load('Target-6.png.png')
]
bullet = [
    pygame.image.load('Saucer bullet-1.png.png'),
    pygame.image.load('Saucer bullet-2.png.png'),
    pygame.image.load('Saucer bullet-3.png.png'),
    pygame.image.load('Saucer bullet-5.png.png'),
    pygame.image.load('Saucer bullet-6.png.png'),
    pygame.image.load('Saucer bullet-7.png.png'),
    pygame.image.load('Saucer bullet-8.png.png')
]
undamagedsaucer = [
    pygame.image.load('Saucer clone-1.png.png'),
    pygame.image.load('Saucer clone-2.png.png'),
    pygame.image.load('Saucer clone-3.png.png'),
    pygame.image.load('Saucer clone-4.png.png'),
    pygame.image.load('Saucer clone-5.png.png'),
    pygame.image.load('Saucer clone-6.png.png'),
    pygame.image.load('Saucer clone-7.png.png')
]
damagedsaucer = [
    pygame.image.load('DSaucer-1.png.png'),
    pygame.image.load('DSaucer-2.png.png'),
    pygame.image.load('DSaucer-3.png.png'),
    pygame.image.load('DSaucer-4.png.png'),
    pygame.image.load('DSaucer-6.png.png'),
    pygame.image.load('DSaucer-7.png.png'),
    pygame.image.load('DSaucer-5.png.png')
]
ylaseranimation = [
    pygame.image.load('New Piskel-1.png.png'),
    pygame.image.load('New Piskel-2.png.png'),
    pygame.image.load('New Piskel-3.png.png'),
    pygame.image.load('New Piskel-4.png.png'),
    pygame.image.load('New Piskel-5.png.png')
]
xlaseranimation = [
    pygame.image.load('Lazar -1.png.png'),
    pygame.image.load('Lazar -2.png.png'),
    pygame.image.load('Lazar -3.png.png'),
    pygame.image.load('Lazar -4.png.png')
]
shipstill = pygame.image.load('Ship-1.png.png')
shipfowards = pygame.image.load('Ship-2.png.png')
shipback = pygame.image.load('Ship-3.png.png')
shiphit = pygame.image.load('Ship_hit.png.png')
shipsheild = pygame.image.load('Ship clone-2.png.png')
b = pygame.image.load('B.png')
o = pygame.image.load('0.png')
s = pygame.image.load('s.png')
x = 318
y = 318
x3 = 400  #stars
y3 = 400
x2 = 50
y2 = 100
x1 = 400
y1 = 350
maxhp = 99
hp = maxhp
shipbackroundloop = 0
blueshipy = 0
blueshipx = 0
orangeshipy = 0
orangeshipx = 0
greenshipy = 0
greenshipx = 0
autoscrollspeed = 3
#variables for main menu
end = True
openscreen = True
firstbossintro = False
run = True
difficultmenu = False
howtoplay = False
mainmeu = False
firstboss = False
firstbossoutro = False
secondbossintro = False
secondboss = False
secondbossp2intro = False
secondbossp2 = False
secondbossoutro = False
thirdbossintro = False
thirdboss = False
thirdbossoutro = False
Finalbossintro = False
FINALBOSS = False

my, mx = 0, 0#mouse pos
mouseupdate = 0
pygame.mouse.set_visible(False)

def update():
    pygame.mouse.center = pygame.mouse.get_pos()

pressed = ""
def sound():
    pass

while True:
    while openscreen == True:
        win.fill((0, 0, 0))
        pygame.time.delay(100)
        win.blit(shipstill,(328,328))
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render('press space to contine', 0, (255, 255, 255))
        win.blit(text, (140,600))
        y1 += 20
        if y1 >= 800:
            y1 = 0
            x1 = random.randint(10, 690)
        y2 += 30
        if y2 >= 800:
            y2 = 0
            x2 = random.randint(10, 690)
        y3 += 25
        if y3 >= 800:
            y3 = 0
            x3 = random.randint(10, 690)
        pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
        pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
        pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()#detect space press
            if keys[pygame.K_SPACE]:
                openscreen = False
                difficultmenu = True
        pygame.display.update()

    while howtoplay == True:
        font = pygame.font.Font('freesansbold.ttf', 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill((0, 0, 0))
        pygame.time.delay(100)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()#detect space press
            if keys[pygame.K_SPACE]:
                howtoplay = False
        win.blit(shipstill,(328,328))
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('This is your ship.', 0, (255, 255, 255))
        win.blit(text, (260,300 ))
        text = font.render('You can move in all directions', 0, (255, 255, 255))
        win.blit(text, (200,400 ))
        text = font.render('with the arrow keys.', 0, (255, 255, 255))
        win.blit(text, (250,436 ))
        #sheild
        pygame.draw.rect(win, (0, 0, 255), (2, 675, 1000/15, 32))
        #hp
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("HP: {0}".format(hp), 1, (255, 9, 12))  #hp variables dont change
        win.blit(text,(3,680))#hp
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('The blue bar is you shield.', 0, (255, 255, 255))
        win.blit(text,(3,550))
        text = font.render('To activate it hold space.', 0, (255, 255, 255))
        win.blit(text,(3,590))
        text = font.render('You will become imune to MOST damage.', 0, (255, 255, 255))
        win.blit(text,(3,630))
        text = font.render('If you get hit your hp decreases,', 0, (255, 255, 255))
        win.blit(text,(100,650))
        text = font.render('when it reaches zero you lose.', 0, (255, 255, 255))
        win.blit(text,(100,680))
        pygame.draw.rect(win, (202, 204, 208),(98, 38, 504, 36))  #bosshp backround
        pygame.draw.rect(win, (255, 0, 0),(100, 40, 1000 // 2, 32))
        text = font.render('This is an objective bar.', 0, (255, 255, 255))
        win.blit(text,(250,50))
        text = font.render('The bar needs to reduce to zero to complete the level.', 0, (255, 255, 255))
        win.blit(text,(150,100))
        text = font.render('You do this by shooting something or surviving a set amount of time.', 0, (255, 255, 255))
        win.blit(text,(70,150))
        text = font.render('press space to return', 0, (255, 0, 0))
        win.blit(text,(250,500))
        pygame.display.update()


    if difficultmenu == True:
        pygame.time.delay(100)
        y1 += 26  #stars movements
        if y1 >= 800:
            y1 = 0
            x1 = random.randint(10, 690)
        y2 += 30
        if y2 >= 800:
            y2 = 0
            x2 = random.randint(10, 690)
        y3 += 15
        if y3 >= 800:
            y3 = 0
            x3 = random.randint(10, 690)

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                update()
            pressed = pygame.mouse.get_pressed()
            if pressed == (True, False,
                           False) and 208 <= mx <= 506 and 57 <= my <= 187:
                maxhp = 99
                mainmeu = True
                difficultmenu = False
            elif pressed == (True, False,
                           False) and 208 <= mx <= 506 and 217 <= my <= 346:
                maxhp = 49
                mainmeu = True
                difficultmenu = False
            elif pressed == (True, False,
                           False) and 208 <= mx <= 506 and 379 <= my <= 491:
                maxhp = 1
                mainmeu = True
                difficultmenu = False
            elif pressed == (True, False,
                           False) and 208 <= mx <= 536 and 484 <= my <= 680:
                howtoplay = True
            elif pressed == (True, False,
                           False) and 600 <= mx and 600 <= my:
                openscreen = True
                difficultmenu = False
                
                
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
        pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
        pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
        for i in range(4):
            win.blit(difficulties[i], (206, 160 * i))
        font = pygame.font.Font('freesansbold.ttf', 43)
        text = font.render('How to play', 0, (0, 0, 0))
        win.blit(text,(230,590))
        win.blit(backbutton,(600,600))
        win.blit(mouse, (mx - 32, my - 32))
        pygame.display.update()


    if mainmeu == True:#level select
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        pygame.time.delay(100)
        y1 += 26  #stars movements
        if y1 >= 800:
            y1 = 0
            x1 = random.randint(10, 690)
        y2 += 30
        if y2 >= 800:
            y2 = 0
            x2 = random.randint(10, 690)
        y3 += 15
        if y3 >= 800:
            y3 = 0
            x3 = random.randint(10, 690)
        #mouse location tracking and click detect
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                update()
            pressed = pygame.mouse.get_pressed()
            #pressing levels
            if pressed == (True, False,
                           False) and 206 <= mx <= 506 and 164 <= my <= 281:
                mainmeu = False
                firstbossintro = True
            elif pressed == (True, False,
                           False) and 206 <= mx <= 506 and 324 <= my <= 441:
                mainmeu = False
                secondbossintro = True
            elif pressed == (True, False,
                           False) and 206 <= mx <= 506 and 484 <= my <= 601:
                thirdbossintro = True
                mainmeu = False
            elif pressed == (True, False,
                           False) and 600 <= mx and 600 <= my:
                mainmeu = False
                difficultmenu = True
                
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
        pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
        pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
        win.blit(backbutton,(600,600))
        for i in range(3):#levels
            win.blit(level[i], (206, 160 * i + 100))
        win.blit(mouse, (mx - 32, my - 32))
        pygame.display.update()

    if firstbossintro == True:
        #dialoge variabws
        speechcount = 0
        speechinterval = 0
        while firstbossintro == True:
            pygame.time.delay(100)
            y1 += 26  #stars movements
            if y1 >= 800:
                y1 = 0
                x1 = random.randint(10, 690)
                y2 += 30
            if y2 >= 800:
                y2 = 0
                x2 = random.randint(10, 690)
            y3 += 15
            if y3 >= 800:
                y3 = 0
                x3 = random.randint(10, 690)
            #dialoge
            speechinterval += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()#detect space press
            if keys[pygame.K_SPACE] and speechinterval >= 3 or speechinterval == 500:
                speechcount += 1
                speechinterval = 0
            win.fill((0, 0, 0))
            pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
            pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
            pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))

            win.blit(shipstill, (x, y))
            text = font.render('', 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (170, 600)
            pygame.draw.rect(win, (130, 135, 136), (0, 534, 700, 700))
            #speech
            if speechcount == 0:
                text = font.render('press space to Continue', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
            elif speechcount == 1:
                text = font.render('Base to scout, you have incoming.', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[0], (0, 540))
            elif speechcount == 2:
                text = font.render('Radar said its damaged so, kill it. ', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[0], (0, 540))
            elif speechcount == 3:
                text = font.render('Try to not get hurt out there.', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[1], (0, 540))
            elif speechcount == 4:
                text = font.render('ORGANICS WE ARE LEAVING!', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            elif speechcount == 5:
                text = font.render('NOW!', 1, (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            elif speechcount == 6:
                text = font.render('SHUT UP METAL HEAD!', 1, (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[1], (0, 540))
            elif speechcount == 7:
                text = font.render('We have to go.', 1, (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[0], (0, 540))
            elif speechcount == 8:
                text = font.render('Scout stay safe an-', 1, (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[1], (0, 540))
            elif speechcount == 9:
                text = font.render('and report back to base', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[0], (0, 540))
            elif speechcount == 10:
                text = font.render('MOVE IT ALREADY!', 1, (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            else:
                firstbossintro = False
            pygame.display.update()
        firstboss = True
        #settinge up player pos
        x = 334
        y = 334

    while firstboss == True:
        sound()
        #setting up variables
        charge = False
        saucerx = -400
        saucery = 0
        bosshp = 0
        damagemulti = 2
        hitx = x - 40  #ship centre x
        hity = y - 30  #ship centre y
        saucermove = True
        iframe = True  #invunrable frames so the bullets cant do more than 10 damage
        iframetime = 10
        starx = [350, 350, 400]
        stary = [350, 350, 400]
        width = 64
        height = 64
        vel = 7  # speed
        shoot = False
        run = True
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        #saucer bullets
        bulletx = 400  #
        bullety = -50
        bulletx1 = 400
        bullety1 = -50
        bulletx2 = 400
        bullety2 = -50
        bulspd = 1
        firingx = hitx + 40
        firingy = hity + 30
        sheild = 1000
        hp = maxhp
        X = size
        Y = size
        spd = 2
        xlaser = 900
        xlasercharge = 0
        ylaser = 900
        ylasercharge = 0
        introcount = 0  #dont change
        chargemulti = 1
        lasermove = 0
        #hp = 9999999#testing
        display_surface = pygame.display.set_mode((X, Y))
        font = pygame.font.Font('freesansbold.ttf', 20)
        # infinite loop
        xlazarbeam = False
        sheild_on = False
        bosshit = False
        intro = True
        phase2 = False
        while run:
            if hp <= 0:
                run = False
                die = True
            pygame.time.delay(100)
            if sheild < 1000:
                sheild += 2
            if bosshp <= 500 and intro == False:
                phase2 = True  # initiates phase2
            if phase2 == True:
                bulspd = 1.25
                chargemulti = 3
                damagemulti = 2
            if intro == True:
                bosshp += 25  #/2#for testing
                introcount += 1
            if introcount == 40:
                intro = False
            sametime = False
            hit = False
            if bosshp <= 850 and ylasercharge == 0 and intro == False:  #laser code
                ylaser = random.randint(200, 540)  #random genaration
                ylasercharge += chargemulti
            elif bosshp <= 850 and ylasercharge <= 100:  #charging
                ylasercharge += chargemulti
            elif ylasercharge >= 100 and ylasercharge < 150:  #firing
                ylasercharge += chargemulti
                if hity >= ylaser and hity <= ylaser + 160 and sheild_on == False:
                    hp -= 2
                    hit = True
            elif ylasercharge >= 150:  #reseting laser
                ylasercharge = 0
                if hity >= ylaser and hity <= ylaser + 160 and sheild_on == False:
                    hp -= 2
                    hit = True

            #phase 2
            if phase2 == True and xlasercharge == 0:  #laser code
                xlaser = random.randint(200, 540)  #random genaration
                xlasercharge += 1
            elif phase2 == True and xlasercharge <= 100:  #charging
                xlasercharge += 1
            elif xlasercharge >= 100 and xlasercharge < 130:  #firing
                xlasercharge += 1
                if hitx >= xlaser + 60 and hitx <= xlaser + 120 and sheild_on == False:
                    hp -= 4
                    hit = True
            elif xlasercharge >= 130:  #reseting laser
                if hitx >= xlaser + 60 and hitx <= xlaser + 120 and sheild_on == False:
                    hp -= 2
                    hit = True
                xlasercharge = 0
            if xlaser + 120 < x:
                xlaser += 2.5
            else:
                xlaser -= 2.5
            #hitboxes
            hitshootx1 = bulletx1 + 110  #dont change
            hitshooty1 = bullety1 + 110  #dont change
            hitshootx2 = bulletx2 + 110  #dont change
            hitshooty2 = bullety2 + 110  #dont change
            hitshootx = bulletx + 110  #dont change
            hitshooty = bullety + 110  #dont change
            y1 += 26  #stars movements
            if y1 >= 800:
                y1 = 0
                x1 = random.randint(10, 690)
            y2 += 30
            if y2 >= 800:
                y2 = 0
                x2 = random.randint(10, 690)
            y3 += 15
            if y3 >= 800:
                y3 = 0
                x3 = random.randint(10, 690)
            if bullety >= 800:  #bullet moving and shooting
                bullety = 0
                bulletx = random.randint(40, 600)
                bullety1 = 0
                bulletx1 = random.randint(40, 600)
                sametime = True
            if bosshp >= 800:
                bullety2 = 900
            elif bullety2 >= 800 and sametime == True:  #bullet moving and shooting
                bullety2 = 0
                bulletx2 = random.randint(40, 600)
            #bullet speeds
            bullety += 20 * bulspd
            bullety1 += 20 * bulspd
            bullety2 += 20 * bulspd
            if hitx <= hitshootx and hitx + 40 >= hitshootx and hity <= hitshooty and hity + 40 >= hitshooty and iframe == False and sheild_on == False or hitx <= hitshootx1 and hitx + 40 >= hitshootx1 and hity <= hitshooty1 and hity + 40 >= hitshooty1 and iframe == False and sheild_on == False or hitx <= hitshootx2 and hitx + 40 >= hitshootx2 and hity <= hitshooty2 and hity + 40 >= hitshooty2 and iframe == False and sheild_on == False:  #bullet hitbox
                hp -= 10
                hit = True
                iframe = True
                iframetime = 10
            if iframe == True:
                iframetime -= 1
                if iframetime == 0:
                    iframe = False
            if saucerx >= 150 and saucermove == True:
                saucerx -= 5
            elif saucerx <= 350:
                saucerx += 5
                saucermove = False
            else:
                saucermove = True

            if sauceranimation + 1 >= 7:
                sauceranimation = 0
            sauceranimation += 1
            if y <= 170:
                hp -= 1
            Fowards = False
            Backwards = False
            if firingx >= saucerx and firingx <= saucerx + 224 and firingy <= 250 and bosshit == False:
                Bosshit = True
                bosshp -= damagemulti
            if firingy <= -10:
                Bosshit = False
                firingy = hity + 40
                firingx = hitx + 30
            firingy -= 30
            text = font.render("HP: {0}".format(hp), 1,
                               (255, 9, 12))  #hp variables dont change
            textRect = text.get_rect()
            textRect.center = (35, 690)  #YOUR HP LOCATION
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()  #inputs working
            if keys[pygame.K_RIGHT] and x < 636:
                x += vel
            if keys[pygame.K_LEFT] and x > 0:
                x -= vel
            if keys[pygame.K_DOWN] and y < 636:
                y += vel
                Backwards = True
            if keys[pygame.K_UP] and y > 30:
                y -= vel
                Fowards = True
            if keys[pygame.K_SPACE] and intro == False and sheild >= 220 and sheild_on == False:
                sheild -= 200
                sheild_on = True
            elif keys[pygame.K_SPACE] and sheild >= 20 and sheild_on == True:
                sheild -= 20
            else:
                sheild_on = False
            win.fill((0, 0, 0))  #drawing and images starts
            pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
            pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
            pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
            #pygame.draw.rect(win,(255,255,255),(saucerx,saucery,3,40))#testing
            overlap = False
            xlazarbeam = False
            ylazarbeam = False
            lasermove += 1
            if lasermove >= 4:
                lasermove = 0
            if ylasercharge >= xlasercharge:
                if xlasercharge <= 98:
                    pygame.draw.rect(win, (0, xlasercharge * 2, 0),
                                     (xlaser + 128, 0, 60, 700))  #testing
                else:
                    xlazarbeam = True
            else:
                overlap = True
            if ylasercharge <= 98:
                pygame.draw.rect(win, (0, ylasercharge * 2, 0),
                                 (0, ylaser + 80, 700, 140))  #testing
            else:
                ylazarbeam = True
            if overlap == True:
                if xlasercharge <= 98:
                    pygame.draw.rect(win, (0, xlasercharge * 2, 0),
                                     (xlaser + 128, 0, 60, 700))  #testing
                else:
                    xlazarbeam = True
            if ylazarbeam == True:
                for i in range(6):
                    win.blit(ylaseranimation[lasermove],
                             (i * 160 - 160, ylaser + 90))
            #xlaser
            if xlazarbeam == True:
                for i in range(6):
                    win.blit(xlaseranimation[lasermove],
                             (xlaser + 90, i * 160 - 160))
            #pygame.draw.rect(win,(255,0,0),(hitshootx,hitshooty,40,40))# testing square

            win.blit(firing[sauceranimation], (firingx, firingy))
            win.blit(bullet[sauceranimation], (bulletx, bullety))
            win.blit(bullet[sauceranimation], (bulletx2, bullety2))
            win.blit(bullet[sauceranimation],
                     (bulletx1, bullety1))  #bullet aimation
            if phase2 == True:
                win.blit(damagedsaucer[sauceranimation], (saucerx, saucery))
            else:
                win.blit(undamagedsaucer[sauceranimation],
                         (saucerx, saucery))  #saucer animation
            #pygame.draw.rect(win,(255,0,0),(x,y,40,40))# testing square
            if Fowards == True:  #ship animations
                win.blit(shipfowards, (x, y))
            elif Backwards == True:
                win.blit(shipback, (x, y))
            else:
                win.blit(shipstill, (x, y))
            if sheild_on == True:
                win.blit(shipsheild, (x, y))
            if hit == True:  #RED getting hit animation
                win.blit(shiphit, (x, y))
            pygame.draw.rect(win, (0, 0, 255), (2, 675, sheild / 15, 32))

            display_surface.blit(text, textRect)
            pygame.draw.rect(win, (202, 204, 208),
                             (98, 38, 504, 36))  #bosshp backround
            pygame.draw.rect(win, (255, 0, 0),
                             (100, 40, bosshp // 2, 32))  # boss hp bar
            win.blit(b, (300, 40))
            win.blit(o, (320, 40))
            win.blit(s, (350, 40))
            win.blit(s, (380, 40))
            pygame.display.update()
            hitx = x - 40  #ship centre x
            hity = y - 36  #ship centre y
            if bosshp <= 0:
                firstbossoutro = True
                run = False
                firstboss = False
        if die == True:  #retry loop
            run = False
            font = pygame.font.Font('freesansbold.ttf', 50)
            text = font.render('press space to retry', 0, (255, 0, 0))
            win.blit(text, (120, 320))
            text = font.render('YOU DIED', 0, (255, 0, 0))
            win.blit(text, (220, 240))
            text = font.render('click to return to main menu.', 0, (255, 0, 0))
            win.blit(text, (25, 380))
            pygame.display.update()
            retry = False
            time.sleep(1)
            while retry == False:  #when space pressed loops
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    pressed = pygame.mouse.get_pressed()
                    if keys[pygame.K_SPACE] and retry == False:
                        retry = True
                        run = True
                        die = False
                        hp = maxhp
                        x = 328
                        y = 328
                    if pressed == (True,False,False):
                        mainmeu = True
                        firstboss = False
                        run = True
                        retry = True
                        die = False
                        hp = maxhp
                        x = 328
                        y = 328
                    pygame.time.delay(40)
    if firstbossoutro == True:
          i = 0
          for i in range(9):
            sound()
            pygame.time.delay(100)
            win.fill((0, 0, 0))
            time.sleep(.3)
            if i <= 4:
               win.blit(damagedsaucer[3],(saucerx,saucery))
            win.blit(explotion[i-1],(saucerx-40,saucery-40))
            win.blit(shipback, (x, y))
            pygame.display.update()
          text = font.render('', 1, (255, 255, 255))
          textRect = text.get_rect()
          textRect.center = (170, 600)
          pygame.draw.rect(win, (130, 135, 136), (0, 534, 700, 700))
          text = font.render('Target destroyed!', 1,
                                   (255, 255, 255))
          win.blit(text, textRect)
          win.blit(characters[2], (0, 540))
          pygame.display.update()
          for i in range(10):
            sound()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.time.delay(100)
            win.blit(winscene[i],(50,50))
            pygame.display.update()
          time.sleep(3)
          sound()
          mainmeu = True
          firstbossoutro = False
    if secondbossintro == True:
        largeshipintro = False
        increase = 0
        shipbackroundloop = 0
        speechcount = 0
        speechinterval = 0
        x = 334
        y = 334
        while secondbossintro == True:
            sound()
            pygame.time.delay(100)
            y1 += 26  #stars movements
            if y1 >= 800:
                y1 = 0
                x1 = random.randint(10, 690)
            y2 += 30
            if y2 >= 800:
                y2 = 0
                x2 = random.randint(10, 690)
            y3 += 15
            if y3 >= 800:
                y3 = 0
                x3 = random.randint(10, 690)

            speechinterval += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.
                    K_SPACE] and speechinterval >= 3 or speechinterval == 500:
                speechcount += 1
                speechinterval = 0
            win.fill((0, 0, 0))
            text = font.render('', 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (170, 600)
            sound()
            if largeshipintro == False:
              pygame.draw.rect(win, (130, 135, 136), (0, 534, 700, 700))
            shipbackroundloop +=1
            if shipbackroundloop ==4:
                shipbackroundloop = 0
            if speechcount == 0:
                text = font.render('press space to Continue', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
            elif speechcount == 1:
                text = font.render('I will go over the plan', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                text = font.render('one more time. ', 1,
                                   (255, 255, 255))
                win.blit(text, (170,650))
                win.blit(characters[0], (0, 540))
            elif speechcount == 2:
                text = font.render('Get to the centre and use ', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                text = font.render('the missiles you were given.', 1,
                                   (255, 255, 255))
                win.blit(text, (170,650))
                win.blit(characters[0], (0, 540))
            elif speechcount == 3:
                text = font.render("Then it will overload the ship's", 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                text = font.render('genarators.', 1,
                                   (255, 255, 255))
                win.blit(text, (170,650))
                win.blit(characters[2], (0, 540))
            elif speechcount == 4:
                text = font.render('Then?', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[1], (0, 540))
            elif speechcount == 5:
                text = font.render('BOOM!', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[0], (0, 540))
            elif speechcount == 6:
                text = font.render('Boom indeed, that would cause a', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
                text = font.render('devisting explotion.', 1,
                                   (255, 255, 255))
                win.blit(text, (170,650))
            elif speechcount == 7:
                text = font.render('How will that not kill us?', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[1], (0, 540))
            elif speechcount == 8:
                text = font.render('I will think of somthing.', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[0], (0, 540))
            elif speechcount == 9:
                speechcount +=1
                largeshipintro = True
            elif largeshipintro == True:
                increase +=70
                win.blit(shipbackround[shipbackroundloop],(0,increase-700))
                if increase == 700:
                    largeshipintro = False
            else:
                win.blit(shipbackround[shipbackroundloop],(0,increase-700))
                secondbossintro = False
                secondboss = True
            pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
            pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
            pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
            win.blit(shipstill, (x, y))
            pygame.display.update()
    if secondboss == True:
       
       #seting up variables
       hp = maxhp
       vel = 10
       x = 334
       y = 334
       xlaser = 0
       xlasercharge = 0
       lxlasercharge = 0
       lxlaser = 0
       llxlasercharge = 0
       llxlaser = 0
       bombfuze = 0
       bomby = 0
       bombx = 0
       bombfuze2 = 0
       bomby2 = 0
       bombx2 = 0
       sheild = 1000
       run = True
       leveltime = 0

       while run == True:
        sound()
        #setting up variable
        shipbackroundloop +=1
        leveltime +=0.5
        if shipbackroundloop ==4:
          shipbackroundloop = 0
        Fowards = False
        Backwards = False
        hit = False
        if y <= 660:
          y += 5
        else:
          hp -=1 
          hit = True
       
        win.fill((0, 0, 0))
        pygame.time.delay(100)
        win.blit(shipbackround[shipbackroundloop],(0,0))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("HP: {0}".format(hp), 1,(255, 9, 12)) #hp variables dont change
        pygame.draw.rect(win, (0, 0, 255), (2, 675, sheild / 15, 32))
        textRect = text.get_rect()
        textRect.center = (35, 690)  #YOUR HP LOCATION
        win.blit(text, textRect)
        text = font.render("Survive", 1,(0, 0, 0))
        textRect.center = (360,50 )
        for event in pygame.event.get():#so everything works
          if event.type == pygame.QUIT:
            run = False
        hitx = x + 40  #ship centre x
        hity = y + 36  #ship centre y
        keys = pygame.key.get_pressed()  #inputs working
        if keys[pygame.K_RIGHT] and x < 636:
          x += vel
        if keys[pygame.K_LEFT] and x > 0:
          x -= vel
        if keys[pygame.K_DOWN] and y < 636:
          y += vel
          Backwards = True
        if keys[pygame.K_UP] and y > 64:
          y -= vel
          Fowards = True
        #sheild inputs
        if keys[pygame.K_SPACE] and sheild >= 220 and sheild_on == False:
          sheild -= 200
          sheild_on = True
        elif keys[pygame.K_SPACE] and sheild >= 20 and sheild_on == True:
            sheild -= 20
        else:
          sheild_on = False
        if xlasercharge == 0:  #laser code
          xlaser = hitx - 80 #tracking
          xlasercharge += 1
          win.blit(lasergun[0],(xlaser,40))
        elif xlasercharge <= 5:  #charging
                xlasercharge += 1
                win.blit(lasergun[0],(xlaser,40))
        elif xlasercharge <= 10:  #charging
                xlasercharge += 1
                win.blit(lasergun[1],(xlaser,40))
        elif xlasercharge <= 15:  #charging
                xlasercharge += 1
                win.blit(lasergun[2],(xlaser,40))
        elif xlasercharge <= 20:  #charging
                xlasercharge += 1
                win.blit(lasergun[3],(xlaser,40))
        elif xlasercharge >= 20 and xlasercharge < 30:  #firing
                for i in range(4):
                    win.blit(bluelaser[shipbackroundloop],
                             (xlaser, i * 160+160))
                win.blit(lasergun[4],(xlaser,40))
                xlasercharge += 1
                if hitx > xlaser +55 and hitx <= xlaser + 110 and sheild_on == False:
                    hp -= 2
                    hit = True
        elif xlasercharge >= 30:  #reseting laser
          xlasercharge = 0
        if leveltime <= 100:#slight speed up + activates late
           vel += 0.01
        elif lxlasercharge == 0:  #laser code
           lxlaser = hitx - 80 + random.randint(-200,200) #random shot
           lxlasercharge +=1.1
           win.blit(lasergun[0],(lxlaser,40))
        elif lxlasercharge <= 5:  #charging
                lxlasercharge += 1.1
                win.blit(lasergun[0],(lxlaser,40))
        elif lxlasercharge <= 10:  #charging
                lxlasercharge += 1.1
                win.blit(lasergun[1],(lxlaser,40))
        elif lxlasercharge <= 15:  #charging
                lxlasercharge += 1.1
                win.blit(lasergun[2],(lxlaser,40))
        elif lxlasercharge <= 20:  #charging
                lxlasercharge += 1.1
                win.blit(lasergun[3],(lxlaser,40))
        elif lxlasercharge >= 20 and lxlasercharge < 30:  #firing
                for i in range(4):#drawinglaser
                    win.blit(bluelaser[shipbackroundloop],
                             (lxlaser, i * 160+160))
                win.blit(lasergun[4],(lxlaser,40))
                lxlasercharge += 1
                if hitx > lxlaser +55 and hitx <= lxlaser + 110 and sheild_on == False:
                    hp -= 2
                    hit = True
        elif lxlasercharge >= 30:  #reseting laser
          lxlasercharge = 0
        if leveltime <= 200:#slight speed up + activates late
           vel += 0.005
        elif llxlasercharge == 0:  #laser code
           if lxlaser >= xlaser:
             llxlaser = hitx - 80 + random.randint(20,200) #random shot
           else:
             llxlaser = hitx - 80 + random.randint(-200,-20) #random shot
           llxlasercharge +=1.5
           win.blit(lasergun[0],(llxlaser,40))
        elif llxlasercharge <= 5:  #charging
                llxlasercharge += 1.1
                win.blit(lasergun[0],(llxlaser,40))
        elif llxlasercharge <= 10:  #charging
                llxlasercharge += 1.1
                win.blit(lasergun[1],(llxlaser,40))
        elif llxlasercharge <= 15:  #charging
                llxlasercharge += 1.1
                win.blit(lasergun[2],(llxlaser,40))
        elif llxlasercharge <= 20:  #charging
                llxlasercharge += 1.1
                win.blit(lasergun[3],(llxlaser,40))
        elif llxlasercharge >= 20 and llxlasercharge < 30:  #firing
                for i in range(4):#drawinglaser
                    win.blit(bluelaser[shipbackroundloop],
                             (llxlaser, i * 160+160))
                win.blit(lasergun[4],(llxlaser,40))
                llxlasercharge += 1
                if hitx > llxlaser +55 and hitx <= llxlaser + 110 and sheild_on == False:
                    hp -= 2
                    hit = True
        elif llxlasercharge >= 30:  #reseting laser
          llxlasercharge = 0
        left = random.randint(0,1)
        #bombs
        
        if leveltime <= 250:#slight speed up + activates late
           vel += 0.0025
        elif bombfuze == 0:  #bomb code
          if left == 1:
            bombx = -40
          else:
              bombx = 740
          bomby = random.randint(40,660)
          bombwantx = random.randint(160,550)#bombmoveto location
          bombwanty = random.randint(160,550)
          bombfuze +=1
          win.blit(bluebomb[0],(bombx,bomby))
        elif bombfuze <= 5:  #charging
                if bombwantx >= bombx:#bombmoving code
                    bombx += bombwantx/20
                else:
                    bombx -= bombwantx/20
                if bombwanty >= bomby:
                    bomby += bombwanty/20
                else:
                    bomby -= bombwanty/20
                bombfuze += 1
                win.blit(bluebomb[0],(bombx ,bomby))
        elif bombfuze <= 10:  #charging
                if bombwantx >= bombx:
                    bombx += bombwantx/20
                else:
                    bombx -= bombwantx/20
                if bombwanty >= bomby:
                    bomby += bombwanty/20
                else:
                    bomby -= bombwanty/20
                bombfuze += 1.
                win.blit(bluebomb[1],(bombx,bomby))
        elif bombfuze < 21:  #charging
                if bombwantx >= bombx:
                    bombx += bombwantx/20
                else:
                    bombx -= bombwantx/20
                if bombwanty >= bomby:
                    bomby += bombwanty/20
                else:
                    bomby -= bombwanty/20
                bombfuze += 1.
                win.blit(bluebomb[2],(bombx,bomby))
        elif bombfuze >= 21 and bombfuze < 22:  #firing
                for i in range(6):#drawinglaser
                    win.blit(blueexplotionlaser[1],
                             (bombx, i * 160-160))
                for i in range(6):#drawinglaser
                    win.blit(blueexplotionlaser[0],
                             ( i * 160-160, bomby))
                bombfuze += 1
                win.blit(bluebomb[3],(bombx,bomby))
                if hitx > bombx  +144 and hitx <= bombx + 184 and sheild_on == False:#working dont change
                    hp -= 22
                    hit = True
                if hity > bomby  +144 and hity <= bomby + 184 and sheild_on == False:#working dont change
                    hp -= 22
                    hit = True
        elif bombfuze >= 22:  #reseting bomb
          bombfuze = 0

        #bomb2

        if leveltime <= 320:#slight speed up + activates late
           vel += 0.0025
        elif bombfuze2 == 0:  #bomb code
          if left == 1:
            bombx2 = -40
          else:
              bombx2 = 740
          bomby2 = random.randint(40,660)
          bombwantx2 = random.randint(160,550)#bombmoveto location
          bombwanty2 = random.randint(160,550)
          bombfuze2 +=1
          win.blit(bluebomb[0],(bombx2,bomby2))
        elif bombfuze2 <= 5:  #charging
                if bombwantx2 >= bombx2:#bombmoving code
                    bombx2 += bombwantx2/20
                else:
                    bombx2 -= bombwantx2/20
                if bombwanty2 >= bomby2:
                    bomby2 += bombwanty2/20
                else:
                    bomby2 -= bombwanty2/20
                bombfuze2 += 1
                win.blit(bluebomb[0],(bombx2 ,bomby2))
        elif bombfuze2 <= 10:  #charging
                if bombwantx2 >= bombx2:
                    bombx2 += bombwantx2/20
                else:
                    bombx2 -= bombwantx2/20
                if bombwanty2 >= bomby2:
                    bomby2 += bombwanty2/20
                else:
                    bomby2 -= bombwanty2/20
                bombfuze2 += 1.
                win.blit(bluebomb[1],(bombx2,bomby2))
        elif bombfuze2 < 21:  #charging
                if bombwantx2 >= bombx2:
                    bombx2 += bombwantx2/20
                else:
                    bombx2 -= bombwantx2/20
                if bombwanty2 >= bomby2:
                    bomby2 += bombwanty2/20
                else:
                    bomby2 -= bombwanty2/20
                bombfuze2 += 1.
                win.blit(bluebomb[2],(bombx2,bomby2))
        elif bombfuze2 >= 21 and bombfuze2 < 22:  #firing
                for i in range(6):#drawinglaser
                    win.blit(blueexplotionlaser[1],
                             (bombx2, i * 160-160))
                for i in range(6):#drawinglaser
                    win.blit(blueexplotionlaser[0],
                             ( i * 160-160, bomby2))
                bombfuze2 += 1
                win.blit(bluebomb[3],(bombx2,bomby2))
                if hitx > bombx2  +144 and hitx <= bombx2 + 184 and sheild_on == False:#working dont change
                    hp -= 22
                    hit = True
                if hity > bomby2  +144 and hity <= bomby2 + 184 and sheild_on == False:#working dont change
                    hp -= 22
                    hit = True
        elif bombfuze2 >= 22:  #reseting bomb
          bombfuze2 = 0
        if Fowards == True:  #ship animations
         win.blit(shipfowards, (x, y))
        elif Backwards == True:
          win.blit(shipback, (x, y))
        else:
          win.blit(shipstill, (x, y))
        if sheild_on == True:
          win.blit(shipsheild, (x, y))
        if hit == True:  #RED getting hit animation
          win.blit(shiphit, (x, y))
        if sheild < 1000:
          sheild += 2#sheild recharge
        pygame.draw.rect(win, (202, 204, 208),
                             (118, 38, 464, 36))  #bark backround
        pygame.draw.rect(win, (255, 0, 0),
                             (120, 40,464- leveltime , 32))  #objective bar
        win.blit(text, textRect)#objective name
        pygame.display.update()
        if hp <= 0:
                run = False  #retry
                die = True
        if 464 - leveltime == 0: #next part of level
            run = False
            secondboss = False
            secondbossp2intro = True
    if die == True:  #retry loop
            run = False
            font = pygame.font.Font('freesansbold.ttf', 50)
            text = font.render('press space to retry', 0, (255, 0, 0))
            win.blit(text, (120, 320))
            text = font.render('YOU DIED', 0, (255, 0, 0))
            win.blit(text, (220, 240))
            text = font.render('click to return to main menu.', 0, (255, 0, 0))
            win.blit(text, (25, 380))
            pygame.display.update()
            hp = maxhp
            retry = False
            while retry == False:  #when space pressed loops
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    pressed = pressed = pygame.mouse.get_pressed()
                    if keys[pygame.K_SPACE] and retry == False:
                        retry = True
                        run = True
                        die = False
                        x = 328
                        y = 328
                    pygame.time.delay(40)
                    if pressed == (True,False,False):
                        mainmeu = True
                        secondboss = False
                        run = True
                        retry = True
                        die = False
                        hp = maxhp
                        x = 328
                        y = 328



    if secondbossp2intro == True:#second part cutseen

        largeshipintro = False
        increase = 0
        shipbackroundloop = 0
        speechcount = 0
        speechinterval = 0
        for i in range(30):
          sound()
          win.fill((0,0,0))
          increase +=70
          if i <= 7:
              reactordamage = 0
          else:
              reactordamage = 1
          shipbackroundloop +=1
          if shipbackroundloop == 4:
              shipbackroundloop = 0
          win.blit(shipbackround[shipbackroundloop],(0,0))
          win.blit(reactor[reactordamage],(50,increase-700))
          win.blit(shipstill,(x,y))
          pygame.display.update()
          pygame.time.delay(100)
        i = 0
        increase = 0
        for i in range(10):
          sound()
          win.fill((0,0,0))
          increase +=70
          win.blit(shipbackround[shipbackroundloop],(0,increase))
          win.blit(shipstill, (x, y))
          pygame.display.update()
          pygame.time.delay(100)
        while secondbossp2intro == True:
            sound()
            pygame.time.delay(100)
            y1 += 26  #stars movements
            if y1 >= 800:
                y1 = 0
                x1 = random.randint(10, 690)
            y2 += 30
            if y2 >= 800:
                y2 = 0
                x2 = random.randint(10, 690)
            y3 += 15
            if y3 >= 800:
                y3 = 0
                x3 = random.randint(10, 690)
            pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
            pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
            pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
            speechinterval += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.
                    K_SPACE] and speechinterval >= 3 or speechinterval == 500:
                speechcount += 1
                speechinterval = 0
            win.fill((0, 0, 0)) #drawing starts
            text = font.render('', 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (170, 600)
            if largeshipintro == False:
              pygame.draw.rect(win, (130, 135, 136), (0, 534, 700, 700))
            shipbackroundloop +=1
            if shipbackroundloop ==4: #animation bacround
                shipbackroundloop = 0
            if speechcount == 0:
                text = font.render('press space to Continue', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
            elif speechcount == 1:
                text = font.render('Targets damaged!', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[0], (0, 540))
            elif speechcount == 2:
                text = font.render('Lets regroup and get outta here.', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                text = font.render('Before they explode. ', 1,
                                   (255, 255, 255))
                win.blit(text, (170,650))
                win.blit(characters[0], (0, 540))
            elif speechcount == 3: #seting up variables for cutseen
                speechcount +=1
                largeshipintro = True
                orangeshipx = -32
                orangeshipy = 350
                blueshipx = -32
                blueshipy = 250
                greenshipx = 732
                greenshipy = 350
                increase = -350
            elif largeshipintro == True: #freindly ships and destroyer emerges
                blueshipx += 7
                greenshipx -= 5
                orangeshipx += 5
                increase -=7
                speechcount = 4
                win.blit(orangeship[0],(orangeshipx,orangeshipy))
                win.blit(blueship[0],(blueshipx,blueshipy))
                win.blit(greenship[0],(greenshipx,greenshipy))
                win.blit(destroyer[shipbackroundloop],(0,increase+700))
                if increase == -700:
                    largeshipintro = False

                    #more dialoge
            elif speechcount == 4:
                win.blit(orangeship[0],(orangeshipx,orangeshipy))
                win.blit(blueship[0],(blueshipx,blueshipy))
                win.blit(greenship[0],(greenshipx,greenshipy))
                win.blit(destroyer[shipbackroundloop],(0,increase+700))
                text = font.render('what is that!', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[1], (0, 540))
            elif speechcount == 5:
                win.blit(orangeship[0],(orangeshipx,orangeshipy))
                win.blit(blueship[0],(blueshipx,blueshipy))
                win.blit(greenship[0],(greenshipx,greenshipy))
                win.blit(destroyer[shipbackroundloop],(0,increase+700))
                text = font.render('Lets move!', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[0], (0, 540))
            else:
                win.blit(orangeship[0],(orangeshipx,orangeshipy))
                win.blit(blueship[0],(blueshipx,blueshipy))
                win.blit(greenship[0],(greenshipx,greenshipy))
                win.blit(destroyer[shipbackroundloop],(0,increase+700))
                time.sleep(0.5)
                secondbossp2intro = False
                secondbossp2 = True
                run = True
            win.blit(shipstill, (x, y))
            pygame.display.update()



    if secondbossp2 == True: #part 2 off level 2
        randomastroid = 0 #usd to randomised the astroid
        autoscrollspeed = 3 #how fast the level moves
        astroidx = random.randint(150,300)
        astroidy = -256#start pos.
        timer = 0 #level last time
        #missile varaiables
        missileshoot = False
        missile = False
        missly = 700
        misslx = 350
        #laser variables
        lasershoot = False
        ylaser = 0
        ylasercharge = 0
        #movement varibles
        bright = random.randint(456,632)
        gright = random.randint(456,632)
        oright = random.randint(456,632)
        bleft = random.randint(200,445)
        gleft = random.randint(200,445)
        oleft = random.randint(200,445)
        gdistance = 6
        bdistance = 5
        odistance = 10
        frontofrock = True
        #sheild and hp variables
        heal = False
        vel = 10
        sheild = 1000
        hit = False
        Fowards = False
        Backwards = False
        sheild_on = False

        while run == True:
            sound()
            if hp <= 0:
                run = False  #retry
                die = True
            #hitbox for player
            hitx = x + 30
            hity = y + 40
            #for animation
            Fowards = False
            Backwards = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render("HP: {0}".format(hp), 1, (255, 9, 12))  #hp variables dont change
            textRect = text.get_rect()
            textRect.center = (35, 690)  #YOUR HP LOCATION
            y += autoscrollspeed
            keys = pygame.key.get_pressed()  #inputs working for movment
            if keys[pygame.K_RIGHT] and x < 636:
                x += vel
            if keys[pygame.K_LEFT] and x > 0:
                x -= vel
            if keys[pygame.K_DOWN] and y < 636:
                y += vel
                Backwards = True
            if keys[pygame.K_UP] and y > 30:
                y -= vel
                Fowards = True
            if keys[pygame.
                    K_SPACE] and sheild >= 220 and sheild_on == False: #sheild start
                sheild -= 200
                sheild_on = True
            elif keys[pygame.K_SPACE] and sheild >= 20 and sheild_on == True:#sheild working
                sheild -= 20
            else:
                sheild_on = False
                if sheild < 1000:
                  sheild += 2
            #timer to increase speed
            timer += 1
            if timer == 100:
                timer = 0
                autoscrollspeed += 1
            win.fill((0,0,0))
            pygame.time.delay(100)
            y1 += 10*autoscrollspeed  #stars movements
            if y1 >= 800:
                y1 = 0
                x1 = random.randint(10, 690)
            y2 += 8*autoscrollspeed
            if y2 >= 800:
                y2 = 0
                x2 = random.randint(10, 690)
            y3 += 7*autoscrollspeed
            if y3 >= 800:
                y3 = 0
                x3 = random.randint(10, 690)
            pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
            pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
            pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
 
            #makes ships feel like they are moving
            orangeshipy += autoscrollspeed
            blueshipy += autoscrollspeed
            greenshipy += autoscrollspeed
            #orange
            if orangeshipy >= random.randint(350,550):
                odistance += random.randint(20,20*autoscrollspeed)
            if odistance >= 0:
                odistance -=1
                orangeshipy -= 10
                win.blit(orangeship[2],(orangeshipx,orangeshipy))
            elif orangeshipy >= 600:
                odistance = 0
            else:
                win.blit(orangeship[0],(orangeshipx,orangeshipy))
            if lasershoot == True and orangeshipx >= ylaser+37 and orangeshipx <= ylaser + 80:
                win.blit(orangeship[3],(orangeshipx,orangeshipy))
            #blue
            if blueshipy >= random.randint(350,550):
                bdistance += random.randint(20,10*autoscrollspeed)
            if bdistance >= 0:
                bdistance -=1
                blueshipy -= 10
                win.blit(blueship[1],(blueshipx,blueshipy))
            elif blueshipy >= 600:
                bdistance = 0
            else:
                win.blit(blueship[0],(blueshipx,blueshipy))
            if lasershoot == True and blueshipx >= ylaser+37 and blueshipx <= ylaser + 80:
                win.blit(blueship[4],(blueshipx,blueshipy))
            if missileshoot == True:
                win.blit(blueship[3],(blueshipx,blueshipy))
            #green
            
            if greenshipy >= random.randint(350,550):
                gdistance += random.randint(20,20*autoscrollspeed)
            if gdistance >= 0:
                gdistance -=1
                greenshipy -= 10
                win.blit(greenship[4],(greenshipx,greenshipy))
            elif greenshipy >= 600:
                gdistance = 0
            else:
                 win.blit(greenship[3],(greenshipx,greenshipy))
            if lasershoot == True and greenshipx >= ylaser+37 and greenshipx <= ylaser + 80:
                win.blit(greenship[5],(greenshipx,greenshipy))
            if timer == 0:#healing
                heal = True
                hp += 10
                win.blit(greenship[1],(greenshipx,greenshipy))
            elif heal == True:
                heal = False
                win.blit(greenship[2],(greenshipx,greenshipy))
            if hp > maxhp: #cant increase hp over max
                hp = maxhp
            
            
            if Fowards == True:  #ship animations
                win.blit(shipfowards, (x, y))
            elif Backwards == True:
                win.blit(shipback, (x, y))
            else:
                win.blit(shipstill, (x, y))
            if sheild_on == True:
                win.blit(shipsheild, (x, y))
            if hit == True:  #RED getting hit animation
                win.blit(shiphit, (x, y))
            hit = False
            shipbackroundloop += 1
            if shipbackroundloop == 4:
                shipbackroundloop = 0

            #astroid
            astroidy += autoscrollspeed*2.5 #falling
            if astroidy >= 700: #reset loop
                astroidy = -256
                astroidx = random.randint(10,434) # change location
                randomastroid = random.randint(0,6) #change imagw
            win.blit(astroids[randomastroid],(astroidx,astroidy))
            if hitx >= astroidx and hitx <= astroidx + 256 and hity >= astroidy -10 and hity <= astroidy + 240:#getting hit by rock
                hit = True
                hp -= 50
            #blueship movent away from rock
            if blueshipx >= astroidx + 128 and blueshipx < 599 and astroidy < blueshipy and blueshipy < astroidy + 500:#right
                blueshipx +=10
                bleft = random.randint(300,345)
            elif  blueshipx <= astroidx + 128 and blueshipx > 0 and astroidy < blueshipy and blueshipy < astroidy + 500:#left
                blueshipx -=10
                bright = random.randint(356,400)
            elif blueshipx < bleft:#recenting
                blueshipx += 10
            elif blueshipx > bright:#recenting
                blueshipx -= 10
            #greenship movent away from rock
            if greenshipx >= astroidx + 128 and greenshipx < 599 and astroidy < greenshipy and greenshipy < astroidy + 500:#right
                greenshipx +=10
                gleft = random.randint(300,345)
            elif  greenshipx <= astroidx + 128 and greenshipx > 0 and astroidy < greenshipy and greenshipy < astroidy + 500:#left
               greenshipx -=10
               gright = random.randint(356,400)
            elif greenshipx < gleft:#recenting
                greenshipx += 10
            elif greenshipx > gright:#recenting
                greenshipx -= 10
            #orangeship
            if orangeshipx >= astroidx + 128 and orangeshipx < 599 and astroidy < orangeshipy and orangeshipy < astroidy + 500:
                orangeshipx +=10
                oleft = random.randint(300,345)
            elif  orangeshipx <= astroidx + 128 and orangeshipx > 0 and astroidy < orangeshipy and orangeshipy < astroidy + 500:
               orangeshipx -=10
               oright = random.randint(356,400)
            elif orangeshipx < oleft:
                orangeshipx += 10
            elif orangeshipx > oright:
                orangeshipx -= 10          
            #destroyer
            win.blit(destroyer[shipbackroundloop],(0,0))
            if y >= 577:#getting to close to it kills you
                hp -= 16
                hit = True
            #laser
            lasershoot = False
            if ylasercharge == 0:  #laser code
                ylaser = random.randint(round(x) - 160,round(x) + 100)  #random genaration
                ylasercharge += 1
            elif ylasercharge <= 20:  #charging
                win.blit(lasercannon[round (ylasercharge/4)],(ylaser,584))
                ylasercharge += 1
            elif ylasercharge >= 20 and ylasercharge < 30:  #firing
                for i in range(6):
                 win.blit(bluelaser[random.randint(0,3)],(ylaser-20,i*160-160))
                win.blit(lasercannon[6],(ylaser,584))
                lasershoot = True
                ylasercharge += 1
                if hitx >= ylaser+37 and hitx <= ylaser + 80 and sheild_on == False:
                    hp -= 5
                    hit = True
            else:  #reseting laser
               ylasercharge = 0

            #missile
            if autoscrollspeed >= 3 and missile == False:
                missile = True
                launchtimer = 0
            elif missile == True and launchtimer <= 50:
                missileshoot = False
                launchtimer += 1
                lock_on = 0
            elif lock_on > 6 and missile == True and firsttime == True:
                win.blit(target[2],(x,y))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('Stay near me, a missle is close.', 1,
                                   (255, 255, 255))
                win.blit(text, (170, 600))
                win.blit(characters[0], (0, 540))
                pygame.display.update()
                time.sleep(4)
                firsttime = False
            elif missile == True and lock_on < 20:
                missly = 700
                win.blit(target[round(lock_on/4)],(x,y))
                lock_on +=1
            elif missile == True and lock_on == 20:
                win.blit(missle[random.randint(0,3)],(misslx,missly))
                win.blit(target[5],(x,y))
                misslx = hitx - 64
                lock_on += 1
                missileshoot = True
            elif missile == True and lock_on > 20:
                if misslx + 64 >= hitx:
                    misslx += 1
                else:
                    misslx -=1
                missly -= 100
                if missly >= blueshipy and missly <= blueshipy + 164 and misslx + 80 >= blueshipx and misslx + 56 <= blueshipx + 64 or missly <= -128:
                    launchtimer = -10
                    missile = False
                if missly >= hity and missly <= hity + 164 and misslx + 80 >= hitx and misslx + 56 <= hitx and sheild_on == False:
                     hit = True
                     hp -= 40
                     launchtimer = -10
                     missile = False
                win.blit(missle[random.randint(0,3)],(misslx,missly))
                win.blit(target[5],(x,y))


            #hp and sheild display
            pygame.draw.rect(win, (0, 0, 255), (2, 675, sheild / 15, 32))
            win.blit(text, textRect)
            #healing tutorial
            if heal == True and firstheal == True and hp < maxhp:
                win.blit(target[2],(x,y))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('stay close, I will repear  you.', 1,
                                   (255, 255, 255))
                win.blit(text, (170, 600))
                win.blit(characters[1], (0, 540))
                pygame.display.update()
                time.sleep(4)
                firstheal = False


            pygame.display.update()#update images
            #autoscrollspeed = 9 #temporary
            if autoscrollspeed ==9:#end loop
               run = False
               secondbossp2 = False
               secondbossoutro = True
               mainmeu = False

    if die == True:  #retry loop
            run = False
            font = pygame.font.Font('freesansbold.ttf', 50)
            text = font.render('press space to retry', 0, (255, 0, 0))
            win.blit(text, (120, 320))
            text = font.render('YOU DIED', 0, (255, 0, 0))
            win.blit(text, (220, 240))
            text = font.render('click to return to main menu.', 0, (255, 0, 0))
            win.blit(text, (25, 380))
            pygame.display.update()
            retry = False
            while retry == False:  #when space pressed loops
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    pressed = pressed = pygame.mouse.get_pressed()
                    if keys[pygame.K_SPACE] and retry == False:
                        retry = True
                        run = True
                        die = False
                        x = 328
                        y = 328
                        font = pygame.font.Font('freesansbold.ttf', 20)
                        hp = maxhp
                    
                    elif pressed == (True,False,False):
                        mainmeu = True
                        secondbossp2 = False
                        run = True
                        retry = True
                        die = False
                        hp = maxhp
                        x = 328
                        y = 328
                    pygame.time.delay(40)
    if secondbossoutro == True:
     end = False
     timer = 0
     laser = False
     laser1 ,laser2 = False,False
     while laser == False and end == False:
            sound()
            #orangeship centre
            if orangeshipx > 333:
             orangeshipx -= 10
            elif orangeshipx < 303:
             orangeshipx += 10
            else:
             laser1 = True

            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Incoming.', 1,
                                    (255, 255, 255))
            win.blit(text, (170, 600))
            win.blit(characters[1], (0, 540))
            pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))

            if orangeshipy > 365:
             orangeshipy -= 10
            elif orangeshipy < 335:
             orangeshipy += 10
            else:
             laser2 = True
            if laser1 == True and laser2 == True:
                orangeshipx =318
                orangeshipy = 350
                laser = True
            win.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            win.fill((0,0,0))
            pygame.time.delay(50)
            y1 += 5*autoscrollspeed  #stars movements
            if y1 >= 800:
                y1 = 0
                x1 = random.randint(10, 690)
            y2 += 4*autoscrollspeed
            if y2 >= 800:
                y2 = 0
                x2 = random.randint(10, 690)
            y3 += 3.5*autoscrollspeed
            if y3 >= 800:
                y3 = 0
                x3 = random.randint(10, 690)
            pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
            pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
            pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
            win.blit(orangeship[1],(orangeshipx,orangeshipy))
            win.blit(blueship[0],(blueshipx,blueshipy))
            win.blit(greenship[4],(greenshipx,greenshipy))
            win.blit(shipstill,(x,y))
            #destroyer
            win.blit(destroyer[shipbackroundloop],(0,0))
            shipbackroundloop += 1
            if shipbackroundloop == 4:
                shipbackroundloop = 0
            pygame.display.update()
     roc = -700
     rok = - 700
     destroyery = 0
     while roc <= -100 and end == False:
            win.fill((0,0,0))
            for event in pygame.event.get():
              if event.type == pygame.QUIT:
                run = False
            win.fill((0,0,0))
            pygame.time.delay(50)
            y1 += 5*autoscrollspeed 
            y2 += 3*autoscrollspeed 
            y3 += 4*autoscrollspeed  #starsmovments movements
            if y1 >= 800:
             y1 = 0
             x1 = random.randint(10, 690)
             y2 += 4*autoscrollspeed
            if y2 >= 800:
             y2 = 0
             x2 = random.randint(10, 690)
             y3 += 3.5*autoscrollspeed
            if y3 >= 800:
             y3 = 0
             x3 = random.randint(10, 690)
            #falling down the screen
            if blueshipy < 444:
             blueshipy += 10
            if greenshipy < 390:
             greenshipy += 10
            if y < 500:
             y += 10
            #stars
            pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
            pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
            #ships
            win.blit(orangeship[1],(orangeshipx,orangeshipy))
            win.blit(blueship[0],(blueshipx,blueshipy))
            win.blit(greenship[4],(greenshipx,greenshipy))
            win.blit(shipstill,(x,y))
            #destroyer
            win.blit(destroyer[shipbackroundloop],(0,destroyery))
            shipbackroundloop += 1
            if shipbackroundloop == 4:
               shipbackroundloop = 0
            win.blit(rockp1[0],(0,roc))
            roc += 10
            if roc > -350:
               destroyery += 10
            if roc >= -300:
              #centres you
              if x > 333:
                x -= 10
              elif x < 303:
                x += 10
            #centres greenship
            if greenshipx > 333:
             greenshipx -= 10
            elif greenshipx < 303:
             greenshipx += 10
            #centres blueship
            if blueshipx > 333:
             blueshipx -= 10
            elif blueshipx < 303:
             blueshipx += 10
            pygame.display.update()
            sound()
     time.sleep(0.5)
     sound()
     timer = 0
     while timer <= 160 and end == False:
        if blueshipy < 444:
            blueshipy += 10
        #centres you
        if x > 333:
             x -= 10
        elif x < 303:
             x += 10
        #centres greenship
        if greenshipx > 333:
             greenshipx -= 10
        elif greenshipx < 303:
             greenshipx += 10
        #centres blueship
        if blueshipx > 333:
             blueshipx -= 10
        elif blueshipx < 303:
             blueshipx += 10
        

        timer += 1 #used to count the time until the next loop of code
        win.fill((0,0,0))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        win.fill((0,0,0))
        pygame.time.delay(50)
        y1 += 5*autoscrollspeed  #stars movements
        if y1 >= 800:
            y1 = 0
            x1 = random.randint(10, 690)
        y2 += 4*autoscrollspeed
        if y2 >= 800:
            y2 = 0
            x2 = random.randint(10, 690)
        y3 += 3.5*autoscrollspeed
        if y3 >= 800:
            y3 = 0
            x3 = random.randint(10, 690)
        if timer < 20:#when lasershoot
            for num in range(10):#laser print
                win.blit(orangelaser,(orangeshipx-32,258-128*num))#res 128
        pygame.draw.rect(win, (255, 255, 255), (x1, y1, 3, 3))  #stars
        pygame.draw.rect(win, (255, 255, 255), (x2, y2, 3, 3))
        pygame.draw.rect(win, (255, 255, 255), (x3, y3, 3, 3))
        win.blit(orangeship[1],(orangeshipx,orangeshipy))
        win.blit(blueship[0],(blueshipx,blueshipy))
        win.blit(greenship[4],(greenshipx,greenshipy))
        win.blit(shipstill,(x,y))
        sound()
        if i < 4:#rock front
           win.blit(rockp1[0],(0,roc))
           roc += 10
           win.blit(rockp2[0],(0,rok))
           rok += 10
        elif frontofrock == False:#rockmoving
           win.blit(rockp2[1],(0,roc))
           roc += 10
           win.blit(rockp2[1],(0,rok))
           rok += 10
        else:#rockmoving mid
           win.blit(rockp1[1],(0,roc))
           roc += 10
           win.blit(rockp2[1],(0,rok))
           rok += 10
        if roc >= 600:
            frontofrock = False
        if roc >= 620:
            roc = -600
        if rok >= 620:
            rok = -600
        if timer >= 100:#moving up the screen
            roc -= 10
            rok -= 10
            y -= 20
            blueshipy -= 20
            orangeshipy -= 20
            greenshipy -= 20
        pygame.display.update()
     hp = maxhp 
     for i in range(10):
        sound()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.time.delay(100)
        win.blit(winscene[i],(50,50))
        pygame.display.update()
     time.sleep(3)
     mainmeu = True#back to main screen
     secondbossoutro = False
     secondbossintrop2 = False
     secondbossp2 = False
     secondboss = False
     end = True
    if thirdbossintro == True:
        missley = -64
        shipx = 318
        shipy = 318
        sity = -600
        sittE = 0
        speechcount = 0
        speechinterval = 0
        while speechcount < 4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            win.fill((0,0,0))
            #printing both city apperences
            win.blit(city[1],(0,sity))
            win.blit(city[0],(0,sittE))
            #city moving
            sity += 10
            sittE += 10
            #city resent movment
            if sity >= 620:
              sity = -600
            if sittE >= 620:
              sittE = -600
            
            #dialoge code
            speechinterval += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.
                    K_SPACE] and speechinterval >= 3 or speechinterval == 100:
                speechcount += 1
                speechinterval = 0
            text = font.render('', 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (170, 600)
            pygame.draw.rect(win, (130, 135, 136), (0, 534, 700, 700))
            if speechcount == 0:
                text = font.render('press space to Continue', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
            elif speechcount == 1:
                text = font.render('Large hostile up ahead.', 1, (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            elif speechcount == 2:
                text = font.render('Regroup and engage it.', 1, (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            elif speechcount == 3:
                text = font.render('Incoming!!', 1, (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[1], (0, 540))
            win.blit(shipstill,(x,y))
            pygame.display.update()
            sound()
        missily = -64
        while missily <= y:
            sound()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            win.fill((0,0,0))
            pygame.time.delay(10)
            #printing both city apperences
            win.blit(city[1],(0,sity))
            win.blit(city[0],(0,sittE))
            #city moving
            sity += 10
            sittE += 10
            #city resent movment
            if sity >= 620:
              sity = -600
            if sittE >= 620:
              sittE = -600
            win.blit(shipstill,(x,y))
            win.blit(redmissle[0],(x,missily))
            missily +=120
            pygame.display.update()
        win.fill((0,0,0))
        win.blit(city[1],(0,sity))
        win.blit(city[0],(0,sittE))
        win.blit(shipstill,(x,y))
        win.blit(redmissle[1],(x,y))
        pygame.display.update()
        time.sleep(0.5)
        sound()
        win.fill((0,0,0))
        pygame.display.update()
        time.sleep(1.5)
        sound()
        topeye = 0
        bottomeye = 0
        while topeye >= -350:
            sound()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            win.fill((0,0,0))
            pygame.time.delay(200)
            win.blit(brokenship,(0,0))
            win.blit(eye[1],(0,topeye))
            win.blit(eye[0],(0,bottomeye))
            topeye -= 35
            bottomeye += 35
            if topeye == -210:
                topeye += 60
                bottomeye -= 60
            pygame.display.update()
        timer = 0
        while timer <= 17:
            sound()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            win.fill((0,0,0))
            timer +=1
            pygame.time.delay(100)
            win.blit(brokenship,(0,0))
            if timer <= 10:
               win.blit(robot[2],(100,100))
            elif timer == 11:
               win.blit(robot[1],(100,100))
            else:
                win.blit(robot[0],(100,100))
            pygame.display.update()
        for i in range(3):
         pygame.display.update()
         win.fill(black)
         win.blit(brokenship,(0,0))
         pygame.draw.rect(win,black, (50,50, 600, 600))
         sound()
         time.sleep(0.1)
        thirdbossintro = False
        thirdboss = True
        hp = maxhp
    if thirdboss == True:
        X = 0
        Y = 0
        class Player(pygame.sprite.Sprite):#player class
            def __init__(self):#create player
                pygame.sprite.Sprite.__init__(self)
                self.image = playerimage[0]
                self.rect = self.image.get_rect()
                self.rect.centerx = 350
                self.rect.centery = 350
                self.speedx = 0
                self.speedy = 0
                self.timer = 0
                self.shooting = False

            def update(self):#update
                self.speedx = 0 #doesnt move unless otherwise
                self.speedy = 0
                win.blit(playerimage[1],(self.rect.x, self.rect.y))

                #movement code
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                keys = pygame.key.get_pressed()#detect keypress
                if keys[pygame.K_LEFT] and self.rect.x > 100:
                    self.speedx = -10
                if keys[pygame.K_RIGHT] and self.rect.x < 590:
                    self.speedx = 10
                if keys[pygame.K_UP] and self.rect.y > 100:
                    self.speedy = -10
                if keys[pygame.K_DOWN] and self.rect.y < 590:
                    self.speedy = 10
                self.rect.x += self.speedx
                self.rect.y += self.speedy
                #print(self.rect.x,self.rect.y)#for testing
                #robots head laser
                if self.rect.centerx > 320 and self.rect.x < 380 and self.timer == 0:
                    self.timer = 1
                elif self.timer > 0 and self.shooting == False:
                    self.timer += 1
                    win.blit(headlaser[0],(270,235))
                if self.timer >= random.randrange(20,30) and self.shooting == False:
                    self.shooting = True
                if self.shooting == True and self.timer > 0:#shooting
                    self.timer -= 1
                    for i in range(6):
                        win.blit(headlaser[random.randint(1,6)],(270,i*160-160))
                    if self.rect.centerx > 314 and self.rect.x < 375:
                        global hp
                        hp -= 10
                elif self.shooting == True:
                    self.shooting = False

        class Bullet(pygame.sprite.Sprite):#bullets
                def __init__(self):#create
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.transform.scale(redbullet[random.randint(0,1)],(4,4))
                    self.rect = self.image.get_rect()
                    self.rect.centerx = random.randrange(0,700)
                    self.rect.centery = random.randrange(-40,-10)
                    self.speedy = random.randrange(1,16)
                    self.speedx = random.randrange(-7,7)#slight strafing

                def update(self):
                    self.rect.y += self.speedy
                    self.rect.x += self.speedx
                    if self.rect.top >= 710 or self.rect.x > 710 or self.rect.x < 0:#if it goes of screen
                        self.rect.x = random.randrange(0,700)#random pos
                        self.rect.y = random.randrange(-40,-10)
                        self.speedy = random.randrange(1,16)#movedoen
                        self.speedx = random.randrange(-3,3)#slight strafing

        class randomexplotion(pygame.sprite.Sprite):
                def __init__(self):#create
                    pygame.sprite.Sprite.__init__(self)
                    self.image = robotexplotion[0]
                    self.rect = self.image.get_rect()
                    self.rect.centerx = player.rect.centerx
                    self.rect.centery = player.rect.centery
                    self.timer = 1
                    self.animation = 0
                    self.explode = False

                def update(self): 
                    self.timer += 1
                    if self.timer >= 40:
                        self.explode = True
                    if self.explode == True:
                       self.animation += 1
                       self.image = robotexplotion[self.animation]
                       if self.animation >= 1:
                           explode.add(self)
                           if self.animation == 6:
                               self.timer = 0
                               self.kill()
        #enemy
        
        class Robotclass(pygame.sprite.Sprite):
                def __init__(self):#create robot
                        
                        pygame.sprite.Sprite.__init__(self)
                        self.phase = 2
                        self.image = o
                        self.rect = self.image.get_rect()
                        self.timer = 0
                        self.rect.centerx = 350
                        self.rect.centery = 350

                def update(self):
                    self.image = pygame.transform.scale( robot[self.phase],(160,160))
                    self.rect = self.image.get_rect()
                    self.timer += 1
                    if self.timer == 48:#telepot animation
                        self.phase = 1
                    elif self.timer >= 50:#actualy spawns
                        self.phase =0
                    self.rect.centerx = 350
                    self.rect.centery = 350
        
        class Missile(pygame.sprite.Sprite):
                def __init__(self):#create player
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.transform.scale(redbullet[random.randint(0,1)],(20,20))
                    self.rect = self.image.get_rect()
                    self.rect.centerx = 350
                    self.rect.centery = 350
                    self.speedy = 0
                    self.speedx = 0
                    self.prevx1 = -100
                    self.prevy1 = -100
                    self.prevx2 = -100
                    self.prevy2 = -100
                    self.prevx3 = -100
                    self.prevy3 = -100
                    self.timer = 0

                def update(self):
                 self.timer += 1
                 if self.timer > 50:
                    if self.rect.centerx > player.rect.centerx:
                        self.speedx -= 5
                    elif self.rect.centerx < player.rect.centerx:
                        self.speedx += 5
                    if self.rect.centery > player.rect.centery:
                        self.speedy -= 5
                    elif self.rect.centery < player.rect.centery:
                        self.speedy += 5
                    if self.speedy < -40:#y limit
                        self.speedy = -40
                    if self.speedy > 40:
                        self.speedy = 40
                    
                    if self.speedx < -40:#x limit
                        self.speedx = -40
                    if self.speedx > 40:
                        self.speedx = 40
                    win.blit(redbullet[4],(self.prevx3 + 5,self.prevy3 + 5))
                    self.prevx3 = self.prevx2
                    self.prevy3 = self.prevy2
                    win.blit(pygame.transform.scale(redbullet[3],(15,15)),(self.prevx2 + 2.5,self.prevy2 + 2.5))
                    self.prevx2 = self.prevx1
                    self.prevy2 = self.prevy1
                    win.blit(pygame.transform.scale(redbullet[2],(17,17)),(self.prevx1 + 1.5,self.prevy1 + 1.5))
                    self.prevy1 = self.rect.y 
                    self.prevx1 = self.rect.x 
                    self.rect.y += self.speedy
                    self.rect.x += self.speedx
                    if self.timer == 200:
                        self.kill()


        #adding player to sprite group
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        explode = pygame.sprite.Group()
        player = Player()
        Randomexplotion = randomexplotion()
        Playergroup = pygame.sprite.Group()
        Playergroup.add(player)
        robotclass = Robotclass()
        all_sprites.add(Randomexplotion)
        all_sprites.add(robotclass)
        all_sprites.add(player)
        timer = 0#timer
        leveltime = 0 
        for i in range(20):#creating 20 of them
            bullet = Bullet()
            all_sprites.add(bullet)
            bullets.add(bullet)
        
        run = True
        while run == True:#main loop
            if hp <= 0:#deth loop
                run = False  
                die = True
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            #timer
            leveltime += 0.5
            timer += 1
            if timer <= 60:
                dam = True
            else:
                dam = False 
            if timer == 100:
                missile = Missile()
                all_sprites.add(missile)
                bullets.add(missile)
                timer = 50
            elif timer == 60:
                        Randomexplotion = randomexplotion()
                        all_sprites.add(Randomexplotion)
                        
            #backround
            win.fill(black)
            win.blit(brokenship,(0,0))
            pygame.draw.rect(win,(40,40,40) ,(90,90, 520, 520))
            pygame.draw.rect(win,black, (100,100, 500, 500))
            #sprites
            all_sprites.update()
            all_sprites.draw(win)
            if player.timer > 0 and player.shooting == False:
                    win.blit(headlaser[0],(270,235))
            #UI
            pygame.draw.rect(win, (202, 204, 208),
                             (118, 38, 464, 36))  #bark backround
            pygame.draw.rect(win, (255, 0, 0),
                             (120, 40,464- leveltime , 32))  #objective bar
            text = font.render("Survive", 1,(0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (360,50)
            win.blit(text, textRect)#bojective bar
            font = pygame.font.Font('freesansbold.ttf', 20)#font
            text = font.render("HP: {0}".format(hp), 1, (255, 9, 12))  #hp variables dont change
            textRect = text.get_rect()
            textRect.center = (35, 690) #position
            win.blit(text, textRect)#hp
            pygame.display.flip()#draw stuff
            #collition
            hits  = pygame.sprite.spritecollide(player,bullets,True)
            if hits:
                hp -= random.randint(1,10)
            hits  = pygame.sprite.spritecollide(player,explode,False)
            if hits and dam == True:
                hp -= 15
            #robot hitbox
            if player.rect.centery > robotclass.rect.centery - 80 and player.rect.centery < robotclass.rect.centery + 80 and timer >= 50 and player.rect.centerx > robotclass.rect.centerx - 80 and player.rect.centerx < robotclass.rect.centerx + 80:
                          hp -= 30#take damage
            sound()
            skip = False
            #skip = True# for testing
            if leveltime >= 464 or skip == True:
                run = False
                thirdboss = False
                thirdbossoutro = True
        if die == True:  #retry loop
            run = False
            font = pygame.font.Font('freesansbold.ttf', 50)
            text = font.render('press space to retry', 0, (255, 0, 0))
            win.blit(text, (120, 320))
            text = font.render('YOU DIED', 0, (255, 0, 0))
            win.blit(text, (220, 240))
            text = font.render('click to return to main menu.', 0, (255, 0, 0))
            win.blit(text, (25, 380))
            pygame.display.update()
            retry = False
            time.sleep(0.5)
            while retry == False:  #when space pressed loops
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    pressed = pressed = pygame.mouse.get_pressed()
                    if keys[pygame.K_SPACE]:
                        retry = True
                        run = True
                        die = False
                        hp = maxhp
                    elif pressed == (True,False,False):
                        mainmeu = True
                        thirdboss = False
                        run = True
                        retry = True
                        die = False
                        hp = maxhp
                        x = 328
                        y = 328
                    pygame.time.delay(40)
    if thirdbossoutro == True:
        land = False
        run = True
        redshipy = -220
        legy = -120
        robotded = -5
        while robotded <= 7:
            pygame.time.delay(300)
            robotded += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            win.fill(black)
            win.blit(brokenship,(0,0))#backround
            if robotded < 1:
                win.blit(roborobotdie[0],(190,190))#robot
            elif robotded <= 5:#robot dying
                win.blit(roborobotdie[robotded],(190,190))#robot
                win.blit(beam[random.randint(0,3)],(190,0))
            sound()
            pygame.display.update()

        while thirdbossoutro == True:#ship decends
            pygame.time.delay(100)
            sound()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if redshipy == 0:
                land = True
            elif redshipy >= 0:
                redshipy = 0
            else:
                redshipy += 22
            win.fill(black)
            win.blit(brokenship,(0,0))#backround
            win.blit(leg,(444,legy))#ship leg
            win.blit(redshipland,(320,redshipy))#ship
           
            pygame.display.update()
            if legy < 168 and redshipy + 168 >= legy:
                legy += 17
            else:#dialoge
                textRect.center = (200, 600)
                pygame.draw.rect(win, (130, 135, 136), (0, 534, 700, 700))
                text = font.render("Get aboard. Let's get out of here.", 1,(255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
                pygame.display.update()
                time.sleep(1.5)
                thirdbossoutro = False
                Finalbossintro = True
    if Finalbossintro == True:
        sity = -600
        sittE = 0
        speechinterval = 300
        speechcount = 0
        while speechcount < 6:
            pygame.time.delay(40)
            win.fill(black)
            #printing both city apperences
            win.blit(city[1],(0,sity))
            win.blit(city[0],(0,sittE))
            #city moving
            sity += 10
            sittE += 10
            #city resent movment
            if sity >= 620:
              sity = -600
            if sittE >= 620:
              sittE = -600
            sound()
            font = pygame.font.Font('freesansbold.ttf', 25)
            win.blit(pygame.transform.scale(redship[0],(500,500)),(100,100))#enlarging ship
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            speechinterval += 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and speechinterval >= 3 or speechinterval == 500:
                speechcount += 1
                speechinterval = 0
            text = font.render('', 1, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (170, 600)
            pygame.draw.rect(win, (130, 135, 136), (0, 534, 700, 700))
            if speechcount == 0:
                text = font.render('press space to Continue', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
            elif speechcount == 1:
                text = font.render('My systems are too damaged to fly.', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            elif speechcount == 2:
                text = font.render('This ship is now under your command.', 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            elif speechcount == 3:
                text = font.render("I cannot fulfill the ships perpose.", 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            elif speechcount == 4:
                text = font.render("But you can.", 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            elif speechcount == 5:
                text = font.render("Good luck.", 1,
                                   (255, 255, 255))
                win.blit(text, textRect)
                win.blit(characters[2], (0, 540))
            pygame.display.update()
        bosstimer = 0
        bossappear = 0
        armappear = 0
        leftarmhp = 0
        rightarmhp = 0
        while leftarmhp < 3200:
            
            bosstimer += 1
            if bosstimer == 20:
                bossappear = 1
                armappear = 4
            elif bosstimer == 22:
                bossappear = 2
                armappear = 1
            pygame.time.delay(60)
            win.fill(black)
            #printing both city apperences
            win.blit(largecity[1],(0,sity))
            win.blit(largecity[0],(0,sittE))
            #city moving
            sity += 10
            sittE += 10
            #city resent movment
            if sity >= 620:
              sity = -600
            if sittE >= 620:
              sittE = -600
            sound()
            #boss
            win.blit(finalboss[bossappear],(230,50))
            win.blit(rightarm[armappear],(-10,50))
            win.blit(leftarm[armappear],(470,50))
            #bosshpbars
            #actual bars
            pygame.draw.rect(win,(40,40,40) ,(5,5,326 ,40 ))
            pygame.draw.rect(win,(255,0,0) ,(8,8,rightarmhp/10 ,34 ))
            rightarmhp += 128
            pygame.draw.rect(win,(40,40,40) ,(355,5,326 ,40 ))
            pygame.draw.rect(win,(255,0,0) ,(358,8,leftarmhp/10 ,34 ))
            leftarmhp += 128
            #text
            textRect.center = (110, 25)
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render("LEFT ARM", 1,(255, 255, 255))
            win.blit(text, textRect)
            textRect.center = (460, 25)
            text = font.render("RIGHT ARM", 1,(255, 255, 255))
            win.blit(text, textRect)
            #text
            font = pygame.font.Font('freesansbold.ttf', 20)

            win.blit(redship[0],(318,500)) #ship
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
        finalbossintro = False
        FINALBOSS = True
    if FINALBOSS == True:
        #for geting hit animtions
        shot = True
        hit = False
        lefthit = False
        righthit = False
        bosshit = False
        sheild = 1000
        #playerlocation
        x = 382
        y = 532 
        #hp
        hp = round((maxhp+1)*100)-1
        #increases missles
        misslemulti = 1
        #creating sprites

        class Boss(pygame.sprite.Sprite):#boss class
            def __init__(self):#create bossplayer
                pygame.sprite.Sprite.__init__(self)
                self.image = finalboss[2]
                self.rect = self.image.get_rect()
                self.rect.centerx = 350
                self.rect.y = 50
                self.animation = 0
            def update(self):
                global finalbosshp
                global bosshit
                if finalbosshp <= 0:
                       self.animation += 1#explode animation
                       self.image = pygame.transform.scale(robotexplotion[self.animation],(260,260))#animation
                       if self.animation == 6:
                                global FINALBOSS
                                FINALBOSS = False#ends bossfight
                                self.kill()#ends
                elif bosshit == True:#gets hit
                    bosshit = False
                    self.image = finalboss[1]
                elif finalbosshp <= 320:#damaged
                    self.image = finalboss[4]
                elif finalbosshp <= 1600:#damaged
                    self.image = finalboss[3]
                else:
                    self.image = finalboss[2]#reset animation



        class Leftarm(pygame.sprite.Sprite):#player class
            def __init__(self):#create player
                pygame.sprite.Sprite.__init__(self)
                self.image = rightarm[1]
                self.rect = self.image.get_rect()
                self.rect.x = -10
                self.rect.y = 50
                self.animation = 0
                global rightarmhp

            def update(self):
                global lefthit
                if rightarmhp <= 0:
                       self.animation += 1#explode animation
                       self.image = pygame.transform.scale(robotexplotion[self.animation],(260,260))#animation
                       if self.animation == 6:
                                self.kill()#ends
                elif lefthit == True:#gets hit
                    lefthit = False
                    self.image = rightarm[4]
                elif rightarmhp <= 320:#damaged
                    self.image = rightarm[3]
                elif rightarmhp <= 1600:#damaged
                    self.image = rightarm[2]
                else:
                    self.image = rightarm[1]
        class Rightarm(pygame.sprite.Sprite):#player class
            def __init__(self):#create player
                pygame.sprite.Sprite.__init__(self)
                self.image = leftarm[1]
                self.rect = self.image.get_rect()
                self.rect.x = 470
                self.rect.y = 50
                self.animation = 0
                global leftarmhp

            def update(self):
                global righthit
                if leftarmhp <= 0:
                       self.animation += 1#explode animation
                       self.image = pygame.transform.scale(robotexplotion[self.animation],(260,260))#animation
                       if self.animation == 6:
                                self.kill()#ends
                elif righthit == True:
                    righthit = False
                    self.image = leftarm[4]
                elif leftarmhp <= 320:
                    self.image = leftarm[3]
                elif leftarmhp <= 1600:
                    self.image = leftarm[2]
                else:
                    self.image = leftarm[1]
        class playership(pygame.sprite.Sprite):#player class
            def __init__(self):#create player
                pygame.sprite.Sprite.__init__(self)
                self.image = redship[0]
                self.rect = self.image.get_rect()
                global x
                global y
                global hp
                self.rect.centerx = x-32
                self.rect.centery = y-32
                self.speedx = 0
                self.speedy = 0
                self.timer = 0
                self.hp = hp
                self.shooting = False

            def update(self):#update
                global x
                global y
                self.speedx = 0 #doesnt move unless otherwise
                self.speedy = 0

                #movement code and sheild
                global sheild_on
                global sheild
                global keys
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                keys = pygame.key.get_pressed()#detect keypress
                if keys[pygame.K_SPACE] and sheild >= 220 and sheild_on == False:#sheild start up
                    sheild -= 100
                    sheild_on = True
                    
                elif keys[pygame.K_SPACE] and sheild >= 20 and sheild_on == True:#sheild run
                    sheild -= 10
                else:#sheild end
                    sheild_on = False
                if keys[pygame.K_LEFT] and self.rect.x > 20:
                    self.speedx = -20
                if keys[pygame.K_RIGHT] and self.rect.x < 616:
                    self.speedx = 20
                if keys[pygame.K_UP] and self.rect.y > 330:
                    self.speedy = -20
                if keys[pygame.K_DOWN] and self.rect.y < 616:
                    self.speedy = 20
                #changeing player pos
                x += self.speedx
                y += self.speedy
                self.rect.centerx = x-32
                self.rect.centery = y-32


                print(self.rect.x,self.rect.y)#for testing
        class Sheild(pygame.sprite.Sprite):#boss sheild
            def __init__(self):#create
                    pygame.sprite.Sprite.__init__(self)
                    self.image = bosssheild
                    self.rect = self.image.get_rect()
                    self.rect.centerx = 350
                    self.rect.centery = 280

            def update(self):
                global phase2
                if phase2 == True:
                    self.kill()

        class shiplaser(pygame.sprite.Sprite):#bullets left gun
                def __init__(self):#create
                    pygame.sprite.Sprite.__init__(self)
                    self.image = laserbullet
                    self.rect = self.image.get_rect()
                    self.rect.centerx = player.rect.centerx
                    self.rect.centery = player.rect.centery

                def update(self):
                    self.rect.y -= 40
                    if self.rect.top >= 720:#if it goes of screen
                        self.kill()

        class BulletL(pygame.sprite.Sprite):#bullets left gun
                def __init__(self):#create
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.transform.scale(redbullet[random.randint(0,1)],(10,10))
                    self.rect = self.image.get_rect()
                    if phase2 == True:
                        self.rect.centerx = 452
                    else:
                        self.rect.centerx = 120
                    self.rect.centery = 248
                    self.speedy = random.randrange(20,32)
                    self.speedx = random.randrange(-16,16)#spred strafing

                def update(self):
                    self.rect.y += self.speedy
                    self.rect.x += self.speedx
                    if self.rect.top >= 720 or self.rect.x > 720 or self.rect.x < -20:#if it goes of screen
                        self.kill()
        class BulletR(pygame.sprite.Sprite):#bullets
                def __init__(self):#create
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.transform.scale(redbullet[random.randint(0,1)],(10,10))
                    self.rect = self.image.get_rect()
                    #bullet spawn
                    if phase2 == True:
                        self.rect.centerx = 252
                    else:
                        self.rect.centerx = 580
                    self.rect.centery = 248
                    #bullet move
                    self.speedy = random.randrange(20,32)
                    self.speedx = random.randrange(-16,16)#spred strafing

                def update(self):
                    self.rect.y += self.speedy
                    self.rect.x += self.speedx
                    if self.rect.top >= 720 or self.rect.x > 720 or self.rect.x < -20:#if it goes of screen
                        self.kill()
        class randomexplotion(pygame.sprite.Sprite):
                def __init__(self):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = robotexplotion[0]
                    self.rect = self.image.get_rect()
                    self.rect.centerx = player.rect.centerx
                    self.rect.centery = player.rect.centery
                    self.timer = 1#exploion timer
                    self.animation = 0
                    self.explode = False

                def update(self): 
                    self.timer += 1
                    if self.timer >= 40 and self.explode == False:
                        self.explode = True 
                        self.rect.centerx = self.rect.centerx - 32
                        self.rect.centery = self.rect.centery - 32
                    if self.explode == True:
                       self.animation += 1#explode animation
                       self.image = pygame.transform.scale(robotexplotion[self.animation],(128,128))
                       if self.animation >= 1:#explode
                           explode.add(self)
                           if self.animation == 6:
                               self.timer = 0
                               self.kill()
                
        class Misile(pygame.sprite.Sprite):
                def __init__(self):#create player
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.transform.scale(redbullet[random.randint(0,1)],(20,20))
                    self.rect = self.image.get_rect()
                    self.rect.centerx = 350
                    self.rect.centery = -50
                    self.speedy = 0
                    self.speedx = 0
                    self.speed = random.randrange(3,8)
                    self.prevx1 = -100
                    self.prevy1 = -100
                    self.prevx2 = -100
                    self.prevy2 = -100
                    self.prevx3 = -100
                    self.prevy3 = -100
                    self.timer = 0
                    self.animation = 0
                    self.explode = False

                def update(self):
                 self.timer += 1
                 if self.timer > 50:
                     #increases speed
                    if self.rect.centerx > player.rect.centerx:
                        self.speedx -= self.speed
                    elif self.rect.centerx < player.rect.centerx:
                        self.speedx += self.speed
                    if self.rect.centery > player.rect.centery:
                        self.speedy -= self.speed
                    elif self.rect.centery < player.rect.centery:
                        self.speedy += self.speed
                    if self.speedy < -40:#y limit
                        self.speedy = -40
                    if self.speedy > 40:
                        self.speedy = 40
                    if self.speedx < -40:#x limit
                        self.speedx = -40
                    if self.speedx > 40:
                        self.speedx = 40
                    #trails
                    win.blit(redbullet[4],(self.prevx3 + 5,self.prevy3 + 5))
                    self.prevx3 = self.prevx2
                    self.prevy3 = self.prevy2
                    win.blit(pygame.transform.scale(redbullet[3],(15,15)),(self.prevx2 + 2.5,self.prevy2 + 2.5))
                    self.prevx2 = self.prevx1
                    self.prevy2 = self.prevy1
                    win.blit(pygame.transform.scale(redbullet[2],(17,17)),(self.prevx1 + 1.5,self.prevy1 + 1.5))
                    self.prevy1 = self.rect.y 
                    self.prevx1 = self.rect.x 
                    self.rect.y += self.speedy
                    self.rect.x += self.speedx
                    #EXPLOTION
                    if self.timer >= 100 and self.explode == False:
                        self.speed = 0

                        self.explode = True 
                        self.rect.centerx = self.rect.centerx - 54
                        self.rect.centery = self.rect.centery - 54
                    elif self.explode == False and self.rect.x >= player.rect.x and  self.rect.x <= player.rect.x +72 and self.rect.y >= player.rect.y and  self.rect.y <= player.rect.y +72:
                        self.speed = 0
                        global hp
                        hp -= 150
                        global hit
                        hit = True
                        self.explode = True 
                        self.rect.centerx = self.rect.centerx - 54
                        self.rect.centery = self.rect.centery - 54
                    if self.explode == True:
                       self.speedx = 0
                       self.speedy = 0
                       self.animation += 1#explode animation
                       self.image = pygame.transform.scale(robotexplotion[self.animation],(128,128))#animation
                       if self.animation >= 1:#explode
                           explode.add(self)
                           if self.animation == 6:
                               self.kill()#ends
        leftarmhp = 3200
        rightarmhp = 3200
        finalbosshp = 3000
        sity = 0
        shoot = False
        phase2 = False
        sittE = -600
        #deth loop
        die = False
        #sprite classes
        allsprite = pygame.sprite.Group()
        bulet = pygame.sprite.Group()
        playershoot = pygame.sprite.Group()
        explode = pygame.sprite.Group()
        player = playership()
        Player = pygame.sprite.Group()
        left = pygame.sprite.Group()
        right = pygame.sprite.Group()
        Player.add(player)
        allsprite.add(player)
        leftARM = Leftarm()
        rightARM = Rightarm()
        boss = Boss()
        allsprite.add(boss)
        left.add(leftARM)
        right.add(rightARM)
        ssheild = Sheild()
        allsprite.add(ssheild)
        allsprite.add(leftARM)
        allsprite.add(rightARM)
        Shiplaser = shiplaser()
        allsprite.add(Shiplaser)
        playershoot.add(Shiplaser)
        #for attack cycles
        shooting = 0
        missilechance = 0
        while FINALBOSS == True and run == True:
            if sheild < 1000:
                sheild += 2
            
            if hp <= 0:#death loop
                die = True
                run = False

            shooting += 1
            pygame.time.delay(60)
            win.fill(black)
            #printing both city apperences
            win.blit(largecity[1],(0,sity))
            win.blit(largecity[0],(0,sittE))
            #city moving
            sity += 10
            sittE += 10
            #city resent movment
            if sity >= 620:
              sity = -600
            if sittE >= 620:
              sittE = -600
            #sprites
            allsprite.update()
            allsprite.draw(win)
            #getting hit
            hits  = pygame.sprite.spritecollide(player,bulet,True)
            if hits and sheild_on == False:
                hp -= random.randint(3,200)
                hit = True
            hits  = pygame.sprite.spritecollide(player,explode,False)
            if hits and sheild_on == False:
                hp -= 75
                hit = True

            hits = pygame.sprite.spritecollide(boss,playershoot,True)
            if hits and phase2 == True:
                bosshit = True
                finalbosshp -= random.randint(10,20)
            if phase2 == True:
                    if shoot == False and shot == True and random.randint(1,6) == 6:#lefthand shooting#lefthand shooting
                        bulletL = BulletL()
                        allsprite.add(bulletL)
                        bulet.add(bulletL)
                        shot = False
                    elif shoot == False and random.randint(1,6) == 6:#righthand shooting
                        bulletR = BulletR()
                        allsprite.add(bulletR)
                        bulet.add(bulletR)
                        shot = True
            #phase 1
            #bosshpbars
            #actual bars
            if shoot == True:
                shoot = False
                Shiplaser = shiplaser()
                allsprite.add(Shiplaser)
                playershoot.add(Shiplaser)
            else:
                shoot = True
            if shooting == 101:#recet attack cycle
                    shooting = 0
            if shooting == 70:
                        Randomexplotion = randomexplotion()
                        allsprite.add(Randomexplotion)
            if phase2 == True:
                misslemulti = random.randint(2,8)
            missilechance += 1
            if missilechance > random.randint(round(200/misslemulti),300):#randomised
                missilechance = 0
                for i in range(1*misslemulti):
                    misslie = Misile()
                    allsprite.add(misslie)
            if phase2 == False:
                hits  = pygame.sprite.spritecollide(leftARM,playershoot,True)
                if hits:
                    rightarmhp -= random.randint(10,20)
                    lefthit = True
                pygame.sprite.spritecollide(ssheild,playershoot,True)
                hits  = pygame.sprite.spritecollide(rightARM,playershoot,True)
                if hits:
                    leftarmhp -= random.randint(10,20)
                    righthit = True
                if leftarmhp <= 0 and rightarmhp <= 0:
                    phase2 = True
                #shooting
                
                if shooting >= 35 and shooting <= 55 and rightarmhp > 0:#lefthand shooting
                    for i in range(2):#lefthand shooting
                        bulletL = BulletL()
                        allsprite.add(bulletL)
                        bulet.add(bulletL)
                elif shooting >= 80 and leftarmhp > 0:#righthand shooting
                    for i in range(2):
                        bulletR = BulletR()
                        allsprite.add(bulletR)
                        bulet.add(bulletR)
                
                #text and UI
                font = pygame.font.Font('freesansbold.ttf', 20)
                text = font.render("LEFT ARM", 1,(255, 255, 255))
                textRect = text.get_rect()
                pygame.draw.rect(win,(40,40,40) ,(5,5,326 ,40 ))
                pygame.draw.rect(win,(255,0,0) ,(8,8,rightarmhp/10 ,34 ))
                pygame.draw.rect(win,(40,40,40) ,(355,5,326 ,40 ))
                pygame.draw.rect(win,(255,0,0) ,(358,8,leftarmhp/10 ,34 ))
                #hp bar names text
                textRect.center = (110, 25)
                win.blit(text, textRect)
                text = font.render("RIGHT ARM", 1,(255, 255,255))
                textRect = text.get_rect()
                textRect.center = (460, 25)
                win.blit(text, textRect)
            #you getting hit animation
            if sheild_on == True:
                win.blit(redshipsheild,(x-96,y-96))
            if hit == True:#getting hit
                   win.blit(redship[1],(player.rect.x, player.rect.y))
                   hit = False
            pygame.draw.rect(win, (0, 0, 255), (2, 675, sheild / 10, 32))
            #your hp
            text = font.render("HP: {0}".format(hp), 1, (255, 9, 12))  #hp variables dont change
            textRect = text.get_rect()
            textRect.center = (50, 690) #position
            win.blit(text, textRect)#hp
            if phase2 == True:
                pygame.draw.rect(win, (202, 204, 208),
                             (98, 38, 504, 36))  #bosshp backround
                pygame.draw.rect(win, (255, 0, 0),
                             (100, 40, finalbosshp/3 // 2, 32))  # boss hp bar
                #boss hp bar sais boss
                win.blit(b, (300, 40))
                win.blit(o, (320, 40))
                win.blit(s, (350, 40))
                win.blit(s, (380, 40))
            
            pygame.display.flip()

        if die == True:  #retry loop
            run = False
            font = pygame.font.Font('freesansbold.ttf', 50)
            text = font.render('press space to retry', 0, (255, 0, 0))
            win.blit(text, (120, 320))
            text = font.render('YOU DIED', 0, (255, 0, 0))
            win.blit(text, (220, 240))
            text = font.render('click to return to main menu.', 0, (255, 0, 0))
            win.blit(text, (100, 360))
            pygame.display.update()
            retry = False
            while retry == False:  #when space pressed loops
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    pressed = pressed = pygame.mouse.get_pressed()
                    if keys[pygame.K_SPACE] and retry == False:
                        retry = True
                        run = True
                        die = False
                        hp = maxhp
                        x = 328
                        y = 328
                    pygame.time.delay(40)
                    if pressed == (True,False,False):
                        mainmeu = True
                        FINALBOSS = False
                        run = True
                        retry = True
                        die = False
                        hp = maxhp
                        x = 328
                        y = 328
        else: 
          text = font.render('', 1, (255, 255, 255))
          textRect = text.get_rect()
          textRect.center = (170, 600)
          pygame.draw.rect(win, (130, 135, 136), (0, 534, 700, 700))
          text = font.render('Target destroyed, lets get out of here.', 1,
                                   (255, 255, 255))
          win.blit(text, textRect)
          win.blit(characters[2], (0, 540))
          pygame.display.update()
          time.sleep(3)
          for i in range(10):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.time.delay(100)
            win.blit(winscene[i],(50,50))
            pygame.display.update()
          time.sleep(6)
          hp = maxhp
          FINALBOSS = False
          thirdboss = False
          thirdbossintro = False
          thirdbossoutro = False
          mainmeu = True