#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
	while not wall_is_above():
		move_up(n=1)
	if wall_is_on_the_left():
		while not wall_is_on_the_right():
			move_right(n=1)
	else:
		while not wall_is_on_the_left():
			move_left(n=1)

if __name__ == '__main__':
    run_tasks()
