#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_6_6():
    y=0
    while wall_is_on_the_right() == 0:
        move_right()
        y+=1
        x=0
        while wall_is_above() == 0: 
            move_up()
            fill_cell()
            x+=1
        if wall_is_above() == 1 and wall_is_beneath() == 0:
            move_down(x)
    move_left(y)

if __name__ == '__main__':
    run_tasks()
