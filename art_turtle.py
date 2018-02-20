import turtle

load_window = turtle.Screen()
turtle.colormode(255)

turtle.speed(0)

for i in range(50):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    turtle.color(i, i, i)
turtle.exitonclick()
