import random
import constants as c
import utils.draw_utils as du
from maze import Maze
from utils.alg_util import get_unvisited_neighbours


def growing_tree(screen, clock):
    maze = Maze()
    generating_approach = ['Prims', 'RB']
    x, y = random.randint(0, c.number_of_horizontal_lines - 1), random.randint(0, c.number_of_vertical_lines - 1)
    cells = [maze.grid[x][y]]
    maze.visited[x][y] = True
    while cells:
        clock.tick(c.frames_growing_tree)
        # randomly select an approach, either Prims or recursive backtracking
        approach = random.randint(0, len(generating_approach) - 1)
        if approach == 'RB':
            current_cell = cells[-1]
        else:
            current_cell = maze.get_random_cell(cells)

        unvisited_neighbours = get_unvisited_neighbours(current_cell, maze.visited)
        if not unvisited_neighbours:
            if approach == 'RB':
                cells.pop()
            else:
                cells.remove(current_cell)
            continue
        x, y, direction = maze.get_random_cell(unvisited_neighbours)
        maze.visited[x][y] = True
        du.remove_line(screen, current_cell.x, current_cell.y, direction)
        cells.append(maze.grid[x][y])
