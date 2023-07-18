import turtle
turtle.title("Square")
turtle.bgcolor("yellow")
t = turtle.Turtle()
t.pencolor("blue")
t.pensize(5)

t.fillcolor("orange")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
turtle.done()