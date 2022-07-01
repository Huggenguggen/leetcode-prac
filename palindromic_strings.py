from inspect import _void


class Solution:
    def countSubstrings0(self, s: str) -> int:
      left = 0
      count = 0
      length = len(s)
      while left < length:
        right = left + 1
        while right < length + 1:
          if Solution.is_palindrome(self, s[left:right]):
            count += 1
          right += 1
        left += 1
      return count
    
    def countSubstrings1(self, s: str) -> int:
      self.res = 0
      for i in range(len(s)):
        self.dfs(s, i, i)
        self.dfs(s, i, i + 1)
      return self.res

    def dfs(self, s: str, i: int, j: int):
      while i >= 0 and j < len(s) and s[i] == s[j]:
        self.res += 1
        i -= 1
        j += 1

    def is_palindrome(self, s: str) -> bool:
      length = len(s)
      if length == 1:
        return True
      else:
        left = 0
        right = length - 1
        while left < right:
          if s[left] != s[right]:
            return False
          else:
            left += 1
            right -= 1
        return True
    
print(Solution.is_palindrome("self", "abba"))
print(Solution.countSubstrings1("self", "aaa"))