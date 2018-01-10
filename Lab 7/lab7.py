from turtle import * 
import random 
import math 
setup(500,500)
class Rectangle(Turtle):
	def __init__(self,height,width,x,y):
		Turtle.__init__(self)
		register_shape("rec",((0-width,0-height),(0-width,height),(width,height),(width,0-height)))
		self.shape("rec")
		self.goto(x,y)
		self.height=height
		self.width=width

	def top(self):
		return self.ycor() + (self.height/2)
	def bottom(self):
		return self.ycor() - (self.height/2)
	def right(self):
		return self.xcor() + (self.width/2)
	def left(self):
		return self.xcor() - (self.width/2)

 
rec1= Rectangle(30,10,100,100)
rec2= Rectangle(40,10,100,101)

def check_collision(rec1, rec2):
	if(	
		rec1.top() >= rec2.bottom() and
		rec1.right() >= rec2.left() and
		rec1.bottom() <= rec2.top() and
		rec1.left() <= rec2.right()
	):
		rec1.goto(-200,-200)
		rec1.color("red")



check_collision(rec1, rec2)
mainloop()