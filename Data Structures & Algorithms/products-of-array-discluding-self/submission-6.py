class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        p = [1] * l
        s = [1] * l
        for i in range(1,l):
            o = nums[i-1]
            p[i] = p[i - 1] * o
        for i in range(l-2, -1, -1):
            o = nums[i+1]
            s[i] = s[i + 1] * o
        res = []
        for i in range(l):
            res.append(s[i] * p[i])
        return res