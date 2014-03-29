import cardClass
import random

class deck:

    suits = ("S", "D", "C", "H")

    def __init__(self):
        self.__cardStack = []
        for suit in deck.suits:
            for x in range(1,14):
                c = cardClass.card(suit,x)
                self.__cardStack.append(c)


    @property
    def cardStack(self):
        return self.__cardStack

    @cardStack.setter
    def cardStack(self, other):
        self.__cardStack = other



    def __str__(self):
        retstr = ""
        for c in self.cardStack:
            retstr += (str(c)+ " ")
        return retstr


    def shuffle(self):
        new_deck = []
        while len(self.cardStack) > 0:
            pos = random.randint(0,len(self.cardStack)-1)
            #print(pos)
            #print("len", len(self.cardStack))
            c =self.cardStack.pop(pos)
            new_deck.append(c)
        self.cardStack = new_deck

    def draw(self):
        return(self.cardStack.pop())


def main():
    pass

if __name__ == '__main__':
    main()
