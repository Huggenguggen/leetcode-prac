def isValidSudoku(board):
  def validRow(row):
    for item in row:
      if all(map(lambda x: x != item or x == ".", row)):
        return True
    return False

  if any(map(lambda x: not validRow(x), board)):
    return False
  
  def validCol(row, restOfBoard):
    for i in range(len(row)):
      num = row[i]
      for r in restOfBoard:
        if r[i] == num and r[i] != ".":
          return False
    return True
  
  if not validCol(board[0], board[1:]):
    return False

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