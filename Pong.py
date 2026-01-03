import pygame
import random
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
GREEN = (0,255,0)
ORANGE = (255,125,0)
YELLOW = (255,255,0)
PURPLE = (125,0,255)

colours = (RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE)
# initialize pygame
pygame.init()
screen_size = (800,600)


# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")

class Box:
    def __init__(self,x,y,speed1,speed2):
        self.speedx = speed1
        self.speedy = speed2
        self.xpos = x
        self.ypos = y
        self.size = 30
        self.colour = colours[random.randint(0,5)]
        self.hitbox = pygame.Rect(x,y,self.size,self.size)
        self.score1 = 0
        self.score2 = 0
    def draw(self):
        pygame.draw.rect(screen,self.colour,self.hitbox)
    def move(self,value):
        if value == "x":
            self.setSpeedx()
            self.setColour()
        elif value == "y":
            self.setSpeedy()
            self.setColour()
        elif value == "p":
            self.setSpeedx()
            self.setSpeedy()
            self.setColour()
        self.xpos += self.speedx
        self.ypos += self.speedy
        if self.xpos < 0:
            self.score1 += 1
            self.xpos = screen_size[0]/2
            self.ypos = screen_size[1]/2
        elif self.xpos > screen_size[0]:
            self.score2 += 1
            self.xpos = screen_size[0]/2
            self.ypos = screen_size[1]/2
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.size,self.size)
    def setSpeedx(self):
        self.speedx *= -1
    def setSpeedy(self):
        self.speedy *= -1
    def setColour(self):
        colour = random.randint(0,5)
        if colour == colours.index(self.colour):
                colour -= 1
        self.colour = colours[colour]

    def getBox(self):
        return self.hitbox
    
    def getScore1(self):
        return self.score1
    
    def getScore2(self):
        return self.score2

class Border:
    def __init__(self):
        self.hitboxX = pygame.Rect(0,0,screen_size[0],10)
        self.hitboxX2 = pygame.Rect(0,screen_size[1]-10,screen_size[0],10)
        # self.hitboxY = pygame.Rect(0,0,10,screen_size[1])
        # self.hitboxY2 = pygame.Rect(screen_size[0]-10,0,10,screen_size[1])
    def draw(self):
        pygame.draw.rect(screen,WHITE,self.hitboxX)
        # pygame.draw.rect(screen,WHITE,self.hitboxY)
        pygame.draw.rect(screen,WHITE,self.hitboxX2)
        # pygame.draw.rect(screen,WHITE,self.hitboxY2)
    def collide(self,object):
        if pygame.Rect.colliderect(self.hitboxX,object) or pygame.Rect.colliderect(self.hitboxX2,object):
            return "y"
        # elif pygame.Rect.colliderect(self.hitboxY,object) or pygame.Rect.colliderect(self.hitboxY2,object):
        #     return "x"
        
class Paddle:

    def __init__(self,player):
        self.scale = 20
        self.width = self.scale
        self.length = self.scale * 4
        self.player = player
        self.speed = 0
        if self.player == 1:
            self.xpos = self.scale * 2
        if self.player == 2:
            self.xpos = screen_size[0] - self.scale *2 
        self.ypos = screen_size[1]/2
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width,self.length)

    def draw(self):
        pygame.draw.rect(screen,WHITE,self.hitbox)

    def setmove(self,value):
        if value == "n":
            self.speed = 0
        elif value:
            self.speed = 5
        else:
            self.speed = -5
        
    def move(self):
        
        self.ypos += self.speed
        if self.ypos <= 0:
            self.ypos = 0
        if self.ypos >= screen_size[1]-self.length:
            self.ypos = screen_size[1] - self.length
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width,self.length)
    
    def collide(self,box):
        if pygame.Rect.colliderect(self.hitbox,box):
            return "p"

    def all(self):
        self.move()
        self.draw()

class Text:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.location = (400,100)
        self.title = (220,50)
    def display(self,score1,score2):
        zoom = self.font.render("Score: ",True,WHITE,BLACK)
        position = self.font.render(f"{score1} : {score2}",True,WHITE,BLACK)
        screen.blit(zoom,self.location)
        screen.blit(position,self.title)
    

# clock is used to set a max fps
clock = pygame.time.Clock()

block1 = Box(random.randint(100,700),random.randint(100,500),2,2) #xy positions xy speeds
player1 = Paddle(1)
player2 = Paddle(2)
barrier = Border()
words = Text()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.setmove(False)
            if event.key == pygame.K_s:
                player1.setmove(True)
            if event.key == pygame.K_UP:
                player2.setmove(False)
            if event.key == pygame.K_DOWN:
                player2.setmove(True)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1.setmove("n")
            if event.key == pygame.K_s:
                player1.setmove("n")
            if event.key == pygame.K_UP:
                player2.setmove("n")
            if event.key == pygame.K_DOWN:
                player2.setmove("n")
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pass

     
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE

    block1.move(barrier.collide(block1.getBox()))
    block1.move(player1.collide(block1.getBox()))
    block1.move(player2.collide(block1.getBox()))
    words.display(block1.getScore1(),block1.getScore2())
    block1.draw()
    player1.all()
    player2.all()
    barrier.draw()


 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()