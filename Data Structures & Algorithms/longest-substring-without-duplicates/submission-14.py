"""
# time to design the algorithm: 13 mins
# time to code:                 17 mins

# what solutions did I consider/miss?
- i tried designing a deque solution but in the end i figured the time complexity was worse

# analysis:
time: O(n)
space: O(w)
optimal: Y
-

# what triggers did I find/miss?
-

# any mistakes I keep making? any bugs to add to the bug list?
-

# what could I have done differently?
- when designing algo 1 i didn't think about how checking if c in a deque is O(n). this made it slower than algo 2 and i should have realised earlier and skipped to designing algo 2
- i totally forgot about the interview checklist and abandoned it instantly

# takeaways
- i'm good at this problem now
- deque exists check is O(n)

# add to cheatsheet
-
```
```

# rubric self-rating
- problem solving: 4/5
- coding: 5/5
- verification: 5/5
- communication: 0/5 didn't speak
"""

"""
algo 1
time: O(n * w) where n is string size and w is largest substring of unique chars
space: O(w)
init empty deque (window)
init counter for max window size (max_size)

for each index in s (r)
    check if char at r is in window
    if yes
        while char is in window
            pop left of window
    
    add it to window
    update max_size if window length is larger
return max_size

algo 2
time: O(n) where n is string size and w is largest substring of unique chars
space: O(w)
init empty set (window)
init counter for max window size (max_size)
init pointer at 0 (l)

for each index in s (r)
    check if char at r is in window
    if yes
        while char is in window
            rm char at l from window
            l += 1
    
    add it to window
    update max_size if window length is larger
return max_size
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = max_size = 0

        for c in s:
            while c in window:
                window.remove(s[l])
                l += 1
            window.add(c)
            max_size = max(max_size, len(window))
        return max_size

        