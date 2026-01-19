import pygame
import math
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (800, 800)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 

# clock is used to set a max fps
clock = pygame.time.Clock()

class Box:

    def __init__(self,x,y,r):
        self._dimension = 50
        self.velx = 1
        self.vely = 0
        self.xpos = x
        self.ypos = y
        self.force = 1
        self.radius = r
        self.adj = r/100
        self.originx = x
        self.originy = y
        self.track = 0
        self.angle = 0
        self.direction = True #true = up and vice versa
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self._dimension,self._dimension)

    def draw(self):
        pygame.draw.line(screen,WHITE,(self.originx,self.originy),(self.xpos+self._dimension/2,self.ypos+self._dimension/2))
        pygame.draw.rect(screen, RED, self.hitbox)
        

    def move(self):
        self.angle += 0.1
        print(round(self.angle,2))
        
        self.xpos = self.radius * math.cos(self.angle) + self.originx
        self.ypos = self.radius * math.sin(self.angle) + self.originy
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self._dimension,self._dimension)
        
    def energy(self):
        Et = -(self.ypos-self.radius-self.originy) 
        # print(Et)
        
        

    # def gravity(self): #I'll make it work like real gravity once I figure this x velocity out 
    #     rope = (self.originx + self.radius)
    #     if (self.xpos >= rope and self.direction) or (self.xpos <= self.originx-self.radius and not self.direction):
    #         self.velx *= -1 
    #         self.direction = not self.direction
    #     self.track += (self.velx) 
    #     self.track = round(self.track,2) #If you don't round it adds like 0.0000001 extra which adds up overtime to create mistakes
      
      

block = Box(375,375,200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    # block.gravity()
    block.energy()
    block.move()

    block.draw()
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(10)
 
pygame.quit()