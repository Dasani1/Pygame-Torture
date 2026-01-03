import pygame
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (50,0,150)
 
# initialize pygame
pygame.init()
screen_size = (1000, 500)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 

# clock is used to set a max fps
clock = pygame.time.Clock()

class Instrument:
    def __init__(self,type):
        self.type = type
    def get_sound(self):
        pass
    def record(self):
        pass
class Piano(Instrument):
    def __init__(self,octave,keys):
        self.octaves = octave
        self.keys = keys
        self.array = []
        self.black_keys = (2,4,7,9,11)
        self.barray = []
        self.test = []
    def create(self):
        for i in range(1,self.keys+1):
            if i not in self.black_keys and i-12 not in self.black_keys:
                self.array.append(Key(i,"w"))
        return self.array
    def createb(self):
        for i in range(1,self.keys+1):
            if i in self.black_keys or i-12 in self.black_keys:
                self.barray.append(Key(i,"b"))
        return self.barray
    def testar(self):
        return self.test

class Key(Piano):
    def __init__(self,number,type):
        self._number = number
        self._type = type
        self.black_keys = 0
        if self._type == "w":
            self.width = 75
            self.length = 200
            self.xpos = (number-1) * self.width
            self.ypos = 300
            self.speedx = -1
        else:
            self.width = 50
            self.length = 125
            self.xpos = 2000
            self.ypos = 300
            self.speedx = -1
        self.state = False
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width-3,self.length-3)
        self.outline = pygame.Rect(self.xpos,self.ypos,self.width,self.length)
    def press_key(self,position,state):
        if self._number == position:
            self.state = state
    def draw(self):
        if self.state:
            pygame.draw.rect(screen,BLACK,self.outline)
            pygame.draw.rect(screen,RED,self.hitbox)
        elif self._type == "w":
            pygame.draw.rect(screen,BLACK,self.outline)
            pygame.draw.rect(screen,WHITE,self.hitbox)
        else:
            pygame.draw.rect(screen,BLACK,self.hitbox) #For the sake of visibility
    def speed(self):
        if self._number > 1:
            self.xpos += self.speedx
    def collide(self,object):
        if self._type == "w":
            if pygame.Rect.colliderect(self.outline,object):
                self.speedx = 0
        elif self._type == "b":
            # print(self.xpos,object*1.5)
            if self.xpos <= (object+(75/2)+13):
                self.speedx = 0
                self.xpos = (object+(75/2)+13)
    def move(self):
        self.outline = pygame.Rect(self.xpos,self.ypos,self.width,self.length)
        self.hitbox = pygame.Rect(self.xpos,self.ypos,self.width-3,self.length-3)
    def getBox(self):
        if self._type == "b":
            return pygame.Rect(1000,1000,1,1)
        else:
            return self.outline
    def getX(self):
        return self.xpos
    def getNum(self):
        return self._number

Pianissimo = Piano(1,24)
Keys = Pianissimo.create()
BKeys = Pianissimo.createb()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            for i in range(len(Keys)):
                if event.key == pygame.K_a:
                    Keys[i].press_key(1,True)
                elif event.key == pygame.K_w:
                    print("c#")
                elif event.key == pygame.K_s:
                    Keys[i].press_key(3,True)   
                elif event.key == pygame.K_e:
                    print("d#")
                elif event.key == pygame.K_d:
                    print("e")
                elif event.key == pygame.K_f:
                    print("f")
                elif event.key == pygame.K_t:
                    print("f#")
                elif event.key == pygame.K_g:
                    print("g")
                elif event.key == pygame.K_y:
                    print("g#")
                elif event.key == pygame.K_h:
                    print("a")
                elif event.key == pygame.K_u:
                    print("a#")
                elif event.key == pygame.K_j:
                    print("b")



     
    #clear the screen
    screen.fill(BLUE)
     
    # draw to the screen
    # YOUR CODE HERE
    
    for i in range(len(Keys)):
        Keys[i].speed()
        Keys[i].collide(Keys[i-1].getBox())
        Keys[i].move()
        Keys[i].draw()
    for i in range(len(BKeys)):
        BKeys[i].speed()
        for note in Keys:
            if note.getNum() == BKeys[i].getNum()-1:
                BKeys[i].collide(note.getX())
            BKeys[i].move()
        BKeys[i].draw()
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()