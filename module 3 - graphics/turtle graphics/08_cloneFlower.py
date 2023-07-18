import turtle
t=turtle.Turtle()

c = t.clone()
t.color("magenta")
c.color("red")

def flower():
    for i in range(5):
        t.circle(100,90)
        t.left(90)
        c.circle(60,90)
        c.left(90)
        t.circle(100,90)
        t.left(18)
        c.circle(60,90)
        c.left(18)

flower()

turtle.done()
