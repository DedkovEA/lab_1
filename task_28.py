#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    k = 0
    while k < 5:
        move_right()
        k += cell_is_filled()


if __name__ == '__main__':
    run_tasks()
