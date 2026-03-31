class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = {}
        for num in nums:
            if num in maps:
                return True
            else:
                maps[num] = 1
        
        return False