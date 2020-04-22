#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    y=1
    move_down()
    move_right()
    while y<14:
        #fill_cell()   
        x=1  
        fill_cell()  
        while x<=y:
            fill_cell()  
            move_right() 
            x+=1
        move_left(x-1)
        move_down()
        y+=1

if __name__ == '__main__':
    run_tasks()
