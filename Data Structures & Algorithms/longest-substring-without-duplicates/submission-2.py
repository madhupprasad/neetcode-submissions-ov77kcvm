class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        start = 0
        end = 0
        res = 0
        while end < len(s):
            while s[end] in charset:
                charset.remove(s[start])
                start += 1
            charset.add(s[end])
            res = max(res, end - start + 1)
            end+=1

        return res