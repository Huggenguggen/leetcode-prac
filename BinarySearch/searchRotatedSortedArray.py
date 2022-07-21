from typing import List

def search(nums: List[int], target: int) -> int:
  lo, hi = 0, len(nums) - 1

  while lo <= hi:
    mid = (lo + hi) // 2

    if nums[mid] == target:
      return mid
    
    if nums[lo] <= nums[mid]:
      if target > nums[mid] or target < nums[lo]:
        lo = mid + 1
      else:
        hi = mid - 1
    else:
      if target < nums[mid] or target > nums[hi]:
        hi = mid - 1
      else:
        lo = mid + 1
  return -1


def test_func():
  assert search([4,5,6,7,0,1,2], 0) == 4
  assert search([4,5,6,7,1,2], 3) == -1
  assert search([1], 0) == -1


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")