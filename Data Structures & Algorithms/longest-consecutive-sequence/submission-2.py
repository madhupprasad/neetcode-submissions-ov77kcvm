class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        a = []
        for n in nums:
            if n-1 not in s:
                a.append(n)
        m = 0
        for n in a:
            ans = 1
            x = n+1
            for _ in nums:
                if x in s:
                    ans+=1
                    x+=1
            m = max(m, ans)
        print(a, m)
        return m