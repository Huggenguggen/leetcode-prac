def isPalindrome(s: str) -> bool:
  lst = []
  for char in s:
    if char.isalpha():
      lst.append(char.lower())
    elif char.isnumeric():
      lst.append(char)
  
  temp = lst[::-1]
  return temp == lst
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome(".,"))