import pygame
import random
import math
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
    def __init__(self,x,y,speed1,speed2,r):
        self.r = r
        self.mass = 5
        self.speedx = speed1
        self.speedy = speed2
        self.xpos = x
        self.ypos = y
        self.pos = (self.xpos,self.ypos)
        self.colour = colours[random.randint(0,5)]
        self.collide = False #Quick collision detector
    def draw(self):
        pygame.draw.circle(screen,self.colour,self.pos,self.r)
        pygame.draw.line(screen,RED,(self.pos),(self.xpos+(self.speedx*10),self.ypos+(self.speedy*10)),5)
    
    def move(self):
        self.xpos += self.speedx
        self.ypos += self.speedy
        self.pos = (self.xpos,self.ypos)

        #Quick temp collision
        if (self.xpos > screen_size[0]-35 and self.speedx > 0) or (self.xpos < 35 and self.speedx < 0):
            self.speedx *= -1
            self.collide = True
        if (self.ypos > screen_size[1]-35 and self.speedy > 0) or (self.ypos < 35 and self.speedy < 0):
            self.speedy *= -1
            self.collide = True

    def arrow(self):
        if self.collide:
            mag = (self.speedx**2 + self.speedy**2)**0.5 #Magnitude of the speed
 
        #Now to find direction...
        self.collide = False

    def setSpeedx(self,speed):
        self.speedx *= speed
    def setSpeedy(self,speed):
        self.speedy *= speed
    def setColour(self,colour):
        if colour == colours.index(self.colour):
            if colour >= 5:
                colour = 0
            else:
                colour += 1
        self.colour = colours[colour]
    def doAll(self):
        self.move()
        self.draw()



class Border:
    def __init__(self):
        self.hitboxX = pygame.Rect(0,0,screen_size[0],10)
        self.hitboxX2 = pygame.Rect(0,screen_size[1]-10,screen_size[0],10)
        self.hitboxY = pygame.Rect(0,0,10,screen_size[1])
        self.hitboxY2 = pygame.Rect(screen_size[0]-10,0,10,screen_size[1])
    def draw(self):
        pygame.draw.rect(screen,WHITE,self.hitboxX)
        pygame.draw.rect(screen,WHITE,self.hitboxY)
        pygame.draw.rect(screen,WHITE,self.hitboxX2)
        pygame.draw.rect(screen,WHITE,self.hitboxY2)
    def collide(self,object):
        if pygame.Rect.colliderect(self.hitboxX,object) or pygame.Rect.colliderect(self.hitboxX2,object):
            return "y"
        elif pygame.Rect.colliderect(self.hitboxY,object) or pygame.Rect.colliderect(self.hitboxY2,object):
            return "x"
    

# clock is used to set a max fps
clock = pygame.time.Clock()

circle1 = Box(random.randint(100,700),random.randint(100,500),random.randint(3,6),random.randint(3,6),25) #xy positions xy speeds and radius
circle2 = Box(random.randint(100,700),random.randint(100,500),random.randint(3,6),random.randint(3,6),25) #xy positions xy speeds and radius

barrier = Border()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    # if barrier.collide(block1.getBox()) == "y":
    #     block1.setSpeedy(-1)
    #     block1.setColour(random.randint(0,5))
    # elif barrier.collide(block1.getBox()) == "x":
    #     block1.setColour(random.randint(0,5))
    #     block1.setSpeedx(-1)

    circle1.doAll()
    circle2.doAll()
    barrier.draw()


 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()