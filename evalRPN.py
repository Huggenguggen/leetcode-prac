from typing import List

def evalRPN(tokens: List[str]) -> int:
  stack = []
  for char in tokens:
    if char == "+":
      stack.append(stack.pop() + stack.pop())
    elif char == "-":
      a, b = stack.pop(), stack.pop()
      stack.append(b - a)
    elif char == "*":
      stack.append(stack.pop() * stack.pop())
    elif char == "/":
      a, b = stack.pop(), stack.pop()
      stack.append(int(b / a))
    else:
      stack.append(int(char))
  return stack[0]

def test_func():
  assert evalRPN(["2","1","+","3","*"]) == 9
  assert evalRPN(["4","13","5","/","+"]) == 6
  assert evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22


if __name__ == "__main__":
  test_func()
  print("Everything passed")
