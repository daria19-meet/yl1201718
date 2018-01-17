from turtle import *
import time
import random 
from ball import Ball
hideturtle()
tracer(0)
colormode(255)
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH= getcanvas().winfo_width()//2
SCREEN_HEIGHT= getcanvas().winfo_height()//2
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]

for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	while dx==0:
		dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy==0:
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))


MY_BALL= Ball(x,y,dx,dy,r,color)
BALLS.append(MY_BALL)
update()
mainloop()