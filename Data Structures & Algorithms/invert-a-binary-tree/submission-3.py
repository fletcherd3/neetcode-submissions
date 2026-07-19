"""
# time to design the algorithm: ?? mins
# time to code:                 ?? mins

# what solutions did I consider/miss?
-

# analysis:
time: O(n)
space: O(h)
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root: 
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root