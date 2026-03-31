class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        sol = []
        l = r = 0
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            #  the above algo gives a unique array where, at any point you will have a feasible non-increasing ordered array -> my own term
            # [1 4 1 2 4] -> at each point -> [1], [4], [4,1], [4,2], [4,4]

            if l > q[0]:
                # if l moves past the current biggest element
                q.popleft()
                # the next new highest element is selected

            if r+1>=k:
                sol.append(nums[q[0]])
                l+=1
            r+=1

        return sol