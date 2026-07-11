"""
# time to code: 9 mins
# time to solve: 16 mins (brute)
# time to solve: ? mins

# thinking
- first thought of summing int rep of chars to a number. thought good idea but dont know how to do in python
- could sort each and compare. slow though ..

# notes
- 

# add to cheatsheet
## hash map with default value

```
from collections import defaultdict

d = defaultdict(lambda: [])
```

# complexity
time:  O(n * klog(k) + n)
space: O(n)
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init anagrams (a) hash map (sort → [s])
        a = defaultdict(lambda: [])

        # iterate over strs (s)
        for s in strs:
            # fe(s): sort str and a[sort(s)] += s
            key = "".join(sorted(s))
            a[key] += [s]

        # return (join a values)
        return [v for v in a.values()]
        