
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Note:
# - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.

# Link: https://leetcode.com/problems/valid-sudoku/

# Idea:
# We can create a mask for each row, column, and sub-box,
# where in the mask, index 'i' appears as 1 only if 'i' appears in that specific column, row, or sub-box. 
# For instance, let's consider the first row with numbers 1, 4, and 5. 
# The mask for this row would be 000011001 (from left to right). We can apply the same concept to individual cell values. 
# For instance, if board[i][j] = 1, its mask would be 000000001.
# To identify duplicates, we can use the bitwise AND operation. 
# If this operation returns 0, then there is no collision. 
# Otherwise, if it returns a non-zero value, we can conclude that there is a collision and return False.

# Function:
# 1. We create an array to store the masks for each row, column, and sub-box.
# 2. We iterate through all rows (from [0][0] to [8][8]).
# 3. If the symbol is ".", we continue to the next cell. 
# Otherwise, we create a mask for the number 'x' that appears in this cell using the mask = 1 << num operation. 
# We then check for collisions in the corresponding row, column, and sub-box by examining the masks in the arrays we created. 
# If we find a collision, we return False.
# Now we update the masks in the arrays for the corresponding row, column, and sub-box by performing a logical OR operation with the mask of 'x'.
# We continue this process. This strategy avoids the need to pre-prepare arrays for rows, columns,
# and sub-boxes before iterating through the board. Instead, we construct these arrays in-place during the iteration.

def isValidSudoku(board):
    rows = [0] * 9
    columns = [0] * 9
    squares = [0] * 9

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = int(board[i][j])
                mask = 1 << num
                if rows[i] & mask or columns[j] & mask or squares[(i // 3) * 3 + j // 3] & mask:
                    return False

                rows[i] |= mask
                columns[j] |= mask
                squares[(i // 3) * 3 + j // 3] |= mask

    return True


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print(isValidSudoku(board))

    board = [
        ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
    ]
    print(isValidSudoku(board))



