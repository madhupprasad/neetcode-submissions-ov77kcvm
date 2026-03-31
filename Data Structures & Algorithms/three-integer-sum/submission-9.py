class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
            a = i+1
            z = len(nums)-1
            while a < z:
                s = nums[a] + nums[z] + v
                if s > 0:
                    z-=1
                elif s < 0:
                    a+=1
                else:
                    res.append([nums[a], nums[z], v])
                    z-=1
                    a+=1
                    while nums[a] == nums[a-1] and a < z:
                        a+=1
        return res