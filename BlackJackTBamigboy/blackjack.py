

from cards import PlayingCard, Deck
from graphics import *
from button import Button

class Blackjack(Deck, PlayingCard):

    def __init__(self, pHand=[], dHand=[]):
        Deck.__init__(self)
        #PlayingCard.__init__(self, rank, suit)
        self.pHand = []
        self.dHand = []
        d = Deck()
        d.shuffle()

    def initDeal(self):
        d = Deck()
        pHand = self.pHand
        pHand = [d.dealCards()]
        #self.dHand = [Deck.dealCards(), Deck.dealCards()]

        rank, suit = pHand[0].getRank(), pHand[0].getSuit()
        print(rank, suit)
        
    #def hit(self, gwin, xPos, yPos):
        


def main():
    #win = GraphWin("hello", 600,600)

    d = Deck()
    d.shuffle()
    b = Blackjack()
    b.initDeal()

    #win.getMouse()
    #win.close()

if __name__ == "__main__":
    main()
