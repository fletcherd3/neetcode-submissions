"""
# time to design the algorithm: ?? mins
# time to code:                 ?? mins

# what solutions did I consider/miss?
-

# analysis:
time: O(h)
space: O(1)
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        