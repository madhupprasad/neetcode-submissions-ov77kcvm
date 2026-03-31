class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # c = Counter(nums)
        # a = sorted(c.items(), key=lambda x: x[1], reverse=True)
        # r=[]
        # for i in range(k):
        #     r.append(a[i][0])
        # return r
        s = []
        for i in range(len(nums)+1):
            s.append([])
        
        c = Counter(nums)
        print(c)
        for i,j in c.items():
            s[j].append(i)
        r = []
        for i in range(len(s)-1, -1, -1):
            for x in s[i]:
                r.append(x)
                if len(r) == k:
                    return r