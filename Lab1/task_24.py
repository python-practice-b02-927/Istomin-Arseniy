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
@task
def task_2_1():
    move_down()
    move_right()
    fill_cross()


if __name__ == '__main__':
    run_tasks()
