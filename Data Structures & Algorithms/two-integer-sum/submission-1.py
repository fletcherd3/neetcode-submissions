"""
# time to solve: 7 mins

# notes
-

# thinking
-

# add to cheatsheet
##
```
```

# complexity
time: O(n)
space: O(n)
"""


from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_to_i = defaultdict(lambda: [])

        for i, n in enumerate(nums):
            n_to_i[n].append(i)
        
        for a_i, a in enumerate(nums):
            # a + b = target
            b = target - a
            if b in n_to_i:
                for b_i in n_to_i[b]:
                    if b_i != a_i:
                        return [a_i, b_i]
            