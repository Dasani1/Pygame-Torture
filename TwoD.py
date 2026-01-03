import pygame
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 

#GOAL: Right now the goal is to make a 2d engine, simple enough
#Make the ability to create circles that can connect in a 2d space I guess
#The idea sounds harder than I realized, but we push through I guess

# initialize pygame
pygame.init()

grid = 5
grid_trans = 50
grid_adj = grid*grid_trans #I'll work this out later
size = 500 #Set a static size for the screen

screen_size = (size, size)
 
# create a window
screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
pygame.display.set_caption("pygame Test")
 

# clock is used to set a max fps
clock = pygame.time.Clock()
#Goal: Point class, Drag class, Connect class, Grid Class
class Static: #All of them should have roughly the same stay mechanic so why not make a parent class that they all inherit
    pass
class Point:
    def __init__(self,x,y): #Standard constructor
        self.a = x #yo this is kinda stupid
        self.b = y
        self.x = (sized[0]/2) + (x*(sized[0]/grid/2)) #divide by 2 because we are doing cartesian for some reason
        self.y = (sized[1]/2) - (y*(sized[1]/grid/2)) #testing
        self.size = 5 #Work on this later 
    def draw(self): #Standard drawing the point
        pygame.draw.circle(screen,WHITE,(self.x,self.y),self.size)
    def update(self): #ensure point knows where it is
        if sized[0] > sized[1]: #These if statements make it so that the point is always scaled properly with screen
            smol = sized[1]
            big = sized[0]
            diff = big-smol
            self.x = (smol/2) + (self.a*(smol/grid/2)) + diff/2
            self.y = (smol/2) - (self.b*(smol/grid/2))
        else:
            smol = sized[0]
            big = sized[1]
            diff = big-smol
            self.x = (smol/2) + (self.a*(smol/grid/2))
            self.y = (smol/2) - (self.b*(smol/grid/2)) + diff/2
    def stay(self): #Ensuring it remembers its spot when moved
        pass
    def getCoord(self):
        return (self.x,self.y)

class Connect:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        pygame.draw.line(screen,RED,(self.p1.getCoord()),(self.p2.getCoord()))
    def stay(self):
        pass

class Drag:
    pass

class Grid:
    def __init__(self): #maybe add a format style (later on)
        self.grid = grid
        self.type = "work on later"
    def draw(self): #Standard drawing
        # If statement to determine how to ensure the graph is always centered at the very middle of the screen
        if sized[0] > sized[1]: # x is bigger than y
            smol = sized[1]
            big = sized[0]
            diff = big-smol
            pygame.draw.circle(screen,WHITE,(big/2,smol/2),5) #origin
            for x in range(grid*2+1):
                pygame.draw.line(screen,WHITE,(0,x*(smol/(grid*2))),(sized[0],x*(smol/(grid*2))))
            for y in range(grid*2+1):
                pygame.draw.line(screen,WHITE,(y*(smol/(grid*2))+diff/2,0),(y*(smol/(grid*2))+diff/2,sized[1]))
        else: #vice versa
            smol = sized[0]
            big = sized[1]
            diff = big-smol
            pygame.draw.circle(screen,WHITE,(smol/2,big/2),5) #origin
            for x in range(grid*2):
                pygame.draw.line(screen,WHITE,(0,x*(smol/(grid*2))+diff/2),(sized[0],x*(smol/(grid*2))+diff/2))
            for y in range(grid*2):
                pygame.draw.line(screen,WHITE,(y*(smol/(grid*2)),0),(y*(smol/(grid*2)),sized[1]))
    def stay(self): #Ensures it remembers its spot when moved
        pass

sized = pygame.display.get_window_size()

x1 = Point(-2,-2)
x2 = Point(-2,2)
x3 = Point(2,2)
x4 = Point(2,-2)
m1 = Connect(x1,x2)
m2 = Connect(x2,x3)
m3 = Connect(x3,x4)
m4 = Connect(x4,x1)

test = Connect(x1,x3)



graph = Grid()
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
     
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE

    sized = pygame.display.get_window_size()
    graph.draw()
    x1.update()
    x1.draw()
    x2.update()
    x2.draw()
    x3.update()
    x3.draw()
    x4.update()
    x4.draw()

    m1.draw()
    m2.draw()
    m3.draw()
    m4.draw()
    
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()