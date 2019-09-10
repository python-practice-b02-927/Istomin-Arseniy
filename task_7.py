#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
	a=0
	while not wall_is_beneath():
		move_down(n=1)
	while wall_is_beneath():
		move_right(n=1)
		a+=1
	move_down(n=1)
	for i in range(a):
		move_left(n=1)


if __name__ == '__main__':
    run_tasks()
