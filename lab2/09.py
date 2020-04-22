import turtle
import time
import math

# turtle.shape('turtle')

turtle.shape('turtle')

def paint_polygon (length_side,polygon_faces):
    x=0
    turtle.left((180-(360/polygon_faces))/2)
    while x<polygon_faces:       
        turtle.left(360/(polygon_faces)) 
        turtle.forward(length_side)
        x+=1
    
length_first_side=50
length_current_side=length_first_side
shapes=0
prev_shapes=0
while shapes<10:
    x=0
    # length_prev_side=length_current_side
    print(shapes, ' --', length_current_side)
    length_current_side = (length_current_side/(2*math.sin((2*math.pi)/(2*(prev_shapes+3)))) + 10*shapes) * ( 2 * math.sin((2*math.pi)/(2*(shapes+3))))
    paint_polygon(length_current_side,shapes+3)
    # turtle.right(360/((shapes+3)*2))
    turtle.right((180-(360/(shapes+3)))/2)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    # turtle.left(360/((shapes+3)*2))

    
    # while x<shapes+3:
    #     turtle.forward(50)
    #     turtle.left(360/(shapes+3))
    #     x+=1
    # turtle.right(360/((shapes+3)*2))
    # turtle.move(5)
    shapes+=1
time.sleep(5)