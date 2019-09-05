#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    k = 1
    flag1=True
    move_right()
    while flag1:
        fill_cell()
        i = 0
        while (not wall_is_on_the_right()) and i<k:
            move_right()
            i+=1
        k+=1
        flag1 = not wall_is_on_the_right()


if __name__ == '__main__':
    run_tasks()
