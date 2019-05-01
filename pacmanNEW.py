# Imports
import pygame
import intersects
import random
from walls import *
from coins import *

# Initialize game engine
pygame.init()


# Window
WIDTH = 380
HEIGHT = 420
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#list for pacman velocities

pacmanlist1 = [0, -1]
pacmanlist2 = [1, -1]
pacmanlist3 = [1, 0]

#Images
manpac = pygame.image.load("MANPAC.PNG")
yeehaw = pygame.image.load("yeehaw1.PNG")
yeehaw = pygame.transform.scale(yeehaw, (509, 56))
yeehaw = pygame.transform.rotate(yeehaw, 45)
pacman = pygame.image.load("pacopen.png")
pacman = pygame.transform.scale(pacman, (20, 20))
pacdown = pygame.transform.rotate(pacman, 90)
pacleft = pygame.transform.rotate(pacman, 180)
pacup = pygame.transform.rotate(pacman, 270)
ghost = pygame.image.load("ghost.PNG")
ghost = pygame.transform.scale(ghost, (20, 20))
ghost2 = pygame.transform.flip(ghost, True, False)
coin = pygame.image.load("coin.PNG")

#font
FONT_XS = pygame.font.Font(None, 30)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# stages
START = 0
PLAYING = 1
END = 2

hop = [180,180]

def setup():
    global player1, stage, vel1,  player1_speed, coins, pacman1, vel2, pacman1_speed
    x = hop[0]
    y = hop[1]
    player1 = screen.blit(ghost, [x,y]) 
    vel1 = [0, 0]
    player1_speed = 5
    direction = 0
    
    pacman1 =  screen.blit(pacman, [20,20])
    vel2 = [0, 0]
    pacman1_speed = 5

    
    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20,
         coin21, coin22, coin23, coin24, coin25, coin26, coin27, coin28, coin29, coin30, coin31, coin32, coin33, coin34, coin35, coin36, coin37, coin38, coin39,
         coin40, coin41, coin42, coin43, coin44, coin45, coin46, coin47, coin48, coin49, coin50, coin51, coin52, coin53, coin54, coin55, coin56, coin57, coin58,
         coin59, coin60, coin61, coin62, coin63, coin64, coin65, coin66, coin67, coin68, coin69, coin70, coin71, coin72, coin73, coin74, coin75, coin76, coin77,
         coin78, coin79, coin80, coin81, coin82, coin83, coin84, coin85, coin86, coin87, coin88, coin89, coin90, coin91, coin92, coin93, coin94, coin95, coin96,
         coin97, coin98, coin99, coin100, coin101, coin102, coin103, coin104, coin105, coin106, coin107, coin108, coin109, coin110, coin111, coin112, coin113,
         coin114, coin115, coin116, coin117, coin118, coin119, coin120, coin121, coin122, coin123, coin124, coin125, coin126, coin127, coin128, coin129, coin130,
         coin131, coin132, coin133, coin134, coin135, coin136, coin137, coin138, coin139, coin140, coin141, coin142, coin143, coin144, coin145, coin146, coin147,
         coin148, coin149, coin150, coin151]
    
    vel2[1] = -1
    vel2[0] = 1

    stage = START
    

def splash():
    screen.blit(manpac, [0,0])

def win():
    restartwin = FONT_XS.render("You Win, Press Space To Restart!", 1, WHITE)
    screen.blit(restartwin, [0, 0])

def lose():
    restartlose = FONT_XS.render("You Lose, Press Space To Restart!", 1, WHITE)
    screen.blit(restartlose, [0, 0])
    printscore = FONT_XS.render("Score: " + str(score1), 1, WHITE)
    screen.blit(printscore, [0, 25])

# Game loop

score1 = 0
setup()
done = False
thingy = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                        stage = PLAYING
                elif event.key == pygame.K_r:
                        stage = START

            
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        vel1[0] = -2
    elif pressed[pygame.K_RIGHT]:
        vel1[0] = 2
    elif pressed[pygame.K_UP] :
        vel1[1] = -2
    elif pressed[pygame.K_DOWN]:
        vel1[1] = 2

    if pressed[pygame.K_a]:
        vel2[0] = -2
        screen.blit(pacleft,pacman1)
    elif pressed[pygame.K_d]:
        vel2[0] = 2
        screen.blit(pacman,pacman1)
    elif pressed[pygame.K_w] :
        vel2[1] = -2
        screen.blit(pacup,pacman1)
    elif pressed[pygame.K_s]:
        vel2[1] = 2
        screen.blit(pacdown,pacman1)


    
        
    ''' process player2 input '''

    # Game logic (Check for collisions, update points, etc.)

    ''' move the player in horizontal direction '''
    if stage == PLAYING:
        player1[0] += vel1[0]
        if player1[0] >= 380:
            player1[0] = -20
        elif player1[0] <= -20:
            player1[0] = 380
        
    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
                vel1[0] = 0
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]
                vel1[0] = 0

    ''' move the player in vertical direction '''
    if stage == PLAYING:
        player1[1] += vel1[1]

    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
                vel1[1] = 0
            elif vel1[1]< 0:
                player1[1] = w[1] + w[3]
                vel1[1] = 0



                

    ''' move the player in horizontal direction '''
    if stage == PLAYING:
        pacman1[0] += vel2[0]
        if pacman1[0] >= 380:
            pacman1[0] = -20
        elif pacman1[0] <= -20:
            pacman1[0] = 380
        
    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(pacman1, w):        
            if vel2[0] > 0:
                pacman1[0] = w[0] - pacman1[2]
                vel2[0] = 0
            elif vel2[0] < 0:
                pacman1[0] = w[0] + w[2]
                vel2[0] = 0

    ''' move the player in vertical direction '''
    if stage == PLAYING:
        pacman1[1] += vel2[1]

    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(pacman1, w):                    
            if vel2[1] > 0:
                pacman1[1] = w[1] - pacman1[3]
                vel2[1] = 0
            elif vel2[1]< 0:
                pacman1[1] = w[1] + w[3]
                vel2[1] = 0

    '''pacman hits ghost'''
    if intersects.rect_rect(pacman1, player1):
        stage = END


    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]

    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 100
        
    if len(coins) == 0:
        setup()
        stage = PLAYING
     
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    

    ''' begin/end'''
    if stage == START:
        screen.blit(manpac, [0,0])
    elif stage == END:
        screen.fill(BLACK)
        screen.blit(yeehaw, [-10,0])
        lose()

    if PLAYING == False:
        splash()

    if stage == PLAYING:
        

        screen.blit(pacman, pacman1)
        
        screen.blit(ghost, player1)
            
        for w in walls:
            pygame.draw.rect(screen, BLUE, w)

        font = pygame.font.Font(None, 40)
        text4 = font.render(str(score1), 1, WHITE)
        screen.blit(text4, [0,0])

        for c in coins:
            screen.blit(coin, c)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
