##This file contains the end screen for the game. This shows up when the 
#game is over.
import pygame
from pygame_functions import *
#pygame_funtions from www.github.com/stevepaget/pygame_function
#only used for font rendering
import mainplay
import gamescreen
from os import path

hsNameFile = "highname.txt"

#template that was modified and added to was from https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py
class EndScreen(object):
    def __init__(self, width=1000, height=800, fps=50, title="112 Hero End"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        self.font = pygame.font.Font('pixelfont.ttf',80)
        self.sfont = pygame.font.Font('pixelfont.ttf',30)
        self.ssfont = pygame.font.Font('pixelfont.ttf',20)
        self.green = (0,138,0)
        self.white = (255,255,255)
        self.congrats = False
        self.playing = True
        self.update = False
        self.dir = path.dirname(__file__)
        
        
    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass
    
    def click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0]==1:
            button = True
        else:
            button = False
        b1L,b1R = (15*self.width//20,(15*self.width//20 + 1.4*self.width//6))
        b1T, b1B = (17*self.height//20,(17*self.height//20+ self.height//12))
        if button == True and mouse[0] > b1L and mouse[0] < b1R and mouse[1] > b1T and mouse[1] <b1B:
            mainplay.gameOverall.score = 0
            mainplay.gameOverall.startScreen = True
            mainplay.gameOverall.endChoice.congrats= False
            mainplay.gameOverall.characterScreen = True
            mainplay.gameOverall.songScreen = True
            mainplay.gameOverall.gameScreen = True
            mainplay.gameOverall.endScreen = True
            mainplay.gameOverall.run()


    def keyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_SPACE:
            mainplay.gameOverall.score = 0
            mainplay.gameOverall.startScreen = True
            mainplay.gameOverall.endChoice.congrats= False
            mainplay.gameOverall.characterScreen = True
            mainplay.gameOverall.songScreen = True
            mainplay.gameOverall.gameScreen = True
            mainplay.gameOverall.endScreen = True
            mainplay.gameOverall.run()
        
            

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        background = pygame.image.load("startbackground.jpg")
        screen.blit(background,(0,0))
        pygame.draw.rect(screen,(0,0,0),(15*self.width/80,self.height/4,50*self.width/80,self.height/2))
        screen.blit(self.font.render('The End!',5,self.white),(7*self.width//24,7*self.height//24))
        screen.blit(self.font.render(f'Score:{mainplay.gameOverall.score}',5,self.white),(13*self.width//48,10*self.height//24))
        screen.blit(self.sfont.render(f'High Score: {mainplay.gameOverall.highscore}',5,(0,0,0)),(3*self.width/80,2*self.height//80))
        
        pygame.draw.rect(screen,self.white,(15*self.width//20,17*self.height//20,1.4*self.width//6,self.height//12))
        screen.blit(self.sfont.render('Play Again',5,(0,0,0)),(123*self.width//160,70*self.height//80))
        
        if self.congrats:
            screen.blit(self.sfont.render('New high score!!',5,self.white),(17*self.width//48,13*self.height//24))
            
    
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
        #self.playing = True
        while self.playing:
            if mainplay.gameOverall.score > mainplay.gameOverall.highscore:
                mainplay.gameOverall.highscore = mainplay.gameOverall.score
                with open(path.join(mainplay.gameOverall.dir,mainplay.hsFile), 'w') as hfile:
                    write = str(mainplay.gameOverall.score)
                    hfile.write(write)
                self.congrats = True
        
     
            else:
                pass
            



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

        pygame.quit()


def main():
    game = EndScreen()
    game.run()

if __name__ == '__main__':
    main()