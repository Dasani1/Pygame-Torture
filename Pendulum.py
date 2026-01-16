import pygame
 
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
        self.velx = 0
        self.vely = 1
        self.xpos = x
        self.ypos = y
        self.force = 1
        self.radius = r
        self.adj = r/100
        self.originx = x
        self.originy = y
        self.track = 0
        self.direction = True #true = up and vice versa
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self._dimension,self._dimension)

    def draw(self):
        pygame.draw.rect(screen, RED, self.hitbox)

    def move(self):
        #Change the equation to y = -sqrt(radius^2 - x^2)
        #rewrite for x, 
        #Need equation Et = 1/2mv^2 + mgh (I wonder what g would be...)
        #Rewrite as Et = m(1/2mv^2 + gh)
        # max = self.radius**0.5
        # min = -max
    
        

        #self.velx = (self.adj**2 - (self.track))**0.5
        
        self.xpos = (self.radius**2 - (self.track)**2)**0.5
        self.ypos += self.vely
        # if self.direction:
        #     self.xpos += self.velx
        # else:
        #     self.xpos -= self.velx
        # print(round(self.xpos/100),round(self.ypos/100,2))
        

        
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self._dimension,self._dimension)

    def gravity(self): #I'll make it work like real gravity once I figure this x velocity out 
        rope = (self.originy + self.radius)
        if (self.ypos >= rope and self.direction) or (self.ypos <= self.originy and not self.direction):
            self.vely *= -1 
            self.direction = not self.direction
        self.track += (self.vely) 
        self.track = round(self.track,2) #If you don't round it adds like 0.0000001 extra which adds up overtime to create mistakes
      
      
        



block = Box(0,0,200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    block.gravity()
    block.move()
    block.draw()
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()