import turtle
t = turtle.Turtle()

turtle.Screen().bgcolor("black")
t.speed(0)

def flower():
	for i in range(175):
		t.fillcolor("yellow")
		t.begin_fill()
		t.pencolor("blue")
		t.circle(190-i,90)
		t.left(90)
		t.end_fill()
		t.fillcolor("orange")
		t.begin_fill()
		t.pencolor("red")
		t.circle(190-i,90)
		t.left(18)
		t.end_fill()

flower()

turtle.done()