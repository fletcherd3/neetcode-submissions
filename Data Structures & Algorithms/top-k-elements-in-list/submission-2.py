"""
# time to code:  14 mins
# time to solve: ? mins

# notes
- ez

# thinking
- 

# add to cheatsheet
## few things here 1) get hash map (key, value) pairs; 2) sort by lambda; 3) reverse sort
```
# sort map (k → v) by desc v
sorted(counts.items(), key=lambda m: m[1], reverse=True)
```

# complexity
time:  O(n + nlog(n)) = O(nlog(n))
space: O(n)
"""

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init map (n → count(n))
        counts = defaultdict(lambda: 0)

        #fe(nums): inc. count
        for n in nums:
            counts[n] += 1

        # sort map (k → v) by desc v
        ranked_desc = sorted(counts.items(), key=lambda m: m[1], reverse=True)
        return [k for k, _ in ranked_desc[:k]]
        