class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {}
        res = 0
        m = 0
        for r in range(len(s)):
            curr = s[r]
            res+=1
            d[s[r]] = 1 + d.get(s[r],0 )

            while d[s[r]] > 1:
                d[s[l]] -= 1
                l+=1
                res-=1
            
            m = max(m, res)
        
        return m