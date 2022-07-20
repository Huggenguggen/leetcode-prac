from typing import List
import math

def minEatingSpeed(piles: List[int], h: int) -> int:
  lo, hi = 1, max(piles)
  min_rate = hi

  while lo <= hi:
    k = (lo + hi) // 2
    hours = 0
    for p in piles:
      hours += math.ceil(p / k)
    
    if hours <= h:
      min_rate = min(min_rate, k)
      hi = k - 1
    else:
      lo = k + 1
  
  return min_rate








def test_func():
  assert minEatingSpeed([3,6,7,11], 8) == 4
  assert minEatingSpeed([30,11,23,4,20], 5) == 30
  assert minEatingSpeed([30,11,23,4,20], 6) == 23

if __name__ == "__main__":
  test_func()
  print("Everything Passed!")