from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
  row, col = len(matrix), len(matrix[0])

  def searchRows(matrix: List[List[int]], target: int) -> List[int]:
    lo, hi = 0, row - 1
    while lo <= hi:
      mid = (lo + hi) // 2
      if matrix[mid][0] <= target and matrix[mid][-1] >= target:
        res_row = matrix[mid]
        res_lo, res_hi = 0, col - 1
        while res_lo <= res_hi:
          res_mid = (res_lo + res_hi) // 2
          if res_row[res_mid] < target:
            res_lo = res_mid + 1
          elif res_row[res_mid] > target:
            res_hi = res_mid - 1
          else:
            return True
        return False
      elif mid == row - 1 and matrix[mid][-1] < target:
        return False
      elif mid == 0 and matrix[mid][0] > target:
        return False
      elif matrix[mid][0] > target:
        hi = mid - 1
      elif matrix[mid][0] < target and matrix[mid][-1] < target:
        lo = mid + 1
  
  return searchRows(matrix, target)

def searchMatrix2(matrix: List[List[int]], target: int) -> bool:
  flattened = []
  for row in matrix:
    flattened += row

  lo, hi = 0, len(flattened) - 1    
  while lo <= hi:
    mid = (lo + hi) // 2
    if flattened[mid] < target:
      lo = mid + 1
    elif flattened[mid] > target:
      hi = mid - 1
    else:
      return True
  return False




def test_func():
  assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
  assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
  assert searchMatrix([[1]], 0) == False
  assert searchMatrix2([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
  assert searchMatrix2([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
  assert searchMatrix2([[1]], 0) == False

if __name__ == "__main__":
  test_func()
  print("Everything Passed!")