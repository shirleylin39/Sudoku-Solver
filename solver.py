import numpy as np

# Check if the given numbers in the puzzle follow the sudoku rule
def check_sudoku(grid):
    for row in grid:
        if not check_number_set(row):
            return False

    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if not check_number_set(column):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not check_number_set(block):
                return False
    
    return True

def check_number_set(nums):
    used_nums = set()
    for num in nums:
        if num != 0 and (num < 1 or num > 9 or num in used_nums):
            return False
        used_nums.add(num)
    return True


# Get valid numbers for each empty cell
def valid_nums(sudoku, row, col,):
    invalid_nums = set(sudoku[row]) | set(sudoku[:, col]) | set(sudoku[row//3*3:row//3*3+3, col//3*3:col//3*3+3].flatten())
    return [num for num in range(1, 10) if num not in invalid_nums]


# Solve the puzzle using backtracking (modified to prioritize cells with fewer possible numbers)
def solve_sudoku(sudoku):
    
    empty_cells = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    empty_cells.sort(key = lambda cell: len(valid_nums(sudoku, cell[0], cell[1])))
        
    for i, j in empty_cells:
        if sudoku[i][j] == 0:
            for num in valid_nums(sudoku, i, j):
                sudoku[i][j] = num
                if solve_sudoku(sudoku):
                    return True
                sudoku[i][j] = 0
            return False
    return True

def sudoku_solver(sudoku):
    
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    
    original_sudoku = np.copy(sudoku)
    
    if not check_sudoku(sudoku):
        return np.full_like(original_sudoku, -1)

    if solve_sudoku(sudoku):
        return sudoku

    return np.full_like(original_sudoku, -1)
