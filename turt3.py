import turtle
import random
turtle.circle(50)
x=random.randint(0,200)
y=random.randint(0,200)
turtle.penup()
turtle.goto(-50,50)
turtle.write("x cordinate is",x)
turtle.goto(-70,50)
turtle.write("y cordinate is",y)
turtle.goto(50,70)
if(((x*x)+(y*y))<=(50*50)):
    turtle.write("Inside")
else:
    turtle.write("Outside")
