import math
import turtle
turtle.title("right triangle")
t = turtle.Turtle()

t.fillcolor("yellow")
t.begin_fill()
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(135)
x = math.sqrt(100**2 + 100**2)
t.fd(x)
t.end_fill()
turtle.done()