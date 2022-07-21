from typing import List
import math, time

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

def minEatingSpeed2(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    while l < r:
        mid = (l + r) // 2
        if h < sum(math.ceil(a / mid) for a in piles): l = mid + 1
        else: r = mid
    return l






def test_func():
  st = time.time_ns()
  assert minEatingSpeed([3,6,7,11], 8) == 4
  assert minEatingSpeed([30,11,23,4,20], 5) == 30
  assert minEatingSpeed([30,11,23,4,20], 6) == 23
  et = time.time_ns()
  print('execution time of first method: ', et - st)

  assert minEatingSpeed2([3,6,7,11], 8) == 4
  assert minEatingSpeed2([30,11,23,4,20], 5) == 30
  assert minEatingSpeed2([30,11,23,4,20], 6) == 23
  e2t = time.time_ns()
  print('execution time of second method: ', e2t - et)


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")