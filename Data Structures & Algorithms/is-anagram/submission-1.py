"""
# time to solve: 4 mins

# notes
- easy after doing a medium anagram problem

# thinking
-

# add to cheatsheet
##
```
```

# complexity
time: O(l) where l is the length of the longest input
space: O(1)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_fingerprint = [0 for _ in range(26)]
        t_fingerprint = [0 for _ in range(26)]
        
        for c in s:
            i = ord(c) - ord('a')
            s_fingerprint[i] += 1
        
        for c in t:
            i = ord(c) - ord('a')
            t_fingerprint[i] += 1
        
        return s_fingerprint == t_fingerprint