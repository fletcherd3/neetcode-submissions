"""
# time to design the algorithm: ?? mins
# time to code:                 ?? mins

# what solutions did I consider/miss?
-

# analysis:
time: worst case: O(n^2) (linked list). best case (balanced tree) : O(nlogn)
space: O(n)
optimal: Y / N 🤷‍♂️
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        l_levels, r_levels = self.levelOrder(root.left), self.levelOrder(root.right)

        levels = [[root.val]]
        i = 0
        while i < min(len(l_levels), len(r_levels)):
            levels.append(l_levels[i] + r_levels[i])
            i += 1
        levels += l_levels[i:] + r_levels[i:]
            
        return levels