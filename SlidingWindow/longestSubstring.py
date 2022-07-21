def lengthOfLongestSubstring(s: str) -> int:
  charSet = set()
  l, res = 0, 0

  for r in range(len(s)):
    while s[r] in charSet:
      charSet.remove(s[l])
      l += 1
    charSet.add(s[r])
    res = max(res, r - l + 1)
  return res

test_case_1 = "abcabcbb"
test_case_2 = "bbbbb"
test_case_3 = "pwwkew"

def test_func():
  assert lengthOfLongestSubstring(test_case_1) == 3, "test case: 'abcabcbb' Should be 3"
  assert lengthOfLongestSubstring(test_case_2) == 1, "test case: 'bbbbb' Should be 1"
  assert lengthOfLongestSubstring(test_case_3) == 3, "test case: 'pwwkew' Should be 3"

if __name__ == "__main__":
  test_func()
  print("Everything passed")