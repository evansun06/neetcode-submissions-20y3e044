import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            distance_sqr = x*x + y*y

            if len(max_heap) == k:
                heapq.heappushpop(max_heap, (-distance_sqr,(x,y)))
            else:
                heapq.heappush(max_heap, (-distance_sqr,(x,y)))

        return [list(entry[1]) for entry in max_heap]