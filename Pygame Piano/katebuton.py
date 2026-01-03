import pygame
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
#initialize pygame
pygame.init()
screen_size = (700, 500)
 
#create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
pygame.font.init()
 

#clock is used to set a max fps
clock = pygame.time.Clock()

class Button:
    def __init__(self,length,width,x,y,text,visibility,key,colour):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.visibility = visibility
        self.sprite = pygame.Rect(self.x,self.y,self.width,self.length)
        self.font = pygame.font.Font("freesansbold.ttf", 25)
        self.text = text
        text_width, text_height = self.font.size(self.text)
        self.text_location = (self.x + (self.width - text_width) / 2, self.y + (self.length - text_height) / 2)
        self.pressed = False
        self.key = key
        self.colour = colour

    def button_draw(self):
        text = self.font.render(self.text,self.visibility,BLACK)
        if self.visibility:
            pygame.draw.rect(screen,self.colour,self.sprite)
            screen.blit(text,self.text_location)

            if self.pressed:
                pygame.draw.rect(screen,RED,self.sprite)
                screen.blit(text, self.text_location)


    def button_pressed(self):
        if self.visibility:
            mouse_pressed = pygame.mouse.get_pressed()[0] #change to 1 for right click, 0 is for left click
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

    def key_pressed(self):
        if self.visibility:
            key = pygame.key.get_pressed()
            mods = pygame.key.get_mods()
            # if self.pressed:
            #     self.pressed = False

            if self.key == "q":
                if key[pygame.K_q] and not pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "Q":
                if key[pygame.K_q] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "w":
                if key[pygame.K_w] and not mods:
                    self.pressed = True
            
            if self.key == "W":
                if key[pygame.K_w] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "e":
                if key[pygame.K_e] and not mods:
                    self.pressed = True

            if self.key == "E":
                if key[pygame.K_e] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "r":
                if key[pygame.K_r] and not mods:
                    self.pressed = True
            
            if self.key == "R":
                if key[pygame.K_r] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "t":
                if key[pygame.K_t] and not mods:
                    self.pressed = True

            if self.key == "T":
                if key[pygame.K_t] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "y":
                if key[pygame.K_y] and not mods:
                    self.pressed = True

            if self.key == "Y":
                if key[pygame.K_y] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "u":
                if key[pygame.K_u] and not mods:
                    self.pressed = True

            if self.key == "U":
                if key[pygame.K_u] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "i":
                if key[pygame.K_i] and not mods:
                    print("i")

            if self.key == "I":
                if key[pygame.K_i] and pygame.KMOD_SHIFT and mods:
                    print("I")

            if self.key == "o":
                if key[pygame.K_o] and not mods:
                    print("o")

            if self.key == "O":
                if key[pygame.K_o] and pygame.KMOD_SHIFT and mods:
                    print("O")

            if self.key == "p":
                if key[pygame.K_p] and not mods:
                    print("p")

            if self.key == "P":
                if key[pygame.K_p] and pygame.KMOD_SHIFT and mods:
                    print("P")

            if self.key == "a":
                if key[pygame.K_a] and not mods:
                    self.pressed = True

            if self.key == "A":
                if key[pygame.K_a] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "s":
                if key[pygame.K_s] and not mods:
                    self.pressed = True

            if self.key == "S":
                if key[pygame.K_s] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "d":
                if key[pygame.K_d] and not mods:
                    self.pressed = True

            if self.key == "D":
                if key[pygame.K_d] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "f":
                if key[pygame.K_f] and not mods:
                    self.pressed = True

            if self.key == "F":
                if key[pygame.K_f] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "g":
                if key[pygame.K_g] and not mods:
                    self.pressed = True

            if self.key == "G":
                if key[pygame.K_g] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "h":
                if key[pygame.K_h] and not mods:
                    self.pressed = True

            if self.key == "H":
                if key[pygame.K_h] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "j":
                if key[pygame.K_j] and not mods:
                    self.pressed = True
            
            if self.key == "J":
                if key[pygame.K_j] and pygame.KMOD_SHIFT and mods:
                    self.pressed = True

            if self.key == "l":
                if key[pygame.K_l] and not mods:
                    print("l")

            if self.key == "L":
                if key[pygame.K_l] and pygame.KMOD_SHIFT and mods:
                    print("L")
    def get_State(self):
        return self.pressed
    
    def get_Letter(self):
        if self.pressed:
            return self.key
        else:
            return "-"
    
    def button_state(self, state):
        self.visibility = state

    def all(self):
        self.button_pressed()
        self.key_pressed()
        self.button_draw()
    
        if self.pressed:
            return self.key
        else:
            return "-"