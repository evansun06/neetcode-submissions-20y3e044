import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def dist_to_origin(point: List[int]):
            return math.sqrt(point[0]**2 + point[1]**2)

        for i, point in enumerate(points):
            if len(heap) == k:
                d = dist_to_origin(point)
                if -1*heap[0][0] > d:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-d, i))
            else:
                heapq.heappush(heap, (-1 * dist_to_origin(point), i))
        
        return [points[p[1]] for p in heap]


