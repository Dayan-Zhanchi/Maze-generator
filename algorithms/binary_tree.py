import random

from constants import dimension_consts as c
from constants import frame_consts
from components.maze import Maze
from utils import draw_utils


def binary_tree(screen, clock):
    maze = Maze()
    bias = 'NW'

    for x in range(c.number_of_horizontal_lines):
        for y in range(c.number_of_vertical_lines):
            clock.tick(frame_consts.frames_binary_tree)
            current_cell = maze.grid[x][y]
            neighbours = current_cell.neighbours
            chosen_random_direction = ''
            jump = False

            if bias == 'NW':
                jump, chosen_random_direction = check_northwest_case(x, y, bias)
            if jump:
                continue

            for (_, _, direction) in neighbours:
                if chosen_random_direction == direction:
                    draw_utils.remove_line(screen, current_cell.x, current_cell.y, chosen_random_direction)
                    break


def check_northwest_case(x, y, bias):
    chosen_random_direction = ''
    jump = False
    if x == 0 and y == 0:
        jump = True
    elif x == 0 and y > 0:
        chosen_random_direction = 'N'
    elif x > 0 and y == 0:
        chosen_random_direction = 'W'
    else:
        chosen_random_direction = bias[random.randint(0, len(bias) - 1)]
    return jump, chosen_random_direction
