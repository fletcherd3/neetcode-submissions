"""
# time to solve: 17 mins

# notes
- watched video on sliding window before hand which helped. but did solve it in my own way that made more sense to me.

# thinking
- 

# add to cheatsheet
## 

```
```

# complexity
time:  O(n)
space: O(min(n, k))
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() # sliding window

        # move R from start to finish
        for R in range(0, len(nums)):
            # is new addition in window already?
            if nums[R] in window:
                return True
            # if not
            # add new addition
            window.add(nums[R])

            L = max(0, R - k) # at start of alg. L is 0 till window grows to k
            # once window gets to len k, start removing L most number
            if abs(L - R) == k:
                window.remove(nums[L])

        return False
            
        