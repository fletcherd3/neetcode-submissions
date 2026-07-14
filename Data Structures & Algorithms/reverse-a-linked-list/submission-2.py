"""
# time to solve: ? mins way too long ...

# notes
- proven to myself that i need pen and paper. i just died with this simple problem untill i got my pen and paper out.

# thinking
- 

# add to cheatsheet
## 

```
```

# complexity
time:  O(n)
space: O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head;

        next = head.next
        head.next = None
        prev = head
        head = next
        while next is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


        