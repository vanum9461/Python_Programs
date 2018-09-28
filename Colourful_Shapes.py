import turtle

turtle.bgcolor("pink")

turtle.pensize(3)
turtle.penup()
turtle.goto(200,50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(-200,50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(50,steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("orange")
turtle.circle(50,steps=4)
turtle.end_fill()

turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("green")
turtle.circle(50,steps=5)
turtle.end_fill()

turtle.penup()
turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(50,steps=6)
turtle.end_fill()

turtle.done()

