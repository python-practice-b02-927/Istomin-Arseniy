#!/usr/bin/python3

from pyrob.api import *

def fill_triangle_left(n):
    a=0
    while True:
        move_left()
        fill_cell()
        if a!=0:
            for i in range(a):
                move_down()
                fill_cell()
            move_up(n=a)
            for i in range(a):
                move_up()
                fill_cell()
            move_down(n=a)
        a+=1
        if wall_is_on_the_left():
            break
def fill_triangle_right(n):
    a=0
    while True:
        move_right()
        fill_cell()
        if a!=0:
            for i in range(a):
                move_down()
                fill_cell()
            move_up(n=a)
            for i in range(a):
                move_up()
                fill_cell()
            move_down(n=a)
        a+=1
        if wall_is_on_the_right():
            break
def fill_triangle_up(n):
    a=0
    while True:
        move_up()
        fill_cell()
        if a!=0:
            for i in range(a):
                move_right()
                fill_cell()
            move_left(n=a)
            for i in range(a):
                move_left()
                fill_cell()
            move_right(n=a)
        a+=1
        if wall_is_above():
            break
def fill_triangle_down(n):
    a=0
    while True:
        move_down()
        fill_cell()
        if a!=0:
            for i in range(a):
                move_right()
                fill_cell()
            move_left(n=a)
            for i in range(a):
                move_left()
                fill_cell()
            move_right(n=a)
        a+=1
        if wall_is_beneath():
            break
        
            
            
            
    
@task(delay=0.01)
def task_9_3():
    count=0
    while not wall_is_on_the_right():
        move_right()
        count+=1
    move_left(count)
    count//=2
    move_right(count)
    move_down(count)
    fill_triangle_left(count)
    move_right(count)
    fill_triangle_up(count)
    move_down(count)
    fill_triangle_right(count)
    move_left(count)
    fill_triangle_down(count)
    move_left(count)
    


if __name__ == '__main__':
    run_tasks()
