class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        res = 1
        charSet = set()
        temp = 1
        temp_k = k
        charSet.add(s[l])
        while r < len(s):
            if s[r] in charSet:
                temp += 1
                r+=1
            elif s[r] not in charSet:
                if temp_k > 0:
                    temp_k-=1
                    temp+=1
                    r+=1
                else:
                    charSet.remove(s[l])
                    temp = 1
                    temp_k = k
                    l+=1
                    r=l+1
                    charSet.add(s[l])
            res = max(res, min(temp + temp_k, len(s)))
        
        return res