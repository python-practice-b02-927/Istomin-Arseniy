#!/usr/bin/python3

from pyrob.api import *

def move_to_the_left_wall():
    while not wall_is_on_the_left():
        move_left(n=1)
        
        
def find_exit():
    while True:
        if not wall_is_above():
            move_up(n=1)
            break
        move_right(n=1)
            
            
def move_to_the_top_left_corner():
    while not wall_is_above():
        move_up(n=1)
    while not wall_is_on_the_left():
        move_left(n=1)
        
        
@task
def task_8_28():
    move_to_the_left_wall()
    find_exit()
    move_to_the_top_left_corner()

if __name__ == '__main__':
    run_tasks()
