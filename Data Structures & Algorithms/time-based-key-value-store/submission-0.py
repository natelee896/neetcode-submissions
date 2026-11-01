class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []
        self.times[key].append((timestamp, value))
        self.times[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        
        arr = self.times[key]

        left = 0
        right = len(arr) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            t, val = arr[mid]

            if t <= timestamp:
                result = val
                left = mid + 1
            else:
                right = mid - 1
        
        return result
        
