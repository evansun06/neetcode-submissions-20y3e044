from collections import defaultdict
import heapq

class Solution:
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Minimum spanning tree

        Graph Representation O(len(p)^2):
        - adjacency list where node maps to list((adjc, abs(manhattan dist)))

        Prims
    
        """

        adjc_list = defaultdict(list)

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                manhat_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                adjc_list[tuple(points[i])].append((manhat_dist, tuple(points[j])))
                adjc_list[tuple(points[j])].append((manhat_dist, tuple(points[i])))
            
        visited = set()
        visited.add(tuple(points[0]))
        total_cost = 0
        min_heap = adjc_list[tuple(points[0])]
        heapq.heapify(min_heap)

        while min_heap and len(visited) < len(points):
        
            cost, point = heapq.heappop(min_heap)

            if point in visited:
                continue
                
            visited.add(point)
            
            total_cost += cost

            for cost, nxt_point in adjc_list[point]:
                heapq.heappush(min_heap, (cost, nxt_point))

        return total_cost


            
