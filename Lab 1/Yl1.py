import turtle
turtle.hideturtle()
turtle.penup()
x=-100
c=0
turtle.goto(-100,100)
turtle.pensize(15)
for i in range(3):
	if c==0:
		turtle.pencolor("blue")
	elif c==1:
		turtle.pencolor("black")
	else:
		turtle.pencolor("red")
	turtle.pendown()
	turtle.circle(40)
	turtle.penup()
	turtle.goto(x+100,100)
	x=x+100
	c=c+1
turtle.goto(50,75)
for i in range(2):
	if c==3:
		turtle.pencolor("green")
	else:
		turtle.pencolor("yellow")
	turtle.pendown()
	turtle.circle(40)
	turtle.penup()
	turtle.goto(-50,75)
	c=c+1

turtle.mainloop()