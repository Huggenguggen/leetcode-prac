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

print(lengthOfLongestSubstring(test_case_1))

assert lengthOfLongestSubstring(test_case_1) == 3, "test case: 'abcabcbb' Should be 3"