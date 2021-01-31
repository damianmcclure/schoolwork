import turtle
draw = turtle.Turtle()

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

draw_circle(draw, "blue", 50, 0, -25)
draw_circle(draw, "blue", 35, 0, 50)
draw_circle(draw, "blue", 20, 0, 110)

input("")
