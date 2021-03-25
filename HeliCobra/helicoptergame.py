import pygame
import time
from random import randint,randrange
#cose Colors
black = (0,0,0)
white = (255,255,255)
grey=(200,200,200)
sunset = (230,230,230)

greenyellow = (184,255,0)
brightblue = (47,228,253)
orange = (255,113,0)
yellow = (255,236,0)
purple = (252,67,255)
new=(50,50,50)

colorChoices = [greenyellow,brightblue,orange,yellow,purple]
#initializing pygame
pygame.init()
#Dispay dimension
surfaceWidth = 1000
surfaceHeight = 500
#heliCopter Size
imageHeight = 42
imageWidth = 101

#Set Dimesnsion mode  with Height and Width
surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
#set Caption of Game
pygame.display.set_caption('Helicopter')
#start Timer
clock = pygame.time.Clock()

#images of Helicopter BackGround And Collision
img = pygame.image.load('Helicopter2.png')

background = pygame.image.load('back.png')
blast = pygame.image.load('blast.png')


# Definition of Fuction s
#Quit game function
def paused():
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Paused P:" ,True, white)
    surface.blit(text, [100,0])
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_p:

                    unpause()
        pygame.display.update()
        clock.tick(15)
def unpause():

    global pause
    pygame.mixer.music.unpause()
    pause = False


def quitgame():
    pygame.quit()
    quit()
#count Score when its= passes block
def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text, [0,0])
  

# Function of block
def blocks(x_block, y_block, block_width, block_height, gap, colorChoice):
    #draw Rectangle  (parameters are)
    #Dimension ,Color, x_axis,Y_axis,Ending_x,endingy
    #upper block
    pygame.draw.rect(surface, colorChoice, [x_block,y_block,block_width,block_height])
    #lower block
    pygame.draw.rect(surface, colorChoice, [x_block,y_block+block_height+gap,block_width, surfaceHeight])
    #shadow
    pygame.draw.rect(surface, black, [x_block,y_block-5,block_width-5,block_height-2])
    pygame.draw.rect(surface, black, [x_block,y_block+block_height+gap+2,block_width-5, surfaceHeight])
    #Design
    for i in range(10,41,10):
        pygame.draw.rect(surface, grey, [x_block+10+i,y_block-10,block_width-70,block_height-10-2*i])
        pygame.draw.rect(surface, grey, [x_block+10+i,y_block+10+block_height+gap,block_width-70, surfaceHeight-400-i*2])





def replay_or_quit():
    pygame.mixer.music.pause()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
        else:
            continue

        return event.key
    
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 25)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf1, typTextRect1 = makeTextObjs('Press any key to continue', smallText)
    typTextSurf, typTextRect = makeTextObjs('Press Q for QUIT', smallText)
    typTextSurfPause, typTextRect = makeTextObjs('Press P for Pause', smallText)
    typTextRect.center =  ((surfaceWidth / 5)+280), ((surfaceHeight / 5) +250)
    typTextRect1.center =  ((surfaceWidth / 5)+280), ((surfaceHeight / 5) +300)
    surface.blit(typTextSurf1, typTextRect1)
    surface.blit(typTextSurf, typTextRect)
    

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()

    

def gameOver():
    
    #Images of explosion aftter collision
    surface.blit(blast,(xh-180,yh-180))
    pygame.mixer.music.pause()

    pygame.mixer.music.load('collision.mp3')
    pygame.mixer.music.play(-1)
    msgSurface('crashed!')
    pygame.mixer.music.pause()

def helicopter(x, y, image):
    surface.blit(img, (x,y))


def back(x, y, image):
    surface.blit(background, (x,y))

def collision(xh,yh,imageWidth,imageHeight,x_block,y_block,block_width,block_height,gap,surfaceWidth,surfaceHeight):
    #Condition for object collision
    if (xh + imageWidth > x_block):
        if (xh < x_block + block_width and yh < block_height+y_block) or (yh + imageHeight > block_height+gap  and xh <  x_block+block_width) :
            gameOver()
    #conditin for baundary Collision
    if yh > surfaceHeight-40 or yh < 0 or xh<0 or xh>surfaceWidth:
            gameOver()



def main():
    global xh,yh,pause
    #initial Posotion of helicopter
    xh = 140
    yh = 200
    #MOVEMENT OF HELICOPTER CHANGE
    y_move = 0
    x_move=0
    # load start
    pygame.mixer.music.load('jazz.wav')
    #start sound
    pygame.mixer.music.play(-1)
    #Block Position
    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0,(surfaceHeight/2))
    gap = imageHeight * 3
    block_move = 4
    current_score = 0
    

    blockColor = colorChoices[randrange(0,len(colorChoices))]
    
    game_over = False

    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move=-5
                    
                if event.key==pygame.K_LEFT:
                    x_move=-4

                if event.key==pygame.K_RIGHT:
                    x_move=4

                if event.key == pygame.K_p:
                    pause = True
                    paused()


                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move=4
                if event.key==pygame.K_LEFT:
                    x_move=-0

                if event.key==pygame.K_RIGHT:
                    x_move=0        

        #movent of Helicopte in y-axix
        yh += y_move
        xh +=x_move
        #Set background
        back(0,0,background)
        #call helicopter
        helicopter(xh,yh,img)
        
        #Call blocks
        blocks(x_block, y_block, block_width, block_height, gap, blockColor)
        #update Score
        score(current_score)
        #movement of block x_axis toward helicopter
        x_block -= block_move
        #Conditions for wall collision

        #condition for restart of blocka
        if x_block <(-block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))
            blockColor = colorChoices[randrange(0,len(colorChoices))]
            current_score+=1
            
        #condton for block collision
        # and wall collision
        collision(xh,yh,imageWidth,imageHeight,x_block,y_block,block_width,block_height,gap,surfaceWidth,surfaceHeight)




            
        if 3 <= current_score < 5:
            block_move = 5
            gap = imageHeight * 2.9
        if 5 <= current_score < 8:
            block_move = 6
            gap = imageHeight *2.8
        if 8 <= current_score < 14:
            block_move = 7
            gap = imageHeight *2.7
        
                
                

        
            

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()