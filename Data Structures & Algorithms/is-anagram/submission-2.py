class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        maps = {}
        for char in s:
            if char in maps:
                maps[char] = maps[char] + 1
            else:
                maps[char] = 1
        for ch in t:
            if ch in maps:
                if maps[ch] > 0:
                    maps[ch] = maps[ch] - 1
                    continue
                else:
                    return False
            else:
                return False

        return True