"""
# time to design the algorithm: ?? mins
# time to code:                 ?? mins
# total: 24 mins

# what solutions did I consider/miss?
-

# analysis:
time: O()
space: O()
optimal: Y / N
-

# what triggers did I find/miss?
-

# any mistakes I keep making? any bugs to add to the bug list?
-

# what could I have done differently?
-

# takeaways
-

# add to cheatsheet
-
```
```

# rubric self-rating
- problem solving: /5
- coding: /5
- verification: /5
- communication: /5
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        init l, r
        init min_num = inf
        


        while l <= r
            calc m (mid point)
            if m < min_num
                update min_num to m
            
            l_num, r_num, m_num = ...

            if break on left
                search left (r = m)
            elif break is right
                search right (l = m+1)
            else # ordered
                min_num = l_num
                break
            
        return min_num
        """

        l, r = 0, len(nums) - 1
        min_num = float('inf')


        while l <= r:
            m = (l + r) // 2
            l_num, m_num, r_num = nums[l], nums[m], nums[r]
            min_num = min(min_num, m_num)

            if l_num > m_num:
                r = m
            elif r_num < m_num:
                l = m + 1
            else:
                min_num = l_num
                break
        
        return min_num
        