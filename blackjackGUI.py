#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      student
#
# Created:     26/03/2014
# Copyright:   (c) student 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import deckClass
import cardClass
import tkinter
import time
import os

class blackjackHand:

    def __init__(self, cardA, cardB):
        self.__hand = [cardA, cardB]


    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, otherHand):
        self.__hand = otherHand


    def __str__(self):
        retstr = ""
        for c in self.hand:
            retstr += (str(c) + " ")
        return retstr

    def value(self):
        total = 0
        inc_val = 0
        num_aces = 0
        for c in self.hand:
            if not c.facedown:
                if c.value > 10:
                    inc_val = 10
                elif c.value == 1:
                    inc_val = 11
                    num_aces += 1
                else:
                    inc_val = c.value
                total += inc_val

        while num_aces > 0 and total > 21:
            total -= 10
            num_aces -= 1

        return total

    def hit(self, card):
        self.hand.append(card)



class gameState():

    def __init__(self):

        #Prepare Deck
        self.d = deckClass.deck()
        self.d.shuffle()

        #Game State Variables
        self.over = False
        self.playerWin = False
        self.push = False


        self.dealerFacedown = self.d.draw()
        self.dealerFacedown.facedown = True
        self.dealerHand = blackjackHand(self.d.draw(), self.dealerFacedown)
        self.playerHand = blackjackHand(self.d.draw(), self.d.draw())

        print(self.dealerHand, self.dealerHand.value())
        print(self.playerHand, self.playerHand.value())




    def endGame(self):
        pass



    def execHit(self, gfx):

        if self.playerHand.value() > 20:
            self.execStand(gfx)
        else:
            self.playerHand.hit(self.d.draw())
            print(self.playerHand, self.playerHand.value())
            gfx.draw(self)

        if self.playerHand.value() > 20:
            self.execStand(gfx)



    def execStand(self, gfx):
        self.over = True
        self.dealerFacedown.facedown = False

        while self.dealerHand.value() < 17 and self.playerHand.value() < 22:

            self.dealerHand.hit(self.d.draw())
            gfx.draw(self)

        if (self.playerHand.value() < 22) and ((self.playerHand.value() >= self.dealerHand.value()) or self.dealerHand.value() > 21):
            if self.playerHand.value() == self.dealerHand.value():
                self.push = True
            else:
                self.playerWin = True


        gfx.draw(self)



    def resetGame(self, gfx):
        self.d = deckClass.deck()
        self.d.shuffle()
        #Game State Variables
        self.over = False
        self.playerWin = False
        self.push = False

        self.dealerFacedown = self.d.draw()
        self.dealerFacedown.facedown = True
        self.dealerHand = blackjackHand(self.d.draw(), self.dealerFacedown)
        self.playerHand = blackjackHand(self.d.draw(), self.d.draw())

        print(self.dealerHand, self.dealerHand.value())
        print(self.playerHand, self.playerHand.value())

        gfx.draw(self)


class simpleapp_tk(tkinter.Tk):

    def __init__(self, parent, game):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.game = game
        self.draw(self.game)


    def procHit(self):
        self.game.execHit(self)

    def procStand(self):
        self.game.execStand(self)

    def procDeal(self):
        self.game.resetGame(self)



    def draw(self, game):
        self.grid()
        self.gfx_list = []

        dlabeltext  = "Dealer: " + str (game.dealerHand.value())
        dealer_label = tkinter.Label(self.parent, text = dlabeltext)
        dealer_label.grid(column = 0, row = 0)

        plabeltext = "Player: " + str(game.playerHand.value())
        player_label = tkinter.Label(self.parent, text = plabeltext)
        player_label.grid(column = 0, row = 1)


        print(game.push, game.playerWin, game.over, game.dealerHand.value(), game.playerHand.value())
        if game.push:
            outcome_label = tkinter.Label(self.parent, text = "Push...", bg = "yellow")
        elif game.over and game.playerWin:
            outcome_label = tkinter.Label(self.parent, text = "WIN!!", bg = "green")
        elif game.over and not game.playerWin:
            outcome_label = tkinter.Label(self.parent, text = "Lose.", bg = "red")
        else:
            outcome_label = tkinter.Label(self.parent, text = "       ")

        outcome_label.grid(column = 0, row = 2, sticky="EW")


        i = 0
        for c in game.dealerHand.hand:
            if c.facedown:
                cardGfx = tkinter.PhotoImage(file = c.facedowngfx)
            else:
                cardGfx = tkinter.PhotoImage(file = c.gfxloc)
            label = tkinter.Label(self.parent, image = cardGfx)
            label.grid(column=i+1, row=0, sticky="EW")
            self.gfx_list.append(cardGfx)
            i+=1

        j = 0
        for x in game.playerHand.hand:
            cardGfx = tkinter.PhotoImage(file = x.gfxloc)
            label = tkinter.Label(self.parent, image = cardGfx)
            label.grid(column=j+1, row=1, sticky="EW")
            self.gfx_list.append(cardGfx)
            j+=1



        self.cmdHit = tkinter.Button(self.parent, text = "Hit", command = self.procHit, width = 8)
        self.cmdHit.grid(column = 1, row = 2,sticky="EW")

        self.cmdStand = tkinter.Button(self.parent, text = "Stand", command = self.procStand, width =8)
        self.cmdStand.grid(column = 2, row = 2, sticky="EW")

        self.cmdDeal = tkinter.Button(self.parent, text = "Deal", command = self.procDeal, width = 8)
        self.cmdDeal.grid(column = 3, row = 2, sticky="EW")






def main():


    state = gameState()

    app = simpleapp_tk(None, state)
    app.title('BlackJack')
    app.geometry("500x240")
    app.mainloop()


if __name__ == '__main__':
    main()
