"""
# time to design the algorithm: ?? mins
# time to code:                 ?? mins

# what solutions did I consider/miss?
-

# analysis:
time: O(h)
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

    def findMinNode(self, root):
        if root.left == None:
            return root
        return self.findMinNode(root.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None: return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                min_node = self.findMinNode(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
            else:
                return root.left or root.right
        
        return root
        