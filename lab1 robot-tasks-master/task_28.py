#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    cou=0
    while wall_is_on_the_right() == 0:
        move_right()
        if cell_is_filled() == 1:
            cou+=1
        if cou == 5:
            break
        


if __name__ == '__main__':
    run_tasks()
