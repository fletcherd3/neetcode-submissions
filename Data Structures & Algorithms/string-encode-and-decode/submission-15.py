"""
# time to design the algorithm: 18 mins
# time to code:                 17 mins

# what solutions did I consider/miss?
- breifly thought about joining with special char, perhaps escaping

# analysis:
where: n is number of strings; l combined length of strings
time: O(n + l)
space: O(n + l)
optimal: Y
-

# what triggers did I find/miss?
-

# any mistakes I keep making? any bugs to add to the bug list?
- messed up .split() again, round wrong way. lost a couple minutes

# what could I have done differently?
- when i was writing pseudocode i fell into ensuring indexes were right. shouldn't go this deep. spent too much time on planning


# takeaways
- took 50m total for this question which i have seen before...
    - 18 + 17 + 16 (post mortem)
    - kinda stressy

# add to cheatsheet
-
```
```

# rubric self-rating
- problem solving: 5/5
- coding: 4/5
- verification: 4/5
- communication: 4/5
"""

class Solution:
    def encode(self, strs: List[str]) -> str:
        str_lens = [str(len(s)) for s in strs]
        
        preamble = ','.join(str_lens)
        payload = ''.join(strs)

        message = f'{preamble}#{payload}'

        return message


    def decode(self, s: str) -> List[str]:
        preamble, payload = s.split('#', 1)
        lengths = [int(l) for l in preamble.split(',') if l != '']

        strs = []
        l = 0
        for str_len in lengths:
            r = l + str_len
            strs.append(payload[l:r])
            l = r
        
        return strs



