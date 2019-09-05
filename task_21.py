#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    for i in range(13):
        fill_cell()
        j=0
        while j<i:
            move_right()
            fill_cell()
            j=j+1
        j=0
        while j<i:
            move_left()
            j+=1
        move_down()


if __name__ == '__main__':
    run_tasks()
