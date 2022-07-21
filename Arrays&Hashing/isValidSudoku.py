def isValidSudoku(board):
  rows = len(board)
  col = len(board[0])
  row_set = [set() for i in range(rows)]
  col_set = [set() for i in range(col)]

  square_set = [set() for i in range(rows//3 * col//3)]
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == '.': continue
      square_col = j // 3
      square_row = i // 3
      square_num = square_row * col // 3 + square_col

      if board[i][j] in col_set[j] or board[i][j] in row_set[i] or board[i][j] in square_set[square_num]:
        return False
      else:
        col_set[j].add(board[i][j])
        row_set[i].add(board[i][j])
        square_set[square_num].add(board[i][j])
  return True


testBoard = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(testBoard))