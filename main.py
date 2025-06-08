#Solving Sudoku using back tracking
def is_Valid(grid, row, col, num):
    
    #checking num is already present in row
    for i in range(9):
        if grid[row][i] == num:
            return False
    
    #checking num is already present in row
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    #checking num is already present in 3x3 box
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row+x][corner_col+y]==num:
                return False
        
    return True


def solveSudoku(grid, row, col):
    
    #if we reached end point
    if col==9:
        if row==8:
            return True
        row+=1
        col=0
    
    if grid[row][col]>0:
        return solveSudoku(grid,row,col+1)
    
    for n in range(1,10):
        if is_Valid(grid,row,col,n):
            
            grid[row][col] = n
            
            if solveSudoku(grid,row,col+1):
                return True
        
        grid[row][col] = 0
        
    return False



#grid for sudoku (0 is considered as no value)
grid = [
        [4, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 9, 8],
        [3, 0, 0, 0, 8, 2, 4, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 8, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 7, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
       ]


if solveSudoku(grid,0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("Didn't found any possible soultion for given Sudoku Puzzle")


