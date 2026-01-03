import pygame
import katebutton #seperate file that runs Kate's button class
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (100,0,200)
 
# initialize pygame
pygame.init()
screen_size = (1240, 720)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
pygame.mixer.init()
pygame.mixer.set_num_channels(24) #Sets how many channels for volume

# clock is used to set a max fps
clock = pygame.time.Clock()


class Piano:
    def __init__(self,keys):
        ''' self.keys determines how many keys you want on your piano (the limit is 24) and each key is numbered to determine if it's in the 
        self.black_keys list or the self.white_keys list'''
        self.keys = keys
        self.bw = [] #This is an empty list that is to be used in the create method
        self.black_keys = (2,4,7,9,11,14,16,19,21,23)
        self.white_keys = (1,3,5,6,8,10,12,13,15,17,18,20,22,24)

    def create(self):
        '''There are many different variables that all serve different purposes. Each variable is used to assist the creation of each instance of
        the key class. The w variable is for white keys, the b variable is for black keys, the rotate is for black keys to determine if they're in 
        groups of 2 or 3. The switch and used variables are used in each group of 2 or 3 to determine if the grouping has completed. The b_fixed
        variable is used to fix the positions of the black keys of where the notes are in the Keys class. Generating the white keys are easy first 
        and you generate the white keys first because the black keys would get covered if they were with or first.'''
        w = 0
        b = 0
        rotate = 0
        switch = False
        used = False
        b_fixed = 0

        for i in (self.white_keys):
            self.bw.append(Keys(i,w,0)) #The Keys class gets the number, the position, and the calibration which white doesn't need so it's at 0
            w += 1
        for i in (self.black_keys):
            if rotate == 2 and not switch: #The first group of black keys is two, so if two are already made, switch turns to true and the group of 3 begins. Used turns to True also for the last If statement
                b += 1
                switch = True
                rotate = 0
                used = True
            elif rotate == 3 and switch: #The group of three begins, once it's made switch turns False and rotate is set back to 0. Used turns True for the last If Statement.
                b += 1
                switch = False
                rotate = 0
                used = True
            else:
                if used:
                    self.bw.append(Keys(i,b,b_fixed)) #Number, Position, Calibration when either the group of two or three get called upon.
                    rotate += 1
                    b += 1
                    b_fixed += 1
                self.bw.append(Keys(i,b,b_fixed)) #Number, Position, Calibration
                b_fixed += 1
                b += 1
                rotate += 1
                used = False
        return self.bw #returns the list from the init 
class Keys:
    def __init__(self,num,value,calibrate):
        '''The three values that it receives from the Create method in the Piano class is the number, the value(position) and for black keys
        the calibration due to the fact that the value does not sync up with the black key lists and therefore cannot read it unless it uses
        the calibration variable.  The Scaled number is used to edit all notes at once so that everything is equal. Self.check is used to check
        if a key is pressed or not in the Sound method.'''
        self.number = num
        self.black_keys = (2,4,7,9,11,14,16,19,21,23)
        self.black_key_notes = ("w","e","t","y","u")*2
        self.white_keys = (1,3,5,6,8,10,12,13,15,17,18,20,22,24)
        self.white_key_notes = ("a","s","d","f","g","h","j")*2
        scaled_num = 80
        self.value = value
        self.calibrate = calibrate
        self.status = False
        self.check = 0

    
        if self.number in self.white_keys: #Length and Width of a white key and the position
            self.xpos = (scaled_num+8)*value + 8
            self.ypos = screen_size[1]-(scaled_num*3.5)
            self.length = scaled_num*3.5
            self.width = scaled_num
            if self.number > 12:
                #To get text and key, while identical, you index the number from the white keys list and then capitalize if it's greater than 12. 
                self.kbutton = katebutton.Button(self.length,self.width,self.xpos,self.ypos,self.white_key_notes[self.white_keys.index(self.number)].capitalize(),True,self.white_key_notes[self.white_keys.index(self.number)].capitalize(),WHITE)#Length, width, x,y, text, visbility, Key assignment, Colour
            else:
                self.kbutton = katebutton.Button(self.length,self.width,self.xpos,self.ypos,self.white_key_notes[self.white_keys.index(self.number)],True,self.white_key_notes[self.white_keys.index(self.number)],WHITE)#Length, width, x,y, text, visbility, Key assignment, Colour
        elif self.number in self.black_keys:
            self.xpos = ((scaled_num+8) * value) + (scaled_num-((scaled_num)/4)) + 12 #Length and Width of a Black key and the position
            self.ypos = screen_size[1]-(scaled_num*3.5)
            self.length = scaled_num * 2.1
            self.width = scaled_num/2
            if self.number > 12:
                #Same idea but we use the calibrate variable as mentioned above to correct everything instead.
                self.kbutton = katebutton.Button(self.length,self.width,self.xpos,self.ypos,self.black_key_notes[self.calibrate].capitalize(),True,self.black_key_notes[self.calibrate].capitalize(),BLACK)#Length, width, x,y, text, visbility, Key assignment, Colour
            else:
                self.kbutton = katebutton.Button(self.length,self.width,self.xpos,self.ypos,self.black_key_notes[self.calibrate],True,self.black_key_notes[self.calibrate],BLACK)#Length, width, x,y, text, visbility, Key assignment, Colour

    def button(self):
        '''Uses the button class from Kate's code to return the self.kbutton variable, all properties of the button can be seen above'''
        return self.kbutton
            
    def Sound(self,state):
        '''Determines if the class has a self.check value of 0, if so, moves on to check which key is being pressed with the state variable
        afterwards if it is then self.check variable will become 1 and it won't be let go again until it reads "-" from that instance. When it is played
        it reaches for the channel it is specified in and plays the note from that file that is selected. '''
        if self.check == 0:
            if state == "a":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("Piano Notes\Octave 1\C4.mp3"))
            if state == "A":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(12).play(pygame.mixer.Sound("Piano Notes\Octave 2\C5.mp3"))
            if state == "s":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Piano Notes\Octave 1\D.mp3"))
            if state == "S":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(13).play(pygame.mixer.Sound("Piano Notes\Octave 2\D5.mp3"))
            if state == "d":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("Piano Notes\Octave 1\E.mp3"))
            if state == "D":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(14).play(pygame.mixer.Sound("Piano Notes\Octave 2\E5.mp3"))
            if state == "f":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(3).play(pygame.mixer.Sound("Piano Notes\Octave 1\F.mp3"))
            if state == "F":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(15).play(pygame.mixer.Sound("Piano Notes\Octave 2\F5.mp3"))
            if state == "g":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(4).play(pygame.mixer.Sound("Piano Notes\Octave 1\G.mp3"))
            if state == "G":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(16).play(pygame.mixer.Sound("Piano Notes\Octave 2\G5.mp3"))
            if state == "h":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(5).play(pygame.mixer.Sound("Piano Notes\Octave 1\A.mp3"))
            if state == "H":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(17).play(pygame.mixer.Sound("Piano Notes\Octave 2\A5.mp3"))
            if state == "j":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(6).play(pygame.mixer.Sound("Piano Notes\Octave 1\B.mp3"))
            if state == "J":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(18).play(pygame.mixer.Sound("Piano Notes\Octave 2\B5.mp3"))
            if state == "w":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(7).play(pygame.mixer.Sound("Piano Notes\Octave 1\C#.mp3"))
            if state == "W":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(19).play(pygame.mixer.Sound("Piano Notes\Octave 2\C#5.mp3"))
            if state == "e":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(8).play(pygame.mixer.Sound("Piano Notes\Octave 1\D#.mp3"))
            if state == "E":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(20).play(pygame.mixer.Sound("Piano Notes\Octave 2\D#5.mp3"))
            if state == "t":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(9).play(pygame.mixer.Sound("Piano Notes\Octave 1\F#.mp3"))
            if state == "T":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(21).play(pygame.mixer.Sound("Piano Notes\Octave 2\F#5.mp3"))
            if state == "y":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(10).play(pygame.mixer.Sound("Piano Notes\Octave 1\G#.mp3"))
            if state == "Y":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(22).play(pygame.mixer.Sound("Piano Notes\Octave 2\G#5.mp3"))
            if state == "u":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(11).play(pygame.mixer.Sound("Piano Notes\Octave 1\A#.mp3"))
            if state == "U":
                self.status = True
                self.check += 1
                pygame.mixer.Channel(23).play(pygame.mixer.Sound("Piano Notes\Octave 2\A#5.mp3"))

        elif state == "-": #Still part of the sound method.
            self.check = 0

            
Pianissimo = Piano(24) 
BwKeys = Pianissimo.create()
BwwKeys = BwKeys[::-1]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    #clear the screen
    screen.fill(PURPLE)
     
    # draw to the screen
    # YOUR CODE HERE

    for key in BwKeys:
        # key.button().button_pressed()
        # print(key.button().key_pressed())
        # key.Sound(key.button().get_Letter())
        # key.button().button_draw()
        key.Sound(key.button().all())
    # for key in BwwKeys:
    #     key.button().draw
        


 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()