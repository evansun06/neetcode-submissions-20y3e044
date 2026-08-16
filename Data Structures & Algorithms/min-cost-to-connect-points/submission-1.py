from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):

                point_1 = tuple(points[i])
                point_2 = tuple(points[j])

                distance = abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

                graph[point_1].append((point_2, distance))
                graph[point_2].append((point_1, distance))
        
        visited = set()
        # edge cost, current node, parent node

        heap = [(0, tuple(points[0]))]
        heapq.heapify(heap)
        cost = 0

        while heap and len(visited) < len(points):
            distance, point = heapq.heappop(heap)

            if point in visited:
                continue
            
            
            visited.add(point)
            cost += distance


            for adjc_point, adjc_d in graph[point]:
                if adjc_point not in visited:
                    heapq.heappush(
                        heap,
                        (adjc_d, adjc_point)
                    )
        
        return cost

