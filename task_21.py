#!/usr/bin/python3

from pyrob.api import *


@task
def task_4_11():
    move_right()
    move_down()
    for i in range(1,14):
        for j in range(i):
            fill_cell()
            move_right()
            pass
        move_left(n=i)
        move_down()

        
        


if __name__ == '__main__':
    run_tasks()
