#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    cou=0
    while wall_is_on_the_right() == 0:
        move_right()
        if cou>0 and cell_is_filled():
            cou+=1
        elif cell_is_filled() == 1:
            cou = 1
        else:
            cou = 0
        if cou == 3:
            break  


if __name__ == '__main__':
    run_tasks()
