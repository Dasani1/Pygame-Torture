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
        self.Blocks = []
        self.array = [[0 for i in range(self.grid)] for j in range(self.grid)]
    def createGrid(self):
        self.Blocks = []
        for i in range(self.grid):
            for j in range(self.grid):
                self.Blocks.append(Block(i,j,self.grid)) #Creates 1d array with 2d properties
        return self.Blocks
    def createPieces(self):
        Pieces = []
        for i in range(self.grid):
            Pieces.append(Piece(self.grid,i)) #creates all pieces (so far)
        return Pieces
    def setAvailability(self,position,type):
        if type == "r": #For rook
            for i in range(self.grid-3):
                self.array[position[0]][position[i]] = "x" #all y positions (I'll add interference later)
                self.array[position[i]][position[1]] = "x" #all x positions
            self.array[position[0]][position[1]] = "r"  #lastly, where the rook actually is
    def getArray(self):
        return self.array


class Piece(Board):
    def __init__(self,size,piece):
        super().__init__(size)
        self.xpos = 100*piece
        self.ypos = 0
        self.width = (screen_size[1]/(2*size))
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width,self.width)
        self.is_clicked = False
        self.locked_in = False
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
    def take(self):
        pass
    def getXY(self):
        return (self.xpos, self.ypos)
    def getStatus(self):
        return self.locked_in
    def setXY(self,new):
        self.xpos = new[0]
        self.ypos = new[1]
    def setStatus(self,status):
        self.locked_in = status

class Rook(Piece):
    def __init__(self):
        self.if_moved = False #castling (later)
        self.position = 7,0
        self.type = "r"
    def straight(self,position):
        for i in range(8): #genuinely do not know
            position[1]

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
        self.position = [row,column]
    def draw(self):
        pygame.draw.rect(screen,BLACK,self.blackbox)
        pygame.draw.rect(screen,WHITE,self.hitbox)
        if self.available:
            pygame.draw.circle(screen, BLACK, (self.xpos+(self.width/2),self.ypos+(self.width/2)),self.width/5) 
    def lock(self):
        return (self.xpos+(self.width/4),self.ypos+(self.width/4)) #Lock in!!
    def inRange(self,piece):
        if self.available:
            if piece[0] > self.xpos-(self.width/2) and piece[0] < self.xpos+(self.width) and piece[1] > self.ypos-(self.width/2) and piece[1] <= self.ypos+self.width: #fix later
                return True
    def getXY(self):
        return (self.ypos-(self.width/2),)
    def getPosition(self):
        return self.position
    def setAvailability(self,check):
        if check[self.position[0]][self.position[1]] == "x": #self explanatory
            self.available = True
        else:
            self.available = False
    
# clock is used to set a max fps
clock = pygame.time.Clock()
make = 8
Map = Board(make)   
Pawns = Map.createPieces()
Blocks = Map.createGrid()
num_map = Map.getArray()
print(num_map)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE


    for stuff in Pawns:
        if stuff.drag():
            stuff.move()
        else:
            for square in Blocks:
                if stuff.getStatus() == False:
                    if square.inRange(stuff.getXY()):
                        stuff.setXY(square.lock())
                        stuff.setStatus(True)
                        # Map.setAvailability(square.getPosition(),"r")
                        stuff.move()
                        break
                else:
                    stuff.setStatus(False)

    for square in Blocks:
        square.draw()
    for stuff in Pawns:
        stuff.draw()



 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()