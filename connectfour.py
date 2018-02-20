import turtle
from turtle import *

penup()
getscreen().setup(1.0,1.0)
RED_DISCS=[]
YELLOW_DISCS=[]
r=40
bgcolor("Navy")
shape("circle")
shapesize(r/10)
color("White")
HOLES=[]
sec=100
goto(-500,300)
y=300
x=-500
def make_columns(width):
	global y
	for i in range(6):
		hole1=turtle.clone()
		HOLES.append(hole1)
		y=y-125
		goto(width,y)
times=0
while times<6:
	make_columns(x)
	x=x+185
	turtle.goto(x,300)
	y=300
	times=times+1

	if times==6:
		turtle.hideturtle()

turns=1 
if turns%2==0:	
	rowy=input("What row yellow?")
	coluy=int(input("What column yellow?"))
else:
	rowrd=input("What row red?")
	colur=int(input("What column red?"))


mainloop()