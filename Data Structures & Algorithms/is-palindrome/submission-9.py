class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = []
        for a in s:
            if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z') or (a >= '0' and a <= '9'):
                x.append(a.lower())

        a,b = 0, len(x)-1
        print(a,b,x)
        while a < b:
            if x[a] != x[b]:
                return False
            b-=1
            a+=1
        
        return True