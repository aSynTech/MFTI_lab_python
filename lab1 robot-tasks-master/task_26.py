#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_2_4():   
    y=0
    while y<5:
        x=0
        while x<11:
            move_right()
            fill_cell()
            move_down()
            fill_cell()
            move_right()
            fill_cell()
            move_down()
            move_left()
            fill_cell()
            move_left()
            move_up()
            fill_cell()
            move_up()
           
            if x<9:
                move_right(4)
            x+=1
        move_left(36)
        if y<4:
            move_down(4)
        y+=1

if __name__ == '__main__':
    run_tasks()
