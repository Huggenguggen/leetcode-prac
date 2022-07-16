def isValid(s: str) -> bool:
  if len(s) < 2 or len(s) % 2 != 0:
    return False
  stack = []
  for char in s:
    if char == '{' or char == '(' or char == '[':
      stack.append(char)
    else:
      if len(stack) == 0:
        return False
      else:
        top = stack[-1]
        if (char == '}' and top == '{') or (char == ')' and top == '(') or (char == ']' and top == '['):
          stack.pop()
        else:
          return False
  
  return len(stack) == 0


def test_func():
  assert isValid("()") == True
  assert isValid("()[]{}") == True
  assert isValid("(]") == False
  assert isValid("([])") == True


if __name__ == "__main__":
  test_func()
  print("Everything passed")