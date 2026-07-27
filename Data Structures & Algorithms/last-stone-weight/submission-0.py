import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [(s*-1) for s in stones]
        heapq.heapify(heap)
        
        while heap:
            if len(heap) == 1:
                return -1*heapq.heappop(heap)
            else:
                x = -1*heapq.heappop(heap)
                y = -1*heapq.heappop(heap)

                if x == y:
                    continue
                elif x < y:
                    y = y - x
                    heapq.heappush(heap, -1*y)
                else:
                    x = x - y
                    heapq.heappush(heap, -1*x)
                    
        return 0
        