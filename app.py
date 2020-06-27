#imported turtle module
import turtle

screen = turtle.Screen() #intilize screen
screen.title("Ping Pong By SamanderLight") #set the title of the window
screen.bgcolor("black") #set the background color of the screen
screen.setup(width=1000, height=800) # set the dim of the screen
screen.tracer(0) #stops the screen from updating automaticlly

#pad1
pad1 = turtle.Turtle() #intializes turtle object
pad1.speed(0) #set the speed of the animation
pad1.shape("square") #set the shape of the pad
pad1.color("green") # set the colore of the pad
pad1.penup() #stop the object from drawing lines
pad1.goto(-450 , 0) #set the postion of the pad 
pad1.shapesize(stretch_wid=5, stretch_len=1) #set the width and length of the pad with stretch

#pad2
pad2 = turtle.Turtle() 
pad2.speed(0) 
pad2.shape("square")
pad2.color("blue")
pad2.penup()
pad2.goto(450 , 0)
pad2.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0 )
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0 , 0)
ball.dx = 0.1
ball.dy = 0.1

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,360)
score.write("P1 : 0 P2 : 0", align="center" , font=("Courier",30,"normal"))

#moveing function
def pad1_up(): 
    y = pad1.ycor() # get the y coordinate of the pad1
    y += 20 #set the y to increase by 20
    pad1.sety(y) #set the y of the pad1 to the new y coorddinate

def pad1_down():
    y = pad1.ycor()
    y -= 20 #set the y to decrease by 20
    pad1.sety(y)

def pad2_up():
    y = pad2.ycor()
    y += 20
    pad2.sety(y)

def pad2_down():
    y = pad2.ycor()
    y -= 20
    pad2.sety(y)

#keyboard binding
screen.listen() # tell the screen to expect keyboard input
screen.onkeypress(pad1_up , "w")   #when pressing the w the function pad_up1 will run
screen.onkeypress(pad1_down , "s")
screen.onkeypress(pad2_up , "Up")
screen.onkeypress(pad2_down , "Down")

#game loop
while True:
    screen.update() #updates the screen everytimethe loop run.

    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball will start moving to the x axis
    ball.sety(ball.ycor() + ball.dy) #ball will start moving to the y axis

    # border check 
    if ball.ycor() > 390: #check if the ball reach the border and then reverse the direction 
        ball.sety(390)
        ball.dy *= -1
    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1

    if ball.xcor() > 490: #check if the ball reach the border and then but the ball in the center
        ball.goto(0,0)
        ball.dx *= -1 #reverse the direction after centering the ball.
        score1 += 1
        score.clear()
        score.write("P1 : {} P2 : {}".format(score1,score2), align="center" , font=("Courier",30,"normal"))

    if ball.xcor() < -490:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("P1 : {} P2 : {}".format(score1,score2), align="center" , font=("Courier",30,"normal"))
    
    #impact the ball to the pads
    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() <pad2.ycor() + 40 and ball.ycor() > pad2.ycor() - 40):
        ball.setx (440)
        ball.dx *= -1

    if (ball.xcor() < -440 and ball.xcor() > -450) and (ball.ycor() <pad1.ycor() + 40 and ball.ycor() > pad1.ycor() - 40):
        ball.setx (-440)
        ball.dx *= -1
    