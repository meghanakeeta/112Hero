##This file contains the song selection screen for the game. A song will
#be chosen to play
import pygame
from pygame_functions import *
#pygame_funtions from www.github.com/stevepaget/pygame_function
#only used for font rendering
import mainplay


#template that was modified and added to was from https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py
class SongScreen(object):
    def __init__(self, width=1000, height=800, fps=50, title="112 Hero Songs"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        self.font = pygame.font.Font('pixelfont.ttf',60)
        self.smallFont = pygame.font.Font('pixelfont.ttf',40)
        self.green = (0,138,0)
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.playing = True

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

    def click(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0]==1:
            button = True
        else:
            button = False
        b1L, b1R = (2*self.width//20,(2*self.width//20+8*self.width//10))
        b1T, b1B = (6*self.height//40,(6*self.height//40+self.height//8))
        b2L, b2R = (2*self.width//20,(2*self.width//20+8*self.width//10))
        b2T, b2B = (13*self.height//40,(13*self.height//40+self.height//8))
        b3L, b3R = (2*self.width//20,(2*self.width//20+8*self.width//10))
        b3T, b3B = (20*self.height//40,(20*self.height//40+self.height//8))
        b4L, b4R = (2*self.width//20,(2*self.width//20+8*self.width//10))
        b4T, b4B = (27*self.height//40,(27*self.height//40+self.height//8))
        b5L, b5R = (2*self.width//20,(2*self.width//20+8*self.width//10))
        b5T, b5B = (34*self.height//40,(34*self.height//40+self.height//8))
        if button == True and mouse[0] > b1L and mouse[0] < b1R and mouse[1] > b1T and mouse[1] <b1B:
            mainplay.gameOverall.song = 1
            mainplay.gameOverall.songScreen = False
            self.playing = False
        elif button == True and mouse[0] > b2L and mouse[0] < b2R and mouse[1] > b2T and mouse[1] <b2B:
            mainplay.gameOverall.song = 2
            mainplay.gameOverall.songScreen = False
            self.playing = False
        elif button == True and mouse[0] > b3L and mouse[0] < b3R and mouse[1] > b3T and mouse[1] <b3B:
            mainplay.gameOverall.song = 3
            mainplay.gameOverall.songScreen = False
            self.playing = False
        elif button == True and mouse[0] > b4L and mouse[0] < b4R and mouse[1] > b4T and mouse[1] <b4B:
            mainplay.gameOverall.song = 4
            mainplay.gameOverall.songScreen = False
            self.playing = False
        elif button == True and mouse[0] > b5L and mouse[0] < b5R and mouse[1] > b5T and mouse[1] <b5B:
            mainplay.gameOverall.song = 5
            mainplay.gameOverall.songScreen = False
            self.playing = False
    def redrawAll(self, screen):
        background = pygame.image.load("back2.jpg")
        screen.blit(background,(0,0))
        screen.blit(self.font.render('Pick a song to perform',5,self.white),(80,30))
        
        pygame.draw.rect(screen,self.white,(2*self.width//20,6*self.height//40,8*self.width//10,self.height//8))
        screen.blit(self.smallFont.render('Eye of the tiger',5,self.black),(300,150))

        pygame.draw.rect(screen,self.white,(2*self.width//20,13*self.height//40,8*self.width//10,self.height//8))
        screen.blit(self.smallFont.render('Hit me with your best shot',5,self.black),(200,290))

        pygame.draw.rect(screen,self.white,(2*self.width//20,20*self.height//40,8*self.width//10,self.height//8))
        screen.blit(self.smallFont.render('Smoke on the water',5,self.black),(280,430))

        pygame.draw.rect(screen,self.white,(2*self.width//20,27*self.height//40,8*self.width//10,self.height//8))
        screen.blit(self.smallFont.render('Sunshine of your Love',5,self.black),(230,570))

        pygame.draw.rect(screen,self.white,(2*self.width//20,34*self.height//40,8*self.width//10,self.height//8))
        screen.blit(self.smallFont.render('Slow Ride',5,self.black),(400,710))

        
    def isKeyPressed(self, key):
        #return whether a specific key is being held 
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

        #pygame.quit()


def main():
    game = SongScreen()
    game.run()

if __name__ == '__main__':
    main()

