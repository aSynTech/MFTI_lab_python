import turtle
import time
import math

turtle.shape('turtle')
turtle.speed(0)

def paint_circle(radius,left_right,paint):
    x = 0
    if paint != '' :
        turtle.color(paint)
        turtle.begin_fill()
    while x < 360:
        if left_right == 'left':
            turtle.left(1)
        elif left_right == 'right':
            turtle.right(1)
        turtle.forward((radius+1)/5)
        x+=1
    if paint != '':
        turtle.end_fill()

def paint_arc(radius,left_right,color):
    x = 0
    if color != '' :
        turtle.color(color)
        # turtle.begin_fill()
    while x < 180:
        if left_right == 'left':
            turtle.left(1)
        elif left_right == 'right':
            turtle.right(1)
        turtle.forward((radius+1)/5)
        x+=1
    # if paint != '':
    #     turtle.end_fill()


paint_circle(10,'right','yellow') 
turtle.right(130)
turtle.forward(100)
turtle.left(130)
print(turtle.position())
paint_circle(0.1,'right','blue')  


turtle.forward(100)
print (turtle.position())
paint_circle(0.1,'right','blue')  

turtle.penup()
turtle.setposition(-14,-90)
turtle.right(90)
turtle.pensize(10)
turtle.pendown()
turtle.color('black')
turtle.forward(50)
print(turtle.position())
turtle.penup()
turtle.setposition(-80,-140)
turtle.pendown()

paint_arc(5,'left','red')




time.sleep(5)