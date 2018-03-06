from turtle import *


getscreen().setup(1.0,1.0)
penup()
hideturtle()
goto(-125,150)
write("GAME X", move=False, align="left", font=("Arial", 50, "bold"))
goto(-95,110)
write("Choose a game", move=False, align="left", font=("Arial", 20, "normal"))
goto(-500,0)
write("Connect four(1)", move=False, align="left", font=("Arial", 20, "normal"))
goto(-110,0)
write("Snake(2)", move=False, align="left", font=("Arial", 20, "normal"))
goto(250,0)
write("Hangman(3)", move=False, align="left", font=("Arial", 20, "normal"))
goto(450,-100)
write("More games", move=False, align="left", font=("Arial", 18, "normal"))


mainloop()