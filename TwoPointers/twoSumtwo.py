from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
  if len(numbers) == 2:
    return [1, 2]

  l, r = 0, len(numbers) - 1
  while l < r:
    if numbers[l] + numbers[r] > target:
      r -= 1
    elif numbers[l] + numbers[r] < target:
      l += 1
    elif numbers[l] + numbers[r] == target:
      return [l + 1, r + 1]
    

    #[-4, 2, 5, 6, 7, 10] target = 7
    # will remove 10 so now it's [-4, 2, 5, 6, 7]
    # since -4 + 7 is less than 7, move l up
    # 2 + 7 is more than 7, how to determine if i move l up or r down

print(twoSum([-4, 2, 5, 6, 7, 10], 7))