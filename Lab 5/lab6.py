from turtle import *
import random
colormode(255)
class Rectangle(Turtle):
	def __init__(self,height,width):
		Turtle.__init__(self)
		register_shape("rec",((0-width,0-height),(0-width,height),(width,height),(width,0-height)))
		self.shape("rec")
rec1=Rectangle(80,50)

class Square(Rectangle):
	def __init__(self, height,width):
		Rectangle.__init__ (self,height,width)
		self.shape("square")
		self.shapesize=(height)

	def random_color(self):
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		self.color(r,g,b)
square1=Square(50,50)
mainloop()

#square1.random_color()




# class Hexagon(Turtle):
# 	def __init__(self,size2):
# 		Turtle.__init__(self)
# 		self.shapesize2(size2)
# 		begin_poly
# mainloop()