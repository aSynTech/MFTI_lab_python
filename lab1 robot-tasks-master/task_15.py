#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_on_the_right() == 0:
        move_right(9)
    elif wall_is_on_the_left() == 0:
        move_left(9)

    if wall_is_above() == 0:
        move_up(9)
    elif wall_is_beneath() == 0:
        move_down(9)
    #while wall_is_on_the_right() != 1 or wall_is_beneath() != 1:
    #    if  wall_is_on_the_right() == 1 :     
    #        if  wall_is_beneath() == 0:       
    #            move_down()
    #    else:
    #        move_right()

if __name__ == '__main__':
    run_tasks()
