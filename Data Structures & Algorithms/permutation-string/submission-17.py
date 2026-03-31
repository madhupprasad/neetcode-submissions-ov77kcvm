class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = [0] * 26
        d2 = [0] * 26

        if len(s1) > len(s2):
            return False

        # calcualte the dict
        for i in range(len(s1)):
            idx1 = ord(s1[i]) - ord('a')
            idx2 = ord(s2[i]) - ord('a')
            d1[idx1] += 1
            d2[idx2] += 1
        
        # something like [0,1,0,0,2] for "bee" and all combinations

        matches = 0
        for i in range(26):
            matches += 1 if d1[i] == d2[i] else 0
        print(matches)
        # we can now get 26 as result if 2 str are combinations
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
        
            idxr = ord(s2[r]) - ord('a')
            d2[idxr] += 1
            if d2[idxr] == d1[idxr]:
                matches+=1
            elif d2[idxr]-1 == d1[idxr]:
                matches-=1
            
            idxl = ord(s2[l]) - ord('a')
            d2[idxl] -= 1
            if d2[idxl] == d1[idxl]:
                matches+=1
            elif d2[idxl] == d1[idxl]-1:
                matches-=1
            print(matches)
            l+=1
        
        if matches == 26:
            return True

        return False

