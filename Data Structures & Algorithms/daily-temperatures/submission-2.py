class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr=[]
        res=[]
        for i in range(len(temperatures)-1, -1, -1):
            val = temperatures[i]
            if arr == []:
                arr.append(i)
                res.append(0)
            else:
                if val < temperatures[arr[-1]]:
                    res.append(arr[-1] - i)
                    arr.append(i)
                else:
                    while arr and val >= temperatures[arr[-1]]:
                        arr.pop()
                    if arr == []:
                        res.append(0)
                        arr.append(i)
                    else:
                        res.append(arr[-1] - i)
                        arr.append(i)
            print(arr, res)
        res.reverse()
        return res