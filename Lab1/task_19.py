#!/usr/bin/python3

from pyrob.api import *

def find_left():
    while not wall_is_on_the_left():
        move_left()
    if not wall_is_above():
        return True
    return False


def find_right():
    while not wall_is_on_the_right():
        move_right()
    if not wall_is_above():
        return True
    return False


def go_home():
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left() 
@task
def task_8_29():
    if find_left():
        go_home()    
    else:
        if find_right():
            go_home()


if __name__ == '__main__':
    run_tasks()
