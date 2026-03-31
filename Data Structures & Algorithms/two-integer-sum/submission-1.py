class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        idx = -1
        for num in nums:
            idx += 1
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[num] = idx