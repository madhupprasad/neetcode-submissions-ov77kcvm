class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        res = 0
        while(l < r):
            y = min(heights[l], heights[r])
            x = r - l
            area = x * y
            print(heights[l], heights[r],y,x,area)
            res = max(res, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return res