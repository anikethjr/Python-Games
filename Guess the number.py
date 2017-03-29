#GUESS THE NUMBER
import random
import math
import simplegui

secret_number=0
numguess=0#STORES THE USER'S GUESS
genrange=100#STORES THE ENTERED RANGE(EITHER 100 OR 1000)
numberofguess=0;#STORES THE NUMBER OF GUESSES THE USER CAN MAKE


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number,numberofguess
    secret_number=random.randrange(0,genrange)
    #calculating the number of guesses for the given range
    numberofguess=int(math.ceil(math.log(genrange+1,2)))
  
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global genrange
    genrange=100
    print "Game range changed to 0 to 100. New game started..."
    new_game()
   
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global genrange
    genrange=1000
    print "Game range changed to 0 to 1000. New game started..."
    new_game()
    
def input_guess(guess):	
    global numberofguess
    numguess=int(guess)
    numberofguess-=1
    print "Guess was",numguess
    if(numguess>secret_number):
        print "Lower"
        if(numberofguess==0):
            print "You Lose. New game started with range 0 to",genrange
            new_game()
        else:
            print"You have",numberofguess,"guesses remaining"
    elif(numguess<secret_number):
        print "Higher"
        if(numberofguess==0):
            print "You Lose. New game started with range 0 to",genrange
            new_game()
        else:
            print"You have",numberofguess,"guesses remaining"
    else:
        print "Correct!! New game started with range 0 to",genrange
        new_game()

    
# create frame
frame=simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range:0-100",range100,50)
frame.add_button("Range:0-1000",range1000,50)
frame.add_input("Make a Guess",input_guess,50)

# call new_game 
new_game()



