from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
            dikjstras

            state = k * n  matrix holding the cheapest cost for k + 1 flights

            k stops means k + 1 flights

        """

        adjc_list = defaultdict(list)

        for source, destination, cost in flights:
            adjc_list[source].append((destination, cost))

        heap = [(0, src, 0)]
        best = [[float('inf')] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        while heap:
            cost, airport, flights = heapq.heappop(heap)

            if airport == dst:
                return cost

            if flights >= k + 1:
                continue
            
            if cost > best[airport][flights]:
                continue

            for adjc_airport, additional_cost in adjc_list[airport]:
                new_cost = cost + additional_cost
                if new_cost < best[adjc_airport][flights + 1]:
                    best[adjc_airport][flights + 1] = new_cost
                    heapq.heappush(
                        heap,
                        (new_cost, adjc_airport, flights + 1)
                    )
        return -1




