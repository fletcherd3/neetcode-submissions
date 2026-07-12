"""
# time to code/solve:  15 mins

# notes
- 

# thinking
- 

# add to cheatsheet
## namedtuples (not used here but could be useful?)

```
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'], defaults=[0]) # !! defaults applied from rhs (z=0)
p1 = Point(2, 1)  # x=2, y=1, z=0
hsh_map[p1] = 123 # immutable so can be a key (if props are also immutable)
```
## switch statement

```
my_name = 'Fletcher'

match my_name:
    case 'Fletcher' | 'fletcher':
        print('hi')
    case _:
        print('default')

```


# complexity
time:  O(n)
space: O(n)
"""

def isClosingBrace(brace):
    return brace in [')', ']', '}']

def matchesEarlierBrace(earlierBrace, brace):
    match earlierBrace:
        case '(':
            return brace == ')'
        case '[':
            return brace == ']'
        case '{':
            return brace == '}'
        case _:
            return False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]

        for c in s[1:]:
            if isClosingBrace(c):
                if len(stack) == 0 or not matchesEarlierBrace(stack.pop(), c):
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
        