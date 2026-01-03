import pygame
 
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
 
#initialize pygame
pygame.init()
screen_size = (700, 500)
 
#create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
pygame.font.init()
 

#clock is used to set a max fps
clock = pygame.time.Clock()

# class Button:
#     def __init__(self,length,width,x,y,text,visibility,key,colour):
#         self.length = length
#         self.width = width
#         self.x = x
#         self.y = y
#         self.visibility = visibility
#         self.sprite = pygame.Rect(self.x,self.y,self.width,self.length)
#         self.font = pygame.font.Font("freesansbold.ttf", 25)
#         self.text = text
#         text_width, text_height = self.font.size(self.text)
#         self.text_location = (self.x + (self.width - text_width) / 2, self.y + (self.length - text_height) / 2)
#         self.pressed = False
#         self.key = key
#         self.colour = colour

#     def button_draw(self):
#         text = self.font.render(self.text,self.visibility,BLACK)
#         if self.visibility:
#             pygame.draw.rect(screen,self.colour,self.sprite)
#             screen.blit(text,self.text_location)

#             if self.pressed:
#                 pygame.draw.rect(screen,RED,self.sprite)
#                 screen.blit(text, self.text_location)


#     def button_pressed(self):
#         if self.visibility:
#             mouse_pressed = pygame.mouse.get_pressed()[0] #change to 1 for right click, 0 is for left click
#             mouse_pos = pygame.mouse.get_pos()
#             if pygame.Rect.collidepoint(self.sprite, mouse_pos):
#                 if mouse_pressed == True:
#                     self.pressed = True
#                     return True
#                 else:
#                     self.pressed = False
#                     return False
#             else:
#                 self.pressed = False

#     def key_pressed(self):
#         if self.visibility:
#             key = pygame.key.get_pressed()
#             mods = pygame.key.get_mods()
#             # if self.pressed:
#             #     self.pressed = False

#             if self.key == "q":
#                 if key[pygame.K_q] and not pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "Q":
#                 if key[pygame.K_q] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "w":
#                 if key[pygame.K_w] and not mods:
#                     self.pressed = True
            
#             if self.key == "W":
#                 if key[pygame.K_w] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "e":
#                 if key[pygame.K_e] and not mods:
#                     self.pressed = True

#             if self.key == "E":
#                 if key[pygame.K_e] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "r":
#                 if key[pygame.K_r] and not mods:
#                     self.pressed = True
            
#             if self.key == "R":
#                 if key[pygame.K_r] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "t":
#                 if key[pygame.K_t] and not mods:
#                     self.pressed = True

#             if self.key == "T":
#                 if key[pygame.K_t] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "y":
#                 if key[pygame.K_y] and not mods:
#                     self.pressed = True

#             if self.key == "Y":
#                 if key[pygame.K_y] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "u":
#                 if key[pygame.K_u] and not mods:
#                     self.pressed = True

#             if self.key == "U":
#                 if key[pygame.K_u] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "i":
#                 if key[pygame.K_i] and not mods:
#                     print("i")

#             if self.key == "I":
#                 if key[pygame.K_i] and pygame.KMOD_SHIFT and mods:
#                     print("I")

#             if self.key == "o":
#                 if key[pygame.K_o] and not mods:
#                     print("o")

#             if self.key == "O":
#                 if key[pygame.K_o] and pygame.KMOD_SHIFT and mods:
#                     print("O")

#             if self.key == "p":
#                 if key[pygame.K_p] and not mods:
#                     print("p")

#             if self.key == "P":
#                 if key[pygame.K_p] and pygame.KMOD_SHIFT and mods:
#                     print("P")

#             if self.key == "a":
#                 if key[pygame.K_a] and not mods:
#                     self.pressed = True

#             if self.key == "A":
#                 if key[pygame.K_a] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "s":
#                 if key[pygame.K_s] and not mods:
#                     self.pressed = True

#             if self.key == "S":
#                 if key[pygame.K_s] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "d":
#                 if key[pygame.K_d] and not mods:
#                     self.pressed = True

#             if self.key == "D":
#                 if key[pygame.K_d] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "f":
#                 if key[pygame.K_f] and not mods:
#                     self.pressed = True

#             if self.key == "F":
#                 if key[pygame.K_f] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "g":
#                 if key[pygame.K_g] and not mods:
#                     self.pressed = True

#             if self.key == "G":
#                 if key[pygame.K_g] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "h":
#                 if key[pygame.K_h] and not mods:
#                     self.pressed = True

#             if self.key == "H":
#                 if key[pygame.K_h] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "j":
#                 if key[pygame.K_j] and not mods:
#                     self.pressed = True
            
#             if self.key == "J":
#                 if key[pygame.K_j] and pygame.KMOD_SHIFT and mods:
#                     self.pressed = True

#             if self.key == "l":
#                 if key[pygame.K_l] and not mods:
#                     print("l")

#             if self.key == "L":
#                 if key[pygame.K_l] and pygame.KMOD_SHIFT and mods:
#                     print("L")
#     def get_State(self):
#         return self.pressed
    
#     def get_Letter(self):
#         if self.pressed:
#             return self.key
#         else:
#             return "-"
    
#     def button_state(self, state):
#         self.visibility = state

#     def all(self):
#         self.button_pressed()
#         self.key_pressed()
#         self.button_draw()
    
#         if self.pressed:
#             return self.key
#         else:
#             return "-"

class Button:
    """ A class that contains all buttons used in the game, which can
    be interacted with using either the mouse or keyboard. """

    # initializes the button
    def __init__(self,length,width,x,y,text,visibility,key,colour):
        """ The init method initializes the button's properties, these
        inclue the following: size, positioning, text, visibility, key
        assignment, and the color.
        
        The arguments are the length / height (int), the width (int), the
        x and y coordinates of the button's position (int) (reminder this
        is starting from the top left corner), the text that's displayed
        (str), the visibility status (bool), the key that's being triggered
        (str), and the colour (all the colours are set as RGBs at the top
        of the code). """

        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.visibility = visibility
        self.sprite = pygame.Rect(self.x,self.y,self.width,self.length)

        # sets sizing of font and the button itself
        font_size = int(self.length* 0.1) # adjusts font to fit button size
        self.font = pygame.font.Font("freesansbold.ttf", font_size)
        self.text = text
        text_width, text_height = self.font.size(self.text) # text size
        self.text_location = (self.x + (self.width - text_width) / 2, self.y + (self.length - text_height) / 2)

        self.pressed = False # default button press status
        self.key = key
        self.colour = colour

    # draws the button on the screen
    def button_draw(self):
        """ Draws the button onto the screen (reminder if the visibility is set
        to true the buttons will show, otherwise they won't). 
        
        The if statement check if the buttons' visibility is true, if so the text
        will be rendered. In the case that the button has a keyboard key assosciated
        with it, meaning it's a piano key, the rectangle would be rendered over it.
        Otherwise it is just the text. """

        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)

        if self.visibility: # if the button is black the text is white and vise versa
            if self.colour == BLACK:
                text = self.font.render(self.text, self.visibility, WHITE)
            else:
                text = self.font.render(self.text, self.visibility, BLACK)
            if self.key != "":
                pygame.draw.rect(screen,self.colour,self.sprite)
                screen.blit(text, self.text_location)

        if self.pressed and self.key != '':
            pygame.draw.rect(screen,RED,self.sprite)
            screen.blit(text, self.text_location)

    # checks if the button is pressed from the mouse
    def button_pressed(self):
        """ Checks if the button is being pressed by the mouse specifically. Inside
        we take in if the mouse is being pressed (specifically the left (if you want
        to change it to the right you would edit the 0 to a 1)), along with the position
        of where the mouse is clicking. The code checks if the position of the mouse is
        clicking inside the button. """

        mouse_pressed = pygame.mouse.get_pressed()[0] # 0 for left click, 1 for right click
        mouse_pos = pygame.mouse.get_pos()

        if pygame.Rect.collidepoint(self.sprite, mouse_pos): # is the mouse inside the button
            if mouse_pressed == True: # if clicked set button as pressed
                self.pressed = True
                return True
            else:
                self.pressed = False
        else:
            self.pressed = False
        return False

    # checks if button is pressed from the keyboard
    def key_pressed(self):
        """ Checks if the keyboard is taking input, specifically the letters in the first
        two rows of the keyboard, as well as there is a version for when shift is being
        pressed. It's used to check when just a letter key is being pressed and not both. """

        key = pygame.key.get_pressed() # gets what keys are pressed
        mods = pygame.key.get_mods() # gets modifier key (shift)

        if self.key == "q":
            if key[pygame.K_q]  and not mods: # key pressed without modifiers
                self.pressed = True # mark as pressed

        if self.key == "Q":
            if key[pygame.K_q] and pygame.KMOD_SHIFT and mods: # key pressed with modifier (shift)
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
                self.pressed = True

        if self.key == "L":
            if key[pygame.K_l] and pygame.KMOD_SHIFT and mods:
                self.pressed = True

    # checks the state of the button
    def get_State(self):
        """ It just checks if the button is being pressed and returns the status """

        return self.pressed

    # calls all the methods together
    def all(self):
        """ All methods have been placed into one method saving lines """

        self.button_pressed() # is it pressed by the mouse
        self.key_pressed() # is it pressed by a key
        self.button_draw() # draws the button
    
        if self.pressed: # returns - when no key is pressed/ gives status of button
            return self.key
        else:
            return "-"

    # sets the button's visibility
    def button_state(self, state):
        """ Returns the visibility status of the button """

        self.visibility = state



    # def button_visibility(self):
    #     if self.visibility == True:
    #         print("x")


# buttons
# instance = Button(300,400,100,200,"Hello, This is button",True,"Q",WHITE) #Length, width, x,y, text, visbility, Key assignment, Colour
# cool = Button(200,200,200,100, "Press to light up",True,"f",WHITE)


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     #clear the screen
#     screen.fill(BLACK)

#     # functions in a single function
#     instance.all()
#     cool.all()


#     # flip() updates the screen to make our changes visible
#     pygame.display.flip()

#     # how many updates per second
#     clock.tick(60)
 
# pygame.quit()