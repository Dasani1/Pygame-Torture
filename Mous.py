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
 
class Box:
    def __init__(self):
        self.is_clicked = False
        self.width = 100
        self.xpos = 250
        self.ypos = 150
        self.movement = False
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width,self.width)

    def draw(self):
        if self.is_clicked:
            pygame.draw.rect(screen,WHITE,self.hitbox)
        else:
            pygame.draw.rect(screen,RED,self.hitbox)

    def move(self):
        if self.movement:
            self.xpos = pygame.mouse.get_pos()[0] - (self.width/2)
            self.ypos = pygame.mouse.get_pos()[1] - (self.width/2)
            self.is_clicked = True
        else:
            self.is_clicked = False
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width,self.width)
    def getBox(self):
        return self.hitbox
    def setMovement(self,status):
        self.movement = status


    # def drag(self):
    #     if (pygame.Rect.collidepoint(self.hitbox,pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) or self.is_clicked:
    #         if pygame.mouse.get_pressed()[0] == False:
    #             self.is_clicked = False
    #             return False
    #         else:
    #             self.xpos = pygame.mouse.get_pos()[0]-(self.width/2)
    #             self.ypos = pygame.mouse.get_pos()[1]-(self.width/2)
    #             self.is_clicked = True
    #             return True
    # def momentum(self,speed):
    #     if len(speed) <= 50:
    #         speed.append(pygame.mouse.get_pos())
    #         return speed
    #     else:
    #         pass





    

        
# clock is used to set a max fps
clock = pygame.time.Clock()
Speed = []
fps = 60
Square = Box()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and pygame.Rect.collidepoint(Square.getBox(),event.pos):
                print(True)
                Square.setMovement(True)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Square.setMovement(False)
                
     
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    Square.move()
    Square.draw()
    # if Square.drag():
    #     Square.move()
    # Square.hover()
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(fps)
 
pygame.quit()