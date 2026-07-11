"""
# time to code:  ? mins
# time to solve: ? mins

# notes
- 

# thinking
- 

# add to cheatsheet
## python regex would be nice to know and time/space complexity

```
```

# complexity
time:  O(n/2) = O(n)
space: O(n)
"""

import re


def isAlphaNum(c):
    return bool(re.fullmatch(r'[a-zA-Z0-9]', c))


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.lower()
        
        while l < r:
            while not isAlphaNum(s[l]) and l < len(s)-1:
                l += 1
            
            while not isAlphaNum(s[r]) and r > 0:
                r -= 1

            if not s[l] == s[r] and l < r:
                return False
            
            l += 1
            r -= 1
        
        return True

        