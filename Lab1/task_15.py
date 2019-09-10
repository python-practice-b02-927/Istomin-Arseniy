#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
	if wall_is_beneath() and wall_is_on_the_left():
		move_right(n=9)
		move_up(n=9)
	elif wall_is_above() and wall_is_on_the_left():
		move_right(n=9)
		move_down(n=9)
	elif wall_is_above() and wall_is_on_the_right():
		move_left(n=9)
		move_down(n=9)
	else:
		move_left(n=9)
		move_up(n=9)



if __name__ == '__main__':
    run_tasks()
