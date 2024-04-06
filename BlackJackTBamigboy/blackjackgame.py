#blackjack.py
from graphics import *
from cards import PlayingCard, Deck
from button import Button
from time import sleep

class Blackjack(Deck):
    #Class for blackjack game

    d = Deck()

    def __init__(self, dHand=[], pHand=[]):
        #initializes class and shuffles and creates player and dealer hand

        
        Deck.__init__(self)
        self.d.shuffle()
        self.dHand = dHand
        self.pHand = pHand

    def initDeal(self,gwin,xposD,yposD,xposP,yposP):#deals out the two inititial player cards 2 for the dealer and 2 for the player and the parameters are for the set postition of the cards
      
        

        dCard1, dCard2 = self.d.dealCards(), self.d.dealCards()
        pCard1,pCard2 = self.d.dealCards(), self.d.dealCards()
        
        dCard1_img, dCard2_img = self.getCard(dCard1), self.getCard(dCard2)
        pCard1_img,pCard2_img = self.getCard(pCard1), self.getCard(pCard2)
        self.dHand.append(dCard1)
        self.dHand.append(dCard2)
        self.pHand.append(pCard1)
        self.pHand.append(pCard2)

        cardimage1 = Image(Point(xposD,yposD),dCard1_img)
        cardimage2 = Image(Point(xposD+10,yposD),dCard2_img)
        cardimage3 = Image(Point(xposP,yposP),pCard1_img)
        cardimage4 = Image(Point(xposP+10,yposP),pCard2_img)
        cardimage2.draw(gwin)
        cardimage3.draw(gwin)
        cardimage4.draw(gwin)

##        return self.dHand,self.pHand
        
        return self.dHand,self.pHand, cardimage1
    
    def getCard(self,card):#takes cards name and converts into str to pull card from the playing card file and output a image
       
        
        card = "playingcards/"+str(card.getSuit()) + str(card.getRank()) + ".gif"
        return card

    def hit(self,gwin,xpos,ypos):#hit function to create a new card for the player when hit is pressed
        
        
        pCard = self.d.dealCards()
        pCardimg = self.getCard(pCard)
        self.pHand.append(pCard)

        image = Image(Point(xpos,ypos),pCardimg)
        image.draw(gwin)
        return self.pHand

    def evaluateHand(self, hand):#function to calculate total value of the cards within the hand
       
        
        total = 0
        for card in hand:
            card = card.value()
            if card == 10:
                total += 10
            elif card == 1:
                if total < 11:
                    total += 11
                elif total >= 11:
                    total += card
            else:
                total += card
                
        for card in hand:
            if card.value() == 1 and total > 21:
                total -= 10
        return total

    def dealerPlays(self, gwin, xpos, ypos):#function for dealer to deal another card
        
        
        dCard = self.d.dealCards()
        dCardimg = self.getCard(dCard)
        self.dHand.append(dCard)

        image = Image(Point(xpos,ypos),dCardimg)
        image.draw(gwin)
        return self.dHand

    def Busted(self, gwin,xpos,ypos):#Checks if players Busted the paramaters xpos,ypos give the position for the message

        
        pTotal = self.evaluateHand(self.pHand)
        dTotal = self.evaluateHand(self.dHand)
        message = Text(Point(xpos,ypos),"")
        message.setStyle("bold")
        message.setTextColor("white")
        message.draw(gwin)
        if (pTotal > 21):
            message.setText("You busted :(")
            return True
        elif pTotal == 21:
            message.setText("Blackjack!")
            return True
        
def introanimation(win):#intro animation window

    win = GraphWin("BlackJack!",650,650)
    win.setBackground("black")

    introtxt = Text(Point(325,325),"Welcome To Black Jack Click Anywhere To Continue!")
    introtxt.setFace('arial')
    introtxt.setSize(15)
    introtxt.setStyle('bold')
    introtxt.setTextColor("white")
    introtxt.draw(win)

    
    pt1 = win.getMouse()
    introtxt.undraw()
    win.close()

    

        
def main():
    
    
    win = GraphWin("BlackJack",650,650)
    win.setBackground("black")

    introanimation(win)
                   



    
    # Create buttons
    hit = Button(win, Point(287.5,275), 50, 50, "Hit")
    stand = Button(win, Point(367.5,275), 50, 50, "Stand")
    quitButton = Button(win, Point(367.5,425), 50, 50, "Quit")
    newGame = Button(win,Point(287.5,425),50,50,"NewGame")


    

    # Define Deck and Blackjack object
    d = Deck()
    d.shuffle()
    b = Blackjack()

    # Initial deal
    cards = b.initDeal(win,150,100,120,550)
    backcard = Image(Point(110,100),"playingcards/b1fv.gif")
    backcard.draw(win)
    pCards = cards[1]
    dCards = cards[0]
    dCard1_img = cards[2]
    
    # Evaluate dealer's and player's hands
    pTotal = b.evaluateHand(pCards)
    dTotal = b.evaluateHand(dCards) - dCards[0].value()

    # Display totals of both hands
    playertxt = Text(Point(50, 70),"Player")
    dealertxt = Text(Point(50, 630),"Dealer")
    playertxt.draw(win)
    playertxt.setFace("arial")
    playertxt.setStyle("bold")
    playertxt.setTextColor("white")
    
    dealertxt.draw(win)
    dealertxt.setFace("arial")
    dealertxt.setStyle("bold")
    dealertxt.setTextColor("white")
    #player total
    pTotaltxt = Text(Point(50, 90),pTotal)
    pTotaltxt.setTextColor("white")
    pTotaltxt.draw(win)
    #dealer total
    dTotaltxt = Text(Point(50, 640),dTotal)
    dTotaltxt.setTextColor("white")
    dTotaltxt.draw(win)

    # Deactivate buttons if player is busted or
    # Gets Blackjack after initial deal
    if b.Busted(win,400,400):
        hit.deactivate()
        stand.deactivate()

    message = Text(Point(325,325),"")
    message.setTextColor("white")
    message.setStyle("bold")
    message.draw(win)
    
    # Positions for cards being dealt after initial deal
    xP,xD = 250, 250
    y = 150
    pt = win.getMouse()
    while not (quitButton.isClicked(pt)):

        if newGame.isClicked(pt):
        
            introanimation(win)
        
        if hit.isClicked(pt):#hit button clicked
            pCards = b.hit(win,xP+15,y)#moves the cards over
            pTotal = b.evaluateHand(pCards)
            pTotaltxt.setText(pTotal)
            if b.Busted(win,325,325):
                hit.deactivate()
                stand.deactivate()
            xP += 70
            
        elif stand.isClicked(pt):#stand button clicked
            
          
            backcard.undraw()
            dCard1_img.draw(win)
            dTotal = b.evaluateHand(dCards)
            dTotaltxt.setText(dTotal)
            hit.deactivate()
            stand.deactivate()
            if ((dTotal > pTotal) and (dTotal <= 21)) or dTotal == 21:#checks if dealer wins
                message.setText("Dealer won!")
                message.setFace("arial")
                
                
            elif (dTotal > 21) or (dTotal < pTotal):#checks if player wins
                message.setText("Congrats! You won!")
                message.setFace("arial")
                
            elif dTotal == pTotal:#if statement to check for a draw
                message.setText("Draw!")
                message.setFace("arial")
                
                 
            while (dTotal < 17) and (dTotal < pTotal):#if statement to check dealer vs player
                dCards = b.dealerPlays(win,xD+15,y+50)
                dTotal = b.evaluateHand(dCards)
                dTotaltxt.setText(dTotal)
                dTotaltxt.setFace("arial")
                if ((dTotal > pTotal) and (dTotal <= 21)) or dTotal == 21:
                    message.setText("Dealer won!")
                    message.setFace("arial")
                    
                
                elif (dTotal > 21) or (dTotal < pTotal):
                    message.setText("You won!")
                    message.setFace("arial")
                    
                
                elif dTotal == pTotal:
                    message.setText("Draw!")
                    message.setFace("arial")
                    
                
            
                xD += 70
    
        pt = win.getMouse()

    win.close()

if __name__ == "__main__":
    main()
        
