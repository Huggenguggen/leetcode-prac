def longestConsecutive(nums):
  s = set()
  res = 0

  for num in nums:
    s.add(num)
  
  for i in range(len(nums)):
    if nums[i] - 1 not in s:
      j = nums[i]
      while j in s:
        j += 1
      
      res = max(res, j - nums[i])
  return res