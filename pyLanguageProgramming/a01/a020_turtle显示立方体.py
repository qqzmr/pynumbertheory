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
    w = 100
    h = 80
    drawRect(-w, -h, 2 * w, 2 * h, 0)
    drawRect(0, 0, 2 * w, 2 * h, 0) # 两个矩形

    x = 0 # 4条线
    y = 0
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x - w, y - h)

    x = 2 * w
    y = 0
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x - w, y - h)

    x = 2 * w
    y = 2 * h
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x - w, y - h)

    x = 0
    y = 2 * h
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x - w, y - h)

    turtle.done()
