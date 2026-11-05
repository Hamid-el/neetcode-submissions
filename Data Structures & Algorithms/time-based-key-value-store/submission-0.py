class TimeMap:

    def __init__(self):
        self.h = collections.defaultdict(list) # key -> list((val, time))


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if not self.h[key]:
            return ""

        l = 0
        r = len(self.h[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if self.h[key][mid][0] <= timestamp:
                l = mid + 1
                res = self.h[key][mid][1]
            else:
                r = mid - 1
                
        return res
