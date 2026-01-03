import pygame
# Drag and Drop 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
size = 800
screen_size = (size, size)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Dragon Drop")


class Board:
    def __init__(self,grid):
        self.grid = grid
    def create(self):
        Blocks = []
        for i in range(self.grid):
            for j in range(self.grid):
                Blocks.append(Block(i,j,self.grid))
        return Blocks
 
class Piece(Board):
    def __init__(self,size):
        super().__init__(size)
        self.xpos = 0
        self.ypos = 0
        self.width = (screen_size[1]/(2*size))
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width,self.width)
        self.is_clicked = True
    def draw(self):
        pygame.draw.rect(screen,RED,self.hitbox)
    def drag(self):
        if (pygame.Rect.collidepoint(self.hitbox,pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) or self.is_clicked:
            if pygame.mouse.get_pressed()[0] == False:
                self.is_clicked = False
                return False
            else:
                self.xpos = pygame.mouse.get_pos()[0]-(self.width/2)
                self.ypos = pygame.mouse.get_pos()[1]-(self.width/2)
                self.is_clicked = True #Fixed drag method
                return True
    def move(self):
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width,self.width)
    def getXY(self):
        return self.xpos, self.ypos
    def setXY(self,new):
        self.xpos = new[0]
        self.ypos = new[1]

class Pown(Piece):
    def __init__(self):
        self.if_moved = False


class Block(Board):
    def __init__(self,row,column,grid):
        super().__init__(grid)
        self.xpos = (screen_size[0]/grid) * row
        self.ypos = (screen_size[1]/grid) * column
        self.width = screen_size[1]/grid
        self.outline = 3
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width-self.outline,self.width-self.outline)
        self.blackbox = pygame.Rect(self.xpos,self.ypos,self.width,self.width)
        self.available = True
    def draw(self):
        pygame.draw.rect(screen,BLACK,self.blackbox)
        pygame.draw.rect(screen,WHITE,self.hitbox)
        if self.available:
            pygame.draw.circle(screen, BLACK, (self.xpos+(self.width/2),self.ypos+(self.width/2)),self.width/5)
    def lock(self):
        return (self.xpos+(self.width/4),self.ypos+(self.width/4))
    def inRange(self,piece):
        if self.available:
            if piece[0] > self.xpos-(self.width/2) and piece[0] < self.xpos+(self.width) and piece[1] > self.ypos-(self.width/2) and piece[1] <= self.ypos+self.width:
                return True
    def getXY(self):
        return (self.ypos-(self.width/2))
    




# clock is used to set a max fps
clock = pygame.time.Clock()
make = 8
Map = Board(make)
Pawn = Piece(make)
Blocks = Map.create()
Pieces = (Pawn)
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    
    if Pawn.drag():
        Pawn.move()
    else:
        for i in range(len(Blocks)):
            if Blocks[i].inRange(Pawn.getXY()):
                Pawn.setXY(Blocks[i].lock())
                Pawn.move()
                break
    for i in range(len(Blocks)):
        Blocks[i].draw()
    Pawn.draw()
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()