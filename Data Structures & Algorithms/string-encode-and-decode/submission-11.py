"""
# time to solve: too long ..

# notes
-

# thinking
-

# add to cheatsheet
##
```
```

# complexity
time: O(n)
space: O(n)
"""


class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = [str(len(s)) for s in strs]
        p = ",".join(lengths) + "#" + "".join(strs)
        print(p)
        return p


    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []
        s_split = s.split("#")
        lengths = [int(n) for n in s_split[0].split(",")]
        msg = "#".join(s_split[1:])

        words = []
        last_i = 0
        for l in lengths:
            word = msg[last_i: last_i+l]
            words.append(word)
            last_i += l
        return words
