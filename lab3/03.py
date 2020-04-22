from graph import *
# from tkinter import *

# def handler_pos()
#     print('x:', event.x, 'y:', event.y)

# root = Tk()

brushColor("yellow")
circle(150, 150, 100)

brushColor("red")
circle(100, 120, 17)
circle(200, 120, 15)

brushColor("black")
circle(100, 120, 10)
circle(200, 120, 10)

polygon([(50,70), (50,80),
        (130,120),(130,110) ])

polygon([(180,110), (180,120),
         (240,90), (240,80)])

rectangle(100,200,200,220)
# x1 = 100; y1 = 100
# x2 = 300; y2 = 200
# N = 10
# rectangle (x1, y1, x2, y2)
# h = (x2 - x1) / (N + 1)
# x = x1 + h
# for i in range(N):
#   line(x, y1, x, y2)
#   x += h


run()