from typing import List

def generateParenthesis(n: int) -> List[str]:
  stack = []
  res = []

  def helper(open, close):
    if open == close == n:
      res.append("".join(stack))
    
    if open < n:
      stack.append("(")
      helper(open + 1, close)
      stack.pop()
    
    if close < open:
      stack.append(")")
      helper(open, close + 1)
      stack.pop()
    
  helper(0, 0)
  return res


def test_func():
  assert generateParenthesis(1) == ["()"]
  assert generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]


if __name__ == "__main__":
  test_func()
  print("Everything Passed!")