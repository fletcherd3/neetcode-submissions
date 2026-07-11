"""
# time to code:  ? mins
# time to solve: ? mins

# notes
- had to learn bucket sort. wtf most cursed shit
- cursed fucking cursed, had two major fuck ups
1) freq = [[]] * len(nums)
this copies the same [] object, if you add to freq[i], you add to ALL of them :(
2) for i in range(len(freq)-1, 0):
wrong for two reasons: 1) doesnt hit index 0; 2) without step=-1 its increments ...
should be for i in range(len(freq)-1, -1, -1): # start at index len-1 → 0

# thinking
- 

# add to cheatsheet
## `[[]] * n` copies [] object
meaning append to one, append to all
instead: `[[] for _ in range(n)]`

```
```

# complexity
time:  O(n)
space: O(n)
"""

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda: 0)
        freq = [[] for _ in range(len(nums))]

        for n in nums:
            count[n] += 1    

        for num, cnt in count.items():
            freq[cnt-1].append(num)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res += [num]
                if len(res) >= k:
                    return res


        