#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while wall_is_on_the_right() == 0:        
        if  wall_is_above() == 0  :
            fill_cell()
        move_right()
    if  wall_is_above() == 0 :
            fill_cell()
            
#    while wall_is_on_the_right() == 0:        
#        if  cell_is_filled() == 1 :
#            fill_cell()
#        move_right()
#    else: 
#        fill_cell()


if __name__ == '__main__':
    run_tasks()
