import turtle
import time

turtle.speed(3)
turtle.shape('turtle')
# turtle.forward(50)
cou=12
x=0
while x<cou:
    # turtle.forward(100)
    turtle.left(360/cou)
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180)
    x+=1




time.sleep(5)