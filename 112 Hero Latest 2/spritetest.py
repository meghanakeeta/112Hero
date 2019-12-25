#this file was used to test teh sprite and make it work
import pygame

class PygameGame(object):

    def init(self):
        self.spriteSheet = pygame.image.load("V1.png")
        self.sprite = None
        self.width = self.spriteSheet.get_width()
        self.height = self.spriteSheet.get_height()
        self.cW = self.width/4
        self.cH = self.height/4
        self.spriteCrop = [(0,0,self.cW,self.cH),(self.cW,0,self.cW,self.cH),(2*self.cW,0,self.cW,self.cH),(3*self.cW,0,self.cW,self.cH),
                            (0,self.cH,self.cW,self.cH),(self.cW,self.cH,self.cW,self.cH),(2*self.cW,self.cH,self.cW,self.cH),(3*self.cW,self.cH,self.cW,self.cH),
                            (0,2*self.cH,self.cW,self.cH),(self.cW,2*self.cH,self.cW,self.cH),(2*self.cW,2*self.cH,self.cW,self.cH),(3*self.cW,2*self.cH,self.cW,self.cH),
                            (0,3*self.cH,self.cW,self.cH),(self.cW,3*self.cH,self.cW,self.cH),(2*self.cW,3*self.cH,self.cW,self.cH),(3*self.cW,3*self.cH,self.cW,self.cH),
                                ]
        self.counter = 0
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
        #self.counter = (self.counter+1) % 16
        self.counter = (self.counter+1) % 16
    '''def spritePrep(self,i,j):
        x0=j*self.cellWidth
        y0=i*self.cellHeight
        x1= ((j+1)*self.cellWidth
        y1= ((i+1)*self.cellHeight)
        return x0,y0,x1,y1
        
    def spriteDraw(self,screen):
        for i in range(4): #height
            for j in range(4): #width
                x0,y0,x1,y1 = spritePrep(i,j)
                screen.blit(self.spriteSheet,(100,230),(x0,y0,
                x1,y1)
    '''

    def redrawAll(self, screen):
        x0,y0,x1,y1 = self.spriteCrop[self.counter] 
        print(x0,y0,x1,y1)
        screen.blit(self.spriteSheet,(100,230),(x0,y0,
                x1,y1))
    
    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1000, height=800, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
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
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()