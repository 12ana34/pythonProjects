def find_next_empty(puzzle): #finds -1 values in the matrix which simbolize empty spaces
  for r in range(9):
    for c in range(9):
      if puzzle[r][c] == -1:
        return r,c
  return None, None

def is_valid(puzzle, guess, row, col): #checks if the value that we want to enter is already entered either in the row, column or smaller matrix
  row_vals = puzzle[row]#checks the row
  if guess in row_vals:
    return False
  
  col_vals = [puzzle[i][col] for i in range(9)]#checks the column
  if guess in col_vals:
    return False

  row_start = (row // 3) * 3
  col_start = (col // 3) * 3

  for r in range(row_start, row_start+3):#checks the small matrix
    for c in range(col_start, col_start+3):
      if puzzle[r][c] == guess:
        return False

  return True

def solve_sudoku(puzzle):
  row, col = find_next_empty(puzzle)#gets indexes of empty spaces
  if row is None:#if row is none true is returned and that means there are no more empty spaces left in the matrix which means we won
    return True
  
  for guess in range(1,10): #pasess the guess
    if is_valid(puzzle, guess, row, col):#tries to fill the empty space with the guess
      puzzle[row][col] = guess#fills the empty space with a value
      if solve_sudoku(puzzle): #calls the function recursevly
        return True

    puzzle[row][col] = -1 #if the guess for this position is not valid reset it and move on 

  return False

example_board = [
  [3,9,-1,    -1,5,-1,     -1,-1,-1],
  [-1,-1,-1,   2,-1,-1,    -1,-1,5],
  [-1,-1,-1,   7,1,9,      -1,8,-1],

  [-1,5,-1,    -1,6,8,     -1,-1,-1],
  [2,-1,6,     -1,-1,3,    -1,-1,-1],
  [-1,-1,-1,   -1,-1,-1,   -1,-1,4],

  [5,-1,-1,   -1,-1,-1,   -1,-1,-1],
  [6,7,-1,     1,-1,5,    -1,4,-1],
  [1,-1,9,     -1,-1,-1,    2,-1,-1]
]

print(solve_sudoku(example_board))
