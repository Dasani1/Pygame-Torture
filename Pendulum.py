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

    def __init__(self,x,y):
        self._dimension = 50
        self.velx = 0
        self.vely = 0
        self.xpos = x
        self.ypos = y
        self.force = 1
        self.direction = True
        self.radius = 5
        self.locked = 250
        self.origin = x
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self._dimension,self._dimension)

    def draw(self):
        pygame.draw.rect(screen, RED, self.hitbox)

    def move(self):
        self.xpos += self.velx
        self.ypos += self.vely
        if self.xpos <= 0:
            self.xpos = 0
        if self.xpos >= screen_size[0]:
            self.xpos = screen_size[0]-50
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self._dimension,self._dimension)

    def gravity(self):
        ground = (screen_size[1]-(self._dimension/2))
        if self.ypos >= ground:
            self.vely *= -1
            self.direction = not self.direction
        else:
            self.vely += self.force

        if self.ypos <= ground/2:
            self.velx += self.force/2
        elif self.ypos >= ground/2:
            self.velx -= self.force/2


    def speed(self):
        pass
block = Box(200,0)

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