#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    runs=0
    while runs<20:
        # left_steps=0
        # right_steps=0
        while wall_is_beneath() == 0:
            move_down()
        while wall_is_beneath() == 1 and wall_is_on_the_right() == 0:
            move_right()
            # left_steps+=1
            while wall_is_beneath() == 0:
                move_down()
        while wall_is_beneath() == 1 and wall_is_on_the_left() == 0:
            move_left()
            # right_steps+=1
            while wall_is_beneath() == 0:
                move_down()
        runs+=1  
        # if right_steps == left_steps:
        #     break
if __name__ == '__main__':
    run_tasks()
