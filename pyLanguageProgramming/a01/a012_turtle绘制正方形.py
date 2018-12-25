# -*-coding:utf-8-*-

import turtle


def drawRect(x, y, w, h, d=None):
    if d != None:
        turtle.setheading(d)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(w)
    turtle.right(-90)
    turtle.forward(h)
    turtle.right(-90)
    turtle.forward(w)
    turtle.right(-90)
    turtle.forward(h)


def drawSquare(x, y, w, d=None):
    if d != None:
        turtle.setheading(d)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(w)
    turtle.right(-90)
    turtle.forward(w)
    turtle.right(-90)
    turtle.forward(w)
    turtle.right(-90)
    turtle.forward(w)


def drawCircle(x, y, r):
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.circle(r)



# if __name__ == "__main__":
#     turtle.showturtle()
#     drawSquare(0, 0, 100, 0)
#     drawSquare(-100, 0, 100, 0)
#     drawSquare(-100, -100, 100, 0)
#     drawSquare(0, -100, 100, 0)
#     turtle.done()
if __name__ == "__main__":

    turtle.showturtle()

    drawSquare(-100, -100, 200, 0)

    turtle.setheading(-90)
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.forward(200)

    turtle.setheading(0)
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.forward(200)

    turtle.penup()
    turtle.goto(-33, 33)
    turtle.done()

