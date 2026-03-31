class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        A small array datastructure will help you
        solve this problem, try to solve in an
        original way without seeing the solution
        -> implicitly we know a sliding window is used
        """

        q = deque()
        sol = []
        l = r = 0
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                # we make sure q[0] always contain the max
                q.pop()
                        
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                # if we cross the k size we start appending the 
                # q[0] which should be the max value
                sol.append(nums[q[0]])
                l+=1
            r+=1

        return sol