from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q = deque()
        for i in range(k):
            Q.append(nums[i])
        
        sol = [max(Q)]

        for i in range(k, len(nums)):
            Q.popleft()
            Q.append(nums[i])
            sol.append(max(Q))

        return sol