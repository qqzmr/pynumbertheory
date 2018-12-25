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
    r = 200
    turtle.showturtle()
    drawCircle(0, 0, r)

    a = 20

    turtle.penup()
    turtle.goto(0, r)
    turtle.pendown()
    turtle.goto(0, r - a)

    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()
    turtle.goto(0, -r + a)

    turtle.penup()
    turtle.goto(r, 0)
    turtle.pendown()
    turtle.goto(r - a, 0)

    turtle.penup()
    turtle.goto(-r, 0)
    turtle.pendown()
    turtle.goto(-r + a, 0)

    turtle.done()
