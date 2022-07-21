from typing import List

def largestRectangleArea(heights: List[int]) -> int:
  stack = []
  maxArea = 0

  for i, h in enumerate(heights):
    start = i
    while stack and stack[-1][1] > h:
      index, height = stack.pop()
      maxArea = max(maxArea, height * (i - index))
      start = index
    stack.append((start, h))

  for i, h in stack:
    maxArea = max(maxArea, h * (len(heights) - i))
  return maxArea



def test_func():
  assert(largestRectangleArea([2,1,5,6,2,3])) == 10
  assert(largestRectangleArea([2,4])) == 4
  assert(largestRectangleArea([10])) == 10
  assert(largestRectangleArea([2,0,2])) == 2


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")