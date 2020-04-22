import turtle
import time

turtle.speed(3)
turtle.shape('turtle')
# turtle.forward(50)
x=1
while x<30:
    turtle.forward(x*2+20)
    turtle.left(90)
    x+=1

time.sleep(5)