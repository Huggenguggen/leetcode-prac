def minWindow(s: str, t: str) -> str:
  charDict = {}
  for char in t:
    charDict[char] = charDict.get(char, 0) + 1
  
  minLength = len(s) + 1
  start, head, matches = 0, 0, 0

  for end in range(len(s)):
    char = s[end]
    if char in charDict:
      charDict[char] -= 1
      if charDict[char] == 0:
        matches += 1
    
    while matches == len(charDict):
      window_size = end - start + 1
      if minLength > window_size:
        minLength = window_size
        head = start
      char_going_out = s[start]
      start += 1

      if char_going_out in charDict:
        if charDict[char_going_out] == 0:
          matches -= 1
        charDict[char_going_out] += 1
  
  if minLength > len(s):
    return ""
  return s[head: head + minLength]


def test_func():
  assert minWindow("ADOBECODEBANC", "ABC") == 'BANC', "test case: 'ADOBECODEBANC' 'ABC' should be 'BANC'"
  assert minWindow("a", "a") == 'a', "test case: 'a' 'a' should be 'a'"
  assert minWindow("a", "aa") == '', "test case: 'a' 'aa' should be ''"

if __name__ == "__main__":
  test_func()
  print("Everything passed")