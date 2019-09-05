#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():

    size = 2
    move_right()
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
        size += 1
    move_left(size-1)
    for i in range(1, size):
        move_down()
        for j in range(size):
            if not (j == i or j == size-i-1):
                fill_cell()
            if not wall_is_on_the_right():
                move_right()
        move_left(size-1)
        


if __name__ == '__main__':
    run_tasks()
