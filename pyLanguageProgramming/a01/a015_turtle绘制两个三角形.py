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


if __name__ == "__main__":
    turtle.showturtle()

    turtle.right(60)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(400)

    turtle.right(-120)
    turtle.forward(200)
    turtle.right(-120)
    turtle.forward(200)

    turtle.done()
