class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in h:
                if i != h[comp]:
                    return sorted([i, h[comp]])