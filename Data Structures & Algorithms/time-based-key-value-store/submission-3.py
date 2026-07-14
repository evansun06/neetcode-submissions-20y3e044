class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(timestamp, value)]
        else:
            self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hashmap:
            return ""
        
        time_series = self.hashmap[key]

        left = 0
        right = len(time_series) - 1
        mid = (left + right) // 2

        while right >= left:
            mid = (left + right) // 2

            if time_series[mid][0] == timestamp:
                return time_series[mid][1]
            elif time_series[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        
        return time_series[right][1] if time_series[right][0] <= timestamp else ""

