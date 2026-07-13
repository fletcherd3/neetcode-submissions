"""
# time to solve: ? mins

# notes
- failed a 20m timer with no solution. watched video, then tried my own solution. took 16m

# thinking
- 

# add to cheatsheet
## 

```
```

# complexity
time:  O(log(n))
space: O(1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        current_min = nums[l]
        while l <= r:
            m = (l + r) // 2

            # break is left
            if nums[l] > nums[m]:
                current_min = min(nums[m], current_min)
                r = m - 1
            elif nums[m] > nums[r]: # break is right
                current_min = min(nums[r], current_min)
                l = m + 1
            else: # ordered, return
                current_min = min(nums[l], current_min)
                return current_min
