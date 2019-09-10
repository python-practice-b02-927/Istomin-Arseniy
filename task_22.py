#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while True:
        i=0
        fill_cell()
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            i+=1
        fill_cell()
        if i!=0:
            move_left(n=i)
        if not wall_is_beneath():
            move_down()
        else:
            break


if __name__ == '__main__':
    run_tasks()
