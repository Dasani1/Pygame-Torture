import pygame
#Gravity.py
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (700, 800)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 
class Box:
    def __init__(self,x,y,bouncy,speed1,speed2,intensity):
        self.bounciness = bouncy
        self.xpos = x
        self.ypos = screen_size[1] - 60 - y
        self.hitbox = pygame.Rect(self.xpos,self.ypos,50,50)
        self.speedx = speed1
        self.speedy = speed2
        self.force = intensity
        self.bounceback = 0
        self.is_clicked = False
    def draw(self):
        pygame.draw.rect(screen,RED,self.hitbox)
    def move(self):
        self.xpos += self.speedx
        self.ypos += self.speedy
        self.hitbox = pygame.Rect(self.xpos,self.ypos,50,50)
        # print("Speed:",self.speedy)

    def gravity(self,floor):
        if pygame.Rect.colliderect(self.hitbox,floor):
            self.bounceback *=(self.bounciness/100)
            self.ypos = screen_size[1]-60
            self.speedy = -self.bounceback*(self.bounciness/100)
            if abs(self.speedy) <= 0.75:
                self.speedy = 0
        elif self.ypos > screen_size[1]-60:
            self.bounceback *=(self.bounciness/100)
            self.ypos = screen_size[1]-60
            self.speedy = - self.bounceback*(self.bounciness/100)
        else:
            self.speedy += self.force

    def kinematics(self): #sqrt(2ad+vi^2) = vf
        if abs(self.speedy) <= 0 and self.ypos != screen_size[1]-60:
            var1 = 2*self.force*(screen_size[1]-self.ypos-60) #2ad
            self.bounceback = var1**0.5 #sqrt(2ad) 
            # print(self.bounceback)


    def border(self,wall1,wall2):
        if self.xpos >= screen_size[0]-60:
            self.xpos = screen_size[0]-60
            self.speedx *= -1
        elif self.xpos <= 10:
            self.xpos = 10
            self.speedx *= -1
        elif self.ypos >= screen_size[1]-60 and self.speedy == 0:
            self.ypos = screen_size[1]-60
        elif pygame.Rect.colliderect(self.hitbox,wall1) or pygame.Rect.colliderect(self.hitbox,wall2): #redundant but I like it so I'm keeping it
            self.speedx *= -1
    
    # def drag(self):
    #     track = pygame.mouse.get_pos()
    #     if pygame.mouse.get_pressed()[0] and track[0] <= self.xpos+50 and track[0] >= self.xpos and track[1] >= self.ypos and track[1] <= self.ypos+50:
    #         self.xpos = track[0]-25
    #         self.ypos = track[1]-25
    #         self.speedy = 0
    #         return True
        
    def drag(self):
        if (pygame.Rect.collidepoint(self.hitbox,pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]) or self.is_clicked:
            if pygame.mouse.get_pressed()[0] == False:
                self.is_clicked = False
                return False
            else:
                self.xpos = pygame.mouse.get_pos()[0]-(25)
                self.ypos = pygame.mouse.get_pos()[1]-(25)
                self.is_clicked = True
                self.speedy = 0
                return True

    def getY(self):
        return self.ypos
    def getSpeed(self):
        return self.speedy

class Barrier:
    def __init__(self):
        # self.hitboxX1 = pygame.Rect(0,0,screen_size[0],10)
        self.hitboxX2 = pygame.Rect(0,screen_size[1]-10,screen_size[0],10)
        self.hitboxY1 = pygame.Rect(0,0,10,screen_size[1])
        self.hitboxY2 = pygame.Rect(screen_size[0]-10,0,10,screen_size[1])
    def draw(self):
        # pygame.draw.rect(screen,WHITE,self.hitboxX1)
        pygame.draw.rect(screen,WHITE,self.hitboxX2)
        pygame.draw.rect(screen,WHITE,self.hitboxY1)
        pygame.draw.rect(screen,WHITE,self.hitboxY2)
    def getFloor(self):
        return self.hitboxX2
    def getWall1(self):
        return self.hitboxY1
    def getWall2(self):
        return self.hitboxY2
    
class Text:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.location = (400,100)
        self.title = (220,50)
    def display(self,speed,pos):
        zoom = self.font.render(f"Speed = {round(speed,2)}",True,WHITE,BLACK)
        position = self.font.render(f"Height = {int(screen_size[1]-60-pos)}",True,WHITE,BLACK)
        screen.blit(zoom,self.location)
        screen.blit(position,self.title)

    
# clock is used to set a max fps
clock = pygame.time.Clock()
block = Box(300,500,100,0,0,1) #position xy, bounciness(later), xy speed and gravity
wall = Barrier()
words = Text()
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill(BLACK)
     
    # draw to the screen
    # YOUR CODE HERE
    words.display(block.getSpeed(),block.getY())
    block.kinematics()
    block.drag()
    if block.getY() != screen_size[1]-60 and not block.drag():
        block.gravity(wall.getFloor())
    block.border(wall.getWall1(),wall.getWall2())
    block.move()
    block.draw()
    wall.draw()
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()