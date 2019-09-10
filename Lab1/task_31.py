#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    f=False
    while True:
        while not wall_is_on_the_right():
            move_right()
        while not wall_is_beneath():
            move_down()
        while wall_is_beneath():
            if wall_is_on_the_left():
                f=True
                break
            move_left()
        if f:
            break
        move_down()        
    
if __name__ == '__main__':
    run_tasks()
