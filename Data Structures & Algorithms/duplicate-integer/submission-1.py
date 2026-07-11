class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = set()
        
        for n in nums:
            duplicate = n in seen_nums

            if duplicate:
                return True

            seen_nums.add(n)
        
        return False
        