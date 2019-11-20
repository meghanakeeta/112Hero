import pygame
from pygame_functions import *

class CharacterScreen(object):
    def __init__(self):
        screenSize(1000,800)
        setBackgroundImage("charback1.jpg")
        '''self.font = pygame.font.Font('pixelfont.ttf',50)
        self.font.render('Design your player',2,(255,255,255),(50,50))'''
        top=makeLabel('DESIGN YOUR PLAYER',90,165,30,fontColour='white',background='clear')
        showLabel(top) #top text

        self.boyButton = makeSprite("boybutton.png") #boy button
        showSprite(self.boyButton)
        moveSprite(self.boyButton,350,100)

        self.girlButton = makeSprite("girlbutton.png") #girl button
        showSprite(self.girlButton)
        moveSprite(self.girlButton,550,100)

        top=makeLabel('Hair',45,660,180,fontColour='white',background='clear')
        showLabel(top) #Hair text

        self.tempSprite = makeSprite("tempsprite.png") #temp sprite
        showSprite(self.tempSprite)
        moveSprite(self.tempSprite,30,200)

        #FIX LOCATIONS
        self.blondButton = makeSprite("blondebutton.png") #blond button
        showSprite(self.blondButton)
        moveSprite(self.blondButton,500,220)

        self.brownButton = makeSprite("brownbutton.png") #brown button
        showSprite(self.brownButton)
        moveSprite(self.brownButton,750,220)

        top=makeLabel('Shirt',45,650,300,fontColour='white',background='clear')
        showLabel(top) #Shirt text

        self.blueButton = makeSprite("bluebutton.png") #blue button
        showSprite(self.blueButton)
        moveSprite(self.blueButton,500,340)

        self.redButton = makeSprite("redbutton.png") #red button
        showSprite(self.redButton)
        moveSprite(self.redButton,750,340)

        top=makeLabel('Pants',45,650,420,fontColour='white',background='clear')
        showLabel(top) #Pants text

        self.blueButton = makeSprite("bluebutton.png") #blue button
        showSprite(self.blueButton)
        moveSprite(self.blueButton,500,460)

        self.blackButton = makeSprite("blackbutton.png") #black button
        showSprite(self.blackButton)
        moveSprite(self.blackButton,750,460)

        top=makeLabel('Shoes',45,650,540,fontColour='white',background='clear')
        showLabel(top) #Shoes text

        self.blackButton = makeSprite("blackbutton.png") #black button
        showSprite(self.blackButton)
        moveSprite(self.blackButton,500,580)

        self.redButton = makeSprite("redbutton.png") #red button
        showSprite(self.redButton)
        moveSprite(self.redButton,750,580)

        self.readyButton = makeSprite("readybutton.png") #reddy button
        showSprite(self.readyButton)
        moveSprite(self.readyButton,720,670)

    def readyButtonClick():
        pass
        #goes to next screen when clicked


    def keyPressed():
        pass 
        # if pressed any of the bottons changes the sprite
        #houses all clicks of buttons

    def boyButtonClick():
        pass
    #has the location of button and changes the sprite drawing

    def girlButtonClick():
        pass

    def blondeButtonClick():
        pass

    def brownButtonClick():
        pass

    def blueShirtButtonClick():
        pass

    def redShirtButtonClick():
        pass

    def bluePantsButtonClick():
        pass

    def blackPantsButtonClick():
        pass

    def blackShoesButtonClick():
        pass

    def redShoesButtonClick():
        pass











CharacterScreen()

endWait()