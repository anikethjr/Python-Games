# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600.0
HEIGHT = 400.0     
BALL_RADIUS = 20.0
PAD_WIDTH = 8.0
PAD_HEIGHT = 80.0
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1=0
score2=0
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel=0.0
paddle2_vel=0.0
# initialize ball_pos and ball_vel for new ball in middle of table
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0.0,0.0]
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if(direction):
        ball_vel[0]=random.randrange(4, 8)
        ball_vel[1]=-random.randrange(2, 6)
    else:
        ball_vel[0]=-random.randrange(4,8)
        ball_vel[1]=random.randrange(2,6)


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1=0
    score2=0
    spawn_ball(random.randrange(0,2))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if(ball_pos[1]>400-BALL_RADIUS):
        ball_vel[1]=-ball_vel[1]
    if(ball_pos[1]<BALL_RADIUS):
        ball_vel[1]=-ball_vel[1]
    if(ball_pos[0]>WIDTH-PAD_WIDTH-BALL_RADIUS and ball_pos[1]>paddle1_pos-HALF_PAD_HEIGHT and ball_pos[1]<paddle1_pos+HALF_PAD_HEIGHT):
        ball_vel[0]=-1.1*ball_vel[0]
    elif(ball_pos[0]<PAD_WIDTH+BALL_RADIUS and ball_pos[1]>paddle2_pos-HALF_PAD_HEIGHT and ball_pos[1]<paddle2_pos+HALF_PAD_HEIGHT):
        ball_vel[0]=-1.1*ball_vel[0]
    elif(ball_pos[0]<PAD_WIDTH+BALL_RADIUS):
        score2+=1
        spawn_ball(RIGHT)
    elif(ball_pos[0]>WIDTH-PAD_WIDTH-BALL_RADIUS):
        score1+=1
        spawn_ball(LEFT)
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "Red")
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_pos+paddle1_vel<=HEIGHT-HALF_PAD_HEIGHT and paddle1_pos+paddle1_vel>=HALF_PAD_HEIGHT):
        paddle1_pos+=paddle1_vel
    if(paddle2_pos+paddle2_vel<=HEIGHT-HALF_PAD_HEIGHT and paddle2_pos+paddle2_vel>=HALF_PAD_HEIGHT):
        paddle2_pos+=paddle2_vel    
    # draw paddles
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH,paddle1_pos+HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([HALF_PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT],[HALF_PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    # draw scores
    canvas.draw_text(str(score1),[125,100],75,"White")
    canvas.draw_text("                   "+str(score2),[75,100],75,"White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if(key==simplegui.KEY_MAP["W"]):
       paddle2_vel-=6
    elif(key==simplegui.KEY_MAP["S"]):
       paddle2_vel+=6
    elif(key==simplegui.KEY_MAP["up"]):
       paddle1_vel-=6
    elif(key==simplegui.KEY_MAP["down"]):
       paddle1_vel+=6
       
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key==simplegui.KEY_MAP["W"]):
       paddle2_vel+=6
    elif(key==simplegui.KEY_MAP["S"]):
       paddle2_vel-=6
    elif(key==simplegui.KEY_MAP["up"]):
       paddle1_vel+=6
    elif(key==simplegui.KEY_MAP["down"]):
       paddle1_vel-=6


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart',new_game)


# start frame
new_game()
frame.start()
