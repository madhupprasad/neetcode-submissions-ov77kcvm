class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        lmax[0] = height[0]
        rmax[len(height)-1] = height[len(height)-1]
        for idx in range(1,len(height)):
            lmax[idx] = max(lmax[idx-1], height[idx])
        
        for idx in range(len(height)-2,-1,-1):
            rmax[idx] = max(rmax[idx+1], height[idx])

        s = 0
        print(rmax, lmax)
        for idx, h in enumerate(height):
            s += min(lmax[idx], rmax[idx]) - h
        
        return s
