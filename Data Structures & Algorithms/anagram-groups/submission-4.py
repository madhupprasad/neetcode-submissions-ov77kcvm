class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            hashes = hash(frozenset(Counter(s).items()))
            res[hashes].append(s)
        return list(res.values())