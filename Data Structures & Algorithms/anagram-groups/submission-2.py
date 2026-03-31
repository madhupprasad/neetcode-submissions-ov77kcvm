from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def checkAnagram(stra, strb):
            if len(stra) != len(strb):
                return False
            if Counter(stra) == Counter(strb):
                return True
        idx = 0
        res = []
        matchAlready = {}
        for string1 in strs:
            idx += 1
            tempRes = []
            if string1 in matchAlready:
                continue
            tempRes.append(string1)
            for i in range(idx, len(strs)):
                string2 = strs[i]
                if checkAnagram(string1, string2):
                    matchAlready[string1] = 1
                    matchAlready[string2] = 1
                    tempRes.append(string2)
            res.append(tempRes)
        return res