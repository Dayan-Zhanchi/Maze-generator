import pygame
import random
import cell as ce
import constants as c
import utils.draw_utils
from utils import algo_utils

""" 
    Since there are no weights in the cells the modification of Prims is that we only randomly select the upcoming cells.
    The removal of lines is done by randomly selecting the direction of an adjacent cell to the current cell
"""


def prims(screen, clock):
    grid = [[ce.Cell((i, j), algo_utils.get_neighbours(i, j, False)) for j in range(c.number_of_vertical_lines)]
            for i in range(c.number_of_horizontal_lines)]
    visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    current_cell = grid[x][y]
    upcoming_cells = []
    add_upcoming_cells(current_cell, upcoming_cells, visited)
    visited[current_cell.x][current_cell.y] = True
    maze = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    maze[current_cell.x][current_cell.y] = current_cell

    while upcoming_cells:
        clock.tick(c.frames_prim)

        x, y = algo_utils.get_random_cell(upcoming_cells)
        current_cell = grid[x][y]
        if visited[current_cell.x][current_cell.y]: continue
        visited[current_cell.x][current_cell.y] = True

        direction = get_random_adj_cell_direction(current_cell.x, current_cell.y, maze)
        utils.draw_utils.remove_line(screen, current_cell.x, current_cell.y, direction)
        upcoming_cells.remove((current_cell.x, current_cell.y))
        pygame.display.update()

        add_upcoming_cells(current_cell, upcoming_cells, visited)
        maze[current_cell.x][current_cell.y] = current_cell


# Add unvisited adjacent cells
def add_upcoming_cells(current_cell, upcoming_cells, visited):
    neighbours = algo_utils.get_unvisited_neighbours(current_cell.neighbours, visited)
    for n in neighbours:
        x, y = n
        if not visited[x][y] and (x, y) not in upcoming_cells:
            upcoming_cells.append(n)


# Get the direction of a randomly selected visited adjacent cell
def get_random_adj_cell_direction(x, y, maze):
    adj_cells = algo_utils.get_neighbours(x, y, True)
    adj_cell_direction = []
    for (x, y, direction) in adj_cells:
        if maze[x][y] != 0:
            adj_cell_direction.append(direction)
    return adj_cell_direction[random.randint(0, len(adj_cell_direction) - 1)]