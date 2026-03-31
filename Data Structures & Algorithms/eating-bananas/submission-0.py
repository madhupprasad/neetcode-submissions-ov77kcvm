class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        I did not solve this, I am not able to come up with the solution. 
        Intuition is we should know the answer will be in the range (1 - max(piles)).
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
