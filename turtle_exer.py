import turtle

p = ['red','blue','green','brown','magenta','pink','purple','gold']

turtle.speed(0)


def star():
    # This code prints a mountain-triangle
    for i in range(0, 1):
        turtle.left(70)
        turtle.forward(200)
        turtle.right(80 + 60)
        turtle.forward(200)

"""
for i in range(0,8) :                               # octagon
   turtle.pencolor(p[i])
   turtle.forward(90)
   turtle.left(45)
"""

"""
for i in range(0,3):                                # triangle
    turtle.forward(200)
    turtle.pencolor(p[i+1])
    turtle.left(120)
"""

"""
turtle.penup()                                      # star 2
turtle.setposition(-100,150)
turtle.pendown()

star()
"""

"""                                         #star 3
turtle.penup()
turtle.setposition(-50,-250)
turtle.pendown()

star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()
turtle.left(100)
star()

"""

star()
turtle.right(220)
star()
turtle.right(145)
turtle.forward(225)

turtle.hideturtle()
turtle.exitonclick()
