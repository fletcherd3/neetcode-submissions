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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        return p.val == q.val \
            and self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)