class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if you think - it is just a straight logic with sliding window
        if len(s) < len(t):
            return ""
        sT = {}
        for i in range(len(t)):
            sT[t[i]] = 1 + sT.get(t[i], 0)
        
        resLen = float("infinity")
        res = [-1, -1]
        l = 0
        win = {}
        have = 0
        need = len(t)
        for r in range(len(s)):
            ch = s[r]
            win[ch] = win.get(ch, 0) + 1

            if ch in sT and win[ch] <= sT[ch]:
                have+=1
            
            print(win, sT, have, need)

            while have == need:
                print(r,l)
                if (r - l + 1) < resLen:
                    resLen = r-l+1
                    res = [l, r]
                
                win[s[l]] -= 1
                if s[l] in sT and win[s[l]] < sT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""
            
