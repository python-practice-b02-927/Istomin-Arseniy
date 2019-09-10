#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    x=0
    while not wall_is_on_the_right():
        x+=1
        move_right()
        a=0
        while not wall_is_above():
            move_up()
            fill_cell()
            a+=1
        if a!=0:
            fill_cell()
            move_down(n=a)
    move_left(n=x)
        


if __name__ == '__main__':
    run_tasks()
