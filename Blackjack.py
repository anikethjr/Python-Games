#Blackjack

import simplegui
import random

# load card sprite - 936x384 
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
score = 0


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cardlist=[]
        self.value=0

    def __str__(self):
        self.printcards="Hand contains "
        for i in self.cardlist:
            self.printcards+=str(i.get_suit())+str(i.get_rank())+" "
        return self.printcards

    def add_card(self, card):
        # add a card object to a hand
        self.cardlist.append(card)

    def get_value(self):
        self.value=0
        check=0
        for i in self.cardlist:
            self.value+=VALUES[i.get_rank()]
            if(i.get_rank()=='A'):
                check+=1
        if(check>0 and self.value+10<=21):
            self.value+=10
        return self.value
        
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        j=0
        for i in self.cardlist:
            i.draw(canvas,[pos[0]+100*j,pos[1]])
            j+=1
        
    
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deckofcards=[]
        for i in SUITS:
            for j in RANKS:
                self.deckofcards.append(Card(i,j))
        random.shuffle(self.deckofcards)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deckofcards)

    def deal_card(self):
        # deal a card object from the deck
        dealtcard=random.choice(self.deckofcards)
        self.deckofcards.remove(dealtcard)
        return dealtcard
        
    def __str__(self):
        # return a string representing the deck
        self.printcards="Deck contains "
        for i in self.deckofcards:
            self.printcards+=str(i.get_suit())+str(i.get_rank())+" "
        return self.printcards

deck = Deck()
player = Hand()
dealer = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play,deck,player,dealer,score
    deck.__init__()
    player.__init__()
    dealer.__init__()
    outcome = "Hit or Stand?"
    if(in_play):
        outcome = "Player looses this hand. Dealing new hand . Hit or Stand?"
        score-=1
        
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())  
    
    in_play = True

def hit(): 
    global outcome, in_play,deck,player,dealer,score
    # if the hand is in play, hit the player
    if(in_play):
        player.add_card(deck.deal_card())
    else:
        outcome = "THIS HAND IS DONE. New deal?"
    if(player.get_value()>21 and in_play):
        outcome = " BUSTED. New deal? "
        in_play = False
        score-=1
    
        
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global outcome, in_play,deck,player,dealer,score
    if(in_play):
        while dealer.get_value() < 17 :
            dealer.add_card(deck.deal_card())
    # assign a message to outcome, update in_play and score
        if(dealer.get_value() > 21):
            outcome = " DEALER BUSTED.. PLAYER WINS. New deal?"
            in_play = False
            score+=1
        elif(dealer.get_value() > player.get_value()):
            outcome = "PLAYER LOOSES BECAUSE OF LOWER VALUE. New Deal?"
            in_play = False
            score-=1
        elif(dealer.get_value() == player.get_value()):
            outcome = "TIE!! BUT PLAYER LOOSES. New Deal?"
            in_play = False
            score-=1
        else:
            outcome = "PLAYER WINS!!!!!!! New Deal?"
            in_play = False
            score+=1
    else:
        outcome = "THIS HAND IS DONE. New deal?"
    
    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player.draw(canvas,[50,100])
    dealer.draw(canvas,[50,300])
    if(in_play):
        canvas.draw_image(card_back,[CARD_BACK_CENTER[0],CARD_BACK_CENTER[1]], CARD_BACK_SIZE,[86,348] , CARD_BACK_SIZE)
    canvas.draw_text("Player's Hand",[50,90],20,'White')
    canvas.draw_text("Dealer's Hand",[50,290],20,'White')
    canvas.draw_text(outcome,[50,500],20,'White')
    canvas.draw_text("Blackjack",[275,30],20,'White','serif')
    canvas.draw_text("Score : " + str(score) ,[475,50],20,'White','serif')
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric