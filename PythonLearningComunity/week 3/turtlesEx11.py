import turtle
window=turtle.Screen()
turtle.bgcolor("green")
gesh=turtle.Turtle()
gesh.shape("turtle")
gesh.color("blue")
gesh.stamp()
for i in range(12):
    gesh.penup()
    gesh.forward(100)
    gesh.pendown()
    gesh.forward(20)
    gesh.penup()
    gesh.forward(20)
    gesh.stamp()
    gesh.forward(-140)
    gesh.left(30)


window.exitonclick()