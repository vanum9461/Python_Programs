import turtle

turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.color("purple")
turtle.write("Olympic Games",font=("Arial", 20, "normal"))

turtle.color("blue")
turtle.penup()
turtle.goto(-120, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(120, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-60, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(60, -75)
turtle.pendown()
turtle.circle(45)
turtle.penup()
turtle.done()
