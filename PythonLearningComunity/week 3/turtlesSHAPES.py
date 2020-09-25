import turtle
window=turtle.Screen()
gesh=turtle.Turtle()
gesh.shape("turtle")
for i in range(5):
    gesh.forward(50)
    gesh.left(72)
gesh.penup()
gesh.forward(100)
gesh.pendown()
# pentagon
for i in range(3):
    gesh.forward(500)
    gesh.left(120)
window.exitonclick()
