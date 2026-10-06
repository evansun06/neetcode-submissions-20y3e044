from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjc_list = defaultdict(list)

        for start, end, time in times:
            adjc_list[start].append((end, time))
        
        time_map = [float('inf')] * n
        time_map[k-1] = 0
        min_heap = [(0, k)]

        while min_heap:

            time, node = heapq.heappop(min_heap)

            if time > time_map[node-1]:
                continue
            
            for adjc_node, extra_time in adjc_list[node]:
                if time + extra_time < time_map[adjc_node-1]:
                    heapq.heappush(min_heap, (time+extra_time, adjc_node))
                    time_map[adjc_node-1] = time + extra_time
        
        total_time = max(time_map)
        return total_time if total_time != float('inf') else -1
                    


