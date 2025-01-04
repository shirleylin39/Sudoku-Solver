# Sudoku Solver

This repository contains an implementation of a Sudoku solver using a constraint satisfaction approach featuring backtracking. By leveraging principles of artificial intelligence, this solver is optimized for solving puzzles across various difficulty levels, ranging from "very easy" to "hard."

## Table of Contents

- [Project Overview](#project-overview)
- [Files in the Repository](#files-in-the-repository)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Optimizations](#optimizations)

## Project Overview

Sudoku is a logic-based puzzle game requiring the placement of numbers in a 9x9 grid such that every row, column, and 3x3 block contains all numbers from 1 to 9 exactly once. This solver employs artificial intelligence techniques, including systematic constraint satisfaction and heuristic optimization, to explore valid solutions, ensuring correctness and efficiency.

## Files in the Repository

1. **`main.py`**
   - Serves as the entry point of the program.
   - Loads Sudoku puzzles and their solutions from pre-saved `.npy` files.
   - Tests the `sudoku_solver` function on puzzles of varying difficulties and reports results.

2. **`solver.py`**
   - Contains the implementation of the Sudoku solver.
   - Implements utility functions like `check_sudoku`, `valid_nums`, and the core backtracking algorithm `solve_sudoku`.

## Usage

### Prerequisites

- Python 3.7 or above
- NumPy library

### Running the Program

1. Ensure you have the required puzzle files (`very_easy_puzzle.npy`, `easy_puzzle.npy`, etc.) in a `data/` directory.
2. Run the program using the following command:
   ```bash
   python main.py
   ```
3. The program will test the solver on puzzles of different difficulties and display the results, including correctness and solving time for each puzzle.

## Implementation Details

The solver is implemented using a backtracking algorithm enhanced with artificial intelligence techniques and constraint satisfaction principles:

1. **Constraint Validation**:
   - Ensures that placing a number in an empty cell satisfies Sudoku rules.

2. **Valid Numbers**:
   - A helper function identifies valid numbers for each empty cell based on current constraints.

3. **Backtracking**:
   - Iteratively fills cells and backtracks upon encountering conflicts.

## Optimizations

1. **Valid Number Precomputation**:
   - Reduces redundant checks by computing possible numbers for each cell in advance.

2. **Priority-Based Exploration**:
   - Prioritizes cells with fewer valid numbers, minimizing the search space and improving efficiency.