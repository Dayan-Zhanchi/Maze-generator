import utils
import pygame
import constants as c


def recursive_backtracking(screen, clock, grid):
    visited = [[0 for _ in range(c.number_of_vertical_lines)] for _ in range(c.number_of_horizontal_lines)]
    current_cell = grid[0][0]
    stack = [current_cell]
    while stack:
        clock.tick(c.frames_rb)
        neighbours = utils.get_unvisited_neighbours(current_cell.neighbours, visited)
        visited[current_cell.x][current_cell.y] = True

        if neighbours:
            next_cell_x, next_cell_y, direction = utils.get_random_cell(neighbours)
            next_cell = grid[next_cell_x][next_cell_y]
            stack.append(next_cell)
            # removing line of a grid to make the maze
            utils.remove_line(screen, current_cell.x, current_cell.y, direction)
            current_cell = next_cell
            pygame.display.update()
        elif stack:
            # reached a dead end so we backtrack, the stack keeps track of previous cells
            current_cell = stack.pop()

    return True
