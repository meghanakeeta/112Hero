import pygame
from pygame_functions import *

class GameScreen(object):
    def __init__(self):
        screenSize(1000,800)
        setBackgroundImage("guitarheroback.jpg")
        self.score = 0
        self.time = 0

GameScreen()
endWait()