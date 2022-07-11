import collections

def groupAnagrams(strs):
  new_strs = []
  groups = {}
  for word in strs:
    symbols = [0] * 26
    for char in word:
      symbols[ord(char) - 97] += 1
    anagram = str(symbols)

    if anagram not in groups:
      groups[anagram] = []
    groups[anagram] += [word]
  
  return groups.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


def groupAnagrams2(strs):
    #for each item in the list, first iterate through the letters (make a temp hashmap of the         #letters), then compare the hashmap to existing hashmaps (which are stored in a list)
    
    res = collections.defaultdict(list)
    
    for item in strs:
      count =[0]*26
      
      for c in item:
        count[ord(c) - ord('a')] += 1
      
      
      res[tuple(count)].append(item)
      
      
    return res.values()