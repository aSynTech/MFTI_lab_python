#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while wall_is_on_the_left() == 0:
        move_left()
    while  wall_is_on_the_right() == 0:   
        if wall_is_above() == 1:
            move_right()
        else:
            break
    while wall_is_above() == 0:
        move_up()
    while wall_is_on_the_left() == 0:
        move_left()       
        
    # if wall_is_above() == 0:
    #         move_up()
    
#    if wall_is_on_the_right() == 0:
#        while  wall_is_on_the_right() == 0:   
#            move_right()
#    elif wall_is_on_the_left() == 0:
#     while wall_is_on_the_left() == 0:
#            move_left()


if __name__ == '__main__':
    run_tasks()
