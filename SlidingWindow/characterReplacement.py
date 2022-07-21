def characterReplacement(s: str, k: int) -> int:
  start = 0
  longest = 0
  max_freq = 0

  freq = {}

  for end in range(len(s)):
    current_char = s[end]

    if current_char not in freq:
      freq[current_char] = 0
    freq[current_char] += 1

    max_freq = max(max_freq, freq[current_char])

    if (end - start + 1 - max_freq) > k:
      char_to_decre = s[start]
      freq[char_to_decre] -= 1
      start += 1
    
    longest = max(longest, end - start + 1)
  return longest

def test_func():
  assert characterReplacement("ABAB", 2) == 4, "test case: 'ABAB', 2 Should be 4"
  assert characterReplacement("AABABBA", 1) == 4, "test case: 'AABABBA', 1 Should be 4"
  assert characterReplacement("ABAB", 0) == 1, "test case: 'ABAB', 0 Should be 1"

if __name__ == "__main__":
  test_func()
  print("Everything passed")