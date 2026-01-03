import pygame
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (700, 500)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 
class Button:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.width = 200
        self.hitbox = pygame.Rect(self.x,self.y,self.width,self.width)
        self.state = False
    def draw(self):
        if self.state:
            pygame.draw.rect(screen,RED,self.hitbox)
        else:
            pygame.draw.rect(screen,WHITE,self.hitbox)
    def setState(self,state):
        self.state = state
    def getBox(self):
        return self.hitbox

# clock is used to set a max fps
clock = pygame.time.Clock()
Clicky = Button()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and pygame.Rect.collidepoint(Clicky.getBox(),event.pos):
                Clicky.setState(True)
                print("Hello")

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Clicky.setState(False)

    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    Clicky.draw()
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(120)
 
pygame.quit()