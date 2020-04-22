import turtle
import time

turtle.speed(3)
turtle.shape('turtle')
# turtle.forward(50)
x=1
while x<360*3:
    turtle.left(7)
    turtle.forward(0.5+x/120)
    x+=1

time.sleep(5)