import turtle

def draw_star(t, length):
    t.begin_fill()
    for _ in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()

def draw_stars_in_circle(t, num_stars, star_size, circle_radius):
    angle_step = 360 / num_stars
    for i in range(num_stars):
        t.penup()
        t.goto(0, 0)
        t.setheading(angle_step * i)
        t.forward(circle_radius)
        t.right(36)  # Adjust to orient the star properly
        t.pendown()
        draw_star(t, star_size)
    t.penup()

drawer = turtle.Turtle()
drawer.shape("turtle")
drawer.speed(2)
drawer.fillcolor("red")

draw_stars_in_circle(drawer, 5, 100, 200)

drawer.hideturtle()
turtle.done()