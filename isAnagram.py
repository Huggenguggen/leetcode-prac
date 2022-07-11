def isAnagram(s, t):
  char_array = [0] * 26
  for char in t:
    char_array[ord(char) - 97] += 1
  for char in s:
    char_array[ord(char) - 97] -= 1
  return all(map(lambda x: x == 0, char_array))


print(isAnagram("anagram", "nagaram"))