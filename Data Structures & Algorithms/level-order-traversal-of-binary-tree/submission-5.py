"""
# time to design the algorithm: 9  mins
# time to code:                 12 mins

# what solutions did I consider/miss?
-

# analysis:
time: O(n)
space: O(n)
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



"""
init listwith [root] ans
init deque with root d

while deque not empty
    save deque state ds
    init empty list level
    for item in ds (popleft)
        continue if null
        add items children to level
        add items children to d
    add level to ans
return ans
"""

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        to_process = deque([root])

        while to_process:
            process_count = len(to_process)
            level = []
            
            for _ in range(process_count):
                node = to_process.popleft()
                level.append(node.val)

                if node.left:
                    to_process.append(node.left)
                if node.right:
                    to_process.append(node.right)
            
            ans.append(level)
        
        return ans

                


        