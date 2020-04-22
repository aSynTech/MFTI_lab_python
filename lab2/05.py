import turtle
import time

turtle.speed(3)
turtle.shape('turtle')
# turtle.forward(50)
x=1
while x<11:
    turtle.forward(x*10+20)
    turtle.left(90)
    turtle.forward(x*10+20)
    turtle.left(90)
    turtle.forward(x*10+20)
    turtle.left(90)
    turtle.forward(x*10+20)

    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(180)
    turtle.pendown()
    x+=1




time.sleep(5)