import pygame
from pygame_functions import *

class StartScreen(object):
    def __init__(self):
        screenSize(1000,800)
        setBackgroundImage("startbackground.jpg")
        
        self.title = makeSprite("fire.png") #fire112
        showSprite(self.title)
        moveSprite(self.title,250,0)
        
        self.guitar = makeSprite("Guitar.png") #guitar
        showSprite(self.guitar)
        moveSprite(self.guitar,100,160)

        self.playButton = makeSprite("playbutton.png") #playbutton
        showSprite(self.playButton)
        moveSprite(self.playButton,570,590)
    
    def keyPressed():
        pass
        #button press to go to next screen

StartScreen()

endWait()