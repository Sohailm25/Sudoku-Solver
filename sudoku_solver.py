#code
#import numpy as np

# READ IN INPUTTED NUMBERS AS LIST
sudoku_input = [3, 0, 6, 5, 0, 8, 4, 0, 0, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 8, 7, 0, 0, 0, 0, 3, 1, 0, 0, 3, 0, 1, 0, 0, 8, 0, 9, 0, 0, 8, 6, 3, 0, 0, 5, 0, 5, 0, 0, 9, 0, 6, 0, 0, 1, 3, 0, 0, 0, 0, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 7, 4, 0, 0, 5, 2, 0, 6, 3, 0, 0]
sudoku_board_init = []

for X in sudoku_input:
    if (X != ' '):
        sudoku_board_init.append(int(X))

# CREATE A 2D MATRIX (SUDOKU BOARD)
start = 0
stop = 9
mat = []
while (stop <= 81):
    row = sudoku_board_init[start:stop]
    mat.append(row)
    start += 9
    stop += 9

# CREATE COPY SO WE DON'T CHANGE ORIGINAL SUDOKU BOARD
solution = mat.copy()

## FUNCTIONS TO CHECK VALIDITY OF SUDOKU ENTRY
def check_row(i, X, board):
    #print("Checking Row for: ", i, " at position ", X)
    # Checks to see if value already exists in the row
    if (board[X].count(i) != 0):
        #print("ROW ALREADY CONTAINS ", i)
        return False
    else:
        return True

def check_col(i, Y, board):
    #print("Checking Col for: ", i, " at position ", Y)
    for X in range(9):
        # Checks to see if value already exists in the column
        if (board[X][Y] == i):
            #print("COL ALREADY CONTAINS ", i)
            return False
    else:
        return True
        
def check_3x3(i, X, Y, board):
    #print("Checking 3x3 for: ", i, " at position ", X, " ", Y)
    mod_row = X%3
    mod_col = Y%3
    row_range = get_range(mod_row, X)
    col_range = get_range(mod_col, Y)
    
    #print("Col Range for ", X , Y, " is ", col_range)

    for Y in row_range:
        for X in col_range:
            if (board[Y][X] == i):
                #print("3x3 ALREADY CONTAINS ", i)
                return False
    return True

def get_range(mod, val):
    if (mod == 0):
        return [val, val+1, val+2]
    elif (mod == 1):
        return [val-1, val, val+1]
    elif (mod == 2):
        return [val-2, val-1, val]

## BACKTRACKING ALGORITHM
def solve_board(startX, startY, board):
    
    #print(solution)

    if (startY > 8):
        startY = 0
        startX += 1
    
    if (startX > 8):
        #print("Final Solution Found")
        #print(board)
        return True

    if (board[startX][startY] == 0):
        
        #print((startX,startY))
        i = 1
                
        while (i < 10):
                    
            if (check_row(i, startX, board) & check_col(i, startY, board) & check_3x3(i, startX, startY, board)):
                        
                board[startX][startY] = i
        
                if (solve_board(startX, startY + 1, board)):
                    return True
                else:
                    board[startX][startY] = 0

            i += 1
                    
                
        #if (i > 9):
        return False

    else:
        if (solve_board(startX, startY + 1, board)):
            return True

def print_board(board):
    for X in range(9):
        for Y in range(9):
            print(board[X][Y], "", end="", flush=True)
        print("\n")

## MAIN FUNCTION ## 
solved = solve_board(0,0,solution)
if (solved):
    #print(solution)
    print("The SOLVED SUDOKU BOARD IS: \n", print_board(solution))
else:
    print("No Solution Found")

















