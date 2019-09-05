#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    k = 0
    while not wall_is_on_the_right():
        move_right()
        j = 0
        while not wall_is_above():
            move_up()
            fill_cell()
            j+=1
        if j: move_down(j)
        k+=1
    if k: move_left(k)
if __name__ == '__main__':
    run_tasks()
