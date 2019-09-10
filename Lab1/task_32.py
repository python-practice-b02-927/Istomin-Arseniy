#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    val=0
    while not wall_is_on_the_right():
        if wall_is_above():
            if cell_is_filled():
                val+=1
            fill_cell()
        move_right()
        a=0
        if wall_is_on_the_right():
            break
        while not wall_is_above():
            move_up()
            if cell_is_filled():
                val+=1
            fill_cell()
            a+=1
        if a!=0:
            fill_cell()
            move_down(a)
    print(val)
    mov('ax', val)


if __name__ == '__main__':
    run_tasks()
