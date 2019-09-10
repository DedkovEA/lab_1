#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    right = wall_is_on_the_right()
    left = wall_is_on_the_left()
    up = wall_is_above()
    down = wall_is_beneath()

    while right and (not wall_is_on_the_left()):
        move_left()
    while left	and (not wall_is_on_the_right()):
       	move_right()
    while up	and (not wall_is_beneath()):
       	move_down()
    while down	and (not wall_is_above()):
       	move_up()


if __name__ == '__main__':
    run_tasks()
