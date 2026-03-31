class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        
        s_count, t_count = {}, {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1
        
        return s_count == t_count

    def groupAnagrams(self, v: List[str]) -> List[List[str]]:
        used = set()
        result = []
        for i in range(len(v)):
            if v[i] in used:
                continue
            temp_result=[v[i]]
            for j in range(i+1,len(v)):
                if self.isAnagram(v[i], v[j]):
                    temp_result.append(v[j])
                    used.add(v[j])
            result.append(temp_result)
            used.add(v[i])
        return result