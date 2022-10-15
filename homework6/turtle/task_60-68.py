import turtle

'''задача 60'''
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()

'''задача 61'''

turtle.forward(100)
turtle.left(120)
turtle.forward(100)

turtle.left(120)
turtle.forward(100)
turtle.exitonclick()

'''задача 62'''
turtle.circle(100)
turtle.exitonclick()

'''задача 63'''
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.forward(120)
turtle.pendown()
turtle.pencolor('yellow')
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.forward(120)
turtle.pendown()
turtle.pencolor('red')
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()

'''задача 64'''
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()

'''задача 65'''
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(40)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(40)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(40)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(180)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(40)
turtle.hideturtle()
turtle.exitonclick()

'''задача 66'''
import random

color = ['red', 'orange', 'yellow', 'green', 'blue', 'black', ]

for i in range(8):
    pencolor = random.choice(color)
    turtle.forward(100)
    turtle.left(45)
    turtle.pencolor(pencolor)
turtle.exitonclick()

'''задача 67'''
import turtle



for i in range(0, 10):
    turtle.right(36)
    for i in range(8):
        turtle.forward(100)
        turtle.left(45)
turtle.exitonclick()

'''задача 68'''
import turtle, random

color = ['red', 'orange', 'yellow', 'green', 'blue', 'black', ]

for i in range(0, 10):
    turtle.right(36)
    for i in range(8):
        pencolor = random.choice(color)
        turtle.forward(100)
        turtle.left(45)
        turtle.pencolor(pencolor)
turtle.exitonclick()

