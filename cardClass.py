#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      student
#
# Created:     25/03/2014
# Copyright:   (c) student 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import collections
import os

class card:


    valueToText = {1:"A",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}

    def __init__(self, suit = " ", value = 0):
        self.__suit = suit
        self.__value = value
        self.__imageDir = os.getcwd() + "/cardImages"
        self.__gfxloc = self.__imageDir + "/" + suit.lower() + card.valueToText[value].lower() + ".gif"
        self.__facedowngfx = self.__imageDir + "/" + "b2fv.gif"
        self.__facedown = False




    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, suit):
        self.__suit = suit

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, suit):
        self.__value = value

    @property
    def gfxloc(self):
        return self.__gfxloc

    @property
    def facedowngfx(self):
        return self.__facedowngfx

    @property
    def imageDir(self):
        return self.__imageDir

    @property
    def facedown(self):
        return self.__facedown

    @facedown.setter
    def facedown(self, facedown):
        self.__facedown = facedown


    def __str__(self):
        return("[{}|{}]".format(card.valueToText[self.value],self.suit))














