#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():    
    y=1
    move_right()
    while y<13:
        fill_cell()
        y+=1   
        x=1    
        while x<27:
            move_right()
            fill_cell()
            x+=1
        move_left(26)
        move_down()

if __name__ == '__main__':
    run_tasks()
