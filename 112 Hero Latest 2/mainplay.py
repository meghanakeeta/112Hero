#This file houses all the screens of the game and controls which screen appears.
#It also houses the variables that are shared between modes.
import pygame
import os 
import sys
import startscreen
import characterscreen
import songscreen
import gamescreen
import endscreen
import chords
from os import path

hsFile = "highscore.txt"
hsNameFile = "highname.txt"

class MainGame(object):
    def __init__(self):
        self.startScreen = True
        self.characterScreen = True
        self.songScreen = True
        self.gameScreen = True
        self.endScreen = True
        self.score = 0
        #self.scoreInt = int(self.score)
        self.song = 1
        self.characterChoice = characterscreen.CharacterScreen()
        self.endChoice = endscreen.EndScreen()
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir,hsFile),'r+') as hfile:
            self.highscore = float(hfile.read())
        #with open(path.join(self.dir,hsNameFile),'r+') as nfile:
            #self.highname = (nfile.read())
           
        
    
    def run(self):
        if self.startScreen:
            start = startscreen.StartScreen()   
            start.run()
    
        if self.characterScreen:
            self.characterChoice.run()
            #characterscreen.main() 
            

        if self.songScreen:
            self.songChoice = songscreen.SongScreen()
            self.songChoice.run()

        if self.gameScreen:
            gamem = gamescreen.GameScreen()
            gamem.run()

        if self.endScreen:
            #end = endscreen.EndScreen()
            self.endChoice.run()
            


        pygame.quit()

gameOverall = MainGame()
gameOverall.run()


