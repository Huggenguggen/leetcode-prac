from typing import List

def search(nums: List[int], target: int) -> int:
  pass


def test_func():
  assert search([4,5,6,7,0,1,2], 0) == 4
  assert search([4,5,6,7,1,2,3], 3) == -1
  assert search([1], 0) == -1


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")