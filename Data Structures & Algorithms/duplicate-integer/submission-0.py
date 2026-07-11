class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = []
        
        for n in nums:
            duplicate = n in seen_nums

            if duplicate == True:
                return True

            seen_nums.append(n)
        
        return False
        