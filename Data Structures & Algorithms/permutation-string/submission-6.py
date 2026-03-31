from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        s2_len = len(s2)
        charset = Counter(s1)

        a_flag = False

        while r < s2_len:
            print(charset, l ,r, s2[r])
            if s2[r] in charset and charset[s2[r]] > 0:
                if a_flag == False:
                    l = r
                    a_flag = True
                charset[s2[r]] -= 1
                r+=1
            else:
                a_flag = False
                charset = Counter(s1)
                l+=1
                r=l

            if sum(charset.values()) == 0:
                return True

        return False