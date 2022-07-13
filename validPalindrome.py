from numpy import character


def isPalindrome(s: str) -> bool:
  lst = []
  for char in s:
    if char.isalpha():
      lst.append(char.lower())
    elif char.isnumeric():
      lst.append(char)
  
  temp = lst[::-1]
  return temp == lst

def isPalindrome2(s: str) -> bool:
  l = 0
  r = len(s) - 1
  while l < r:
    while l < r and not alphaNum(s[l]):
      l += 1
    while r > 1 and not alphaNum(s[r]):
      r -= 1

    if s[l].lower() != s[r].lower():
      return False
    
    l += 1
    r -= 1
  return True

def alphaNum(c: character) -> bool:
  return (ord('A') <= ord(c) <= ord('Z') or 
      ord('a') <= ord(c) <= ord('z') or 
      ord('0') <= ord(c) <= ord('9'))
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome(".,"))