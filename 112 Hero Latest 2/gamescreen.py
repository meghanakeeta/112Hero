#This is the main game screen for the game where the actual game is ran.
import pygame
from pygame_functions import *
#pygame_funtions from www.github.com/stevepaget/pygame_function
#only used for font rendering
import sys
import os 
import math
import copy
import mainplay
import characterscreen #get sprite from here
import endscreen
import chords
from os import path

hsFile = "highscore.txt"

def guitarNeck(image,size=None):
        width,height = image.get_size()
        neck = []
        for cy in range(height):
            row = pygame.Surface((width,1))
            row.blit(image,(0,-cy))
            neck += [row]
            return neck

#template that was modified and added to was from https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py
class GameScreen(object):
    def __init__(self, width=1000, height=800, fps=50, title="112 Hero Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        self.playing = True
        self.collide = None
        pygame.init()
        
        self.inputG = (255,255,255)
        self.inputR = (255,255,255)
        self.inputY = (255,255,255)
        self.inputB= (255,255,255)
        self.inputO= (255,255,255)
            
        '''self.inputG = (0,153,0)
        self.inputR = (165,70,62)
        self.inputY = (255,255,147)
        self.inputB= (0,142,197)
        self.inputO= (199,122,71)'''
    
    def init(self):
        self.paused = False
        self.score = 0
        self.time = 0
        self.notes = None
        self.largestFont = pygame.font.Font('pixelfont.ttf',60)
        self.largeFont = pygame.font.Font('pixelfont.ttf',40)
        self.sFont = pygame.font.Font('pixelfont.ttf',20)
        self.song = self.songChoice()
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(0)
        self.position = [-1,1.7,1.4]
        self.targetTop = 0.45
        self.targetBottom = 0.1
        self.target = (self.targetTop + self.targetBottom)/2
        self.speed = 2
        self.neckPosition= 0 
        self.white = (255,255,255)
        self.colors = (0,153,0),(165,70,62),(255,255,147),(0,142,197),(199,122,71)
        #self.colors = (0,204,0),(204,0,0),(255,255,0),(0,102,204),(255,128,0)
        #self.collideColors = (0,255,0),(255,0,0),(255,255,147),(0,128,255),(255,153,51)
        self.collideColors = (0,255,0),(204,0,0),(255,255,0),(0,102,204),(255,128,0)
        self.collideCG = (255,0,127),(204,0,0),(255,255,0),(0,102,204),(255,128,0)
        self.collideCR = (0,255,0),(255,0,127),(255,255,0),(0,102,204),(255,128,0)
        self.collideCY = (0,255,0),(204,0,0),(255,0,127),(0,102,204),(255,128,0)
        self.collideCB = (0,255,0),(204,0,0),(255,255,0),(255,0,127),(255,128,0)
        self.collideCO = (0,255,0),(204,0,0),(255,255,0),(0,102,204),(255,0,127)
        self.collideCGR = (255,0,127),(255,0,127),(255,255,0),(0,102,204),(255,128,0)
        self.collideCGY = (255,0,127),(204,0,0),(255,0,127),(0,102,204),(255,128,0)
        self.collideCGB = (255,0,127),(204,0,0),(255,255,0),(255,0,127),(255,128,0)
        self.collideCGO = (255,0,127),(204,0,0),(255,255,0),(0,102,204),(255,0,127)
        self.collideCRY = (0,255,0),(255,0,127),(255,0,127),(0,102,204),(255,128,0)
        self.collifeCRB = (0,255,0),(255,0,127),(255,255,0),(255,0,127),(255,128,0)
        self.collideCRO = (0,255,0),(255,0,127),(255,255,0),(0,102,204),(255,0,127)
        self.collideCYB = (0,255,0),(204,0,0),(255,0,127),(255,0,127),(255,128,0)
        self.collideCYO = (0,255,0),(204,0,0),(255,0,127),(0,102,204),(255,0,127)
        self.collideCBY = (0,255,0),(204,0,0),(255,255,0),(255,0,127),(255,0,127)
        
        if mainplay.gameOverall.song == 1: 
            self.chords = chords.chordsSong1()
        elif mainplay.gameOverall.song == 2:
            self.chords = chords.chordsSong2()
        elif mainplay.gameOverall.song == 3:
            self.chords = chords.chordsSong3()
        elif mainplay.gameOverall.song ==4:
            self.chords = chords.chordsSong4()
        elif mainplay.gameOverall.song ==5:
            self.chords = chords.chordsSong5()

        self.neckPic = pygame.image.load("guitarback.jpg")
        size = self.neckPic.get_size()
        self.fractions = [2*h/size[1] for h in range(size[1])] 
        self.neck = [guitarNeck(self.neckPic,size),size]

        self.c = False
        self.v = False
        self.b = False
        self.n = False
        self.m = False
        
        

    def songChoice(self): 
        if mainplay.gameOverall.song == 1:
            return'eyeOfTiger.wav'
        elif mainplay.gameOverall.song == 2:
            return 'hitme.wav'
        elif mainplay.gameOverall.song == 3:
            return 'smoke.wav'
        elif mainplay.gameOverall.song == 4:
            return 'sunshine.wav'
        elif mainplay.gameOverall.song == 5:
            return 'slowRide.wav'
    
    #ANGLE/DRAWS
    def tiltAngle(self,position,rad):
        x,y = position
        sin = math.sin(rad)
        cos = math.cos(rad)
        newX= x*cos - y*sin
        newY= x*sin + y*cos
        return newX, newY
    
    def tilt(self,position,rad):
        x,y,z = position
        z,x = self.tiltAngle((z,x),0)
        y,z = self.tiltAngle((y,z),5)
        return x,y,z
    

    def neckPicture(self):
        size = self.neckPic.get_size()
        self.fractions = [2*h/size[1] for h in range(size[1])]    



    def update(self,time):
        self.time+=time
        if self.speed>0:
            self.move = time*self.speed
            self.neckPosition += self.move
            for chord in self.chords:
                chord[1] -=self.move
        if self.paused:
            self.speed = 0
            #make song stop aswell 
        else:
            self.speed = 1
        #add slow down once song is over
    
    def drawAngle(self,x,z):
        x1,y1,z1 = self.position
        x,y,z = self.tilt((x-x1,-y1,z-z1),(5,0,0))
        rotate = 300/z
        cx = self.width//2
        cy = self.height//2
        return int(cx+x*rotate),int(cy-y*rotate)


    def keyPressed(self, keyCode, modifier):
        if keyCode == pygame.K_p:
            if self.paused == True:
                self.paused = False
                pygame.mixer.music.unpause()
            else:
                self.paused = True
                self.songPlay = False
                pygame.mixer.music.pause()
        elif keyCode == pygame.K_LEFT:
            self.c = True
            self.inputG = (0,153,0)
        elif keyCode == pygame.K_UP:
            self.v = True
            self.inputR = (165,70,62)
        elif keyCode == pygame.K_RIGHT:
            self.b = True
            self.inputY = (255,255,147)
        elif keyCode == pygame.K_DOWN:
            self.n = True
            self.inputB= (0,142,197)
        elif keyCode == pygame.K_SPACE:
            self.m = True
            self.inputO= (199,122,71)
        elif keyCode == pygame.K_q:
            mainplay.gameOverall.gameScreen = False
            self.playing = False

        
        
        

    def neckDraw(self,screen):
        neck,(width,height) = self.neck
        for x in range(0,6,2):
            for y in range(height):
                fract = self.fractions[y]
                z = (fract+x - self.neckPosition)%6
                a,b = self.drawAngle(-1,z),self.drawAngle(1,z)
                   

    def stringsDraw(self,screen):
        for x in (-1/5,-3/5,1/5,3/5):
            pygame.draw.line(screen,(255,255,255),self.drawAngle(x,0),self.drawAngle(x,6),2)
        for z in range(0,6,2):
            point = [self.drawAngle(cx,(cz-self.neckPosition)%6) for cx,cz in ((-1,z),(1,z))]
            pygame.draw.line(screen,(255,0,255),point[0],point[1],8)
    def inputDraw(self,screen):
        screen.blit(self.largeFont.render(f'Inputs',5,self.white),(150,660))
        pygame.draw.ellipse(screen,self.inputG,(30,700,80,80))
        pygame.draw.ellipse(screen,self.inputR,(115,700,80,80))
        pygame.draw.ellipse(screen,self.inputY,(200,700,80,80))
        pygame.draw.ellipse(screen,self.inputB,(285,700,80,80))
        pygame.draw.ellipse(screen,self.inputO,(370,700,80,80))
        #pygame.draw.ellipse(screen,self.colors[i if i else x+2],rectangle)

    def fretDraw(self,screen,x,z,i=None,color=None):
            if z>20 or z<-0.4:
                return
            position = self.drawAngle(x/2.5,z)
            a,b = self.drawAngle(-1/10,z),self.drawAngle(1/10,z)
            r = min(abs(a[0]-b[0]),100)
            cx,cy,cw,ch = position[0]-r, position[1]-r,r*2,r*2
            rectangle = cx+4,cy+4,cw-8,ch-8

            if self.collide:
                if self.c and self.v and self.notes == (1,1,0,0,0):
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCGR[i if i else x+2],rectangle)
                elif self.c and self.b and self.notes[0]==1 and self.notes[2]==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCGY[i],rectangle)
                elif self.c and self.n and self.notes[0]==1 and self.notes[3] ==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCGB[i],rectangle)
                elif self.c and self.m and self.notes[0]==1 and self.notes[4]==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCGO[i],rectangle)
                
                elif self.v and self.b and self.notes[1]==1 and self.notes[2]==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCRY[i],rectangle)
                elif self.v and self.n and self.notes[1]==1 and self.notes[3]==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCRB[i],rectangle)
                elif self.v and self.m and self.notes[1]==1 and self.notes[4]==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCRO[i],rectangle)

                elif self.b and self.n and self.notes[2]==1 and self.notes[3]==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCYB[i],rectangle)
                elif self.b and self.m and self.notes[2]==1 and self.notes[4]==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCYO[i],rectangle)

                elif self.n and self.m and self.notes[3]==1 and self.notes[4]==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCBY[i],rectangle)
                elif self.c and self.notes[0] == 1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCG[i],rectangle)
                elif self.v and self.notes[1] == 1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCR[i],rectangle)
                elif self.b and self.notes[2] ==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCY[i],rectangle)
                elif self.n and self.notes[3] ==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCB[i],rectangle)
                elif self.m and self.notes[4] ==1:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideCO[i],rectangle)
    
                else:
                    pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                    pygame.draw.ellipse(screen,self.collideColors[i if i else x+2],rectangle)
            else:
                pygame.draw.ellipse(screen,(0,0,0),(cx,cy,cw,ch))
                pygame.draw.ellipse(screen,self.colors[i if i else x+2],rectangle)
    
    def notesDraw(self,screen):
        s = tuple(self.drawAngle(x,z)for x,z in ((-1,self.targetTop),(-1,self.targetBottom), (1,self.targetBottom),(1,self.targetTop)))
        for x in (-2,-1,0,1,2):
            i=x+2
            c = self.colors[i]
            color = (c[0]//4,c[1]//4,c[2]//4)
            self.fretDraw(screen,x,self.target,i,c)
        for self.notes,time in self.chords:
            #self.notes = notes
            for x in (-2,-1,0,1,2):
                i=x+2
                if self.notes[i]:
                    self.collide = time<self.targetTop and time>self.targetBottom
                    if self.collide:
                        if self.notes[0] == 1:
                            if self.c:
                                mainplay.gameOverall.score += (1/2)
                        if self.notes[1] == 1:
                            if self.v:
                                mainplay.gameOverall.score += (1/2)
                        if self.notes[2] == 1:
                            if self.b:
                                mainplay.gameOverall.score += (1/2)
                        if self.notes[3] == 1:
                            if self.n:
                                mainplay.gameOverall.score += (1/2)
                        if self.notes[4] == 1:
                            if self.m:
                                mainplay.gameOverall.score += (1/2)
                    
                    else:          
                        #print(mainplay.gameOverall.score)
                        #print("no")
                        pass
                    self.fretDraw(screen,x,time,i,(255,0,255))

 
    def pauseDraw(self,screen):
        if self.paused:
            pygame.draw.rect(screen,(255,255,255),(self.width/4,self.height/4,self.width/2,self.height/2))
            screen.blit(self.largestFont.render('Paused',5,(0,0,0)),(3*self.width/8,7*self.height/16))
            

    def redrawAll(self, screen):
        background = pygame.image.load("guitarheroback.jpg")
        screen.blit(background,(0,0))
        screen.blit(self.largeFont.render(f'Score: {mainplay.gameOverall.score}',5,self.white),(3*self.width//80,3*self.height//80))
        screen.blit(self.largeFont.render(f'High Score: {mainplay.gameOverall.highscore}',5,self.white),(3*self.width/80,9*self.height//80))
        
        screen.blit(self.sFont.render(f'Press p',5,self.white),(66*self.width/80,5*self.height//80))
        screen.blit(self.sFont.render(f'to pause',5,self.white),(66*self.width/80,7*self.height//80))
        screen.blit(self.sFont.render(f'Press q',5,self.white),(66*self.width/80,10*self.height//80))
        screen.blit(self.sFont.render(f'to end',5,self.white),(66*self.width/80,12*self.height//80))
        
        self.stringsDraw(screen)
        self.neckDraw(screen)
        self.notesDraw(screen)
        self.pauseDraw(screen)
        mainplay.gameOverall.characterChoice.spriteDraw(screen)
        self.inputDraw(screen)
        self.pauseDraw(screen)
        '''if mainplay.gameOverall.endChoice.congrats == True:
            print('help')
            pygame.draw.rect(screen,(255,255,255),(self.width/4,self.height/4,self.width/2,self.height/2))
            screen.blit(self.largestFont.render('High Score',5,(0,0,0)),(3*self.width/8,7*self.height/16))
            screen.blit(self.largestFont.render('Enter your name',5,(0,0,0)),(3*self.width/8,10*self.height/16))'''


    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)
    
    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass
 
    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyReleased(self, keyCode, modifier):
        self.inputG = (255,255,255)
        self.inputR = (255,255,255)
        self.inputY = (255,255,255)
        self.inputB = (255,255,255)
        self.inputO = (255,255,255)

    def timerFired(self, dt):
        self.c = False
        self.v = False
        self.b = False
        self.n = False
        self.m = False
        mainplay.gameOverall.characterChoice.counter = (mainplay.gameOverall.characterChoice.counter+1) % 16
        if self.paused == True:
            mainplay.gameOverall.characterChoice.counter = 1
    def timeUp(self):
        pass
        #figure out how to go to endscreen when time is up
        #mainplay.gameOverall.gameScreen = False
        #self.playing = False
    def songOver(self):
        mainplay.gameOverall.gameScreen = False
        self.playing = False
    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        if pygame.mixer.music.set_endevent():
            print("end")
            self.songOver()
        while self.playing:
            time = clock.tick(self.fps)/1000
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
                    self.playing = False
                    mainplay.gameOverall.startScreen=False
                    mainplay.gameOverall.characterScreen = False
                    mainplay.gameOverall.songScreen = False
                    mainplay.gameOverall.gameScreen = False
                    mainplay.gameOverall.endScreen = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()
            self.update(time)
    

        pygame.mixer.music.stop()


        #pygame.quit()
