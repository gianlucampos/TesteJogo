import turtle

# define a estrutura do tiro
tiro = turtle.Turtle()
tiro.shape("triangle")
tiro.color("red")
tiro.shapesize(0.5, 0.5)
tiro.penup()
tiro.setheading(90)
tiro.speed(0)
tiro.setposition(0, -210)
tiro.hideturtle()
estado_tiro = "pronto"
