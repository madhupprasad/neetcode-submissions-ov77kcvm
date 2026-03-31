class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        temp = float("inf")

        while l < r:
            mid = (l + r)//2
            temp = min(nums[mid], temp)

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
            
        return min(temp, nums[l])


