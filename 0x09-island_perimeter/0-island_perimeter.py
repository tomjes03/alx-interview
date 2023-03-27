#!/usr/bin/python3
""" Perimeter of the island """


def island_perimeter(grid):
    """
    A function that returns the perimeter of the island

    Argument:
    grid: list of list of integers

    Returns: integer
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    # add rows of only zeros at top and bottom of grid
    grid = [[0]*n_cols] + grid + [[0]*n_cols]
    # add cols of only zeros at left and right of grid
    for i in range(n_rows + 2):
            grid[i] = [0] + grid[i] + [0]
    perimeter = 0
    islands = 0
    for row in range(n_rows + 1):
        for col in range(n_cols + 1):
            if grid[row][col] == 1:
                up = grid[row - 1][col]
                down = grid[row + 1][col]
                left = grid[row][col - 1]
                right = grid[row][col + 1]
                total = up + down + left + right
                if total == 0:
                    islands += 1
                    perimeter += 4 - total
                else:
                    perimeter += 4 - total
    if islands > 1:
        return
    return perimeter

if __name__ == '__main__':
    island_perimeter(grid)
