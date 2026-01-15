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
        self.originx = x
        self.originy = y
        self.direction = True #true = up and vice versa
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self._dimension,self._dimension)

    def draw(self):
        pygame.draw.rect(screen, RED, self.hitbox)

    def move(self):
        #Change the equation to y = -sqrt(radius - x^2)
        #rewrite for x, 
        #Need equation Et = 1/2mv^2 + mgh (I wonder what g would be...)
        #Rewrite as Et = m(1/2mv^2 + gh)
        # max = self.radius**0.5
        # min = -max
        # self.velx = -(self.radius-self.xpos**2)**0.5
        #if y is at origin, 
        # if self.ypos <= (self.originy+self.radius) and self.direction: #My dumbass can't figure out how to bound it so it moves up at origin but moves down at above origin
        #     self.ypos += self.vely
        # elif self.ypos > (self.originy):
        #     self.ypos -= self.vely
        # self.velx = -(self.radius-(self.vely)**2)**0.5
        # self.velx = (self.radius - self.vely**2)**0.5
        self.ypos += self.vely
        self.xpos += self.velx
        

        
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self._dimension,self._dimension)

    def gravity(self):
        rope = (self.originy + self.radius)
        if self.ypos >= rope:
            self.vely *= -1
            self.direction = not self.direction
        else:
            if self.vely != abs(1):
                self.vely += self.force


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
    block.gravity()
    block.move()
    block.draw()
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()