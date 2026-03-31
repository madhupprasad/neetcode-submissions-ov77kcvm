from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        res = []
        for value in num_counter.most_common(k):
            res.append(value[0])

        return res