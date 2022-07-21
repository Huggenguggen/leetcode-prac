from typing import List
import collections

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
  if k >= len(nums): return [max(nums)]

  l, res = 0, []
  while l < len(nums) - (k - 1):
    temp = nums[l:l+k]
    res.append(max(temp))
    l += 1
  return res

def maxSlidingWindow2(nums: List[int], k: int) -> List[int]:
  output = []
  q = collections.deque()
  l = r = 0

  while r < len(nums):
    while q and nums[q[-1]] < nums[r]:
      q.pop()
    q.append(r)

    if l > q[0]:
      q.popleft()

    if (r + 1) >= k:
      output.append(nums[q[0]])
      l += 1
    r += 1

  return output


def test_func():
  assert maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
  assert maxSlidingWindow([1], 1) == [1]
  assert maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
  assert maxSlidingWindow2([1], 1) == [1]


if __name__ == "__main__":
  test_func()
  print("Everything passed")