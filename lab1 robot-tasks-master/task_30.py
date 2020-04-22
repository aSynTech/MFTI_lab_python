#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    side=0
    while wall_is_on_the_right() == 0:
        move_right()
        side+=1
    move_left(side) 
    x=0
    lev_coun=0
    for x in range (side,1,-2):
        cicle=1
        while cicle <5:
            cur=0
            while cur<x:
                if cicle == 1:
                    move_right()
                elif cicle == 2:
                    move_down()
                elif cicle == 3:
                    move_left()
                else:
                    move_up()

                if cur<x-1:
                    fill_cell()
                cur+=1
            cicle+=1
        move_right()
        move_down()
        lev_coun+=1

    to_home=0
    while to_home <lev_coun:
        move_left()
        move_down()
        to_home+=1
            
            




if __name__ == '__main__':
    run_tasks()
