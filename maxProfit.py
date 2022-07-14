from typing import List

def maxProfit(prices: List[int]) -> int:
  res, l = 0, 0

  for r in range(1, len(prices)):
    if prices[r] < prices[l]:
      l = r
    
    res = max(res, prices[r] - prices[l])
  return res
