import turtle
import time
import math

turtle.shape('turtle')
turtle.speed(3)

def star(apex):
    count_apex=0
    while count_apex<apex:
        turtle.forward(300)
        turtle.left(180-(360/(2*apex)))
        count_apex+=1


star(37)

time.sleep(15)