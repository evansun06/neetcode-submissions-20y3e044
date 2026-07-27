class MedianFinder:

    def __init__(self):
        self.min_heap = [] # tracks upper bound
        self.max_heap = [] # tracks lower bound
        self.median = 0
        self.count = 0


    def addNum(self, num: int) -> None:
        if self.count == 0:
            self.median = num
            self.count += 1
            return

        if self.count % 2 == 0:
            if num <= self.min_heap[0] and num >= -self.max_heap[0]:
                self.median = num
            elif num > self.min_heap[0]:
                self.median = self.min_heap[0]
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
            else:
                self.median = -self.max_heap[0]
                heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -num)
        else:
            if num >= self.median:
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -self.median)
            else:
                heapq.heappush(self.min_heap, self.median)
                heapq.heappush(self.max_heap, -num)

        self.count += 1

    def findMedian(self) -> float:
        if (self.count) % 2 == 0:
            return (self.min_heap[0] + (-1*self.max_heap[0])) / 2
        else:
            return self.median
        
        