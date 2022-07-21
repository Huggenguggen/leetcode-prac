from typing import List

def search(nums: List[int], target: int) -> int:
  lo, hi = 0, len(nums)
  while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      lo = mid + 1 
    else:
      hi = mid

  return -1

def search2(nums: List[int], target: int) -> int:
  lo, hi = 0, len(nums) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      lo = mid + 1 
    else:
      hi = mid - 1

  return -1





def test_func():
  assert search([-1,0,3,5,9,12], 9) == 4
  assert search([-1,0,3,5,9,12], 2) == -1
  assert search2([-1,0,3,5,9,12], 9) == 4
  assert search2([-1,0,3,5,9,12], 2) == -1

if __name__ == "__main__":
  test_func()
  print("Everything passed!")