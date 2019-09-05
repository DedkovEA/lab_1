#!/usr/bin/python3

from pyrob.api import *


def cross():
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_up(2)
    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_up()


@task
def task_2_2():
    move_down()
    for i in range(4):
        cross()
        move_right(2);
    cross()
    move_left(2)


if __name__ == '__main__':
    run_tasks()
