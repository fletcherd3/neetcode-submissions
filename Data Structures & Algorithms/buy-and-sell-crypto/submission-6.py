"""
# time to design the algorithm: ?? mins
# time to code:                 ?? mins
# total: 24 mins

# what solutions did I consider/miss?
-

# analysis:
time: O()
space: O()
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
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        max_profit = 0

        for r in range(len(prices)):
            buy_price, sell_price = prices[l], prices[r]
            profit = sell_price - buy_price
            max_profit = max(profit, max_profit)

            if profit <= 0:
                l = r
        
        return max_profit
            

    