#!/usr/bin/python3

from pyrob.api import *


def fill_upper_and_lower_cells():
	if not wall_is_beneath():
		move_down(n=1)
		fill_cell()
		move_up(n=1)
	if not wall_is_above():
		move_up(n=1)
		fill_cell()	
		move_down(n=1)


@task
def task_8_10():
	while not wall_is_on_the_right():
		fill_upper_and_lower_cells()
		move_right(n=1)
	fill_upper_and_lower_cells()



if __name__ == '__main__':
    run_tasks()
