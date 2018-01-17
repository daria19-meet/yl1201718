from turtle import * 
import random 
import math 
setup(500,500)
class Ball(Turtle):
	def __init__ (self, x,y, dx, dy, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color) 
		self.speed(speed)
		self.goto(x,y)
		self.dx= dx
		self.dy= dy 

ball1 = Ball(100,100,5,6,7,"red", 5)
ball2= Ball(100,90, 8, 9, 10, "blue", 7)

def check_collision(ball1, ball2):
	r2=ball2.radius+ball1.radius
	d=math.sqrt(math.pow(ball2.xcor() - ball1.xcor(),2) + math.pow(ball2.ycor() - ball1.ycor(),2))
	if d <= r2:
		if ball1.radius > ball2.radius:
			x1 = y1 =random.randint(-250,250)
			ball2.goto(x1, y1)
		else: 
			x1 = y1 =random.randint(-250,250)
			ball1.goto(x1, y1)


check_collision(ball2, ball1)
mainloop()	
