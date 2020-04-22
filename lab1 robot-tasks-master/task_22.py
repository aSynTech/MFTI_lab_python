#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    par = 0
    fill_cell()
    while wall_is_on_the_right() == 0:
        move_right()
        par+=1  
    y=0
    
    while wall_is_beneath() == 0: 
        x=0
        # fill_cell()
        while x < par:
            fill_cell()
            move_left()
            x+=1
        y+=1
        fill_cell()
        move_down()
        move_right(par)
    x2=0
    while x2 < par:
            fill_cell()
            move_left()
            x2+=1
    fill_cell()
           
if __name__ == '__main__':
    run_tasks()
