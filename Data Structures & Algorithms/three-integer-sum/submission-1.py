"""
# failed a 20m and then went for much much longer
# time to code:  ? mins
# time to solve: ? mins

# notes
- two things i was missing
1) wan't de-duplicating answers
    ans.add(tuple([a, b, c])) → ans.add(tuple(sorted([a, b, c])))
2) wasn't casting back to expected ans type [[]] , prev was [()]

# thinking
- 

# add to cheatsheet
## 

```
```

# complexity
time:  O(n^2*)
space: O(n)
"""


from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n_to_i = defaultdict(lambda: [])


        for i, n in enumerate(nums):
            n_to_i[n].append(i)
        
        ans = set()
        for a_i, a in enumerate(nums): # O(n)
            for b_i in range(a_i+1, len(nums)): # O(n)
                
                b = nums[b_i]
                c = -a - b
                
                if c in n_to_i:
                    for c_i in n_to_i[c]: # O(k) where k is largest freq of a number
                        if c_i not in [a_i, b_i]:
                            ans.add(tuple(sorted([a, b, c])))
                    
        return [list(s) for s in ans]

