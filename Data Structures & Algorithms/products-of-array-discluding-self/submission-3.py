class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zcount = 0
        for i in nums:
            if i == 0:
                zcount+=1
        
        if zcount > 1:
            return [0] * len(nums)
 
        total_multiply = 1
        zero_mul = 1
        for num in nums:
            total_multiply *= num
            if num != 0:
                zero_mul *= num
        res = []
        for num in nums:
            if num == 0:
                res.append(int(zero_mul))
            else:
                res.append(int(total_multiply/num))
        return res