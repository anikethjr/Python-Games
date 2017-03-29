#Stopwatch: The Game
import simplegui
# define global variables
count=0
x=0
y=0
check=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes=str(t//600)    
    seconds=str((t//10)%60)
    if(int(seconds)<10):
        seconds="0"+seconds
    tenths=str(t%10);
    return minutes+":"+seconds+"."+tenths
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global check
    check=1
def stop():
    timer.stop()
    global check
    if check==1:
        global x,y
        if count%10==0:
            x+=1
        y+=1
        check=0
    
def reset():
    global count,x,y
    timer.stop()
    count=0
    x=0
    y=0

# define event handler for timer with 0.1 sec interval
def timex():
    global count
    count+=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(count),(95,170),50,'White','sans-serif')
    canvas.draw_text(str(x)+"/"+str(y),(200,50),50,'Green','sans-serif')
    
    
# create frame
frame=simplegui.create_frame("Stopwatch:The Game",300,300)

# register event handlers
timer=simplegui.create_timer(100,timex)
startbutton=frame.add_button("Start",start)
stopbutton=frame.add_button("Stop",stop)
resetbutton=frame.add_button("Reset",reset)
frame.set_draw_handler(draw)

# start frame
frame.start()
