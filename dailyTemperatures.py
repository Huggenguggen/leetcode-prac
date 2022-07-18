from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
  stack = []
  answer = [0] * len(temperatures)
  
  for i, temp in enumerate(temperatures):
    while stack and temp > stack[-1][0]:
      stackT, stackInd = stack.pop()
      answer[stackInd] = (i - stackInd)
    stack.append([temp, i])
  
  return answer



def test_func():
  assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
  assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
  assert dailyTemperatures([30,60,90]) == [1,1,0]


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")