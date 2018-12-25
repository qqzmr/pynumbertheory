# -*-coding:utf-8-*-

import turtle


def drawCircle(x, y, r):
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.circle(r)


if __name__ == "__main__":
    r = 100
    turtle.showturtle()
    drawCircle(r, r, r)
    drawCircle(-r, r, r)
    drawCircle(-r, -r, r)
    drawCircle(r, -r, r)
    turtle.done()
