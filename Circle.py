import pygame
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
s = 800
screen_size = (s, s)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 #Goal to make a circle that goes around a circle

# clock is used to set a max fps
clock = pygame.time.Clock()

class Circle():
    def __init__(self,r,rr):
        self.r = r
        self.rr = rr #real radius
        self.dim = 50
        self.originx = (s/2)
        self.originy = (s/2)
        self.x = self.originx
        self.y = self.originy + 50
        self.vely = 1
        self.velx = 1
        self.track = 0
        self.dir = True

    def math(self):
        #y^2 + x^2 = r^2
        y = self.y**2
        x = self.track**2
        rr = self.rr**2
        if self.dir:
            self.y = (rr - x)**0.5 + self.originy
        else:
            self.y = -(rr - x)**0.5 + self.originy

    def move(self):

        if (self.x >= self.originx + self.rr) or (self.x <= self.originx - self.rr):
            self.velx *= -1
            self.dir = not self.dir
        # if (self.y >= self.originy + self.rr) or (self.y <= self.originy - self.rr*2):
        #     self.vely *= -1

        self.track += self.velx
        self.x += self.velx
        self.y += self.vely

    def draw(self):
        pygame.draw.circle(screen,WHITE,(self.originx,self.originy),10) #origin circle
        pygame.draw.circle(screen,RED,(self.x,self.y),self.r)


Round = Circle(20,100)
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(BLACK)

    Round.math()
    Round.move()
    Round.draw()

     
    # draw to the screen
    # YOUR CODE HERE
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()