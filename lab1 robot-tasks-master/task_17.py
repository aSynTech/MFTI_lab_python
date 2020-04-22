#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while cell_is_filled() == 0:
        move_up()
    move_left()
    if cell_is_filled() == 0:
        move_right(2)

#    elif wall_is_beneath() == 0:
#        while wall_is_beneath() == 0:
#            move_down()
#
#    if wall_is_on_the_right() == 0:
#        while  wall_is_on_the_right() == 0:   
#            move_right()
#    elif wall_is_on_the_left() == 0:
#        while wall_is_on_the_left() == 0:
#            move_left()



if __name__ == '__main__':
    run_tasks()
