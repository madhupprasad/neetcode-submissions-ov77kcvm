class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {}
        maxx = 0
        res = 0
        for r in range(len(s)):
            curr = s[r]
            d[curr] = d.get(curr, 0) + 1
            res+=1
            while d[curr] > 1:
                d[s[l]] -= 1
                l+=1
                res-=1
            maxx = max(res, maxx)

        return maxx



