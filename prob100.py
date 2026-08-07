# Problem 100 - Basic Sudoku Validator


def is_valid_sudoku(grid):
    for i in range(9):
        for j in range(9):
            num = grid[i][j]

            if num == 0:
                continue

            for x in range(9):
                if x != j and grid[i][x] == num:
                    return False

            for x in range(9):
                if x != i and grid[x][j] == num:
                    return False

            start_row = (i // 3) * 3
            start_col = (j // 3) * 3
            for x in range(start_row, start_row + 3):
                for y in range(start_col, start_col + 3):
                    if (x != i or y != j) and grid[x][y] == num:
                        return False

    return True


grid = []
for i in range(9):
    row = list(
        map(int, input("Enter row " + str(i + 1) + " (space separated): ").split())
    )
    grid.append(row)

if is_valid_sudoku(grid):
    print("Valid Sudoku")
else:
    print("Invalid Sudoku")
