#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    counter=0
    if cell_is_filled():
        counter+=1
    while not wall_is_on_the_right():
        move_right()
        if cell_is_filled():
            counter+=1
        else:
            counter=0
        if counter==3:
            break
        


if __name__ == '__main__':
    run_tasks()
