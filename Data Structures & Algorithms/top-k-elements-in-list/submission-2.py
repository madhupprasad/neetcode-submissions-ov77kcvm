class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = sorted(c.items(), key=lambda x: x[1], reverse=True)
        r=[]
        for i in range(k):
            r.append(a[i][0])
        return r

            
            