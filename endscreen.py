import pygame
from pygame_functions import *

class EndScreen(object):
    def __init__(self):
        screenSize(1000,800)
        setBackgroundImage("startbackground.jpg")
        label = makeLabel("112 Hero",100,400,300,fontColour='red')
        showLabel(label)


EndScreen()

endWait()