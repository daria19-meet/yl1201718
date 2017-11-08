import turtle
turtle.speed(200)
x=0
for i in range(360):
	turtle.left(x)
	turtle.pendown()
	turtle.forward(200)
	turtle.right(50)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	x=x+1
	turtle.home()
turtle.mainloop()