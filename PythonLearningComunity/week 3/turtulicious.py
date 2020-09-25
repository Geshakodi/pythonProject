import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

leonardo.shape("turtle")
leonardo.color("red", "green")

leonardo.circle(40)
leonardo.pendown()
leonardo.forward(25)
leonardo.penup()
leonardo.circle(40)


leonardo.pendown()

paper.exitonclick()
