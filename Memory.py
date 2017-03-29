# implementation of card game - Memory

import simplegui
import random

card=[]
exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
click1=-1
click2=-1
count=1
turn=0
# helper function to initialize globals
def new_game():
    global card,exposed,click1,click2,count,turn
    deck1=[]
    deck2=[]
    exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    click1=-1
    click2=-1
    count=1
    turn=0
    for i in range(0,8):
        deck1.append(i)
        deck2.append(i)
    card=deck1+deck2
    random.shuffle(card)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed,click1,click2,count,turn
    if(exposed[pos[0]/50]==0):
        exposed[pos[0]/50]=1
        if(count==1):
            if(card[click1]!=card[click2]):
                exposed[click1]=0
                exposed[click2]=0
            click1=pos[0]/50
            count+=1
            turn+=1
        elif(count==2):
            click2=pos[0]/50
            if(card[click1]==card[click2]):
                exposed[click1]=2
                exposed[click2]=2
            count=1
 
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card,exposed,turn
    label.set_text("Turns : "+str(turn))
    for i in range(0,16):
        canvas.draw_text(str(card[i]),[i*50+15,63],40,'Red')
        if(exposed[i]==0):
            canvas.draw_polygon([(i*50,0),(i*50,100),((i+1)*50,100),((i+1)*50,0)],1,'Black','Green')
   


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns : "+str(turn))


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric