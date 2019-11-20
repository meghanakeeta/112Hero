import pygame
from pygame_functions import *
from pygamegame import PygameGame
from startscreen import StartScreen
from characterscreen import CharacterScreen
from songscreen import SongScreen
from gamescreen import GameScreen
from endscreen import EndScreen

class Main(PygameGame):
    def init(self):
        screenSize(1000,800)
        setBackgroundImage("guitarheroback.jpg")

Main(1000,800).run()

