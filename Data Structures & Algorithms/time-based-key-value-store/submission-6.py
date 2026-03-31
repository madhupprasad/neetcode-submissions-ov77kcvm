class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timemap.get(key, [])
        l = 0
        r = len(arr) - 1
        res = ""
        while l <= r:
            mid = (l + r)//2
            if arr[mid][0] <= timestamp:
                l = mid + 1
                res = arr[mid][1]
            else:
                r = mid - 1
        return res
