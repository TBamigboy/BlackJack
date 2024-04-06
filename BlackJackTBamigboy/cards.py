#cards.py

from graphics import *
from random import *

class PlayingCard:#class for the playing cards
 

    def __init__(self, rank, suit):
        
        self.rank = rank
        self.suit = suit

    def getRank(self):#gets rank of the card
        
        return self.rank

    def getSuit(self):#gets suit and returns suit of a card
        
        return self.suit

    def value(self):#returns the value of the cards
        
        if self.getRank() < 10:
            return self.rank
        else:
            return 10

    def __str__(self):#returns the string of the card
        
        rank = [None, "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                "Nine", "Ten", "Jack", "Queen", "King"]
        suits = {"s": "Spades", "d": "Diamonds", "c": "Clubs", "h": "Hearts"}
        if self.suit == "d":
            return str(rank[self.rank]+" of "+ suits.get("d"))
        elif self.suit == "c":
            return str(rank[self.rank]+" of "+suits.get("c"))
        elif self.suit == "s":
            return str(rank[self.rank]+" of "+suits.get("s"))
        elif self.suit == "h":
            return str(rank[self.rank]+" of "+suits.get("h"))


class Deck:

    def __init__(self):
        self.cards = []
        for suit in "csdh":
            for rank in range(1,14):
                self.cards.append(PlayingCard(rank,suit))

    def shuffle(self):#shuffles deck 52 cards in a deck
        self.shuffled = []
        deck_length = len(self.cards)
        count = 52
        
        for card in range(deck_length):
            card = self.cards[randrange(count)]
            self.cards.remove(card)
            self.shuffled.append(card)
            count = count - 1
            
        return self.shuffled

    def dealCards(self):
        return self.shuffled.pop(0)

    def cardsLeft(self):
        return len(self.shuffled)
            

        
def main():

    
    x = int(input("How many cards? "))
    d = Deck()
    d.shuffle()
    for i in range(x):
        print(d.dealCards())
    

if __name__ == "__main__":
    main()
