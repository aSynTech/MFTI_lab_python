#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    while wall_is_on_the_right() == 0:
        if wall_is_above() == 1:
            fill_cell()
        up_step=0
        while wall_is_above() == 0:  
            # if cell_is_filled() == 0:
            #     move_up()
            # else:
            move_up()
            if cell_is_filled() == 0:
                fill_cell()
            up_step+=1
        while wall_is_beneath() == 0:
            move_down()
        move_right()


if __name__ == '__main__':
    run_tasks()
