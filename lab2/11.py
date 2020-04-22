import turtle
import time
import math

turtle.shape('turtle')
turtle.speed(0)

def paint_circle(radius,left_right):
    x = 0
    while x < 360:
        if left_right == 'left':
            turtle.left(1)
        elif left_right == 'right':
            turtle.right(1)
        turtle.forward((radius+1)/5)
        x+=1
num_circles = 8
curr_circle = 0
turtle.left(90)
while curr_circle < num_circles: 
    paint_circle(curr_circle,'left')  
    paint_circle(curr_circle,'right')
    
    curr_circle+= 1

time.sleep(5)