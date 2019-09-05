#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    left=True

    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        fill_cell()

    flag1= not wall_is_beneath()
    while flag1:
        move_down()
        fill_cell()
        flag2=True
        while flag2:
            if left:
                 move_left()
                 fill_cell()
            else:
                 move_right()
                 fill_cell()
            flag2=not (wall_is_on_the_right() or wall_is_on_the_left())
        left=wall_is_on_the_right()
        flag1 = not wall_is_beneath()

    if left:
        while not wall_is_on_the_left():
            move_left()

if __name__ == '__main__':
    run_tasks()
