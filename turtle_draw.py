import turtle

t = turtle.Turtle()

for i in range(6):
    t.pensize(4)
    t.pencolor("Pink")
    t.speed(1)

    # Square
    t.forward(100)
    t.left(90)

    t.forward(100)
    t.left(90)

    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

    turtle.done()