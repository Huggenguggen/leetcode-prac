from typing import List

def trap(height: List[int]) -> int:
  
  maxL, maxR, l, r = 0, 0, 0, len(height) - 1
  res = 0
  while l < r:
    maxL = max(maxL, height[l])
    maxR = max(maxR, height[r])
    if height[l] < height[r]:
      curr_unit = min(maxL, maxR) - height[l]
      if curr_unit <= 0:
        res += 0
      else:
        res += curr_unit
      l += 1 
    else:
      curr_unit = min(maxL, maxR) - height[r]
      if curr_unit <= 0:
        res += 0
      else:
        res += curr_unit
      r -= 1
  return res

def trap2(height: List[int]) -> int:
   
  if not height: return 0
  l, r = 0, len(height) - 1
  LMax, RMax = height[l], height[r]
  res = 0
  while l < r:
    if LMax < RMax:
      l += 1
      LMax = max(LMax, height[l])
      res += LMax - height[l]
    else:
      r -= 1
      RMax = max(RMax, height[r])
      res += RMax - height[r]
  return res

test_height_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#answer should be 6

test_height_2 = [4, 2, 0, 3, 2, 5]
#answer should be 9
     #
#????#
#??#?#
##?###
##?###

test_height_3 = [4, 2, 3]
print(trap(test_height_1))