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
pygame.font.init()

# clock is used to set a max fps
clock = pygame.time.Clock()

class Button:

    # initializes the button
    def __init__(self,length,width,x,y,text,visibility,key,colour):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.visibility = visibility
        self.sprite = pygame.Rect(self.x,self.y,self.width,self.length)

        # sets sizing of font and the button itself
        font_size = int(self.width * 0.075)
        self.font = pygame.font.Font("freesansbold.ttf", font_size)
        self.text = text
        text_width, text_height = self.font.size(self.text)
        self.text_location = (self.x + (self.width - text_width) // 2, self.y + (self.length - text_height) // 2)

        self.pressed = False
        self.key = key
        self.colour = colour

    # draws the button on the screen
    def button_draw(self):
        text = self.font.render(self.text,self.visibility,BLACK)
        if self.visibility:
            pygame.draw.rect(screen,self.colour,self.sprite)
            screen.blit(text,self.text_location)

            if self.pressed:
                pygame.draw.rect(screen,RED,self.sprite)
                screen.blit(text,self.text_location)

    # checks if the button is pressed from the mouse
    def button_pressed(self):
        mouse_pressed = pygame.mouse.get_pressed()[0] # 0 for left click, 1 for right click
        mouse_pos = pygame.mouse.get_pos()

        if pygame.Rect.collidepoint(self.sprite, mouse_pos):
            if mouse_pressed == True:
                self.pressed = True
                return True
            else:
                self.pressed = False
                return False
        else:
            self.pressed = False

    # checks if button is pressed from the keyboard
    # def key_pressed(self):
    #     key = pygame.key.get_pressed()
    #     mods = pygame.key.get_mods()
    #     if self.visibility:
    #         if self.key == "q":
    #             if key[pygame.K_q]  and not mods:
    #                 self.pressed = True

    #         if self.key == "Q":
    #             if key[pygame.K_q] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "w":
    #             if key[pygame.K_w] and not mods:
    #                 self.pressed = True
            
    #         if self.key == "W":
    #             if key[pygame.K_w] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "e":
    #             if key[pygame.K_e] and not mods:
    #                 self.pressed = True

    #         if self.key == "E":
    #             if key[pygame.K_e] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "r":
    #             if key[pygame.K_r] and not mods:
    #                 self.pressed = True
            
    #         if self.key == "R":
    #             if key[pygame.K_r] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "t":
    #             if key[pygame.K_t] and not mods:
    #                 self.pressed = True

    #         if self.key == "T":
    #             if key[pygame.K_t] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "y":
    #             if key[pygame.K_y] and not mods:
    #                 self.pressed = True

    #         if self.key == "Y":
    #             if key[pygame.K_y] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "u":
    #             if key[pygame.K_u] and not mods:
    #                 self.pressed = True

    #         if self.key == "U":
    #             if key[pygame.K_u] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "i":
    #             if key[pygame.K_i] and not mods:
    #                 print("i")

    #         if self.key == "I":
    #             if key[pygame.K_i] and pygame.KMOD_SHIFT and mods:
    #                 print("I")

    #         if self.key == "o":
    #             if key[pygame.K_o] and not mods:
    #                 print("o")

    #         if self.key == "O":
    #             if key[pygame.K_o] and pygame.KMOD_SHIFT and mods:
    #                 print("O")

    #         if self.key == "p":
    #             if key[pygame.K_p] and not mods:
    #                 print("p")

    #         if self.key == "P":
    #             if key[pygame.K_p] and pygame.KMOD_SHIFT and mods:
    #                 print("P")

    #         if self.key == "a":
    #             if key[pygame.K_a] and not mods:
    #                 self.pressed = True

    #         if self.key == "A":
    #             if key[pygame.K_a] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "s":
    #             if key[pygame.K_s] and not mods:
    #                 self.pressed = True

    #         if self.key == "S":
    #             if key[pygame.K_s] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "d":
    #             if key[pygame.K_d] and not mods:
    #                 self.pressed = True

    #         if self.key == "D":
    #             if key[pygame.K_d] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "f":
    #             if key[pygame.K_f] and not mods:
    #                 self.pressed = True

    #         if self.key == "F":
    #             if key[pygame.K_f] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "g":
    #             if key[pygame.K_g] and not mods:
    #                 self.pressed = True

    #         if self.key == "G":
    #             if key[pygame.K_g] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "h":
    #             if key[pygame.K_h] and not mods:
    #                 self.pressed = True

    #         if self.key == "H":
    #             if key[pygame.K_h] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "j":
    #             if key[pygame.K_j] and not mods:
    #                 self.pressed = True
            
    #         if self.key == "J":
    #             if key[pygame.K_j] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    #         if self.key == "l":
    #             if key[pygame.K_l] and not mods:
    #                 self.pressed = True

    #         if self.key == "L":
    #             if key[pygame.K_l] and pygame.KMOD_SHIFT and mods:
    #                 self.pressed = True

    def get_State(self):
        return self.pressed

    def all(self):
        self.button_pressed()
        self.key_pressed()
        self.button_draw()
        return self.get_State()

    def button_state(self, state):
        self.visibility = state
    
    def key_pressed(self, state):
        pass

    def getNote(self):
        pass


# buttons
instance = Button(300,400,100,200,"Hello, This is button",False,"Q",WHITE) #Length, width, x,y, text, visbility, Key assignment, Colour
cool = Button(200,200,200,100, "Press to light up",True,"f",WHITE)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #clear the screen
    screen.fill(BLACK)

    # functions in a single function
    instance.all()
    cool.all()


    # flip() updates the screen to make our changes visible
    pygame.display.flip()

    # how many updates per second
    clock.tick(60)
 
pygame.quit()