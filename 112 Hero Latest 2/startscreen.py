#This file contains the start screen for the game 
import pygame
from pygame_functions import *
#pygame_funtions from www.github.com/stevepaget/pygame_function
#only used for font rendering
import mainplay
import characterscreen

#template that was modified and added to was from https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py
class StartScreen(object):
    def __init__(self, width=1000, height=800, fps=50, title="112 Hero Start"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        self.font = pygame.font.Font('pixelfont.ttf',35)
        self.green = (0,138,0)
        self.white = (255,255,255)
        self.playing = True
    def click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            button = True
        else:
            button = False
        bL, bR = (12*self.width//20,(12*self.width//20 + self.width//8))
        bT, bB = (15*self.height//20, (15*self.height//20 + self.height//12))
        if button == True and mouse[0] > bL and mouse[0] < bR and mouse[1] > bT and mouse[1] <bB:
            mainplay.gameOverall.startScreen = False
            self.playing = False
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
        pass

    def redrawAll(self, screen):
        background = pygame.image.load("startbackground.jpg")
        screen.blit(background,(0,0))
        fire = pygame.image.load("fire.png")
        screen.blit(fire,(250,0))
        guitar = pygame.image.load("Guitar.png")
        screen.blit(guitar,(100,160))
        pygame.draw.rect(screen,self.green,(12*self.width//20,15*self.height//20,self.width//8,self.height//12))
        screen.blit(self.font.render('Play!',5,self.white),(97*self.width//160,123*self.height//160))

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

        #nextState = characterScreen.main()
        #pygame.quit()

'''
def main():
    game = StartScreen()
    game.run()

if __name__ == '__main__':
    main()'''