#This file contains the character choosing screen for the game. A sprite can
#modified that will appear as your character in the game
import pygame
from pygame_functions import *
#pygame_funtions from www.github.com/stevepaget/pygame_function
#only used for font rendering
import mainplay
import songscreen
import gamescreen

#pygame_funtions from www.github.com/stevepaget/pygame_function
#only used for font rendering

#template that was modified and added to was from https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py
class CharacterScreen(object):
    def __init__(self, width=1000, height=800, fps=50, title="112 Hero Characters"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        self.largeFont = pygame.font.Font('pixelfont.ttf',60)
        self.smallFont = pygame.font.Font('pixelfont.ttf',40)
        self.font = pygame.font.Font('pixelfont.ttf',20)
        self.white = (255,255,255)
        self.blue = (0,0,255)
        self.red = (255,0,0)
        self.black = (0,0,0)
        self.pink = (255,0,255)
        self.grey = (127,127,127)
        self.green = (0,138,0)
        self.player = 1
        self.shirt = True
        self.skirt = True
        self.pants = True
        self.shoes = True
        self.spriteImage()
        self.spritesheetInit()
        self.i = 0
        self.playing = True
    
    def spritesheetInit(self):
        self.sprite = self.combo1
        self.spriteWidth = self.sprite.get_width()
        self.spriteHeight = self.sprite.get_height()
        self.cW = self.spriteWidth/4
        self.cH = self.spriteHeight/4
        self.spriteCrop = [(0,0,self.cW,self.cH),(self.cW,0,self.cW,self.cH),(2*self.cW,0,self.cW,self.cH),(3*self.cW,0,self.cW,self.cH),
                            (0,self.cH,self.cW,self.cH),(self.cW,self.cH,self.cW,self.cH),(2*self.cW,self.cH,self.cW,self.cH),(3*self.cW,self.cH,self.cW,self.cH),
                            (0,2*self.cH,self.cW,self.cH),(self.cW,2*self.cH,self.cW,self.cH),(2*self.cW,2*self.cH,self.cW,self.cH),(3*self.cW,2*self.cH,self.cW,self.cH),
                            (0,3*self.cH,self.cW,self.cH),(self.cW,3*self.cH,self.cW,self.cH),(2*self.cW,3*self.cH,self.cW,self.cH),(3*self.cW,3*self.cH,self.cW,self.cH),
                                ]
        self.counter = 0
    
    
    def spriteDraw(self,screen):
        x0,y0,x1,y1 = self.spriteCrop[self.counter] 
        screen.blit(self.sprite,(80,160),(x0,y0,
                x1,y1))
    
    def click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0]==1:
            button = True
        else:
            button = False
        b1L,b1R = (10*self.width//20,(10*self.width//20 + self.width//10))
        b1T, b1B = (4*self.height/20,(4*self.height/20+ self.height/15))
        b2L,b2R = (15*self.width/20,(15*self.width/20 + self.width/10))
        b2T, b2B = (4*self.height/20,(4*self.height/20+ self.height/15))
        b3L,b3R = (10*self.width//20,(10*self.width//20 + self.width//10))
        b3T, b3B = (8*self.height/20,(8*self.height/20+ self.height/15))
        b4L,b4R = (15*self.width/20,(15*self.width/20 + self.width/10))
        b4T, b4B = (8*self.height/20,(8*self.height/20+ self.height/15))
        b5L,b5R = (10*self.width//20,(10*self.width//20 + self.width//10))
        b5T, b5B = (12*self.height/20,(12*self.height/20+ self.height/15))
        b6L,b6R = (15*self.width/20,(15*self.width/20 + self.width/10))
        b6T, b6B = (12*self.height/20,(12*self.height/20+ self.height/15))
        b7L,b7R = (10*self.width//20,(10*self.width//20 + self.width//10))
        b7T, b7B = (16*self.height/20,(16*self.height/20+ self.height/15))
        b8L,b8R = (15*self.width/20,(15*self.width/20 + self.width/10))
        b8T, b8B = (16*self.height/20,(16*self.height/20+ self.height/15))
    
        bGL, bGR = (17*self.width//20, (17*self.width//20 + self.width//10))
        bGT, bGB = (18*self.height/20,(18*self.height/20+ self.height/15))

        if button == True and mouse[0] > b1L and mouse[0] < b1R and mouse[1] > b1T and mouse[1] <b1B:
            self.shirt = True
        elif button == True and mouse[0] > b2L and mouse[0] < b2R and mouse[1] > b2T and mouse[1] <b2B:
            self.shirt = False
        elif button == True and mouse[0] > b3L and mouse[0] < b3R and mouse[1] > b3T and mouse[1] <b3B:
            self.skirt = True
        elif button == True and mouse[0] > b4L and mouse[0] < b4R and mouse[1] > b4T and mouse[1] <b4B:
            self.skirt = False
        elif button == True and mouse[0] > b5L and mouse[0] < b5R and mouse[1] > b5T and mouse[1] <b5B:
            self.pants = True
        elif button == True and mouse[0] > b6L and mouse[0] < b6R and mouse[1] > b6T and mouse[1] <b6B:
            self.pants = False
        elif button == True and mouse[0] > b7L and mouse[0] < b7R and mouse[1] > b7T and mouse[1] <b7B:
            self.shoes = True
        elif button == True and mouse[0] > b8L and mouse[0] < b8R and mouse[1] > b8T and mouse[1] <b8B:
            self.shoes = False
        self.playerChoice()
        if button == True and mouse[0] > bGL and mouse[0] < bGR and mouse[1] > bGT and mouse[1] <bGB:
            mainplay.gameOverall.characterScreen = False
            self.playing = False
            

            '''mainplay.gameOverall.songScreen = True
            print(mainplay.gameOverall.characterScreen)'''
    
    def playerChoice(self):
        if self.skirt == True and self.shirt == True and self.pants == True and self.shoes == True:
            self.player = 1
            self.sprite = self.combo1
        elif self.skirt == True and self.shirt == False and self.pants == True and self.shoes == True:
            self.player = 2
            self.sprite = self.combo2
        elif self.skirt == True and self.shirt == False and self.pants == False and self.shoes == True:
            self.player = 3
            self.sprite = self.combo3
        elif self.skirt == True and self.shirt == False and self.pants == False and self.shoes == False:
            self.player = 4
            self.sprite = self.combo4
        elif self.skirt == True and self.shirt == False and self.pants == True and self.shoes == False:
            self.player = 5
            self.sprite = self.combo5
        elif self.skirt == True and self.shirt == True and self.pants == True and self.shoes == False:
            self.player = 6
            self.sprite = self.combo6
        elif self.skirt == True and self.shirt == True and self.pants == False and self.shoes == False:
            self.player = 7
            self.sprite = self.combo7
        elif self.skirt == True and self.shirt == True and self.pants == False and self.shoes == True:
            self.player = 8
            self.sprite = self.combo8
        elif self.skirt == False and self.shirt == True and self.pants == True and self.shoes == True:
            self.player = 9
            self.sprite = self.combo9
        elif self.skirt == False and self.shirt == True and self.pants == False and self.shoes == False:
            self.player = 10
            self.sprite = self.combo10
        elif self.skirt == False and self.shirt == False and self.pants == True and self.shoes == True:
            self.player = 11
            self.sprite = self.combo11
        elif self.skirt == False and self.shirt == False and self.pants == False and self.shoes == True:
            self.player = 12
            self.sprite = self.combo12
        elif self.skirt == False and self.shirt == False and self.pants == False and self.shoes == False:
            self.player = 13
            self.sprite = self.combo13
        elif self.skirt == False and self.shirt == False and self.pants == True and self.shoes == False:
            self.player = 14
            self.sprite = self.combo14
        elif self.skirt == False and self.shirt == True and self.pants == True and self.shoes == False:
            self.player = 15
            self.sprite = self.combo15
        elif self.skirt == False and self.shirt == True and self.pants == False and self.shoes == True:
            self.player = 16
            self.sprite = self.combo16

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        self.counter = (self.counter+1) % 16
    

    def optionsDraw(self,screen):
        screen.blit(self.largeFont.render('Design your player',5,self.white),(2*self.width//15,1*self.height//20))
        #Create buttons to light up when pressed in future
        pygame.draw.rect(screen,self.grey,(10*self.width//20,4*self.height//20,self.width//10,self.height//15))
        pygame.draw.rect(screen,self.blue,(15*self.width//20,4*self.height//20,self.width//10,self.height//15))
        screen.blit(self.font.render('grey',5,self.black),(42*self.width//80,18*self.height//80))
        screen.blit(self.font.render('blue',5,self.black),(62*self.width//80,18*self.height//80))
        
        pygame.draw.rect(screen,self.blue,(10*self.width//20,8*self.height//20,self.width//10,self.height//15))
        pygame.draw.rect(screen,self.pink,(15*self.width//20,8*self.height//20,self.width//10,self.height//15))
        screen.blit(self.font.render('blue',5,self.black),(42*self.width//80,34*self.height//80))
        screen.blit(self.font.render('pink',5,self.black),(62*self.width//80,34*self.height//80))

        pygame.draw.rect(screen,self.grey,(10*self.width//20,12*self.height//20,self.width//10,self.height//15))
        pygame.draw.rect(screen,self.red,(15*self.width//20,12*self.height//20,self.width//10,self.height//15))
        screen.blit(self.font.render('grey',5,self.black),(42*self.width//80,50*self.height//80))
        screen.blit(self.font.render('red',5,self.black),(62*self.width//80,50*self.height//80))

        pygame.draw.rect(screen,self.white,(10*self.width//20,16*self.height//20,self.width//10,self.height//15))
        pygame.draw.rect(screen,self.blue,(15*self.width//20,16*self.height//20,self.width//10,self.height//15))
        screen.blit(self.font.render('white',5,self.black),(42*self.width//80,66*self.height//80))
        screen.blit(self.font.render('blue',5,self.black),(62*self.width//80,66*self.height//80))

        screen.blit(self.smallFont.render('Shirt',5,self.white),(49*self.width//80,17*self.height//80))
        screen.blit(self.smallFont.render('Skirt',5,self.white),(49*self.width//80,33*self.height//80))
        screen.blit(self.smallFont.render('Pants',5,self.white),(48*self.width//80,49*self.height//80))
        screen.blit(self.smallFont.render('Shoes',5,self.white),(48*self.width//80,65*self.height//80))

        pygame.draw.rect(screen,self.green,(17*self.width//20,18*self.height//20,self.width//10,self.height//15))
        screen.blit(self.font.render('Next!',5,self.black),(69*self.width//80,74*self.height//80))

    def redrawAll(self, screen):
        background = pygame.image.load("charback1.jpg")
        screen.blit(background,(0,0))
        self.optionsDraw(screen)
        self.spriteDraw(screen)
        
    def spriteImage(self):
        self.combo1 = pygame.image.load("V1.png")
        self.combo2 = pygame.image.load("V2.png")
        self.combo3 = pygame.image.load("V3.png")
        self.combo4 = pygame.image.load("V4.png")
        self.combo5 = pygame.image.load("V5.png")
        self.combo6 = pygame.image.load("V6.png")
        self.combo7 = pygame.image.load("V7.png")
        self.combo8 = pygame.image.load("V8.png")
        self.combo9 = pygame.image.load("V9.png")
        self.combo10 = pygame.image.load("V10.png")
        self.combo11 = pygame.image.load("V11.png")
        self.combo12 = pygame.image.load("V12.png")
        self.combo13 = pygame.image.load("V13.png")
        self.combo14 = pygame.image.load("V14.png")
        self.combo15 = pygame.image.load("V15.png")
        self.combo16 = pygame.image.load("V16.png")
        self.sprite = self.combo1


    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)


    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)
 
        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        #self.init()
        while self.playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            self.click()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    self.playing = False
                    mainplay.gameOverall.startScreen=False
                    mainplay.gameOverall.characterScreen = False
                    mainplay.gameOverall.songScreen = False
                    mainplay.gameOverall.gameScreen = False
                    mainplay.gameOverall.endScreen = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        #nextState = songscreen.main()
        #pygame.quit()


def main():
    game = CharacterScreen()
    game.run()

if __name__ == '__main__':
    main()