#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    N = 0
    while not wall_is_on_the_right():
        if wall_is_above():
            fill_cell()
        else:
            i = 0
            while not wall_is_above():
                move_up()
                i+=1
                if cell_is_filled():
                    N+=1
                else:
                    fill_cell()
            move_down(i)
        move_right()
    mov("ax", N)


if __name__ == '__main__':
    run_tasks()
