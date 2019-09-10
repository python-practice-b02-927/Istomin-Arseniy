#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    a=1
    i=0
    while True:
        if not wall_is_on_the_right():
            move_right()
            i+=1
            if i==a:
                fill_cell()
                a+=1
                i=0
        else:
            break
        
           
    


if __name__ == '__main__':
    run_tasks()
