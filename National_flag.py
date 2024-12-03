import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
t = turtle.Turtle()
t.speed(2)
t.pensize(5)

# Draw green rectangle
t.penup()
t.goto(-200, 100)
t.pendown()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.right(90)
    t.forward(240)
    t.right(90)
t.end_fill()

# Draw red circle
t.penup()
t.goto(0, -70)
t.color("red")
t.begin_fill()
t.circle(60)
t.end_fill()

# Hide turtle and display
t.hideturtle()
screen.mainloop()

