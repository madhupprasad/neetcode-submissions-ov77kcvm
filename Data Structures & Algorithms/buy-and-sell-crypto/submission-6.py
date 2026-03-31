
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        leng = len(prices)
        res = 0
        while(right < leng):
            if prices[left] > prices[right]:
                left=right
                right+=1
            else:
                res = max(res, prices[right] - prices[left])
                right += 1
        
        return res
