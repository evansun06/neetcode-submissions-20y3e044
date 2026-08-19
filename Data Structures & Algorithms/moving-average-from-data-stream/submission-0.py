from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.stream = deque()
        self.size = size
        self.sum = 0
        

    def next(self, val: int) -> float:
        if self.size == len(self.stream):
            remove = self.stream.popleft()
            self.sum -= remove


        self.stream.append(val)
        self.sum += val

        return float(self.sum) / float(len(self.stream))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
