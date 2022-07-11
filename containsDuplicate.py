def containsDuplicate(nums):
  value = {}

  for num in nums:
    if num not in value:
      value[num] = 0
    value[num] += 1
    if value[num] > 1:
      return True
  return False