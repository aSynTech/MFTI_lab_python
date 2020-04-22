from graph import *
# from tkinter import *
import math
import turtle

# def handler_pos()
#     print('x:', event.x, 'y:', event.y)

# root = Tk()
#ffb082
windowSize(500,600)

#sky
brushColor("#84cfff")
polygon([(0,0), (500,0),
        (500,600),(0,600) ])

def cloud(pos_x,pos_y,width):
    penColor("#8cd2ff")
    brushColor("white")
    cloud_x=pos_x
    cloud_y=pos_y
    while cloud_x-pos_x<width:
        cloud_y=math.sin(cloud_x)*width/7 + pos_y
        circle(cloud_x, cloud_y, width/7)
        cloud_x+=1
#sea
brushColor("#00ffff")
polygon([(0,200), (500,200),
        (500,600),(0,600) ])

#sea_wave
penColor("white")
brushColor("#00ffff")
wave_x=0
wave_y=270
while wave_x<501:
    wave_y=math.sin(wave_x)*10 + 270
    circle(wave_x, wave_y, 10)
    wave_x+=1

#dust
brushColor("Yellow")
polygon([(0,270), (500,270),
        (500,600),(0,600) ])

def sun(pos_x,pos_y,width, rays):
    brushColor("Yellow")
    circle(pos_x, pos_y, width)
    # count_rays=0
    # while count_rays<rays:
    #     turtle.forward(width)
    #     turtle.left(180-(360/(2*rays)))
    #     count_rays+=1


# print(windowSize())
# rectangle(100,200,200,220)

def trunk_segment(position_x, position_y,width,lenght):   #левый нижний край верхнего сегмента
    rectangle(position_x,position_y, position_x+width, position_y-lenght)

def trunk_upper_segment1(position_x, position_y,width,lenght):   #левый нижний край среднего сегомента
    polygon([(position_x,position_y), (position_x+width,position_y)
    ,(position_x+(lenght/7)+width,position_y-(lenght*.9)), (position_x+(lenght/7),position_y-(lenght*0.9))])

def trunk_upper_segment2(position_x, position_y,width,lenght):   #левый нижний край среднего сегомента
    polygon([(position_x,position_y), (position_x+width,position_y)
    ,(position_x+(lenght/4)+width,position_y-(lenght*0.6)), (position_x+(lenght/4),position_y-(lenght*0.6))])

def branch(position_x,position_y,width,lenght,segm_num,left_right): #позиция левого нижнего сегмента ствола
    N = 15
    if left_right == 'left':
        segm_to_right=1
    else:
        segm_to_right=2
    x0=position_x+width*(segm_num-segm_to_right)
    y0=position_y-segm_num*lenght
    x1=x0
    x2=x1
    y1=y0
    y2=y1
    for x in range(N):
        # y = ((x-4)**2)
        y=-(x**0.5)*10
        x1=x2

        y1=y2
        if left_right == 'left':
            x2=x0+x*lenght/12
        else:
            x2=x0-x*lenght/12
        y2=y0+y
        if x != 0:
            line(x1, y1, x2, y2)
        x += 1
        if x>3 and (x-2)%4==0 and segm_num==2:
            circle(x2, y2, 10)
        if x>3 and x%3==0 and segm_num==3:
            circle(x2, y2, 10)
            moveTo(x2, y2+100)

def trunk (position_x, position_y,width_segm,lenght_segm): #параметры первого сегмента
    brushColor("#006834")
    penColor("#105d29")
    trunk_segment(position_x,position_y,width_segm,lenght_segm)
    trunk_segment(position_x,position_y-lenght_segm-5,width_segm,lenght_segm)
    trunk_upper_segment1(position_x,position_y-(2*lenght_segm)-10,width_segm,lenght_segm)
    trunk_upper_segment2(position_x+(lenght_segm/7),position_y-(2*lenght_segm)-(lenght_segm*0.9)-15,width_segm,lenght_segm)
    branch (position_x,position_y,width_segm,lenght_segm,3,'left')
    branch (position_x,position_y,width_segm,lenght_segm,2,'left')
    branch (position_x,position_y,width_segm,lenght_segm,3,'right')
    branch (position_x,position_y,width_segm,lenght_segm,2,'right')

sun(100,100,50,37)

cloud(50,70,30)
cloud(200,30,50)
cloud(300,100,20)
cloud(400,80,50)

trunk (210,450,20,120)
trunk (110,400,10,80)
trunk (60,400,7,50)
trunk (280,425,7,50)
trunk (370,350,10,80)

run()