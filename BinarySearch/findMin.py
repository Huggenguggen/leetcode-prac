from typing import List

def findMin(nums: List[int]) -> int:
  lo, hi = 0, len(nums) - 1
  res = nums[0]
  
  while lo <= hi:
    if nums[lo] < nums[hi]:
      res = min(res, nums[lo])
      break
    mid = (lo + hi) // 2
    res = min(res, nums[mid])
    if nums[mid] >= nums[lo]:
      lo = mid + 1
    else:
      hi = mid - 1
  return res


def test_func():
  assert findMin([3,4,5,1,2]) == 1
  assert findMin([1]) == 1
  assert findMin([4,5,6,7,0,1,2]) == 0
  assert findMin([11,13,15,17]) == 11


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")