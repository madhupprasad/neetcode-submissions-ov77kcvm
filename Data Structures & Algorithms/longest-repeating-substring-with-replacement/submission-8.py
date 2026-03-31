class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # DO AGAIN - DONT READ SOLUTION - YOU WERE SLEEPY WHEN YOU DID THIS
        # XYYXXXXXYYXXXX
        # XYXXXXYXXXXYXXXXXXXXXXXXXXXX
        # YYXXXXXXXXXXXX
        # { Y : 2, X : 10}
        # {A : 4, B : 3}
        # BAAABABB
        
        l = 0
        count = {}
        max_f = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l+=1
            res = max(r-l+1, res)

        return res

