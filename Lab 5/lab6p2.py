from turtle import *

# class Hexagon(Turtle):
# 		Turtle. __init__(self)
# 		self.penup()
# 		self.begin_poly()
# 		for i in range(6):
# 			self.forward(size)
# 			self.left(60)
# 		self.end_poly()
# 		h=self.get_poly()
# 		register_shape("Hex",h)
# 		self.shape("Hex")

# he=Hexagon(100)


class Polygon(Turtle):
	def __init__ (self,sides):
		Turtle. __init__(self)
		self.penup()
		self.begin_poly()
		for i in range(sides):
			self.forward(100)
			self.left(360/sides)
		self.end_poly()
		h=self.get_poly()
		register_shape("Hex",h)
		self.shape("Hex")

s=Polygon(17)
mainloop()