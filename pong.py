#Pong game for Python 3 
#Based on tutorial by @TokyoEdTech

import turtle       #we will use the module turtle for the graphics.
import winsound     #module for using sounds on windows

#We create a window with the title Pong. We set the background color to purple and the dimensions to 800x600 
window = turtle.Screen()
window.title("Pong")
window.bgcolor("purple")
window.setup(width=800, height=600)
window.tracer(0)     #Keeps the window from updating automatically to speed up the game

#Paddle A
paddle_a = turtle.Turtle()   #creating a turtle object
paddle_a.speed(0)            #giving the object maximum speed of animation
paddle_a.shape("square")     #there are built-in shapes in turtle. square: 20 pixels x 20 pixels
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)      #stretching the dimensions of the shape
paddle_a.penup()             #turtle by definition will draw lines but we do not need that for pong
paddle_a.goto(-350,0)        #initial position of the paddle    

#Paddle B
paddle_b = turtle.Turtle()   
paddle_b.speed(0)            
paddle_b.shape("square")     
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)     
paddle_b.penup()             
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()         # turtle = module name; Turtle = method name (method for creating an object)  
ball.speed(0)            
ball.shape("circle")     
ball.color("red")    
ball.penup()             
ball.goto(0,0)
ball.dx = 0.4       #the ball will move by 0.4 pixels
ball.dy = 0.4

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()    #hiding this turtle (object)
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))         #writing the text     

#Scores
score_a = 0
score_b = 0       #creating variables for the scores

#Functions
def paddle_a_up():      #defining the first function
	y = paddle_a.ycor()     #defining the variable y as the y coordinate of the paddle. .ycor is a method of the turtle module.
	y += 30                 
	paddle_a.sety(y)        #updating the coordinate

def paddle_a_down():      
	y = paddle_a.ycor()    
	y -= 30                  
	paddle_a.sety(y)

def paddle_b_down():      
	y = paddle_b.ycor()    
	y -= 30                  
	paddle_b.sety(y)

def paddle_b_up():      
	y = paddle_b.ycor()     
	y += 30                  
	paddle_b.sety(y)

#Keyboard binding
window.listen()        #the program will listen for keyboard input
window.onkeypress(paddle_a_up, "w")      #the program will run the paddle_a_up function when the key w is pressed
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")     #arrow keys
window.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
	window.update()     #the window will update every time the looop runs

	#Move the ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border checking 
	if ball.ycor() > 290:                                           #when the ball gets to the border 
		ball.sety(290)
		ball.dy *= -1                                               #reverse the direction of the ball's movement
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)         #and play the bounce.wav file in the background (the program will not stop)

	if ball.ycor() < -290:   
		ball.sety(-290)
		ball.dy *= -1 
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 

	if ball.xcor() > 390:    #if the ball passes the paddle
		ball.goto(0,0)       #it returns to the center
		ball.dx *= -1
		score_a += 1         #player a's score goes up by 1 
		pen.clear()          #clean the writing
		pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))        #update the scores by using the .format method 

	if ball.xcor() < -390:   
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()   
		pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal")) 

	#Paddle and ball collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
		ball.setx(340)
		ball.dx *= -1     #if the ball collides against the paddle, we set the x coordinate to 340 and reverse the motion of the ball 		
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 