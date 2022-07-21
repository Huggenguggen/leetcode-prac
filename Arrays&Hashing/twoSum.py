def twoSum(nums, target):
  res = [0,0]
  map = {}
  for num in range(len(nums)):
    diff = target - nums[num]
    if diff in map:
      res[0] = num
      res[1] = map[diff]
      return res
    map[nums[num]] = num
  return res

print(twoSum([3,2,4], 6))