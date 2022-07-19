from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
  stack = []
  pair = [[p, s] for p, s in zip(position, speed)]
  for p, s in sorted(pair)[::-1]:
    stack.append((target - p) / s)
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
      stack.pop()
  
  return len(stack)


def test_func():
  assert carFleet(10, [3,5,7], [3,2,1]) == 1
  assert carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
  assert carFleet(10, [3], [3]) == 1
  assert carFleet(100, [0,2,4], [4,2,1]) == 1


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")