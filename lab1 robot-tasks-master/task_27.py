#!/usr/bin/python3

from pyrob.api import *

@task
def task_7_5():





    move_right()
    fill_cell()
    
    end = 0
    cur = 0
    while end == 0:      
        x=1
        while x<cur:           
            if wall_is_on_the_right() == 1:
                break
            move_right()
            x+=1
        if wall_is_on_the_right() == 0:
            fill_cell()
        cur+=1
        if wall_is_on_the_right() == 1:
            end = 1













if __name__ == '__main__':
    run_tasks()
