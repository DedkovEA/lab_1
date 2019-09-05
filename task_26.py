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


def cross_line():
    for i in range(9):
        cross();
        move_right(2);
    cross();
    move_left(38);


@task(delay=0.02)
def task_2_4():
    cross_line();
    for j in range(4):
        move_down(4);
        cross_line();


if __name__ == '__main__':
    run_tasks()
