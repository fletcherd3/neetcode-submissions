"""
# time to solve: 19 mins 17s (too close wow)

# notes
- 2nd time back on this problem, solved it but had a few bugs along the way. slower than i'd like. will try again

# thinking
-

# add to cheatsheet
##
```
```

# complexity
time: O(n^2)
space: O(n)
"""

from collections import defaultdict

 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        n_to_i = defaultdict(list)

        for i, n in enumerate(nums):
            n_to_i[n].append(i)

        for a_i, a in enumerate(nums):
            for b_i in range(a_i+1, len(nums)):
                b = nums[b_i]
                # a + b + c = 0 ==> c = -a - b
                c = -a - b
                if c in n_to_i:
                    for c_i in n_to_i[c]:
                        if c_i not in [a_i, b_i]:
                            solution = tuple(sorted([a, b, c]))
                            solutions.add(solution)
        
        return [list(t) for t in solutions]
                    

        