"""
# time to code:  ? mins
# time to solve: ? mins

# notes
- 

# thinking
- 

# add to cheatsheet
## 

```
```

# complexity
time:  O(n * m + g) = O(nm)
space: O(g + nm) = O(nm)
where m is max string and g is groups
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(lambda: [])

        for s in strs:
            key = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                key[i] += 1
            key = tuple(key)
            
            anagrams[key] += [s]
        
        return list(anagrams.values())
        