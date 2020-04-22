import turtle
import time
import math

turtle.shape('turtle')
turtle.speed(0)

def paint_circle():
    x=0
    while x<360:
        turtle.left(1)
        turtle.forward(1)
        x+=1
num_circles = 8
curr_circle=0
while curr_circle<num_circles:
    turtle.left(360/num_circles)
    curr_circle+=1
    paint_circle()

time.sleep(5)