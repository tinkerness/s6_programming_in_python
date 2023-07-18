import turtle
turtle.title("circle")
t = turtle.Turtle()
t.speed(0)

t.fillcolor("yellow")
t.begin_fill()
for i in range(360):
    t.forward(2)
    t.right(1)
t.end_fill()

turtle.done()