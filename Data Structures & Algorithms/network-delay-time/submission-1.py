from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
            dikjstras + max
        """
        
        adjc_list = defaultdict(list)

        for source, target, time in times:
            adjc_list[source].append((target, time))
        
        heap = [(0, k)]
        distances = [float('inf')] * (n + 1)
        distances[k] = 0

        while heap:
            time, node = heapq.heappop(heap)


            # if distances[node] < time:
            #     continue
            
            for adjc_node, cost in adjc_list[node]:
                new_time = time + cost

                if new_time < distances[adjc_node]:
                    distances[adjc_node] = new_time
                    heapq.heappush(heap, (new_time, adjc_node))
        

        return max(distances[1:]) if max(distances[1:]) != float('inf') else -1





