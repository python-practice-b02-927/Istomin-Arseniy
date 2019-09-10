#!/usr/bin/python3

from pyrob.api import *


def fill_cross():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_left()
    move_up()
    fill_cell()
    move_up()


@task(delay=0.02)
def task_2_4():
    for i in range(5):
        for j in range(9):
            fill_cross()
            move_right(n=4)
        fill_cross()
        move_left(n=36)
        if not i==4:
            move_down(n=4)


if __name__ == '__main__':
    run_tasks()
