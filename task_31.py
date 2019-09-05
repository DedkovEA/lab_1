#!/usr/bin/python3

from pyrob.api import *


def check():
    while not wall_is_on_the_right():
        move_right()
    while (not wall_is_on_the_left()) and wall_is_beneath():
        move_left()
    if wall_is_beneath():
        return False
    else:
        return True


@task(delay=0.01)
def task_8_30():
    while check():
        move_down()


if __name__ == '__main__':
    run_tasks()
