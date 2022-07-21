def checkInclusion(s1: str, s2: str) -> bool:
  check = {}
  for char in s1:
    check[char] = check.get(char, 0) + 1
  
  s1_len = len(s1)
  l = 0
  while l < len(s2):
    while l < len(s2) and s2[l] not in s1:
      l += 1
    if l <= len(s2) - len(s1):
      temp = {}
      r = l + s1_len
      for char in s2[l:r]:
        temp[char] = temp.get(char, 0) + 1
      if temp == check:
        return True
      else:
        l += 1

    else: 
      return False
  return False

def checkInclusion2(s1: str, s2: str) -> bool:
  if len(s1) > len(s2): return False
  s1_count = [0] * 26
  s2_count = [0] * 26
  
  for i in range(len(s1)):
    s1_count[ord(s1[i]) - ord('a')] += 1
    s2_count[ord(s2[i]) - ord('a')] += 1
  
  matches = 0
  for i in range(26):
    if s2_count[i] == s2_count[i]:
      matches += 1
  
  l = 0
  for r in range(len(s1), len(s2)):
    if matches == 26:
      return True
    
    index = ord(s2[r]) - ord('a')
    s2_count[index] += 1
    if s1_count[index] == s2_count[index]:
      matches += 1
    elif s1_count[index] + 1 == s2_count[index]:
      matches -= 1
    
    index = ord(s2[l]) - ord('a')
    s2_count[index] -= 1
    if s1_count[index] == s2_count[index]:
      matches += 1
    elif s1_count[index] + 1 == s2_count[index]:
      matches -= 1
    l += 1
  return matches == 26

def test_func():
  assert checkInclusion("ab", "eidbaooo") == True, "test case: 'ab' 'eidbaooo should be true"
  assert checkInclusion("ab", "eidboaoo") == False, "test case: 'ab' 'eidboaoo should be false"
  assert checkInclusion("a", "a") == True, "test case: 'a' 'a' should be true"
  assert checkInclusion("adc", "dcda") == True, "test case: 'adc' 'dcda' should be true"

if __name__ == "__main__":
  test_func()
  print("Everything passed")